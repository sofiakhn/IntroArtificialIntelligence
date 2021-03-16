# Sofia Khan
# CS 540 Fall 2020
import matplotlib
import numpy
import scipy.linalg
import matplotlib.pyplot as plt


# load the dataset from a provided .npy file, re-center it around the origin and return it as a NumPy array of floats
from scipy import linalg


def load_and_center_dataset(filename):
    x = numpy.load(filename)
    x = numpy.reshape(x, (2000, 784))
    centered = x - numpy.mean(x, axis=0)
    return centered

# calculate and return the covariance matrix of the dataset as a NumPy matrix (d x d array)
def get_covariance(dataset):
    x = dataset
    transposed = numpy.transpose(x)
    mult = numpy.dot(transposed, x)
    ans = mult/1999
    # print (ans[350][350])
    return ans

## perform eigen decomposition on the covariance matrix S and return a diagonal matrix (NumPy array) with the largest m
# eigenvalues on the diagonal, and a matrix (NumPy array) with the corresponding eigenvectors as columns
def get_eig(S, m):

    values, vectors = scipy.linalg.eigh(S)

    eigenVal = numpy.sort(values)[::-1]
    eigenArray = numpy.diag(eigenVal)

    eigVecArray = []
    for i in range(numpy.size(eigenVal) - 1, numpy.size(eigenVal)-1-m, -1):
        eigVecArray.append(vectors[:,i])

    eigVecArray = numpy.array(eigVecArray)
    eigVecArray = numpy.transpose(eigVecArray)

    return eigenArray, eigVecArray

#similar to get_eig, but instead of returning the first m, return all eigenvectors that explains more than perc % of variance
def get_eig_perc(S, perc):

    eig = scipy.linalg.eigh(S)
    eigenValues = eig[0]
    eigenVectors = eig[1]
    val = []
    vec = []
    c = 0
    sum = numpy.sum(eigenValues)
    n = numpy.size(eigenValues) - 1 ## upper bound of for loop

    for i in range(len(eigenValues)): ## go through the list backwards!
        variation = eigenValues[len(eigenValues)-i-1]/sum
        if(variation>= perc):
            c += 1
            val.append(eigenValues[len(eigenValues)-i-1])
            vec.append(eigenVectors[:,len(eigenValues)-i-1]) ## add this column

    diag = numpy.diag(val)
    # print(diag)
    vec = numpy.array(vec)
    vec = numpy.transpose(vec)
    # print(len(validVectors[0]))
    # print ('Shape of vector', numpy.shape(validVectors))
    return diag, vec

## project each image into your m-dimensional space and return the new representation as a d x 1 NumPy array
def project_image(image, U) :
    # print (numpy.shape(image))
    # print (numpy.shape(U))
    #
    # answer = []
    # for i in range(0,784):
    #     x_i = image[i] ## value at x_i
    #     # u_j_top = U[0][i]
    #     # u_j_bottom = U[1][i]
    #     # u_j = [u_j_top, u_j_bottom] ## u_j vector
    #     u_j = U[i]
    #     u_j_transpose = numpy.transpose(u_j) ## u_j transposed vector
    #
    #     value = numpy.dot(x_i, u_j_transpose) * u_j
    #     answer.append(value)
    #
    # return answer

    transU = numpy.transpose(U)
    xi = image
    dotProd = numpy.dot(transU, xi)
    projImage = numpy.matmul(U, dotProd)

    return projImage

# use matplotlib to display a visual representation of the original image and the projected image side-by-side
def display_image(orig, proj):

    ## reshape the images
    originale = numpy.reshape(orig, (28,28))
    projectione = numpy.reshape(proj, (28,28))

    fig, (img1, img2) = plt.subplots(1,2, sharex=True, sharey=False, figsize=(9,3))
    img1.plot(28,28)
    img2.plot(28,28)
    img1.set_title('Original')
    img2.set_title('Projection')

    plot1 = img1.imshow(originale, aspect='equal',cmap='gray')
    plot2 = img2.imshow(projectione, aspect='equal',cmap='gray')

    fig.colorbar(plot1, ax=img1)
    fig.colorbar(plot2, ax=img2)

    plt.show()

    return

################ Testing ##################

dataset = load_and_center_dataset('mnist.npy')
# print('dataset: ' , dataset)
S = get_covariance(dataset)
Lambda, U = get_eig(S, 2)
print(Lambda)
print(numpy.sum(U))

images = load_and_center_dataset('mnist.npy')
s = get_covariance(images)
Lambda, U = get_eig(s, 3)

image = images[2]

image_proj = project_image(image, U)
display_image(image, image_proj)