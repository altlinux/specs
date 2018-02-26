# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-wiki.spec,v 1.4 2006/05/27 13:10:23 eugene Exp $

%define base_rel alt2

Version: 2.72
%ifdef cvsdate
Release: %base_rel.%cvsdate
%else
Release: %base_rel
%endif
Name: emacs-wiki
License: GPL
Group: Editors
Url: http://mwolson.org/projects/EmacsWiki.html
Summary: Wiki package for Emacs
Requires: emacs-common emacs-misc-modes

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

%ifdef cvsdate
Source: http://mwolson.org/static/dist/%name-latest.tar.gz
%else
Source: http://www.mwolson.org/static/dist/%name/%name-%version.tar.gz
%endif
Source1: %name.el

BuildArch: noarch

BuildPreReq: emacs-misc-modes >= 0.2-alt3
BuildPreReq: emacs-devel

# Automatically added by buildreq on Wed Nov 16 2005
BuildRequires: emacs-common fontconfig freetype2 xorg-x11-locales

%description
Emacs-wiki allows you to create a wiki on your local system and export
HTML pages.

Emacs-wiki has many uses. It has been used to organize links. It can
make web page maintenance and design a lot easier. It is used as the
back-end of Planner. You can store and link together various bits of
information in a coherent manner. A weblog of sorts can be made with
it, but RSS syndication is not supported.

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%prep
%ifdef cvsdate
%setup -q -n %name
%else
%setup -q -n %name-%version
%endif

%build
%__make PREFIX=%prefix

%install
%__mkdir_p %buildroot%_emacslispdir/%name
%__install -m 644 *.el* %buildroot%_emacslispdir/%name

%__mkdir_p %buildroot%_infodir
%__install -m 644 *.info* %buildroot%_infodir/

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%name.el

gzip ChangeLog*

%files
%doc ChangeLog.gz ChangeLog.2004.gz README
%_infodir/*
%dir %_emacslispdir/%name
%_emacslispdir/%name/*.elc
%config(noreplace) %_emacs_sitestart_dir/*

%files el
%_emacslispdir/%name/*.el


%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 2.72-alt2
- applied repocop patch: removed obsolete (un)install_info macros

* Mon Jan 01 2007 Eugene Vlasov <eugvv@altlinux.ru> 2.72-alt1
- New version, fixed problems with latest emacs22 builds

* Sat May 27 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.71-alt1
- New version

* Sat Feb 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 2.70-alt0.1.20060103
- Initial build for Sisyphus

