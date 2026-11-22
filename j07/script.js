let n = 101;
str_n = String(n);

let reversed_n;

for (i = str_n.length; i >= 0; i--){
    reversed_n += str_n[i]
}

if (+reversed_n == n) console.log("YES");
else console.log("NO");

console.log(reversed_n);

