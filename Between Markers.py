def between_markers(text: str, start: str, end: str) -> str:
    iterations = 0
    for index in range(0, len(text)):
        iterations = iterations+1
        if text[index] == start:
            index_start = index
        if text[index] == end:
            index_end = index
            return text[index_start+1:index_end]
            
    print("this program ran for %s iterations"%iterations)
    #print(index_start, index_end)
    final = ""
    for index in range(index_start+1, index_end):
        final = final + text[index]
    return final

print("Example:")
print(between_markers("What is >apple<", ">", "<"))
print(between_markers("<123>jdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvgjdjic2ifj2jf9en92f9v9nvn9n 2n2ivn2  2incincn2iecneicnie2cn2inv 2in zx b bjvg", "<", ">"))
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")