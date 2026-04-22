mkdir -p ~/.ssh

ssh-keygen -t ed25519 -C "<email@email.com>"
/c/Users/<userPC>/.ssh/id_ed25519_personal

ssh-keygen -t ed25519 -C "<email@email.com>"
/c/Users/<userPC>/.ssh/id_ed25519_trabajo

ssh -T git@github-personal
ssh -T git@github-trabajo

<!-- git remote set-url origin git@github-trabajo:TU_USUARIO_SECUNDARIO/NOMBRE_DEL_REPO.git -->

git config user.name "<username>"
git config user.email "<email@email.com>"

git config user.name "<username>"
git config user.email "<email@email.com>"


----------------------------------------
---------------------------------------

<!-- git remote add origin git@github-personal:TU_USUARIO_PERSONAL/NOMBRE_DEL_REPO.git -->

# all files
git add .

# Create commit with a message
git commit -m "Primer commit"

# branch principal is 'main'
git branch -M main

# Push to GitHub
git push -u origin main


-------


gcloud auth login
gcloud auth list
gcloud config list

gcloud config set account e.rangel@globant.com
gcloud config set project avianca-adbid-pl

gcloud auth application-default login

gcloud config set account emrangelacolm@gmail.com
gcloud config set project project-d0c76d9f-d27a-4298-8e3

gcloud auth application-default login


----
gcloud iam service-accounts create sa-cloud-functions \
    --description="Cuenta para ejecutar cloud functions" \
    --display-name="SA Cloud Function"

gcloud projects add-iam-policy-binding project-d0c76d9f-d27a-4298-8e3 \
    --member="serviceAccount:sa-cloud-functions@project-d0c76d9f-d27a-4298-8e3.iam.gserviceaccount.com" \
    --role="roles/storage.objectViewer"

cd functions/function-1

gcloud functions deploy sd-emra-hello-world \
  --gen2 \
  --runtime=python310 \
  --region=us-central1 \
  --trigger-http \
  --entry-point=hello_world \
  --service-account="sa-cloud-functions@project-d0c76d9f-d27a-4298-8e3.iam.gserviceaccount.com" \
  --allow-unauthenticated

----

gcloud components update

setx CLOUDSDK_PYTHON "C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\platform\bundledpython\python.exe"