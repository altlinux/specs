Name: xemacs-python-modes
Version: 1.14
Release: alt1.1

BuildRequires(pre): xemacsen
%define_xemacs_package python-modes

Summary: Python support
License: GPL
Group: Editors
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

BuildRequires: python-base

%description
Python editing support for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.14-alt1.1
- Rebuild with Python-2.7

* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Fri Dec 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1.1
- Rebuilt with python 2.6

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.06-alt2.1
- Rebuilt with python-2.5.

* Sat Apr  2 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt2
- rebuilt in new env

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt1
- 1.06

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.02-alt1
- 1.02

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.01-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.01-alt1
- first build for %distribution distribution

