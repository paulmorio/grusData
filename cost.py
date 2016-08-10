def compute_cost(x,y,m,b):
    """
    Compute the MSE cost of a prediction based on m,b
    
    x: input vector
    y: observed output vector
    m,b regression parameters
    
    Returns: cost::double
    """
    yhat = m*x + b
    diff = yhat - y
    
    cost = np.dot(diff.T, diff)/float(x.shape[0])
    return cost.flat[0]
    
