# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-bbdb.spec,v 1.1 2005/10/01 19:30:09 eugene Exp $

%define cvsdate 20050811
%define pkg_name bbdb
%define rel_base 3

Version: 2.35
%ifdef cvsbuild
Release: alt%rel_base.%cvsdate
%else
Release: alt%rel_base
%endif
Name: emacs-%pkg_name
License: GPL
Group: Editors
Url: http://%pkg_name.sourceforge.net/
Summary: BBDB package for Emacs
Summary(ru_RU.UTF-8): Big Brother Database для Emacs
Requires: emacs-common gnus

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

%ifdef cvsbuild
Source: %pkg_name-%cvsdate.tar.gz
%else
Source: %pkg_name-%version.tar.gz
%endif
Source1: %pkg_name-emacs.el

BuildArch: noarch

# Automatically added by buildreq on Thu Jul 26 2002
BuildRequires: emacs-common texinfo gnus emacs-leim
BuildPreReq: autoconf >= 2.53, automake >= 1.7

%description
Big Brother Database for Emacs

All Emacs Lisp code is byte-copmpiled, install %name-el for sources.

%description -l ru_RU.UTF-8
Big Brother Database для Emacs

Весь код на Emacs Lisp откомпилирован, для получения исходных текстов установите
пакет %name-el

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%description el -l ru_RU.UTF-8
Пакет %name-el содержит исходные тексты для пакета %name, который
является дополнением к редактору Emacs.

%name-el необходим вам только, если вы собираетесь изменять файлы
входящие в %name, или хотите посмотреть некоторые примеры.

%prep
%ifdef cvsbuild
%setup -q -n %pkg_name
%else
%setup -q -n %pkg_name-%version
%endif

%build
autoconf
%configure --with-lispdir=%_emacslispdir/%pkg_name \
           --enable-gnus --enable-rmail
make

%install
%__mkdir_p %buildroot%_emacslispdir/%pkg_name
%__install -m 644 lisp/*.el* %buildroot%_emacslispdir/%pkg_name

%__mkdir_p %buildroot%_infodir
%__install -m 644 texinfo/*.info* %buildroot%_infodir/

%__mkdir_p %buildroot/etc/emacs/site-start.d
%__install -m 644 %SOURCE1 %buildroot/etc/emacs/site-start.d/%pkg_name.el

%files
%doc ChangeLog README INSTALL
%_infodir/*
%dir %_emacslispdir/%pkg_name
%_emacslispdir/%pkg_name/*.elc
%config(noreplace) /etc/emacs/site-start.d/*

%files el
%_emacslispdir/%pkg_name/*.el

%changelog
* Mon Dec 21 2009 Terechkov Evgenii <evg@altlinux.ru> 2.35-alt3
- Build with Emacs23 fixed

* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 2.35-alt2
- applied repocop patch: removed obsolete (un)install_info macros

* Sun Feb 17 2008 Eugene Vlasov <eugvv@altlinux.ru> 2.35-alt1
- New version
- Removed --with-emacs configure key

* Sun Oct 02 2005 Eugene Vlasov <eugvv@altlinux.ru> 2.35-alt0.2.20050811
- New snapshot
- Removed load-path modification
- Dir %_emacslispdir/%pkg_name now belongs to package

* Mon Sep 15 2003 Ott Alex <ott@altlinux.ru> 2.35-alt0.1.20030915
- New snapshot

* Mon Feb 17 2003 Ott Alex <ott@altlinux.ru> 2.34-alt5
- Fixing spec file

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 2.34-alt4
- Fixing spec-file

* Thu Aug 22 2002 Ott Alex <ott@altlinux.ru> 2.34-alt3
- Splitting on byte-compiled & source packages

* Tue Aug 06 2002 Ott Alex <ott@altlinux.ru> 2.34-alt2
- Adding right Requires to spec

* Sun Aug 04 2002 Ott Alex <ott@altlinux.ru> 2.34-alt1
- Initial build

