Name: xcompmgr
Version: 1.1.4
Release: alt1
Serial: 1
Summary: sample X compositing manager
License: GPL
Group: System/X11

Url: http://www.freedesktop.org/Software/xapps
Source: %name-%version.tar.bz2
Source1: transset.tar.bz2

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xorg-x11-%name = %version-%release
Obsoletes: xorg-x11-%name

BuildRequires: libX11-devel libXcomposite-devel libXdamage-devel libXfixes-devel
BuildRequires: libXrender-devel xorg-x11-proto-devel

%description
xcompmgr  is  a sample compositing manager for X servers supporting the
XFIXES, DAMAGE, and COMPOSITE extensions.  It enables  basic  eye-candy
effects.

%prep
%setup -q -a1

%build
%autoreconf
%configure
%make_build

pushd transset
%make_build
popd

%install
%make DESTDIR=%buildroot install
%__install -m755 transset/transset %buildroot%_bindir/

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.4-alt1
- 1.1.4

* Sun Feb 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.3-alt1
- Updated build dependencies

* Wed Oct 20 2004 Valery Inozemtsev <shrek@altlinux.ru> 20041020-alt1
- cvs snapshot 2004.10.20

* Sun Sep 26 2004 Valery Inozemtsev <shrek@altlinux.ru> 20040923-alt1
- cvs snapshot 2004.09.23

