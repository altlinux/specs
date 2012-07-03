# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-text-modes.spec,v 1.6 2006/02/04 18:06:36 eugene Exp $

Version: 0.2
Release: alt3
Name: emacs-text-modes
License: GPL
Group: Editors
Summary: Various text packages for Emacs
Summary(ru_RU.UTF-8): Дополнительные пакеты Emacs для работы с текстами
Requires: emacs-common

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %name.tar.gz
Source1: emacs-mode-markdown-site-start.el

BuildArch: noarch

BuildPreReq: emacs-devel >= 0.0.1-alt2

# Automatically added by buildreq on Tue Dec 24 2002
BuildRequires: emacs-common emacs-mode-auctex

%description
Various text packages for Emacs.

%description -l ru_RU.UTF-8
Дополнительные пакеты Emacs для работы с текстами на естественных языках

%prep
%setup -q -n %name

%install
mkdir -p %buildroot%_emacslispdir
install -m 644 *.el* %buildroot%_emacslispdir/
install -m 644 -pD %SOURCE1 %buildroot%_emacs_sitestart_dir/markdown.el

%add_lisp_loadpath %_emacslispdir/auctex
%add_lisp_loadpath %buildroot%_emacslispdir
%byte_recompile_lispdir

%files
%config(noreplace) %_emacs_sitestart_dir/*
%_emacslispdir/*.el*


%changelog
* Sat Dec 26 2009 Terechkov Evgenii <evg@altlinux.ru> 0.2-alt3
- Markdown-mode added (ALT #20383)
- Spec cleanup

* Sat Feb 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt2
- Removed delim-col, table
- Updated a2ps-print, show-wspace

* Wed Oct 19 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt1
- Updated bhl, html-helper-mode, xxml
- Renamed highlight-current-line file
- Replaced show-whitespace-mode by show-wspace
- Added def-face-const, igrep
- Fixed sgml-id
- Build with emacs-devel (0.0.1-alt2 needed)
- Fixed requires

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.1-alt9
- Added new packages

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.1-alt8
- Remove modules, that are now in emhacks

* Sun Nov 30 2003 Ott Alex <ott@altlinux.ru> 0.1-alt7
- New versions

* Sun Oct 26 2003 Ott Alex <ott@altlinux.ru> 0.1-alt5
- Adding new packages

* Tue Sep 23 2003 Ott Alex <ott@altlinux.ru> 0.1-alt4
- New snapshot

* Tue Dec 31 2002 Ott Alex <ott@altlinux.ru> 0.1-alt2
- Remove unneeded dependence

* Tue Dec 24 2002 Ott Alex <ott@altlinux.ru> 0.1-alt1
- Initial build
