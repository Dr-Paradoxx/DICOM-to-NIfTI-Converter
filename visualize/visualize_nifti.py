import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

def load_nifti_file(file_path):
    """Load a NIfTI file and return the image data."""
    nifti_img = nib.load(file_path)
    return nifti_img.get_fdata()

def plot_middle_slices(image_data):
    """Plot the middle slice from each orthogonal plane of the image data."""
    # Calculate the middle index for each axis
    z_middle = image_data.shape[2] // 2
    y_middle = image_data.shape[1] // 2
    x_middle = image_data.shape[0] // 2

    # Create subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Axial view
    axes[0].imshow(image_data[:, :, z_middle].T, cmap='gray', origin='lower')
    axes[0].set_title('Axial View')

    # Coronal view
    axes[1].imshow(image_data[:, y_middle, :].T, cmap='gray', origin='lower')
    axes[1].set_title('Coronal View')

    # Sagittal view
    axes[2].imshow(image_data[x_middle, :, :].T, cmap='gray', origin='lower')
    axes[2].set_title('Sagittal View')

    # Hide axes and display the plot
    for ax in axes:
        ax.axis('off')
    plt.show()

if __name__ == '__main__':
    # Example usage
    file_path = 'path/to/your/nifti/file.nii'
    image_data = load_nifti_file(file_path)
    plot_middle_slices(image_data)