# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-nxml-mode.spec,v 1.3 2005/11/13 14:26:31 eugene Exp $

%define shortname nxml-mode
%define snapshot 20041004

Name: emacs-%shortname
Version: 0.1.%snapshot
Release: alt4
License: GPL
Group: Editors
Summary: Emacs mode for editing XML
URL: http://www.thaiopensource.com/nxml-mode/
Requires: emacs-common
Requires: emacs-base >= 0.0.5-alt2

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

BuildArch: noarch

Source: %shortname-%snapshot.tar.gz
Source1: emacs-%shortname-site-start.el
Source2: nxml-menu.zip

Patch0: nxml-menu-question_binding.patch
Patch1: %shortname-no_load-path.patch

BuildPreReq: emacs-devel

# Automatically added by buildreq on Tue Jun 17 2003
BuildRequires: emacs-common texinfo unzip

%description
This is a new major mode for GNU Emacs for editing XML documents. It
supports editing well-formed XML documents and also provides
schema-sensitive editing of XML documents using RELAX NG Compact Syntax.

%prep
%setup -q -n %shortname-%snapshot
unzip %SOURCE2
%patch0 -p1

%build
%__make clean
echo "" | %__make all
%__patch -p1 < %PATCH1

%install
%__mkdir_p %buildroot/%_emacslispdir/%shortname
%__install -m 644 *.el* %buildroot/%_emacslispdir/%shortname
%__cp -R nxml-manual %buildroot/%_emacslispdir/%shortname
touch %buildroot/%_emacslispdir/%shortname/nxml-manual/.nosearch
%__mkdir_p %buildroot/%_infodir
%__install -m 644 *.info* %buildroot/%_infodir
%__cp -R schema %buildroot/%_emacslispdir/%shortname
touch %buildroot/%_emacslispdir/%shortname/schema/.nosearch
%__mkdir_p %buildroot/%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot/%_emacs_sitestart_dir/%shortname.el

%files
%doc NEWS TODO README 
%doc test.invalid.xml test.valid.xml nxml-mode.xml nxml-mode.rnc
%_emacslispdir/%shortname
%config(noreplace) %_emacs_sitestart_dir/%shortname.el
%_infodir/*

%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.20041004-alt4
- applied repocop patch: removed obsolete (un)install_info macros

* Sun Nov 13 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.1.20041004-alt3
- Removed load-path modification from site-start script and rng-auto.el
- Added .nosearch in non-lisp dirs
- Build with emacs-devel
- On emacs22 modify magic-mode-alist
- Fixed build

* Sat Sep 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.1.20041004-alt2
- Updated nxml-menu
- Fixed bindings in nxml-menu

* Fri Jul 08 2005 Ivan Fedorov <ns@altlinux.ru> 0.1.20041004-alt1
- 20041004

* Sat Nov 01 2003 Ott Alex <ott@altlinux.ru> 0.1.20031031-alt1
- New snapshot
- adding nxml-menu package

* Mon Oct 20 2003 Ott Alex <ott@altlinux.ru> 0.1.20031018-alt1
- New snapshot
- adding hook example in site start file

* Mon Sep 29 2003 Ott Alex <ott@altlinux.ru> 0.1.20030929-alt1
- New snapshot

* Mon Sep 29 2003 Ott Alex <ott@altlinux.ru> 0.1.20030915-alt1
- First build

