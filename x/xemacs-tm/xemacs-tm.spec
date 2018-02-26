Name: xemacs-tm
Version: 1.39
Release: alt1

%define_xemacs_package tm

Patch: tm-1.39-infodir.patch

Summary: Emacs MIME support. Not needed for gnus >= 5.8.0
License: GPL
Group: Editors

%description
Emacs MIME support. Not needed for gnus >= 5.8.0

%prep
%setup -qc
%patch -p1

%install
%xemacs_package_install
rm -f -- %buildroot%_xemacs_infodir/tm-view-ja.*
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.39-alt1
- 1.39

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.38-alt1
- 1.38

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.37-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.37-alt1
- 1.37

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.36-alt1
 - 1.36

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.35-alt1
- 1.35

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.34-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.34-alt1
- first build for %distribution distribution

