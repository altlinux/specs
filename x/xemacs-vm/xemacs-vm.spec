Name: xemacs-vm
Version: 8.08
Release: alt1

%define_xemacs_package vm

Summary: An Emacs mailer
License: GPL
Group: Networking/Mail

%description
An Emacs mailer

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.08-alt1
- 8.08

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.07-alt1
- 8.07

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.22-alt1
- 7.22

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.19-alt1
- 7.19

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.18-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.18-alt1
- 7.18

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.17-alt1
- 7.17

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 7.14-alt1
 - 7.14

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 7.07-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 7.07-alt1
- first build for %distribution distribution

