# -*- rpm-spec -*-

Name: xemacs-git
Version: 0.01
Release: alt1

%define_xemacs_site_package git

Summary: XEmacs frontend to GIT
License: GPL
Group: Editors

Url: http://kernel.org/pub/software/scm/git
# :pserver:cvs@cvs.xemacs.org:/pack/xemacscvs XEmacs/packages/unsupported/scop/vc
Source0: %name.tar

BuildRequires: xemacs-base xemacs-dired xemacs-ediff xemacs-fsf-compat xemacs-pcl-cvs xemacs-xetla
Requires: xemacs-base xemacs-dired xemacs-ediff xemacs-fsf-compat xemacs-pcl-cvs xemacs-xetla

%description
XEmacs frontend to GIT revision control system.

%prep
%install
mkdir -p %buildroot%_xemacs_package_lisp_dir/%xemacs_package
tar xf %SOURCE0 -C %buildroot%_xemacs_package_lisp_dir/
%xemacs_package_make
%xemacs_package_find_files

%files -f %name-files

%changelog
* Sun Oct  1 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.01-alt1
- initial build
