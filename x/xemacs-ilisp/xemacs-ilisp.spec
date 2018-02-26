Name: xemacs-ilisp
Version: 1.36
Release: alt1

%define_xemacs_package ilisp

Summary: Front-end for Inferior Lisp
License: GPL
Group: Editors

%description
Front-end for Inferior Lisp

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files
cp -p lisp/%xemacs_package/extra/README README.extra
cp -p lisp/%xemacs_package/ilisp.emacs .

%files -f %name-files
%doc lisp/%xemacs_package/[A-Z]* README.extra ilisp.emacs
%_xemacs_package_lisp_dir/%xemacs_package/*.lisp
%_xemacs_package_lisp_dir/%xemacs_package/*.scm

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.36-alt1
- 1.36

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.34-alt1
- 1.34

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.33-alt2
- some missed files resurreced

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.33-alt1
- 1.33

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.32-alt1
 - 1.32

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.31-alt1
 - 1.31

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.29-alt1
- 1.29

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.28-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.28-alt1
- 1.28

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.27-alt1
- first build for %distribution distribution

