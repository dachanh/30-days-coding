import tensorflow as tf 
from tensorflow as keras 
from tensorflow.keras import layers

def vgg_block(num_convs,num_channels):
    blocks = keras.Sequential()
    for _ in range(num_convs):
        blocks.add(layers.Conv2D(num_channels,kernel_size=3,padding=1,activation='relu'))
    blocks.add(tf.keras.MaxPool2D(pool_size=2,strides=2))
    return blocks
def VGG11_models(conv_arch):
    net = keras.Sequential()
    for (num_convs,num_channels) in conv_arch:
        net.add(vgg_block(num_convs,num_channels))
    net.add(tf.keras.Dense(4096,activation='relu'),tf.keras.Dropout(0.5))
    net.add(tf.keras.Dense(4096,activation='relu'),tf.keras.Dropout(0.5))
    net.add(tf.keras.Dense(10,activation='softmax'))
    return net 

def main():
    datasets = keras.datasets.fashion_mnist
    (X_train,y_train), (X_test,y_test) = datasets.load_data()


if __name__ == "__main__":
    main()