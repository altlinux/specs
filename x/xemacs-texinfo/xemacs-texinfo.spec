Name: xemacs-texinfo
Version: 1.30
Release: alt2

%define_xemacs_package texinfo

Summary: XEmacs TeXinfo support
License: GPL
Group: Editors

%description
XEmacs TeXinfo support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.30-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.30-alt1
- 1.30

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.29-alt1
- 1.29

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt1
- 1.28

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.25-alt1
- 1.25

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.24-alt1
 - 1.24

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.23-alt1
- 1.23

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.21-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.21-alt1
- 1.21

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.20-alt1
- first build for %distribution distribution

