from django.utils.translation import ugettext_lazy as _

LANGUAGE_CHOICES = (('abap', 'ABAP'),
                    ('actionscript', 'ActionScript'),
                    ('ada', 'ADA'),
                    ('apache_conf', 'Apache Conf'),
                    ('asciidoc', 'AsciiDoc'),
                    ('assembly_x86', 'Assembly x86'),
                    ('autohotkey', 'AutoHotKey'),
                    ('batchfile', 'BatchFile'),
                    ('c9search', 'C9Search'),
                    ('c_cpp', 'C/C++'),
                    ('cirru', 'Cirru'),
                    ('clojure', 'Clojure'),
                    ('cobol', 'Cobol'),
                    ('coffee', 'CoffeeScript'),
                    ('coldfusion', 'ColdFusion'),
                    ('csharp', 'C#'),
                    ('css', 'CSS'),
                    ('curly', 'Curly'),
                    ('d', 'D'),
                    ('dart', 'Dart'),
                    ('diff', 'Diff'),
                    ('dot', 'Dot'),
                    ('erlang', 'Erlang'),
                    ('ejs', 'EJS'),
                    ('forth', 'Forth'),
                    ('ftl', 'FreeMarker'),
                    ('gherkin', 'Gherkin'),
                    ('glsl', 'Glsl'),
                    ('golang', 'Go'),
                    ('groovy', 'Groovy'),
                    ('haml', 'HAML'),
                    ('handlebars', 'Handlebars'),
                    ('haskell', 'Haskell'),
                    ('haxe', 'haXe'),
                    ('html', 'HTML'),
                    ('html_ruby', 'HTML (Ruby)'),
                    ('ini', 'INI'),
                    ('jack', 'Jack'),
                    ('jade', 'Jade'),
                    ('java', 'Java'),
                    ('javascript', 'JavaScript'),
                    ('json', 'JSON'),
                    ('jsoniq', 'JSONiq'),
                    ('jsp', 'JSP'),
                    ('jsx', 'JSX'),
                    ('julia', 'Julia'),
                    ('latex', 'LaTeX'),
                    ('less', 'LESS'),
                    ('liquid', 'Liquid'),
                    ('lisp', 'Lisp'),
                    ('livescript', 'LiveScript'),
                    ('logiql', 'LogiQL'),
                    ('lsl', 'LSL'),
                    ('lua', 'Lua'),
                    ('luapage', 'LuaPage'),
                    ('lucene', 'Lucene'),
                    ('makefile', 'Makefile'),
                    ('matlab', 'MATLAB'),
                    ('markdown', 'Markdown'),
                    ('mel', 'MEL'),
                    ('mysql', 'MySQL'),
                    ('mushcode', 'MUSHCode'),
                    ('nix', 'Nix'),
                    ('objectivec', 'Objective-C'),
                    ('ocaml', 'OCaml'),
                    ('pascal', 'Pascal'),
                    ('perl', 'Perl'),
                    ('pgsql', 'pgSQL'),
                    ('php', 'PHP'),
                    ('powershell', 'Powershell'),
                    ('prolog', 'Prolog'),
                    ('properties', 'Properties'),
                    ('protobuf', 'Protobuf'),
                    ('python', 'Python'),
                    ('r', 'R'),
                    ('rdoc', 'RDoc'),
                    ('rhtml', 'RHTML'),
                    ('ruby', 'Ruby'),
                    ('rust', 'Rust'),
                    ('sass', 'SASS'),
                    ('scad', 'SCAD'),
                    ('scala', 'Scala'),
                    ('smarty', 'Smarty'),
                    ('scheme', 'Scheme'),
                    ('scss', 'SCSS'),
                    ('sh', 'SH'),
                    ('sjs', 'SJS'),
                    ('space', 'Space'),
                    ('snippets', 'snippets'),
                    ('soy_template', 'Soy Template'),
                    ('sql', 'SQL'),
                    ('stylus', 'Stylus'),
                    ('svg', 'SVG'),
                    ('tcl', 'Tcl'),
                    ('tex', 'Tex'),
                    ('text', 'Text'),
                    ('textile', 'Textile'),
                    ('toml', 'Toml'),
                    ('twig', 'Twig'),
                    ('typescript', 'Typescript'),
                    ('vbscript', 'VBScript'),
                    ('velocity', 'Velocity'),
                    ('verilog', 'Verilog'),
                    ('xml', 'XML'),
                    ('xquery', 'XQuery'),
                    ('yaml', 'YAML'),)

WORKSPACE_PERMISSIONS = (
    (0, _('Admin')),
    (1, _('Editor')),
    (2, _('Subscriber'))
)