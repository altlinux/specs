Name: xemacs-speedbar
Version: 1.29
Release: alt1

%define_xemacs_package speedbar

Summary: Provides a separate frame with convenient references
License: GPL
Group: Editors

%description
Provides a separate frame with convenient references

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.29-alt1
- 1.29

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt1
- 1.28

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt1
- 1.27

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.26-alt1
- 1.26

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.24-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.24-alt1
- 1.24

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.23-alt1
- first build for %distribution distribution

