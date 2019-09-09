Name: xcompmgr
Version: 1.1.8
Release: alt1
Summary: sample X compositing manager
License: GPL
Epoch: 1
Group: System/X11

Url: http://www.freedesktop.org/Software/xapps
Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Sep 05 2019
# optimized out: glibc-kernheaders-generic libX11-devel libXfixes-devel perl pkg-config python-base python-modules sh4 xorg-proto-devel
BuildRequires: libXcomposite-devel libXdamage-devel libXrender-devel libXext-devel libXfixes-devel

BuildRequires: xorg-util-macros

%description
xcompmgr  is  a sample compositing manager for X servers supporting the
XFIXES, DAMAGE, and COMPOSITE extensions.  It enables  basic  eye-candy
effects.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README*
%_bindir/*
%_man1dir/*

%changelog
* Mon Sep 09 2019 Fr. Br. George <george@altlinux.ru> 1:1.1.8-alt1
- Restore epoch for history reason

* Thu Sep 05 2019 Fr. Br. George <george@altlinux.ru> 1.1.8-alt1
- Autobuild version bump to 1.1.8
- Resurrect from orphaned

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.4-alt1
- 1.1.4

* Sun Feb 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.3-alt1
- Updated build dependencies

* Wed Oct 20 2004 Valery Inozemtsev <shrek@altlinux.ru> 20041020-alt1
- cvs snapshot 2004.10.20

* Sun Sep 26 2004 Valery Inozemtsev <shrek@altlinux.ru> 20040923-alt1
- cvs snapshot 2004.09.23

