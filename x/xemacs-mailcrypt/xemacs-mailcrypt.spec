Name: xemacs-mailcrypt
Version: 2.14
Release: alt3

%define_xemacs_package mailcrypt

Summary: mailcrypt mode for XEmacs
License: GPL
Group: Editors

%description
mailcrypt mode for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.14-alt3
- rebuilt in new env

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.14-alt2
- rebuilt in new env

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.14-alt1
- 2.14

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.13-alt1
- 2.13

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.12-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.12-alt1
- 2.12

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.11-alt1
- first build for %distribution distribution

