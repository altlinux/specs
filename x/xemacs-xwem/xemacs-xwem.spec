Name: xemacs-xwem
Version: 1.23
Release: alt1

%define_xemacs_package xwem

Summary: XEmacs Window Manager
License: GPL
Group: Graphical desktop/Other

%description
X Emacs Window Manager (sic!)

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt1
- 1.23

* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt2
- rebuilt in new env

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Wed Oct  6 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Mon Sep 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt2
- bash AI 'bout EMACS env var fooled

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Jun  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

