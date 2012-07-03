# -*- rpm-spec -*-
# $Id: xemacs-locate,v 1.3 2005/04/03 17:29:25 me Exp $

Name: xemacs-locate
Version: 0.01
Release: alt0.1

%define_xemacs_site_package locate

Summary: XEmacs frontend to locate command
License: GPL
Group: Editors

BuildRequires: xemacs-dired
Requires: xemacs-base xemacs-dired

Source0: %xemacs_package.el

%description
XEmacs frontend to locate command, borrowed from FSF Emacs

%prep
%install
%__install -p -m0644 -D %SOURCE0 \
  %buildroot%_xemacs_package_lisp_dir/%xemacs_package/%xemacs_package.el
%xemacs_package_make
%xemacs_package_find_files

%files -f %name-files

%changelog
* Sun Apr  3 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.01-alt0.1
- first attempt

