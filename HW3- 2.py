import numpy as np
import matplotlib.pyplot as plt

x_val = 1
y_val = 1
approx_val = 1

def centeral_derivative(f, x, h):
    '''
    parameters:
    f (function) : the function to differentiate 
    x(ndarray) : Array of values where the derivative is computed 
    h(float) : the step-size 
    '''
    return ( f(x+h) - f(x-h) ) / (2 * h)
def run_verification():
    x_val = 1.0
    x_plot = np.linspace(0, 2 * np.pi, 200)
    h_visual = 0.01
    num_deriv_sin = centeral_derivative(np.sin, x_plot, h_visual)
    true_deriv_sin = np.cos(x_plot)
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(x_plot, true_deriv_sin, label='true cos(x)', color='black', linewidth=2)
    plt.plot(x_plot, num_deriv_sin, '--', label='Numerical derivative', color='orange')
    plt.title("Derivative of sin(x)")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('derivative_verification.png')
    plt.show()
    
step_sizes = np.logspace(0, -6, 50)
errors = []
    
true_val = np.cos(x_val)
for h in step_sizes:
    approx_val = centeral_derivative(np.sin, x_val, h)
    error = np.abs(approx_val - true_val)
    errors.append(error)
    
plt.plot(step_sizes, errors, 'o')
plt.title("Error vs Step Size (Log-Log Scale)")
plt.xlabel("Step Size (h)")
plt.ylabel("Absolute Error")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('error_scaling.png')
plt.show()
    

    
    