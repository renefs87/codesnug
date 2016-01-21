# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(related_name='owned_goals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=b'text', max_length=100, choices=[(b'abap', b'ABAP'), (b'actionscript', b'ActionScript'), (b'ada', b'ADA'), (b'apache_conf', b'Apache Conf'), (b'asciidoc', b'AsciiDoc'), (b'assembly_x86', b'Assembly x86'), (b'autohotkey', b'AutoHotKey'), (b'batchfile', b'BatchFile'), (b'c9search', b'C9Search'), (b'c_cpp', b'C/C++'), (b'cirru', b'Cirru'), (b'clojure', b'Clojure'), (b'cobol', b'Cobol'), (b'coffee', b'CoffeeScript'), (b'coldfusion', b'ColdFusion'), (b'csharp', b'C#'), (b'css', b'CSS'), (b'curly', b'Curly'), (b'd', b'D'), (b'dart', b'Dart'), (b'diff', b'Diff'), (b'dot', b'Dot'), (b'erlang', b'Erlang'), (b'ejs', b'EJS'), (b'forth', b'Forth'), (b'ftl', b'FreeMarker'), (b'gherkin', b'Gherkin'), (b'glsl', b'Glsl'), (b'golang', b'Go'), (b'groovy', b'Groovy'), (b'haml', b'HAML'), (b'handlebars', b'Handlebars'), (b'haskell', b'Haskell'), (b'haxe', b'haXe'), (b'html', b'HTML'), (b'html_ruby', b'HTML (Ruby)'), (b'ini', b'INI'), (b'jack', b'Jack'), (b'jade', b'Jade'), (b'java', b'Java'), (b'javascript', b'JavaScript'), (b'json', b'JSON'), (b'jsoniq', b'JSONiq'), (b'jsp', b'JSP'), (b'jsx', b'JSX'), (b'julia', b'Julia'), (b'latex', b'LaTeX'), (b'less', b'LESS'), (b'liquid', b'Liquid'), (b'lisp', b'Lisp'), (b'livescript', b'LiveScript'), (b'logiql', b'LogiQL'), (b'lsl', b'LSL'), (b'lua', b'Lua'), (b'luapage', b'LuaPage'), (b'lucene', b'Lucene'), (b'makefile', b'Makefile'), (b'matlab', b'MATLAB'), (b'markdown', b'Markdown'), (b'mel', b'MEL'), (b'mysql', b'MySQL'), (b'mushcode', b'MUSHCode'), (b'nix', b'Nix'), (b'objectivec', b'Objective-C'), (b'ocaml', b'OCaml'), (b'pascal', b'Pascal'), (b'perl', b'Perl'), (b'pgsql', b'pgSQL'), (b'php', b'PHP'), (b'powershell', b'Powershell'), (b'prolog', b'Prolog'), (b'properties', b'Properties'), (b'protobuf', b'Protobuf'), (b'python', b'Python'), (b'r', b'R'), (b'rdoc', b'RDoc'), (b'rhtml', b'RHTML'), (b'ruby', b'Ruby'), (b'rust', b'Rust'), (b'sass', b'SASS'), (b'scad', b'SCAD'), (b'scala', b'Scala'), (b'smarty', b'Smarty'), (b'scheme', b'Scheme'), (b'scss', b'SCSS'), (b'sh', b'SH'), (b'sjs', b'SJS'), (b'space', b'Space'), (b'snippets', b'snippets'), (b'soy_template', b'Soy Template'), (b'sql', b'SQL'), (b'stylus', b'Stylus'), (b'svg', b'SVG'), (b'tcl', b'Tcl'), (b'tex', b'Tex'), (b'text', b'Text'), (b'textile', b'Textile'), (b'toml', b'Toml'), (b'twig', b'Twig'), (b'typescript', b'Typescript'), (b'vbscript', b'VBScript'), (b'velocity', b'Velocity'), (b'verilog', b'Verilog'), (b'xml', b'XML'), (b'xquery', b'XQuery'), (b'yaml', b'YAML')])),
                ('version_number', models.IntegerField(default=1)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(related_name='owned_snippets', to=settings.AUTH_USER_MODEL)),
                ('goal', models.ForeignKey(related_name='snippets', to='goals.Goal')),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(related_name='owned_tags', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=b'text', max_length=100, choices=[(b'abap', b'ABAP'), (b'actionscript', b'ActionScript'), (b'ada', b'ADA'), (b'apache_conf', b'Apache Conf'), (b'asciidoc', b'AsciiDoc'), (b'assembly_x86', b'Assembly x86'), (b'autohotkey', b'AutoHotKey'), (b'batchfile', b'BatchFile'), (b'c9search', b'C9Search'), (b'c_cpp', b'C/C++'), (b'cirru', b'Cirru'), (b'clojure', b'Clojure'), (b'cobol', b'Cobol'), (b'coffee', b'CoffeeScript'), (b'coldfusion', b'ColdFusion'), (b'csharp', b'C#'), (b'css', b'CSS'), (b'curly', b'Curly'), (b'd', b'D'), (b'dart', b'Dart'), (b'diff', b'Diff'), (b'dot', b'Dot'), (b'erlang', b'Erlang'), (b'ejs', b'EJS'), (b'forth', b'Forth'), (b'ftl', b'FreeMarker'), (b'gherkin', b'Gherkin'), (b'glsl', b'Glsl'), (b'golang', b'Go'), (b'groovy', b'Groovy'), (b'haml', b'HAML'), (b'handlebars', b'Handlebars'), (b'haskell', b'Haskell'), (b'haxe', b'haXe'), (b'html', b'HTML'), (b'html_ruby', b'HTML (Ruby)'), (b'ini', b'INI'), (b'jack', b'Jack'), (b'jade', b'Jade'), (b'java', b'Java'), (b'javascript', b'JavaScript'), (b'json', b'JSON'), (b'jsoniq', b'JSONiq'), (b'jsp', b'JSP'), (b'jsx', b'JSX'), (b'julia', b'Julia'), (b'latex', b'LaTeX'), (b'less', b'LESS'), (b'liquid', b'Liquid'), (b'lisp', b'Lisp'), (b'livescript', b'LiveScript'), (b'logiql', b'LogiQL'), (b'lsl', b'LSL'), (b'lua', b'Lua'), (b'luapage', b'LuaPage'), (b'lucene', b'Lucene'), (b'makefile', b'Makefile'), (b'matlab', b'MATLAB'), (b'markdown', b'Markdown'), (b'mel', b'MEL'), (b'mysql', b'MySQL'), (b'mushcode', b'MUSHCode'), (b'nix', b'Nix'), (b'objectivec', b'Objective-C'), (b'ocaml', b'OCaml'), (b'pascal', b'Pascal'), (b'perl', b'Perl'), (b'pgsql', b'pgSQL'), (b'php', b'PHP'), (b'powershell', b'Powershell'), (b'prolog', b'Prolog'), (b'properties', b'Properties'), (b'protobuf', b'Protobuf'), (b'python', b'Python'), (b'r', b'R'), (b'rdoc', b'RDoc'), (b'rhtml', b'RHTML'), (b'ruby', b'Ruby'), (b'rust', b'Rust'), (b'sass', b'SASS'), (b'scad', b'SCAD'), (b'scala', b'Scala'), (b'smarty', b'Smarty'), (b'scheme', b'Scheme'), (b'scss', b'SCSS'), (b'sh', b'SH'), (b'sjs', b'SJS'), (b'space', b'Space'), (b'snippets', b'snippets'), (b'soy_template', b'Soy Template'), (b'sql', b'SQL'), (b'stylus', b'Stylus'), (b'svg', b'SVG'), (b'tcl', b'Tcl'), (b'tex', b'Tex'), (b'text', b'Text'), (b'textile', b'Textile'), (b'toml', b'Toml'), (b'twig', b'Twig'), (b'typescript', b'Typescript'), (b'vbscript', b'VBScript'), (b'velocity', b'Velocity'), (b'verilog', b'Verilog'), (b'xml', b'XML'), (b'xquery', b'XQuery'), (b'yaml', b'YAML')])),
                ('version_number', models.IntegerField(default=1)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='owned_versions', to=settings.AUTH_USER_MODEL)),
                ('snippet', models.ForeignKey(related_name='versions', to='goals.Snippet')),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(related_name='owned_workspaces', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='goal',
            name='tags',
            field=models.ManyToManyField(related_name='goals', to='goals.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='workspaces',
            field=models.ManyToManyField(related_name='goals', to='goals.Workspace', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='workspace',
            unique_together=set([('title', 'owner')]),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('snippet', 'version_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('title', 'owner')]),
        ),
        migrations.AlterUniqueTogether(
            name='goal',
            unique_together=set([('title', 'owner')]),
        ),
    ]
