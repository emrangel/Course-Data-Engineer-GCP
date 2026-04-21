mkdir -p ~/.ssh

ssh-keygen -t ed25519 -C "<email@email.com>"
/c/Users/e.rangel/.ssh/id_ed25519_personal

ssh-keygen -t ed25519 -C "<email@email.com>"
/c/Users/e.rangel/.ssh/id_ed25519_trabajo

ssh -T git@github-personal
ssh -T git@github-trabajo

<!-- git remote set-url origin git@github-trabajo:TU_USUARIO_SECUNDARIO/NOMBRE_DEL_REPO.git -->

git config user.name "<username>"
git config user.email "<email@email.com>"

git config user.name "<username>"
git config user.email "<email@email.com>"


----

<!-- git remote add origin git@github-personal:TU_USUARIO_PERSONAL/NOMBRE_DEL_REPO.git -->

# all files
git add .

# Create commit with a message
git commit -m "Primer commit"

# branch principal is 'main'
git branch -M main

# Push to GitHub
git push -u origin main