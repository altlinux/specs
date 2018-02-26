Name: xemacs-guided-tour
Version: 0.52
Release: alt1

%define_xemacs_package guided-tour

Summary: Phil Sung's Guided Tour of Emacs.
License: GPL
Group: Editors

%description
Phil Sung's Guided Tour of Emacs.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.52-alt1
- 0.52

