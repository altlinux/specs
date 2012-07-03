# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-dictionary.spec,v 1.1 2005/11/25 22:15:03 eugene Exp $

%define pkg_name dictionary

Version: 1.8.7
Release: alt1
Name: emacs-%pkg_name
License: GPL
Group: Editors
Url: http://www.myrkr.in-berlin.de/dictionary/index.html
Summary: Dictionary (RFC 2229) client for Emacs
Summary(ru_RU.UTF-8): Клиент dictionary (RFC 2229) для Emacs
Requires: emacs-common

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %pkg_name-%version.tar.gz
Source1: %pkg_name-emacs.el

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 24 2002
BuildRequires: emacs-common emacs-devel

%description
Dictionary (RFC 2229) client for Emacs

All Emacs Lisp code is byte-compiled, install %name-el for sources.

%description -l ru_RU.UTF-8
Клиент dictionary (RFC 2229) для Emacs

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

%build
%__make

%install
%__mkdir_p %buildroot%_emacslispdir/%pkg_name
%__install -m 644 *.el* %buildroot%_emacslispdir/%pkg_name
%__rm %buildroot%_emacslispdir/%pkg_name/lpath.el
%__rm %buildroot%_emacslispdir/%pkg_name/install-package.el
%__rm %buildroot%_emacslispdir/%pkg_name/dictionary-init.el

mkdir -p %buildroot%_emacs_sitestart_dir
install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%pkg_name.el

%files
%doc README
%dir %_emacslispdir/%pkg_name
%_emacslispdir/%pkg_name/*.elc
%config(noreplace) %_emacs_sitestart_dir/*

%files el
%_emacslispdir/%pkg_name/*.el

%changelog
* Fri Nov 25 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.8.7-alt1
- New version
- Fixed Url
- Dir %_emacslispdir/%pkg_name now belongs to package
- Dropped load-path modification
- Build with emacs-devel
- Cleanup spec

* Wed Apr 21 2004 Ott Alex <ott@altlinux.ru> 1.8.5-alt1
- Nev version

* Mon Feb 17 2003 Ott Alex <ott@altlinux.ru> 1.8.4-alt3
- Fixing spec file

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 1.8.4-alt2
- fixinf spec file

* Thu Oct 24 2002 Ott Alex <ott@altlinux.ru> 1.8.4-alt1
- Initial build

