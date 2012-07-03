Name: xemacs-locale
Version: 1.28
Release: alt1

%define_xemacs_mule_package locale

Summary: Localized menubars and localized splash screens
License: GPL
Group: Editors

%description
Localized menubars and localized splash screens

%prep
%setup -qc

%install
mkdir -p %buildroot%_xemacs_package_dir
cp -a . %buildroot%_xemacs_package_dir 

%files
%dir %_xemacs_package_etc_dir/start-files
%lang(fr) %_xemacs_package_etc_dir/start-files/fr
%lang(ja) %_xemacs_package_etc_dir/start-files/ja
%lang(ro) %_xemacs_package_etc_dir/start-files/ro
%dir %_xemacs_package_etc_dir/app-defaults
%lang(de) %_xemacs_package_etc_dir/app-defaults/de
%lang(fr) %_xemacs_package_etc_dir/app-defaults/fr
%lang(ja) %_xemacs_package_etc_dir/app-defaults/ja
%lang(ro) %_xemacs_package_etc_dir/app-defaults/ro
%dir %_xemacs_package_lisp_dir/locale
%_xemacs_package_lisp_dir/locale/_pkg.el
%_xemacs_package_lisp_dir/locale/auto-autoloads.elc

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt1
- 1.28

* Sun Dec 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt2
- rebuilt in new env

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.20-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.20-alt1
- 1.20

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.19-alt1
- 1.19

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.18-alt1
- first build for %distribution distribution

