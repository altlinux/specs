Name: xemacs-x-symbol
Version: 1.13
Release: alt1

%define_xemacs_package x-symbol

Summary: Semi WISIWYG for LaTeX, HTML, etc, using additional fonts
License: GPL
Group: Editors

%description
When you edit LaTeX, HTML, BibTeX or TeXinfo sources in Emacs,
package X-Symbol provides some kind of WYSIWYG by using real characters
for tokens like `\oplus' or `&trade;'.  It also provides various input
methods to insert these characters.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt2
- rebuilt in new env

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt1
- 1.07

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.05-alt1
 - 1.05

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.04-alt1
- 1.04

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.03-alt1
- first build for %distribution distribution

