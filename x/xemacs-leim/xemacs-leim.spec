Name: xemacs-leim
Version: 1.32
Release: alt1

%define_xemacs_mule_package leim

Summary: All non-English and non-Japanese language support
License: GPL
Group: Editors

%description
All non-English and non-Japanese language support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files
%_xemacs_package_lisp_dir/%xemacs_package/leim-list.el

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt1
- 1.28

* Sun Dec 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
 - 1.21

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.20-alt1
- 1.20

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.19-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.19-alt1
- 1.19

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.18-alt1
- first build for %distribution distribution

