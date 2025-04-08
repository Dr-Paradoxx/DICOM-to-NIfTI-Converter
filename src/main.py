import os
from dicom_utils import gather_dicom_files, organize_series_by_modality
from nifti_converter import convert_series_to_nifti
from config import dicom_root, output_root

def process_dicom_directory():
    for folder in os.listdir(dicom_root):
        folder_path = os.path.join(dicom_root, folder)
        if os.path.isdir(folder_path):
            print(f'\nProcessing folder: {folder}')
            output_subfolder = os.path.join(output_root, folder)
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            dicom_files = gather_dicom_files(folder_path)
            series_dict = organize_series_by_modality(dicom_files)
            for modality, files in series_dict.items():
                if files:
                    output_path = os.path.join(output_subfolder, f'{modality.lower()}.nii.gz')
                    print(f'Converting {modality} series with {len(files)} slices...')
                    convert_series_to_nifti(files, output_path)
                else:
                    print(f'No {modality} series found in this folder.')

if __name__ == '__main__':
    process_dicom_directory()
