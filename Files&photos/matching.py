def matching(arr1, arr2):
    cnt = 0
    for i in range(arr1.shape[0] - 25):
        for j in range(arr1.shape[1] - 25):
            if arr1[i][j] == 0:
                for m in range(-15, 15):
                    for n in range(-15, 15):
                        if i + m < arr2.shape[0] - 1:
                            if j + n < arr2.shape[1] - 1:
                                if arr2[i + m][j + n] == 0:
                                    cnt += 1
                                    break
    return cnt
