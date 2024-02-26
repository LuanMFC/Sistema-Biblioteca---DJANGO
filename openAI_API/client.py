import os
from openai import OpenAI
client = OpenAI(
    api_key= "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"
)
def get_book_synopsis(title, author, publishing_company, edition):
    messageSynopsis = '''
        Descreva uma sinopse do livro {} escrito por {}, da editora {} {} edição. Descreva em 300 caracteres.
    '''

    messageSynopsis = messageSynopsis.format(title, author, publishing_company, edition)
    response = client.chat.completions.create(
       max_tokens=1000,
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", 
                "content": messageSynopsis},
        ]
    )

    return response.choices[0].message.content