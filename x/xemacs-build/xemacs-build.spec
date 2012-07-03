Name: xemacs-build
Version: 1.15
Release: alt1

%define_xemacs_package build

Summary: Build XEmacs from within
License: GPL
Group: Editors

%description
Build XEmacs from within

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.10-alt1
- 1.10

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.07-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.07-alt1
- 1.07

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.06-alt1
- first build for %distribution distribution

