# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-w3m.spec,v 1.6 2005/11/12 21:39:21 eugene Exp $

%define pkg_name w3m

Version: 1.5
Release: alt0.1.20120203
Name: emacs-%pkg_name
License: GPL
Group: Editors
Summary: Emacs-%pkg_name is a simple Emacs interface to w3m
Url: http://emacs-w3m.namazu.org/
BuildArch: noarch

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %name-%version.tar.gz
Source1: %name-start-script.el

# Automatically added by buildreq on Tue Oct 14 2003
BuildRequires: emacs-common emacs-devel

Requires: emacs-common emacsen-startscripts w3m

%description
Emacs-%pkg_name is a simple Emacs interface to %pkg_name. 

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
%setup -q -n %name-%version

%build
autoconf
%configure --with-icondir=%_emacs_etc_dir/%pkg_name/icons \
	   --with-lispdir=%_emacslispdir/%pkg_name
make clean
make

%install
mkdir -p %buildroot/%_emacslispdir/%pkg_name
mkdir -p %buildroot/%_emacs_etc_dir/%pkg_name/icons
install -m 644 icons/*.xpm %buildroot/%_emacs_etc_dir/%pkg_name/icons/
install -m 644 *.el* %buildroot/%_emacslispdir/%pkg_name/
mkdir -p %buildroot/%_infodir/
install -m 644 doc/emacs-%pkg_name.info* %buildroot/%_infodir/
mkdir -p %buildroot/%_emacs_sitestart_dir
install -m 644 %SOURCE1 %buildroot/%_emacs_sitestart_dir/%pkg_name.el

gzip -f -9 ChangeLog*


%files
%doc README ChangeLog*
%dir %_emacslispdir/%pkg_name/
%_emacslispdir/%pkg_name/*.elc
%_emacs_etc_dir/%pkg_name/
%config(noreplace) %_emacs_sitestart_dir/%pkg_name.el
%_infodir/emacs-%pkg_name.info*

%files el
%_emacslispdir/%pkg_name/*.el

%changelog
* Fri Feb 03 2012 Michael Pozhidaev <msp@altlinux.ru> 1.5-alt0.1.20120203
- New version from CVS

* Sat Nov 28 2009 Eugene Vlasov <eugvv@altlinux.ru> 1.4.371-alt0.3.20091106
- Update to emacs-w3m CVS snapshot 20091106
- Cleanup %%__ macro
- Compress ChangeLog files

* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 1.4.259-alt0.2.20080303
- applied repocop patch: removed obsolete (un)install_info macros

* Tue Mar 11 2008 Eugene Vlasov <eugvv@altlinux.ru> 1.4.259-alt0.1.20080303
- Update to emacs-w3m CVS snapshot (20080303)

* Sun Nov 13 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.4.4-alt2
- Removed load-path modification from site-start script
- Icons moved to %_emacs_etc_dir/%pkg_name
- Build with emacs-devel

* Sat Sep 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.4.4-alt1
- New version
- Fixed BuildArch
- Added info page registration
- Dir %_emacslispdir/w3m now belongs to package

* Mon May 03 2004 Ott Alex <ott@altlinux.ru> 1.4-alt1
- New version, support for w3m 0.5.1

* Tue Oct 14 2003 Ott Alex <ott@altlinux.ru> 1.3.6-alt1
- First build

