"""
====================================================
  ResNet18 Training Script — run this in Google Colab
====================================================
STEP 1: Open https://colab.research.google.com
STEP 2: New notebook → paste this entire file → Runtime > Run All
STEP 3: After training, upload the saved .pt to Google Drive
STEP 4: Get file ID → paste into GDRIVE_FILE_ID in app.py
"""

# ---------- MOUNT DRIVE ----------
from google.colab import drive
drive.mount('/content/drive')

# ⚠️  CHANGE THIS to where your PlantVillage dataset folder is on Drive
DATA_DIR   = "/content/drive/MyDrive/PlantVillage"
SAVE_PATH  = "/content/drive/MyDrive/plant_disease_model_1_latest.pt"
NUM_CLASSES = 39
EPOCHS      = 3        # 3 is enough with pretrained ImageNet weights
BATCH_SIZE  = 32

# ---------- IMPORTS ----------
import torch, torch.nn as nn
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader

# ---------- DATA ----------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

dataset = datasets.ImageFolder(DATA_DIR, transform=transform)
loader  = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
print(f"Classes found: {len(dataset.classes)}")

# ---------- MODEL ----------
model = models.resnet18(pretrained=True)        # pretrained = fast convergence
model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)

device = "cuda" if torch.cuda.is_available() else "cpu"
model  = model.to(device)
print(f"Training on: {device}")

# ---------- TRAIN ----------
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(EPOCHS):
    model.train()
    correct = total = loss_sum = 0
    for imgs, labels in loader:
        imgs, labels = imgs.to(device), labels.to(device)
        optimizer.zero_grad()
        out  = model(imgs)
        loss = criterion(out, labels)
        loss.backward()
        optimizer.step()
        loss_sum += loss.item()
        correct  += out.argmax(1).eq(labels).sum().item()
        total    += labels.size(0)
    print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {loss_sum/len(loader):.4f} | Acc: {100*correct/total:.1f}%")

# ---------- SAVE ----------
torch.save(model.state_dict(), SAVE_PATH)
print(f"\n✅ Model saved to: {SAVE_PATH}")
print("Now open that file in Drive → Share → Anyone with link → copy the ID")
print("Paste the ID into GDRIVE_FILE_ID in app.py")
