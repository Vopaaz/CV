set node_options=--openssl-legacy-provider 
call npm run icons
call npm run build

cd dist

call git init
call git add -A
call git commit -m 'deploy'

call git push -f git@github.com:Vopaaz/CV.git master:gh-pages
