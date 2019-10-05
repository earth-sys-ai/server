# json parser
import json

# create array of values through data
def transect(data, line):

     # test
     # curl "http://0.0.0.0:5000?com=transect&level=5&line=(25.637675852300642,-81.67236328125001)"
     # print(getValue(data, parseLine(line)[0]))

    # define output array
        outVals = []

    # loop through line points
        for i in parseLine(line):
                outVals.append(getValue(data, i))

    # return array
        return parseArr(outVals)

# get value at point in date
def getValue(data, point):

    # loop through polygons
    for level in data["levels"]:
        for poly in level["polygons"]:
                minV = poly["minV"]
                maxV = poly["maxV"]
                if polyContains(poly["vertices"], point):
                        return level["value"]

    # if contains point, return value of containing layer

# query parameter to coordinate array
def parseLine(txt):
        coords = []
        s = txt.split('(')
        for coord in s:
                if coord:
                        xy = coord.split(')')[0].split(',')
                        coords.append((float(xy[0]), float(xy[1])))
        return coords


# return if a polygon contains a given point
def polyContains(poly, point):

    # declare intersect tally
    tally = 0

    # loop through points
    for i in range(0, len(poly)):

        # get adjacent points
        j1 = poly[(i - 1) % len(poly)] 
        j2 = poly[i % len(poly)]
        t1 = (j1["lng"], j1["lat"])
        t2 = (j2["lng"], j2["lat"])
        
        # check if ray collides with line
        if ((t1[1] >= point[1] and t2[1] <= point[1] or
            t1[1] <= point[1] and t2[1] >= point[1]) and
            (t1[0] >= point[0] or t2[0] >= point[0])):

            # add tally
            tally += 1

    # check if even amount of collitions
    return (tally % 2 != 0 and tally > 0)

# parse array of points into json response
def parseArr(arr):
        return json.dumps({
                "count": len(arr),
                "values": arr
        })

