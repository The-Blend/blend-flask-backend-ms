const { GoogleGenerativeAI } = require("@google/generative-ai");
const fs = require("fs");
const genAI = new GoogleGenerativeAI("AIzaSyDzImntV-hrmMzqKclsQ6N7Pb-qUjbFDmM");

async function run() {
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});
const result = await model.generateContent([
""]
);
console.log(result.response.text());
}
run();




//AIzaSyDzImntV-hrmMzqKclsQ6N7Pb-qUjbFDmM