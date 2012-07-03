# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-elib.spec,v 1.1 2005/11/06 20:23:55 eugene Exp $

%define pkg_name elib

Version: 1.0
Release: alt8
Name: emacs-%pkg_name
Copyright: GPL
Group: Editors
Url: ftp://ftp.lysator.liu.se/pub/emacs/
Summary: The Emacs Lisp Library
Summary(ru_RU.UTF-8): Библиотека функций для Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %pkg_name-%version.tar.gz
Source1: %pkg_name-emacs.el
Patch: %pkg_name-%version-texinfo.patch

Obsoletes: %pkg_name
Provides: %pkg_name = %version

BuildArch: noarch

Requires: emacs-common
# Automatically added by buildreq on Thu Jul 18 2002
BuildRequires: emacs-common emacs-devel

%description
Elib contains code for:
 - container data structures (queues, stacks, AVL trees, etc)
 - string handling functions missing in standard emacs
 - minibuffer handling functions missing in standard emacs
 - routines for handling lists of so called cookies in a buffer.

All Emacs Lisp code is byte-copmpiled, install %name-el for sources.

%description -l ru_RU.UTF-8
Elib содержит функции для:
 - хранения данных (очереди, стеки, деревья и т.п.)
 - работы со строками, которые отсутствуют в стандартной поставке emacs
 - функции работы с минибуфером
 - функции работы со списками кличиков в буфере

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
%setup -q -n %pkg_name-%version
%patch -p1

%build
make all

%install
%__mkdir_p %buildroot%_emacslispdir/%pkg_name
%__install -m 644 *.el* %buildroot%_emacslispdir/%pkg_name

%__mkdir_p %buildroot%_infodir
%__install -m 644 %pkg_name.info* %buildroot%_infodir

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/20elib.el

%files
%doc README RELEASING INSTALL ChangeLog NEWS TODO
%_infodir/*
%dir %_emacslispdir/%pkg_name
%_emacslispdir/%pkg_name/*.elc
%_emacs_sitestart_dir/*

%files el
%_emacslispdir/%pkg_name/*.el

%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 1.0-alt8
- applied repocop patch: removed obsolete (un)install_info macros

* Mon Nov 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.0-alt7
- Removed load-path modification
- Dir %_emacslispdir/%pkg_name now belongs to package
- Build with emacs-devel
- Cleanup spec

* Mon Feb 17 2003 Ott Alex <ott@altlinux.ru> 1.0-alt6
- Fixing spec file

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 1.0-alt5
- fixing spec

* Thu Aug 22 2002 Ott Alex <ott@altlinux.ru> 1.0-alt3
- Splitting on byte-compiled & source packages

* Mon Aug 12 2002 Ott Alex <ott@altlinux.ru> 1.0-alt2
- Correcting spec file

* Mon Aug 12 2002 Ott Alex <ott@altlinux.ru> 1.0-alt1
- Initial build
