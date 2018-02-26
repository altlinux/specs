Name: xzoom
Version: 0.3
Release: alt3
License: distributable
Group: System/X11
Summary: X zoomer
Source: ftp://metalab.unc.edu/pub/Linux/libs/X/%name-%version.tgz
Patch0: %name-%version.debian.diff
Patch1: %name-%version.shm.diff
Url: ftp://metalab.unc.edu/pub/Linux/libs/X/
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue Apr 12 2011
# optimized out: libX11-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: imake libXext-devel xorg-cf-files

%description
Xzoom displays in its window a magnified area of the X11 display.
The user can interactively change the zoomed area, the window size,
magnification (optionally different magnification for X and Y axes)
or rotate or mirror the image.

Authors:
--------
    Itai Nahshon <nahshon@best.com>

%prep
%setup
%patch0 -p 1
%patch1

%build
xmkmf
make

%install
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_man1dir
install -m 755 -s xzoom $RPM_BUILD_ROOT%_bindir
install -m 644 xzoom.man $RPM_BUILD_ROOT%_man1dir/xzoom.1

%files
%_bindir/*
%doc %_man1dir/*
%doc README xzoom.lsm

%changelog
* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 0.3-alt3
- BuildRequires recalculated

* Tue Dec 09 2008 Fr. Br. George <george@altlinux.ru> 0.3-alt2
- libXext-devel added

* Mon Aug 27 2007 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build for ALT

* Mon Nov 11 2002 - ro@suse.de
- changed neededforbuild <xf86 xdevel> to <x-devel-packages>
* Mon Dec 03 2001 - egmont@suselinux.hu
- Initial release.
