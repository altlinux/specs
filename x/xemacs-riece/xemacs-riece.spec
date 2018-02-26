Name: xemacs-riece
Version: 1.23
Release: alt1

%define_xemacs_package riece

Summary: IRC (Internet Relay Chat) client for XEmacs
License: GPL
Group: Networking/IRC

%description
IRC (Internet Relay Chat) client for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt1
- 1.23

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Nov 22 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.12-alt1
- first build for %distribution distribution

