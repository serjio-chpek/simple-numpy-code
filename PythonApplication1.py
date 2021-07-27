echo "# simple-numpy-code" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/serjio-chpek/simple-numpy-code.git
git push -u origin main
import nympy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1], 
                            [0,1,1]])
                            
training_outputs = np.array ([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) -1 

print("something:")
print(synaptic_weights)

for i in range (20000):

    input_layer = training_inputs
    outputs =  sigmoid (np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    adjustments = np.dot(init_layer.T, err * (outputs * (1-outputs)))
    synaptic_weights += adjustments

print (synaptic_weights)

print("Equal:")
print(outputs)