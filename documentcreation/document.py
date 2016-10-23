import subprocess

__author__ = 'Jonathan Morton'
import os

import jinja2

from api.models import Foreclosure

latex_jinja_env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.abspath('documentcreation/template'))
)
template = latex_jinja_env.get_template('jinja-letter.tex')


def make_tex():
    global django_forclosures
    django_forclosures = Foreclosure.objects.filter(state__contains="NJ")
    with open('documentcreation/template/letter-header.tex', 'r') as f:
        header = f.read()
    with open('documentcreation/template/letter-footer.tex', 'r') as f:
        footer = f.read()
    with open('documentcreation/template/letter.tex', "w") as f:
        pass
    with open('documentcreation/template/letter.tex', "a") as f:
        f.write(header)
        for foreclosure in django_forclosures[:100]:
            stripped_address = foreclosure.address.strip("#").strip("&")
            if "#" in stripped_address or "&" in stripped_address:
                continue
            f.write(template.render(
                name=foreclosure.name,
                address=stripped_address,
                sale_date=foreclosure.sale_date,
                zip=foreclosure.zip,
                state=foreclosure.state,
                city=foreclosure.city
            ))
        f.write(footer)
    tex_dir = os.getcwd() + "/documentcreation/template/"
    print(tex_dir)
    p = subprocess.Popen(["pdflatex", "letter.tex"], cwd=tex_dir)
    p.wait()
