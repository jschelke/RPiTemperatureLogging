git add .

#echo 'Enter the commit message:'
$commitMessage = date

git commit -m "$commitMessage"

#echo 'Enter the name of the branch:'
read branch

git push origin master
