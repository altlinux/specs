Name: xemacs-dictionary
Version: 1.16
Release: alt2

%define_xemacs_package dictionary

Summary: Interface to RFC2229 dictionary servers	
License: GPL
Group: Editors

%description
Interface to RFC2229 dictionary servers

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Tue Jun  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt2
- rebuilt

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.12-alt1
 - 1.12

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt1
- first build for %distribution distribution

