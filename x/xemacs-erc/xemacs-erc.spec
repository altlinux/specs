Name: xemacs-erc
Version: 0.23
Release: alt1

%define_xemacs_package erc

Summary: IRC client for Emacs
License: GPL
Group: Networking/IRC

%description
%name is a IRC client for Emacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23-alt1
- 0.23

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22-alt1
- 0.22

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21-alt1
- 0.21

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19-alt1
- 0.19

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17-alt1
- 0.17

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15-alt1
- 0.15

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12-alt1
- 0.12

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.09-alt1
- 0.09

* Sat Feb  7 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.05-alt1
- 0.05

