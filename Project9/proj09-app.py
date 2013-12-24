from Project9.triangle import Triangle
import sys


def main():
    try:
        f = open(sys.argv[1])

        line_num = 0
        valid_triangles_num = 0
        perimeter_total = 0
        area_total = 0
        t_largest_perimeter = Triangle()
        t_largest_area = Triangle()

        for line in f:
            print("Line %s: " % (line_num+1), end="")

            sideA = line.split(',')[0].strip()[1:]
            sideB = line.split(',')[1].strip()
            sideC = line.split(',')[2].strip()[:-1]

            curr_triangle = Triangle(sideA, sideB, sideC)
            if curr_triangle.is_valid():
                print("Triangle: ", end="")
                print(curr_triangle, end="\t")
                print("Perimeter: ", end="")
                print(curr_triangle.perimeter(), end="\t")
                print("Area: ", end="")
                print(curr_triangle.area(), end="")

                valid_triangles_num += 1
                perimeter_total += curr_triangle.perimeter()
                area_total += curr_triangle.area()

                if t_largest_perimeter.perimeter() < curr_triangle.perimeter():
                    t_largest_perimeter = curr_triangle
                if t_largest_area.area() < curr_triangle.area():
                    t_largest_area = curr_triangle
            else:
                print("The triangle is not a valid triangle", end="")
            line_num += 1
            print()

        print("------------------------")
        print("SUMMARY")
        print("Total number of lines processed: %s" % line_num)
        print("Total number of valid triangles processed: %s" % valid_triangles_num)
        print("Average Perimeter of valid triangles processed: %s" % (perimeter_total/valid_triangles_num))
        print("Average Area of valid triangles processed: %s" % (area_total/valid_triangles_num))
        print("Triangle with largest perimeter: Triangle:", end="")
        print(t_largest_perimeter, end="\t")
        print("Perimeter: %s \tArea: %s" % (t_largest_perimeter.perimeter(), t_largest_perimeter.area()))
        print("Triangle with largest area: Triangle:", end="")
        print(t_largest_area, end="\t")
        print("Perimeter: %s \tArea: %s" % (t_largest_area.perimeter(), t_largest_area.area()))

    except FileNotFoundError:
        print("File not found at path: %s" % sys.argv[1])

if __name__ == "__main__":
    main()