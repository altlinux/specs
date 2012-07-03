Name: xemacs-vc
Version: 1.48
Release: alt1

%define_xemacs_package vc

Summary: Version Control for Free systems
License: GPL
Group: Editors

%description
Version Control for Free systems

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.48-alt1
- 1.48

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.45-alt1
- 1.45

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.41-alt1
- 1.41

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.40-alt1
- 1.40

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.38-alt1
- 1.38

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.37-alt1
 - 1.37

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.35-alt1
- 1.35

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.33-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.33-alt1
- first build for %distribution distribution

