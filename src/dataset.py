from pathlib import Path
import cv2 as cv

class ImageDataset:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        if not self.root_dir.exists():
            raise FileNotFoundError(
                f"Dataset directory does not exist: {root_dir}"
            )

        valid_extensions = {".jpg", ".jpeg", ".png"}
        self.image_paths = sorted(
            path
            for path in self.root_dir.iterdir()
            if path.suffix.lower() in valid_extensions
        )

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        image_path = self.image_paths[index]
        image = cv.imread(str(image_path))

        if image is None:
            raise RuntimeError(
                f"Could not read image: {image_path}"
            )

        return image