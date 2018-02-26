%define pear_name HTML_Template_Xipe

Name: pear-HTML_Template_Xipe
Version: 1.7.6
Release: alt3

Summary: A simple, fast and powerful template engine

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTML_Template_Xipe

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Template_Xipe-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Tree >= 0.2, pear-Log >= 1.8

%description
The template engine is a compiling engine, all templates are compiled into
PHP-files.
This will make the delivery of the files faster on the next request, since
the template
doesn't need to be compiled again. If the template changes it will be
recompiled.

There is no new template language to learn. Beside the default mode, there
is a set of constructs
since version 1.6 which allow you to edit your templates with WYSIWYG
editors.

By default the template engine uses indention for building blocks (you can
turn that off).
This feature was inspired by Python and by the need I felt to force myself
to write proper HTML-code, using proper indentions, to make the code
better readable.

Every template is customizable in multiple ways. You can configure each
template or an entire directory to use different delimiters, caching
parameters, etc.
via either an XML-file or a XML-chunk which you simply write anywhere
inside the tpl-code.

Using the Cache the final file can also be cached (i.e. a resulting
HTML-file).  The caching options can be customized as needed. The cache
can reduce the server load by very much, since the entire php-file
doesn't need to be processed again, the resulting client-readable data
are simply delivered right from the cache (the data are saved using
php's output buffering).

The template engine is prepared to be used for multi-language applications
too.  If you i.e. use the PEAR::I18N for translating the template,
the compiled templates need to be saved under a different name for each
language.  The template engine is prepared for that too, it saves the
compiled template including the language code if required (i.e. a compiled
index.tpl which is saved for english gets the filename index.tpl.en.php).

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/HTML/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt1
- initial build for ALT Linux Sisyphus

