#CODING PRACTICE PAGE

import streamlit as st

st.set_page_config(
    page_title="Level up your code!"
)

st.header("Practice Coding!")
st.write("Try some introductory coding problems!")
codingSelect = st.selectbox(
       "Choose a language:", 
       ("c++", "Python"),)


#practicing c++
if codingSelect == "c++":
    st.subheader("Leveling up c++")

    level1Done, level2Done, level3Done = false
    levelChoice = st.selectbox(
        "Choose a level:",
        ("Level 1", "Level 2", "Level 3"),
    )

    if levelChoice == "Level 1":
        st.subheader("Introduction to c++")
        st.write("C++ is a BLA BLABLA")
        st.write ("C++ is most useful BLAAA")

        st.write("Here, we go over the basics of a typical c++ file, and make a \"hello world\" program!")
        
        st.write("Let's go over this code line by line")
        fullCode = '''#include <iostream>
            using namespace std;
            
            int main() {
                cout << "Hi! Check out this text!" << endl;
                return 0;
            }'''
        st.code(fullCode, language='c++')
        st.write("Let's go over this code line by line")

        
        code1 = '''#include <iostream>'''
        st.code(code1, language='c++')
        st.write("There are certain built-in libraries that a programmer can include in their code to do certain actions.")
        st.write("For example, if someone wanted to calculate 2 to the power of 3, we would have to multiply 2 on itself multiple times. But if we included the csmath library, there is already a exponential operation")
        st.write("Here, we include the iostream library, because it gives us the cout command, which we will explain soon.")
        st.write("To include a library, we use #include followed by the library name surrounded by <>")

        code2 = '''using namespace std;'''
        st.write("Important names of variables and other objects must be written with \"std::\" in front if it to be recognized by the compiler, like the following example.")
        st.write("This means that the compiler will know what important symbols are without preluding them with \"std::\"")

        


    
