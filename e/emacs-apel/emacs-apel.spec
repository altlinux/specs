# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-apel.spec,v 1.1 2005/11/06 17:40:52 eugene Exp $

%define cvsversion 20050606
%define pkg_name apel

Version: 10.6
Release: alt1.%cvsversion
Name: emacs-%pkg_name
Copyright: GPL
Group: Editors
Summary: A Portable Emacs Library
Requires: emacs-common
Url: ftp://ftp.m17n.org/pub/mule/apel/

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %pkg_name.tar.gz
Source1: %pkg_name-emacs.el

BuildArch: noarch

# Automatically added by buildreq on Tue Dec 31 2002
BuildRequires: emacs-devel emacs-common

%description 
APEL stands for "A Portable Emacs Library" and intended to write portable
emacs modules.

%prep

%setup -q -n %pkg_name

%build
make elc

%install
make install EMACS=emacs PREFIX=%buildroot/usr
%__install -pD -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%pkg_name.el

%files
%doc README.en ChangeLog 
%_emacslispdir/*
%config(noreplace) %_emacs_sitestart_dir/*

%changelog
* Mon Nov 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 10.6-alt1.20050606
- New snapshot
- Removed load-path modification from site-start script
- Fixed dir layout
- Build with emacs-devel

* Sat Jan 11 2003 Ott Alex <ott@altlinux.ru> 10.3-alt1
- Initial build of package

