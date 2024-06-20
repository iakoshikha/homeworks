// const basket = document.getElementById('basket');
// const boxs = document.getElementById('boxs');


// let name = 'iako'
// const surname = 'shikhshvili'
// var adress = 'rustavi'

// console.log()

// //or= ||

// if(name == 'iako' || name == 'nuca'){
//     console.log(true)

// }else if (num1 > 10 && num1 <15){
//     console.log(true)
// }

//len
//if,else
//or, and 
//let,const var
//stypeoff
//number
//  let i = 15 

//  while(10 > i){
//      console.log(i + 'hello')
// }


//  let userNumber = prompt("enter your promo code for shopping : ")

// (function(){

//     ("#cart-cartss").slideUp();
//     (".cart").on("click", function () {
//     ("#cart-cartss").slideToggle();
//     });

//     ("#cartss-basket").text("(" + (("#list-carts").children().length) + ")");

    
//     (".carts").on("click", function () {
//       ("#cart-cartss").slideDown();
//      setTimeout(function(){
//         ("#cart-cartss").slideUp();
//      }, 2000)
//       //add cartss to basket
//       (this).each(function () {
//         var name = (this).children(".carts-detail").children("h4").text();
//         var remove = "<button class='remove'> X </button>";
//         var cena = "<span class='eachPrice'>" + (parseFloat((this).children(".carts-detail").children(".prices").children(".price").text())) + "</span>";
//         ("#list-carts").append("<li>" + name + "&#09; - &#09;" + cena + "" + remove + "</li>");

//         //number of cartss in basket
//         ("#carts-basket").text("(" + (("#list-carts").children().length) + ")");
//         ("#carts-basket").text();
        
//           //calculate total price
//           var totalPrice = 0;
//             (".eachPrice").each(function (){ 
//               var cenaEach = parseFloat((this).text());
//               totalPrice+=cenaEach;
//             });
//             ("#total-price").text(totalPrice + "");
//       });

//       //remove cartss from basket
//       (".remove").on("click", function () {
//         (this).parent().remove();

//             var totalPrice = 0;
//             (".eachPrice").each(function (){ 
//             });
//             ("#total-price").text(totalPrice + "");
//         ("#cartss-basket").text("(" + (("#list-carts").children().length) + ")");
//       });
//     });
// })



const totalPrice = document.getElementById('totalPrice')
const btns = document.getElementsByClassName('basket')
const price = document.getElementsByClassName('discount')
const counter = document.getElementById('counter')
const minus = document.getElementById('minus')



let x = 0
// console.log(price[0].innerHTML)
let c = 0
let original = []
for (let index = 0; index < btns.length; index++) {
    btns[index].addEventListener('click',function(){
    //   console.log(price[index].innerHTML.slice(1,price[index].length))
      x += Number(price[index].innerHTML.slice(1,price[index].length))
      c++
      counter.innerHTML = c
      original.push (Number(price[index].innerHTML.slice(1,price[index].length)))
      totalPrice.innerHTML = x
    })
}

    console.log(original)
    
    minus.addEventListener('click',function(){
    if (original.length !==0) {
    totalPrice.innerHTML -= original[original.length-1]
    original.pop()
}
})









