def list_to_table(ls):
    '''Takes a generic list and converts it into an HTML table.'''
   start_str  = '<table>'
   for item in ls:
       start_str += '<tr><td>' + str (item) +'</tr></td>'
   start_str += '</table>'
   return start_str

def populate_template(template,vals):
    '''Takes a template and fills it in with a dictionary format: {placeholder: string}'''
    return template%vals



def TODOs_to_html(ls):
    ''' Takes the TODO list and converts it to HTML usinf generic functions. Returns a string with HTML format.'''
    table = list_to_table(ls)
    templ= open("template.txt")
    all_text = templ.read()
    string_output = populate_template(all_text,{"TODOs" : table})
    return string_output

    
    

