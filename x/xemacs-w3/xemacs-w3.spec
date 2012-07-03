Name: xemacs-w3
Version: 1.35
Release: alt1

%define_xemacs_package w3

Summary: A Web browser
License: GPL
Group: Editors

%description
A Web browser

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.35-alt1
- 1.35

* Sun Jan 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.31-alt1
- 1.31

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.30-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.30-alt1
- 1.30

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.29-alt1
- 1.29

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.28-alt1
- 1.28

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.26-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.26-alt1
- 1.26

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.25-alt1
- first build for %distribution distribution

