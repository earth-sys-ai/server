# json parser
import json

# create array of values through data
def transect(data, line):

    # define output array
        outVals = []

    # loop through line points
        for i in parseLine(line):
                outVals.append(getValue(data, i))

    # return array
        return parseArr(outVals)


# get value at point in date
def getValue(data, point):

    # loop through polygons from last added
    for level in reversed(data["levels"]):
        for poly in reversed(level["polygons"]):

                # get boundaries of polygon
                minV = poly["minV"]
                maxV = poly["maxV"]

                # check if point is in polygon's domain / range
                if (point[0] >= minV[0] and point[0] <= maxV[0] and
                    point[1] >= minV[1] and point[1] <= point[1]):

                        # point in polygon (13.21)               
                        if polyContains(poly["vertices"], point):
                                return level["value"]
        
    # return top polygon
    return out


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
        t1 = (j1["lat"], j1["lng"])
        t2 = (j2["lat"], j2["lng"])
        
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

