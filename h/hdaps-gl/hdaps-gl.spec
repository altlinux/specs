Name: hdaps-gl
Version: 0.0.5
Release: alt1

Summary: GL-based laptop model that rotates in real-time via hdaps
License: GPLv2
Group: Toys

Url: http://hdaps.sourceforge.net
Source0: %name-%version.tar.gz
Source1: hdaps-gl.1
Source2: hdaps-gl.desktop
Patch: hdaps-gl-0.0.5-alt-makefile.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu Apr 02 2009
BuildRequires: libGL-devel libfreeglut-devel

%description
%summary

%prep
%setup
%patch -p1

%build
%make_build

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %SOURCE1 %buildroot%_man1dir/%name.1
install -pDm644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_man1dir/*
%_desktopdir/*

%changelog
* Thu Apr 02 2009 Michael Shigorin <mike@altlinux.org> 0.0.5-alt1
- built for ALT Linux
- fixed build with -Wl,--as-needed (whoops, also in gentoo already)
- added debian manpage
- added brand new desktop file
