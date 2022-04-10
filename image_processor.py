from PIL import Image


class ImageProcessor:
    def __init__(self, image_path, watermark_path, save_path):
        self.image_path = image_path
        self.watermark_path = watermark_path
        self.save_path = save_path
        self.merged_image = None

    def merge_image(self):
        try:
            image = Image.open(self.image_path)
        except:
            print(f"Processor => Error while opening '{self.image_path}'. Is the path correct?")

        try:
            watermark = Image.open(self.watermark_path)
            watermark.putalpha(80)
        except:
            print(f"Processor => Error while opening '{self.watermark_path}'. Is the path correct?")

        bg_w = image.size[0]
        bg_h = image.size[1]
        resulting_image = Image.new("RGBA", (bg_w, bg_h))

        resulting_image.paste(image)

        wm_w, wm_h = watermark.size

        offset = (int((bg_w - wm_w) * 0.98), int((bg_h - wm_h) * 0.98))

        resulting_image.paste(watermark, offset, watermark)

        self.merged_image = resulting_image

    def show_merged_image(self):
        if self.merged_image == None:
            print("Processor => Unable to show merged image. There is no merged image.\nDid you run merge_image()?")
            return 1
        else:
            self.merged_image.show(title="Merged Image")
            return 0

    def save_merged_image(self):
        # try:
        print(self.save_path)
        if self.save_path == "":
            self.save_path == "."
        else:
            self.merged_image.save(f"{self.save_path}/MergedImage.png")
        #     return 0
        # except:
        #     print("Processor => Unable to save the image.")
        #     return 1


if __name__ == "__main__":
    processor = ImageProcessor(image_path="./background.jpg", watermark_path="./smaple_watermark.jpg", save_path="./")

    processor.merge_image()

    processor.show_merged_image()

    processor.save_merged_image()