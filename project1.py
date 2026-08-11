import cv2

def text():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    title = input("Set title: ")
    X = int(input("Enter X coordinate: "))
    Y = int(input("Enter Y coordinate: "))
    size = float(input("Enter font scale: "))

    r = int(input("Enter Red: "))
    g = int(input("Enter Green: "))
    b = int(input("Enter Blue: "))

    thickness = int(input("Enter text thickness: "))

    if image is None:
        print("Image not found!")
        return

    color = (b, g, r)

    cv2.putText(
        image,
        title,
        (X, Y),
        cv2.FONT_HERSHEY_SIMPLEX,
        size,
        color,
        thickness
    )

    cv2.imshow("Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blur():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    kernel = int(input("Enter blur kernel size (odd number): "))

    if image is None:
        print("Image not found!")
        return

    blurred = cv2.GaussianBlur(image, (kernel, kernel), 0)

    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def black_and_white():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    if image is None:
        print("Image not found!")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    X1 = int(input("Enter starting X: "))
    Y1 = int(input("Enter starting Y: "))
    X2 = int(input("Enter ending X: "))
    Y2 = int(input("Enter ending Y: "))

    if image is None:
        print("Image not found!")
        return

    cropped = image[Y1:Y2, X1:X2]

    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def line():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    X1 = int(input("Enter starting X: "))
    Y1 = int(input("Enter starting Y: "))
    X2 = int(input("Enter ending X: "))
    Y2 = int(input("Enter ending Y: "))

    r = int(input("Enter Red: "))
    g = int(input("Enter Green: "))
    b = int(input("Enter Blue: "))

    thickness = int(input("Enter line thickness: "))

    if image is None:
        print("Image not found!")
        return

    color = (b, g, r)

    cv2.line(
        image,
        (X1, Y1),
        (X2, Y2),
        color,
        thickness
    )

    cv2.imshow("Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def shape():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    X = int(input("Enter center X: "))
    Y = int(input("Enter center Y: "))
    radius = int(input("Enter radius: "))

    r = int(input("Enter Red: "))
    g = int(input("Enter Green: "))
    b = int(input("Enter Blue: "))

    thickness = int(input("Enter circle thickness: "))

    if image is None:
        print("Image not found!")
        return

    color = (b, g, r)

    cv2.circle(
        image,
        (X, Y),
        radius,
        color,
        thickness
    )

    cv2.imshow("Shape", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def flip():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    direction = int(input("Enter flip direction (1=Horizontal, 0=Vertical, -1=Both): "))

    if image is None:
        print("Image not found!")
        return

    flipped = cv2.flip(image, direction)

    cv2.imshow("Flipped Image", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))

    if image is None:
        print("Image not found!")
        return

    resized = cv2.resize(image, (width, height))

    cv2.imshow("Resized Image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotate():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    angle = int(input("Enter rotation angle (90, 180, 270): "))

    if image is None:
        print("Image not found!")
        return

    if angle == 90:
        rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    elif angle == 180:
        rotated = cv2.rotate(image, cv2.ROTATE_180)

    elif angle == 270:
        rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    else:
        print("Invalid angle!")
        return

    cv2.imshow("Rotated Image", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def edge():
    path = input("Enter the image path: ")
    image = cv2.imread(path)

    lower = int(input("Enter lower threshold: "))
    upper = int(input("Enter upper threshold: "))

    if image is None:
        print("Image not found!")
        return

    edges = cv2.Canny(image, lower, upper)

    cv2.imshow("Edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


while True:

    print("\n===== IMAGE EDITOR =====")
    print("1. ADD TEXT")
    print("2. BLUR IMAGE")
    print("3. CONVERT INTO B/W")
    print("4. CROP IMAGE")
    print("5. DRAW LINE")
    print("6. DRAW SHAPE")
    print("7. FLIP IMAGE")
    print("8. RESIZE IMAGE")
    print("9. ROTATE IMAGE")
    print("10. EDGE DETECTION")
    print("11. EXIT")

    choice = input("What do you want to do: ")

    if choice == "1":
        text()

    elif choice == "2":
        blur()

    elif choice == "3":
        black_and_white()

    elif choice == "4":
        crop()

    elif choice == "5":
        line()

    elif choice == "6":
        shape()

    elif choice == "7":
        flip()

    elif choice == "8":
        resize()

    elif choice == "9":
        rotate()

    elif choice == "10":
        edge()

    elif choice == "11":
        print("Program closed!")
        break

    else:
        print("Invalid Choice!!")