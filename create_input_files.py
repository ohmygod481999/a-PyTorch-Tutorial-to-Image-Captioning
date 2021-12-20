from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr8k',
                       karpathy_json_path='/content/drive/MyDrive/lame_caption_recommendation/flickr8k_translate/flickr7k9.json',
                       image_folder='/content/drive/MyDrive/lame_caption_recommendation/flickr8k_images',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/content/drive/MyDrive/lame_caption_recommendation/out_flickr8k',
                       max_len=50)
