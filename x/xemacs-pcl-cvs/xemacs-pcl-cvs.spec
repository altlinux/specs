Name: xemacs-pcl-cvs
Version: 1.70
Release: alt1

%define_xemacs_package pcl-cvs

Patch: %xemacs_package-1.63-alt-pty.patch

BuildRequires: xemacs-base xemacs-elib xemacs-dired xemacs-vc

Summary: CVS frontend
License: GPL
Group: Editors

%description
PCL-CVS is a front-end to CVS.  It integrates the most
frequently used CVS commands into emacs.

%prep
%setup -qc
%patch0 -p1

%build
%xemacs_byterecompile -C lisp/pcl-cvs

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.70-alt1
- 1.70

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.68-alt1
- 1.68

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.66-alt2
- pty patch resurrected

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.66-alt1
- 1.66

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.65-alt1
- 1.65

* Tue Mar 11 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.64-alt1
- 1.64

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.63-alt3
- #1531 fixed

* Mon Sep  9 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.63-alt2
- fixed parse errors on large directories

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.63-alt1
- first build for %distribution distribution

