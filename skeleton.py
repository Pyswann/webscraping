import google.generativeai as genai


def table(dicti):
    codes = f'<!-- wp:table --><figure class="wp-block-table"><table>'
    for key, value in dicti.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += tr_data
    codes += '</tr></tbody></table></figure><!-- /wp:table -->'
    return codes


def h2_gen(txt):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{txt}</h2><!-- /wp:heading -->'


def h3_gen(txt):
    return f'<!-- wp:heading --><h3 class="wp-block-heading">{txt}</h3><!-- /wp:heading -->'


def h4_gen(txt):
    return f'<!-- wp:heading --><h4 class="wp-block-heading">{txt}</h4><!-- /wp:heading -->'


def image(link, name):
    return f'<!-- wp:image{{"align": "center", "sizeSlug": "large"}} --><figure class="wp-block-image aligncenter size-large"><img src="{link}" alt="{name}"/><figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'


def w_paragraph(txt):
    codes = f'<!-- wp:paragraph --><p>{txt}</p><!-- /wp:paragraph -->'
    return codes


def col_table(dicti):
    codes = '<!-- wp:table --><figure class="has-text-align-center"><table class="has-fixed-layout"><tbody>'
    row_index = 0
    for key, value in dicti.items():
        if value:
            f_data, l_data = value
        else:
            f_data, l_data = "", ""

        # Determine row color
        background_color = "ffe5d9" if row_index % 2 == 0 else "f28482"

        # Generate table row with background color
        tr_data = f'<tr style="background-color: {background_color};"><td>{key}:</td><td>{f_data}</td><td>{l_data}</td></tr>'
        codes += tr_data

        row_index += 1

    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes


b_info = (f'<!-- wp:table --><figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr><td '
          f'class="has-text-align-center" data-align="center">Price</td><td class="has-text-align-center" '
          f'data-align="center">Enter the Price</td><td class="has-text-align-center" data-align="center">'
          f'Enter the Price</td></tr><tr><td class="has-text-align-center" data-align="center">Best Place to Buy</td>'
          f'<td class="has-text-align-center" data-align="center">Loc</td><td class="has-text-align-center" '
          f'data-align="center">Loc</td></tr></tbody></table></figure><!-- /wp:table -->')


api_key = 'AIzaSyBJ_VMAkDCOpIAJ2cZaCqZahL2MYUSPPHQ'

genai.configure(api_key="AIzaSyBJ_VMAkDCOpIAJ2cZaCqZahL2MYUSPPHQ")


def gemini(prompt):
    generation_config = {
      "temperature": 1,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro",
                                  generation_config = generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])
    convo.send_message(prompt)
    return convo.last.text












