# -*- rpm-spec -*-
# $Id: xemacs-mpg123,v 1.6 2005/11/12 14:12:51 me Exp $

%define __mule__ 1

Name: xemacs-mpg123
Version: 1.44
Release: alt0.3

%define_xemacs_site_package mpg123

Summary: XEmacs frontend to various audio players
License: GPL
Group: Editors

Requires: aumix-minimal mpg321 xemacs-fsf-compat

BuildRequires: xemacs-fsf-compat
Source0: %xemacs_package.el

%description
XEmacs frontend to various audio players, like mpg123 or ogg123

%prep
%install
%__install -p -m0644 -D %SOURCE0 \
  %buildroot%_xemacs_package_lisp_dir/%xemacs_package/%xemacs_package.el
%xemacs_package_make
%xemacs_package_find_files

%files -f %name-files

%changelog
* Sat Nov 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44-alt0.3
- buildreqs fixed

* Sun Nov  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44-alt0.2
- added requirements to aumix-minimal and mpg321

* Sun Mar 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44-alt0.1
- first attempt

