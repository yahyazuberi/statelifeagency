import streamlit as pt
import PyPDF2
import nltk
import hyperlink
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import base64
import webbrowser
from PIL import Image
import webbrowser

def main(h):
    #pt.sidebar.header("About")
    pt.title('STATE LIFE AGENCY ADMIN ')
    #openb = pt.button('Open Book')
    #if openb:
     #   webbrowser.open("https://dochub.com/statelifeproject/JWop0ZAKk2zjjmNRrYa9GP/master-pdf?dt=56xEgJiVrjArsvFxv6yi&pg=1")
    img=Image.open("images.jpeg")
    pt.image(img,width=300)
    query=pt.text_input('Enter Query Here')
    s=pt.button('Search')
    #pt.spinner('Searching ..')
    if s:
        
        test(query)
        
        if len(h)==0:
            pt.error("NO RESULT")
        else:
        #pr()
            pt.success('Successful')
            pt.header("Your result")
            for i in range(0,len(h),1):
                st=[]
                pg="https://dochub.com/statelifeproject/JWop0ZAKk2zjjmNRrYa9GP/master-pdf?dt=56xEgJiVrjArsvFxv6yi&pg="+str(h[i])
                st="The result is on page number "+str(h[i])
                st+=' click the link below to open this page'
                pt.subheader(st)
                pt.write(pg)
def test(query):
    
    vector=[]
    pdfFileObj = open('master.pdf', 'rb') 

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    # printing number of pages in pdf file 
    print(pdfReader.numPages)
     
    for i in range (0,133,1):
    # creating a page object
        tem=[]
        pageObj = pdfReader.getPage(i) 

    # extracting text from page 
        temp=pageObj.extractText()
        tem=temp.split()
        #tem=temp.split('.')
        #tem=temp.split('(')
        #tem=temp.split(')')
        vector.append(tem)

    # closing the pdf file object 
    pdfFileObj.close()
    #query = input("Enter your Query")
    q=[]
    q=query.split()
    vector.append(q)
     
    l=[]
    stop_words = set(stopwords.words('english')) 
    lemmatizer = WordNetLemmatizer()
    for j in range (0,len(vector),1):
        l=[]
        for i in range(0,len(vector[j]),1):
            vector[j][i]=lemmatizer.lemmatize(vector[j][i].lower())
            if vector[j][i]=='-' or vector[j][i]=='(' or vector[j][i]==')' or vector[j][i]=='' or vector[j][i]==' ' or vector[j][i]=='.':
                l.append(vector[j][i])
            for o in stop_words:
                if vector[j][i]== o :
                    l.append(vector[j][i])
        for word in l:
            vector[j].remove(word)
    nvec=[]
    for i in range(0,len(vector),1):
        st=''
        for j in range(0,len(vector[i]),1):
            st+=vector[i][j]
            st+=' '
            st=st.replace(':', '')
            st=st.replace('.', '')
            st=st.replace(',', '')
            st=st.replace(')', '')
            st=st.replace('(', '')
            #st=st.replace('-', '')
        nvec.append(st)
    #print(st)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(nvec)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    from sklearn.metrics.pairwise import cosine_similarity
    cos=[]
    b=[]
    for i in range(0,len(df)-1,1):
    #print(i)
        b.append(cosine_similarity(df.iloc[[i]],df.iloc[[len(df)-1]]))
    cos=[]
    for i in range(0,len(b),1):
        cos.append(b[i][0][0])
    while(max(cos)>=0.05):
        
        
        h.append(cos.index(max(cos))+1)
        #pt.header('Your result is on page #')
        #pt.subheader(h)
        #print(h)
        #print("page number",cos.index(max(cos))+1)
        cos[cos.index(max(cos))]=0
         

    #pdf_file='/home/yahya/Desktop/streamlit/master.pdf'    

    #base64_pdf = base64.b64encode(pdf_file.read('master.pdf')).decode('utf-8')
    #pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">' 
    #pt.markdown(pdf_display, unsafe_allow_html=True)   

    
            #pt.write(better_url.get(u'utm_source')[0])
# prints: https://github.com/python-hyper/
            
           
        #if pt.button('boook'):
            #@cache_on_button_press('Authenticate')
                
                #print('heelo')
                #webbrowser.open("http://www.pdf995.com/samples/pdf.pdf#page=5")
       

if __name__=='__main__':

    h=[]
    
    main(h)
    #print('oi')
    #prop(h)
#print("page number",cos.index(max(cos))+1)

