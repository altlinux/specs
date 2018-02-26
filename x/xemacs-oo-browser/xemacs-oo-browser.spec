Name: xemacs-oo-browser
Version: 1.05
Release: alt1

%define_xemacs_package oo-browser

Summary: The Multi-language Object-Oriented Code Browser
License: GPL
Group: Editors

%description
The OO-Browser (pronounced owe-owe-browse-er) is a multi-windowed,
interactive, object-oriented class browser designed for professional
use.  It is one of the world's most powerful tools for exploring and
developing object-oriented software.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files
%_xemacs_package_lisp_dir/%xemacs_package/BR-*
%_xemacs_package_lisp_dir/%xemacs_package/br-c-tags
%_xemacs_package_lisp_dir/%xemacs_package/br-help*
%_xemacs_package_lisp_dir/%xemacs_package/Make-Env

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt1
- 1.04

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

