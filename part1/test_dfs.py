import dfs
import pytest

mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]]

def check_matrix(test):
    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j] != mtx[i][j]:
                return False
    
    return True

def test_best(sample1):
    assert check_matrix(dfs.tree(sample1)) == True

def test_worst(sample2):
    assert check_matrix(dfs.tree(sample2)) == True

