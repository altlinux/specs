# -*- rpm-spec -*-
# $Id: xemacs-psvn,v 1.6 2006/03/07 13:20:27 me Exp $

Name: xemacs-psvn
Version: 0.02
Release: alt2

%define_xemacs_site_package psvn

Summary: XEmacs frontend to Subversion
License: GPL
Group: Editors

Url: http://xsteve.nit.at/prg/emacs/
Source: %url/psvn.el

BuildRequires: xemacs-dired xemacs-ediff
Requires: xemacs-base xemacs-dired xemacs-ediff

%description
XEmacs frontend to Subversion revision control system

%prep
%install
%__install -p -m0644 -D %SOURCE0 \
  %buildroot%_xemacs_package_lisp_dir/%xemacs_package/%xemacs_package.el
%xemacs_package_make
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue Mar  7 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.02-alt2
- proper tempfile creation (morozov@)

* Mon Nov  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.02-alt1
- updated from upstream

* Sun Mar 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.01-alt1
- updated, rebuilt against recent xemacs rpm macro

* Sun Jul  4 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.01-alt0.1
- first build for %distribution distribution

