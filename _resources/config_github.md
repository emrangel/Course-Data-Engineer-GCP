# Configuration Guide: GitHub & Google Cloud CLI

This document contains essential commands and configurations for managing multiple GitHub accounts and Google Cloud SDK environments.

---

## 1. GitHub SSH Key Configuration

To manage multiple accounts (e.g., personal and work), generate separate SSH keys and configure your SSH client.

### Generate SSH Keys
```bash
# Create SSH directory if it doesn't exist
mkdir -p ~/.ssh

# Generate Personal Key
ssh-keygen -t ed25519 -C "your-personal-email@email.com"
# When prompted, save as: /c/Users/<userPC>/.ssh/id_ed25519_personal

# Generate Work Key
ssh-keygen -t ed25519 -C "your-work-email@email.com"
# When prompted, save as: /c/Users/<userPC>/.ssh/id_ed25519_trabajo
```

### Test SSH Connections
```bash
ssh -T git@github-personal
ssh -T git@github-trabajo
```

---

## 2. Git Configuration

### Local User Identity
Configure your username and email for the current repository.

```bash
# Set work identity
git config user.name "Your Name"
git config user.email "your-work-email@email.com"

# Set personal identity
git config user.name "Your Name"
git config user.email "your-personal-email@email.com"
```

### Remote URL Setup
Update the remote URL to use the specific SSH host defined in your `~/.ssh/config`.

```bash
# Examples:
# git remote set-url origin git@github-trabajo:ORGANIZATION/REPO_NAME.git
# git remote add origin git@github-personal:USERNAME/REPO_NAME.git
```

### Basic Git Workflow
```bash
# Add all changes
git add .

# Create commit
git commit -m "Your commit message"

# Ensure main branch name
git branch -M main

# Push to remote
git push -u origin main
```

---

## 3. Google Cloud CLI (gcloud) Configuration

### Authentication & Listing
```bash
# Login to gcloud
gcloud auth login

# List active accounts
gcloud auth list

# List current configuration
gcloud config list
```

### Switching Environments (Work vs. Personal)

#### Work Environment
```bash
gcloud config set account e.rangel@globant.com
gcloud config set project avianca-adbid-pl
gcloud auth application-default login
```

#### Personal Environment
```bash
gcloud config set account emrangelacolm@gmail.com
gcloud config set project project-d0c76d9f-d27a-4298-8e3
gcloud auth application-default login
```

---

## 4. IAM & Cloud Functions

### Service Account Management
```bash
# Create a service account for Cloud Functions
gcloud iam service-accounts create sa-cloud-functions \
    --description="Cuenta para ejecutar cloud functions" \
    --display-name="SA Cloud Function"

# Assign Storage Object Viewer role
gcloud projects add-iam-policy-binding project-d0c76d9f-d27a-4298-8e3 \
    --member="serviceAccount:sa-cloud-functions@project-d0c76d9f-d27a-4298-8e3.iam.gserviceaccount.com" \
    --role="roles/storage.objectViewer"
```

### Deploying a Cloud Function
Navigate to your function directory and deploy:
```bash
cd functions/function-1

gcloud functions deploy sd-emra-hello-world \
  --gen2 \
  --runtime=python310 \
  --region=us-central1 \
  --trigger-http \
  --entry-point=hello_world \
  --service-account="sa-cloud-functions@project-d0c76d9f-d27a-4298-8e3.iam.gserviceaccount.com" \
  --allow-unauthenticated
```

---

## 5. Maintenance & Environment

```bash
# Update gcloud components
gcloud components update

# Set Windows Environment Variable for Python (if needed)
setx CLOUDSDK_PYTHON "C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\platform\bundledpython\python.exe"
```
