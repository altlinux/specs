# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-w3.spec,v 1.5 2006/02/04 17:33:19 eugene Exp $

%define cvsversion 20070309
%define pkg_name w3

Version: 4.0
%define SubVer  pre.47
Release: alt5.%SubVer.%cvsversion
Name: emacs-%pkg_name
Copyright: GPL
Group: Editors
Url: http://www.gnu.org/software/w3/
Summary: W3 package for Emacs
Summary(ru_RU.UTF-8): Пакет W3 для Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Requires: emacs-common >= 22.0.0
Requires: emacs-gnus
Provides: emacs-%pkg_name-el
Obsoletes: emacs-%pkg_name-el
Obsoletes: emacs22-%pkg_name <= 4.0-alt0.9.pre.47.20030626
Provides: emacs22-%pkg_name <= %version-%release

Source: %pkg_name-%cvsversion.tar.gz
Source1: %pkg_name-emacs.el

Patch0: %pkg_name-build_with_elc.patch

BuildArch: noarch

BuildRequires(build): emacs-common >= 22.0.0

# Automatically added by buildreq on Thu Jul 26 2002
BuildRequires: emacs-gnus emacs-devel

%description
Emacs/W3 is a full-featured web browser, written entirely in Emacs-Lisp.
This package only for emacs22.

%description -l ru_RU.UTF-8
Emacs/W3 - полнофункциональная программа для просмотра страниц WWW из Emacs,
написанная целиком на Emacs-Lisp.
Этот пакет работает только с emacs22.


%prep
%setup -q -n %pkg_name
%patch0 -p1

%build
./configure --prefix=%_prefix \
	    --with-lispdir=%_emacslispdir/%pkg_name \
	    --with-emacs \
	    --datadir=%_emacs_etc_dir/%pkg_name
make

%install
%__mkdir_p %buildroot%_emacslispdir/%pkg_name
%__install -m 644 lisp/*.el* %buildroot%_emacslispdir/%pkg_name

%__mkdir_p %buildroot%_infodir
%__install -m 644 texi/*.info* %buildroot%_infodir

%__mkdir_p %buildroot%_emacs_etc_dir/%pkg_name
%__install -m 644 etc/default.css %buildroot%_emacs_etc_dir/%pkg_name

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/30w3.el

%files
%doc INSTALL ChangeLog README* TODO HOWTO BUGS NOTES
%_infodir/*
%dir %_emacslispdir/%pkg_name/
%_emacslispdir/%pkg_name/*
%_emacs_sitestart_dir/*
%dir %_emacs_etc_dir/%pkg_name/
%_emacs_etc_dir/%pkg_name/*


%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 4.0-alt5.pre.47.20070309
- applied repocop patch: removed obsolete (un)install_info macros

* Thu Jul 26 2007 Eugene Vlasov <eugvv@altlinux.ru> 4.0-alt4.pre.47.20070309
- New snapshot
- emacs22-common in requires and build requires replaced by 
  emacs-common >= 22.0.0

* Sat Nov 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 4.0-alt3.pre.47.20061101
- New snapshot, fixed work with latest emacs22
- Compile all elisp files
- Fixed description
- Fixed Url

* Sat Feb 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 4.0-alt2.pre.47.20030626
- CVS snapshot
- URL package excluded from upstream, this package requires emacs22 now
- Cleanup spec
- %_emacslispdir/%pkg_name and %_emacs_etc_dir/%pkg_name now belongs to package
- Removed load-path modification from 30w3.el
- Fixed build with url/url-vars.elc
- Build with emacs-devel
- Temporary leave some elisp files uncompiled

* Sun Dec 18 2005 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1.pre.47
- fixed build with emacs22

* Tue Feb 03 2004 Ott Alex <ott@altlinux.ru> 4.0-alt0.8.pre.47
- fix spec

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 4.0-alt0.7.pre.47
- Fixing spec

* Fri Sep 27 2002 Ott Alex <ott@altlinux.ru> 4.0-alt0.5.pre.47
- Merging both package in one

* Thu Aug 22 2002 Ott Alex <ott@altlinux.ru> 4.0-alt0.4.pre.47
- Splitting on byte-compiled & source packages

* Tue Aug 06 2002 Ott Alex <ott@altlinux.ru> 4.0-alt0.3.pre.47
- Inserted right BuildRequires

* Thu Jul 26 2002 Ott Alex <ott@altlinux.ru> 4.0-alt0.1.pre.47
- Initial build

