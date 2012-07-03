Name: xemacs-viper
Version: 1.67
Release: alt1

%define_xemacs_package viper

Summary: VI emulation support
License: GPL
Group: Editors

%description
VI emulation support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.67-alt1
- 1.67

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.65-alt1
- 1.65

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.48-alt1
- 1.48

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.47-alt1
- 1.47

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.40-alt1
- 1.40

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.38-alt1
- 1.38

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.37-alt1
- 1.37

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.36-alt1
 - 1.36

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.35-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.35-alt1
- 1.35

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.34-alt1
- first build for %distribution distribution

