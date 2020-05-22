Name: cwm
Version: 6.7
Release: alt1

Summary: Calm Window Manager by OpenBSD project
Url: https://github.com/chneukirchen/cwm
Group: Graphical desktop/Other

# The entire source code is licensed under ISC license, except queue.h which
# is BSD
License: ISC and BSD

VCS: git://github.com/leahneukirchen/cwm
Source0: %name-%version.tar
Source1: %name.desktop

# Automatically added by buildreq on Wed Feb 19 2020
# optimized out: fontconfig fontconfig-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXrender-devel libfreetype-devel pkg-config python2-base sh4 xorg-proto-devel
BuildRequires: libXft-devel libXrandr-devel

%description
cwm (calm window manager) is a window manager for X11 which contains many
features that concentrate on the efficiency and transparency of window
management, while maintaining the simplest and most pleasant aesthetic.

This package contains a Linux port of the official project, which changes the
source for the port portion but doesn't touches the original functionality
provided by the original OpenBSD's project.

%prep
%setup

%build
%make_build

%install
export CFLAGS="%optflags"
make PREFIX=%prefix DESTDIR=%buildroot install
install -d %buildroot/%_datadir/xsessions
install -m 644 %SOURCE1 %buildroot/%_datadir/xsessions

%files
%doc README
%_bindir/cwm
%_datadir/xsessions/cwm.desktop
%_mandir/man1/cwm.1*
%_mandir/man5/cwmrc.5*

%changelog
* Sat May 23 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.7-alt1
- Updated to 6.7.

* Wed Feb 19 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.6-alt1
- Initial build for ALT Sisyphus based on Fedora spec.
