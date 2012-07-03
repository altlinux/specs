Name: xemacs-latin-unity
Version: 1.20
Release: alt1

%define_xemacs_mule_package latin-unity

Summary: find single ISO 8859 character set to encode a buffer
License: GPL
Group: Editors

%description
find single ISO 8859 character set to encode a buffer

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt1
- 1.20

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sun Jan 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sun Dec 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt2
- rebuilt in new env

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.07-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.07-alt1
- 1.07

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.05-alt1
- first build for %distribution distribution

