# r^2 based on the latest measured y-values
import numpy as np

# Calculate r^2 based on the latest measured y-values
# measuredy and estimatedy must be vectors.
def r2lm( measuredy, estimatedy ):
    measuredy  = np.array( measuredy ).flatten()
    estimatedy = np.array( estimatedy ).flatten()
    return float( 1 - sum( (measuredy-estimatedy )**2 ) / sum((measuredy[1:]-measuredy[:-1])**2) )
