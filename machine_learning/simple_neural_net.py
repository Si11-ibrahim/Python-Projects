"""
Simple Neural Network Example - Step by Step
============================================

This is a simplified version to help you understand neural networks basics.
We'll create a very simple network to understand the core concepts.

Key Concepts Covered:
1. What is a neural network?
2. How do layers work?
3. Training process
4. Making predictions
"""

import tensorflow as tf
import numpy as np

# Set random seed for consistent results
tf.random.set_seed(42)

def simple_example():
    """
    A very simple neural network example with synthetic data.
    This helps understand the basic concepts without complex data.
    """
    print("=== SIMPLE NEURAL NETWORK EXAMPLE ===\n")
    
    # Create simple synthetic data
    # Let's say we want to learn the pattern: y = 2*x + 1
    print("1. Creating synthetic data:")
    x_data = np.array([[1], [2], [3], [4], [5]], dtype=float)
    y_data = np.array([[3], [5], [7], [9], [11]], dtype=float)  # 2*x + 1
    
    print(f"Input data (x): {x_data.flatten()}")
    print(f"Output data (y): {y_data.flatten()}")
    print("Pattern: y = 2*x + 1\n")
    
    # Create a simple neural network with just one neuron
    print("2. Creating neural network:")
    model = tf.keras.Sequential([
        # One dense layer with 1 neuron (this will learn the pattern)
        tf.keras.layers.Dense(1, input_shape=[1])
    ])
    
    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')
    print("   - Created 1 layer with 1 neuron")
    print("   - Using Adam optimizer and Mean Squared Error loss\n")
    
    # Train the model
    print("3. Training the neural network:")
    print("   The network will try to learn the pattern y = 2*x + 1")
    
    history = model.fit(x_data, y_data, epochs=1000, verbose=0)
    
    print(f"   Training completed! Final loss: {history.history['loss'][-1]:.6f}\n")
    
    # Test the model
    print("4. Testing the trained model:")
    test_x = np.array([[6], [7], [8]])
    predictions = model.predict(test_x, verbose=0)
    
    for i, x_val in enumerate(test_x.flatten()):
        expected = 2 * x_val + 1
        predicted = predictions[i][0]
        print(f"   Input: {x_val}, Expected: {expected}, Predicted: {predicted:.2f}")
    
    # Show what the network learned
    weights = model.get_weights()
    print(f"\n5. What the network learned:")
    print(f"   Weight (slope): {weights[0][0][0]:.2f} (should be close to 2)")
    print(f"   Bias (intercept): {weights[1][0]:.2f} (should be close to 1)")

def neural_network_concepts():
    """
    Explain key neural network concepts with examples.
    """
    print("\n" + "="*60)
    print("NEURAL NETWORK CONCEPTS EXPLAINED")
    print("="*60 + "\n")
    
    print("🧠 WHAT IS A NEURAL NETWORK?")
    print("   A neural network is inspired by how brain neurons work.")
    print("   It consists of interconnected nodes (neurons) that process information.\n")
    
    print("🔗 LAYERS:")
    print("   - Input Layer: Receives the raw data")
    print("   - Hidden Layer(s): Process and transform the data")
    print("   - Output Layer: Produces the final result\n")
    
    print("⚡ ACTIVATION FUNCTIONS:")
    print("   - ReLU: f(x) = max(0, x) - Most common, simple and effective")
    print("   - Sigmoid: f(x) = 1/(1+e^-x) - Outputs between 0 and 1")
    print("   - Softmax: Converts outputs to probabilities that sum to 1\n")
    
    print("📚 TRAINING PROCESS:")
    print("   1. Forward Pass: Data flows through network to make prediction")
    print("   2. Calculate Loss: Compare prediction with actual answer")
    print("   3. Backward Pass: Adjust weights to reduce error")
    print("   4. Repeat: Do this many times with different data samples\n")
    
    print("🎯 KEY TERMS:")
    print("   - Epoch: One complete pass through all training data")
    print("   - Batch Size: Number of samples processed before updating weights")
    print("   - Learning Rate: How big steps to take when adjusting weights")
    print("   - Loss Function: Measures how wrong our predictions are")
    print("   - Optimizer: Algorithm that adjusts weights (like Adam, SGD)\n")

def main():
    """
    Run both examples to understand neural networks.
    """
    print("LEARNING NEURAL NETWORKS - BASIC CONCEPTS")
    print("="*50)
    
    # Run simple example first
    simple_example()
    
    # Explain concepts
    # neural_network_concepts()
    
    print("🎉 CONGRATULATIONS!")
    print("You've learned the basics of neural networks!")
    print("\nNext steps:")
    print("- Run the main neural_net.py for a more complex example")
    print("- Try modifying the network architecture")
    print("- Experiment with different datasets")

if __name__ == "__main__":
    main()