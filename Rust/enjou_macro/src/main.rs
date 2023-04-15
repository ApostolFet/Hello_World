use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;


#[derive(HelloMacro)]
struct MyStruct;

fn main(){
    MyStruct::hello_macro();
}