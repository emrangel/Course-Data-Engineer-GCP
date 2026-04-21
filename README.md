mkdir -p ~/.ssh

ssh-keygen -t ed25519 -C "erriick1122@gmail.com"
/c/Users/e.rangel/.ssh/id_ed25519_personal

ssh-keygen -t ed25519 -C "e.rangel@globant.com"
/c/Users/e.rangel/.ssh/id_ed25519_trabajo

ssh -T git@github-personal
ssh -T git@github-trabajo

git remote set-url origin git@github-trabajo:TuUsuarioDeTrabajo/NombreDelRepo.git

git config user.name "emrangel"
git config user.email "erriick1122@gmail.com"

git config user.name "emraco"
git config user.email "e.rangel@globant.com"