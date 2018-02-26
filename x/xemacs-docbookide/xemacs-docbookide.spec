Name: xemacs-docbookide
Version: 0.08
Release: alt1

%define_xemacs_package docbookide

Summary: DocBook editing support
License: GPL
Group: Editors

%description
DocBook editing support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.08-alt1
- 0.08

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.07-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.07-alt1
- 0.07

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.06-alt1
- 0.06

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.05-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.05-alt1
- first build for %distribution distribution

