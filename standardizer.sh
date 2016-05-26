old=( '"javascript"' '"JavaScript"' '"php"' '"HTML4"' '"CSS"' '"JQuery"' '"python"' '"angularjs"' '"AngularJS"' '"mongodb"' '"Angular.JS"' '"Rails"' '"asp.net-mvc"' '"mysql"' '"Postgres"' '"PostreSQL"' '"Jquery"' '"java"' '".net"' '"node.js"' '"git"' '"ruby"' '"NodeJS"'  )
new=( '"Javascript"' '"Javascript"' '"PHP"' '"HTML"' '"CSS3"' '"jQuery"' '"Python"' '"Angular.js"' '"Angular.js"' '"MongoDB"' '"Angular.js"' '"Rails"' '"ASP.NET"' '"MySQL"' '"PostgreSQL"' '"PostgreSQL"' '"jQuery"' '"Java"' '".NET"' '"Node.js"' '"Git"' '"Ruby"' '"Node.js"' )

for ((i=0;i<${#old[@]};i++))
do
  echo ${old[$i]}
    grep -o ${old[$i]} *.json | wc -l
    grep -o ${new[$i]} *.json | wc -l
  sed -i .bak "s/${old[$i]}/${new[$i]}/g" *.json
  echo ${new[$i]}
    grep -o ${new[$i]} *.json | wc -l
done
