Name: xemacs-calendar
Version: 1.38
Release: alt1

%define_xemacs_package calendar

Summary: Calendar and diary support
License: GPL
Group: Editors

%description
Calendar and diary support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.38-alt1
- 1.38

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt2
- rebuilt in new env

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt1
- 1.23

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
 - 1.21

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.19-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.19-alt1
- 1.19

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.18-alt1
- first build for %distribution distribution
