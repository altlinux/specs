# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-gnuserv.spec,v 1.5 2006/02/03 23:31:59 eugene Exp $

Name: emacs-gnuserv
Version: 3.12.8
Release: alt1
License: GPL
Group: Editors
Url: http://meltin.net/hacks/emacs/
Summary: Gnuserv allows you to attach to an already running Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source0: gnuserv-%version.tar.gz
Source1: emacs-gnuserv-init.el

Patch0: gnuserv-3.12.5.fixname.asp.patch
Patch1: gnuserv-3.12.7-xorg7_build.patch

Requires: emacs-common >= 22.0.0

BuildPreReq: emacs-devel

BuildRequires(build): emacs-common >= 22.0.0

# Automatically added by buildreq on Sun Sep 18 2011
BuildRequires: libXau-devel libX11-devel

%description
gnuserv allows you to attach to an already running Emacs.  This allows
external programs to make use of Emacs' editing capabilities.  It is
like GNU Emacs' emacsserver/server.el, but has many more features.

%prep
%setup -q -n gnuserv-%version
%patch0 -p1
%patch1 -p1

%build
export EMACS=emacs 
autoreconf -fisv
%configure --with-resolv --with-x --enable-xauth
make

%install
%makeinstall
mv %buildroot%_bindir/gnuserv %buildroot%_bindir/egnuserv
mv %buildroot%_bindir/gnuclient %buildroot%_bindir/egnuclient
mv %buildroot%_bindir/gnudoit %buildroot%_bindir/egnudoit
mv %buildroot%_bindir/gnuattach %buildroot%_bindir/egnuattach

mv %buildroot%_prefix/man %buildroot%_datadir

mkdir -p %buildroot%_emacslispdir/
mkdir -p %buildroot%_sysconfdir/emacs/site-start.d/
for f in *.{el,elc}; do \
	install -m 0644 $f %buildroot%_emacslispdir/ ; done
cp %SOURCE1 %buildroot%_emacs_sitestart_dir/gnuserv.el

%files
%doc ChangeLog README README.orig
%_bindir/*
%_man1dir/*
%_emacslispdir/*.el
%_emacslispdir/*.elc
%_emacs_sitestart_dir/gnuserv.el

%changelog
* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 3.12.8-alt1
- new version; fixed build

* Thu Jul 26 2007 Eugene Vlasov <eugvv@altlinux.ru> 3.12.7-alt3
- emacs22-common in requires and build requires replaced by 
  emacs-common >= 22.0.0

* Fri Feb 03 2006 Eugene Vlasov <eugvv@altlinux.ru> 3.12.7-alt2
- Rebuild with emacs22
- Removed post/postun scripts
- Build with emacs-devel
- Fixed build with xorg-7.0

* Sun Sep 18 2005 Eugene Vlasov <eugvv@altlinux.ru> 3.12.7-alt1
- New version
- Updated BuildRequires

* Wed Nov 26 2003 Ott Alex <ott@altlinux.ru> 3.12.6-alt1
- Rebuild for ALTLinux
- cleanup spec

* Sat May  3 2003 Grigory Bakunov <black@asplinux.ru>
- Initial build.

