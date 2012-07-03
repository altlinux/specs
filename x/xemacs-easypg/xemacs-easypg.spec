Name: xemacs-easypg
Version: 1.03
Release: alt1

%define_xemacs_package easypg

Summary: GnuPG interface for Emacs.
License: GPL
Group: Editors

%description
GnuPG interface for Emacs.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt1
- 1.02

