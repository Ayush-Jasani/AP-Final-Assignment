def minOp(str1, str2):
    def len_str(s):
        count = 0
        for _ in s:
            count += 1
        return count

    m = len_str(str1)
    n = len_str(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    i = 0
    while i <= m:
        j = 0
        while j <= n:
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                cost = 0 if str1[i - 1] == str2[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # remove
                    dp[i][j - 1] + 1,    # insert
                    dp[i - 1][j - 1] + cost  # replace
                )
            j += 1
        i += 1
    return dp[m][n]
