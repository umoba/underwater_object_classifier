from pathlib import Path
import cv2


class ImageDataset:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)

        if not self.root_dir.exists():
            raise FileNotFoundError(
                f"Dataset directory does not exist: {root_dir}"
            )

        valid_extensions = {".jpg", ".jpeg", ".png"}

        self.class_names = sorted(
            path.name
            for path in self.root_dir.iterdir()
            if path.is_dir()
        )

        self.class_to_idx = {
            class_name: index
            for index, class_name in enumerate(self.class_names)
        }

        self.samples = []

        for class_name in self.class_names:
            class_dir = self.root_dir / class_name
            label = self.class_to_idx[class_name]

            for image_path in sorted(class_dir.iterdir()):
                if image_path.suffix.lower() in valid_extensions:
                    self.samples.append(
                        (image_path, label)
                    )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        image_path, label = self.samples[index]

        image = cv2.imread(str(image_path))

        if image is None:
            raise RuntimeError(
                f"Could not read image: {image_path}"
            )

        return image, label