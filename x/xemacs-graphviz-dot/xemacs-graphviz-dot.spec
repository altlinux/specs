# -*- rpm-spec -*-
# $Id: xemacs-graphviz-dot,v 1.1 2005/06/13 18:19:15 me Exp $

Name: xemacs-graphviz-dot
Version: 0.01
Release: alt0.1

%define_xemacs_site_package graphviz-dot

Summary: XEmacs mode for GraphViz dot language
License: GPL
Group: Editors

Requires: graphviz xemacs-base

Source0: %xemacs_package-mode.el

%description
XEmacs mode for editing files in GraphViz dot language

%prep
%install
%__install -p -m0644 -D %SOURCE0 \
  %buildroot%_xemacs_package_lisp_dir/%xemacs_package/%xemacs_package.el
%xemacs_package_make
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon Jun 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.01-alt0.1
- author version 0.3.4

