Name: xemacs-ocaml
Version: 0.06
Release: alt1

%define_xemacs_package ocaml

Summary: Objective Caml editing support
License: GPL
Group: Editors

%description
Objective Caml editing support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.06-alt1
- 0.06

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.05-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.05-alt1
- 0.05

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.04-alt1
- 0.04

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.03-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.03-alt1
- first build for %distribution distribution

