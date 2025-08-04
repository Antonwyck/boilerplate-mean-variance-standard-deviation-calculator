import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arrnum = np.array(input_list).reshape(3, 3)
    np.set_printoptions(precision=16, suppress=False)
    
    calculations = {
        'mean': [list(np.mean(arrnum, axis=0)), list(np.mean(arrnum, axis=1)), np.mean(arrnum).item()],
        'variance': [list(np.var(arrnum, axis=0)), list(np.var(arrnum, axis=1)), np.var(arrnum).item()],
        'standard deviation': [list(np.std(arrnum, axis=0)), list(np.std(arrnum, axis=1)), np.std(arrnum).item()],
        'max': [list(np.max(arrnum, axis=0)), list(np.max(arrnum, axis=1)), np.max(arrnum).item()],
        'min': [list(np.min(arrnum, axis=0)), list(np.min(arrnum, axis=1)), np.min(arrnum).item()],
        'sum': [list(np.sum(arrnum, axis=0)), list(np.sum(arrnum, axis=1)), np.sum(arrnum).item()]
    }
    
    return calculations
