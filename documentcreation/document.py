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
    loader=jinja2.FileSystemLoader(os.path.abspath('.'))
)
template = latex_jinja_env.get_template('jinja-document.tex')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vega.settings")
django_forclosures = Foreclosure.objects.filter(city__icontains="Camden")
print(template.render(foreclosures=django_forclosures))
