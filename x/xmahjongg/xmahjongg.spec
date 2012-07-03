Name: xmahjongg
Version: 3.7
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Mahjongg game
License: GPLv2+
Group: Games/Other

URL: http://www.lcdf.org/xmahjongg/
Source: %url/xmahjongg-%version.tar.gz
Source1: xmahjongg.desktop

# Automatically added by buildreq on Wed Dec 17 2008
BuildRequires: gcc-c++ imake libXt-devel xorg-cf-files

%description
Xmahjongg is a simple solitaire game. The object is to remove all 144 Mah Jongg
tiles from the playing area by matching them two at a time.

%prep
%setup

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/xmahjongg.desktop

%files
%_bindir/xmahjongg
%_man6dir/*
%_datadir/xmahjongg
%_desktopdir/*

%changelog
* Wed Dec 17 2008 Victor Forsyuk <force@altlinux.org> 3.7-alt2
- Remove obsolete install time scripts.

* Tue Apr 05 2005 Victor Forsyuk <force@altlinux.ru> 3.7-alt1
- 3.7

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.6.1-alt2.1
- Rebuilt with libstdc++.so.6.

* Mon Sep 22 2003 Ott Alex <ott@altlinux.ru> 3.6.1-alt2
- Fixing spec

* Sat Sep 28 2002 Ott Alex <ott@altlinux.ru> 3.6.1-alt1
- Initial build
