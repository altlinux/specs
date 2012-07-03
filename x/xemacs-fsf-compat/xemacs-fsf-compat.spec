Name: xemacs-fsf-compat
Version: 1.19
Release: alt1

%define_xemacs_package fsf-compat

Summary: FSF Emacs compatibility files
License: GPL
Group: Editors

%description
FSF Emacs compatibility files

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.12-alt1
- 1.12

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt1
- first build for %distribution distribution

