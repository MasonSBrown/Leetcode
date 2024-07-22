class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        final_list = []
        def descendingSort(heights):
            sorted_height = []
            highest = 0
            for i in range(len(heights)):
                if heights[i] > highest:
                    highest = heights[i]
                    sorted_height.insert(0, highest)
                else:
                    for j in range(len(sorted_height)):
                        if heights[i] > sorted_height[j]:
                            sorted_height.insert(j, heights[i])
                        elif j == len(sorted_height) - 1:
                            sorted_height.insert(j+1, heights[i])
            return(sorted_height)

        hashmap = defaultdict()

        for index, height in enumerate(heights):
            hashmap[height] = index

        sorted_height_list = sorted(heights, reverse=True)
        for height in sorted_height_list:
            location = hashmap[height]
            final_list.append(names[location])
        return final_list
