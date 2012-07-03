Name: xemacs-semantic
Version: 1.21
Release: alt1

%define_xemacs_package semantic

Summary: Semantic bovinator (Yacc/Lex for XEmacs)
License: GPL
Group: Editors

%description
Semantic bovinator (Yacc/Lex for XEmacs)

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt1
- 1.20

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.17-alt1
- 1.17

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.14-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.14-alt1
- 1.14

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt1
- first build for %distribution distribution

