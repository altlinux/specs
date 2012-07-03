Name: xemacs-cogre
Version: 1.02
Release: alt1

%define_xemacs_package cogre

Summary: Graph editing mode.
License: GPL
Group: Editors

%description
Graph editing mode.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt1
- 1.02

