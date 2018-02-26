Name: xemacs-hyperbole
Version: 1.17
Release: alt1

%define_xemacs_package hyperbole

Patch: hyperbole-1.17-infodir.patch

Summary: Everyday net-centric information management system
License: GPL
Group: Editors

%description
Everyday net-centric information management system.
Includes context-sensitive mouse and keyboard support,
a powerful contact manager, an autonumbered outliner
with hyperlink anchors for each outline cell, and extensible
hypertext facilities including hyperlinks in mail and news messages.

%prep
%setup -qc
%patch -p1

%install
%xemacs_package_install
rm -f -- %buildroot%_xemacs_infodir/hyperbole.*
%xemacs_package_find_files

%files -f %name-files
%_xemacs_package_lisp_dir/%xemacs_package/DEMO
%_xemacs_package_lisp_dir/%xemacs_package/h-skip-bytec.lsp

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

