Name: xemacs-general-docs
Version: 1.06
Release: alt1

%define_xemacs_package general-docs

Summary: General XEmacs documentation
License: GPL
Group: Editors

%description
General XEmacs documentation.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt1
- 1.06

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt1
- 1.04

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

