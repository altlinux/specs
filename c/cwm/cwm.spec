Name: cwm
Version: 7.1
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
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Wed Feb 19 2020
# optimized out: fontconfig fontconfig-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXrender-devel libfreetype-devel pkg-config python2-base sh4 xorg-proto-devel
BuildRequires: libXft-devel libXrandr-devel
Requires: /usr/bin/xvt

%description
cwm (calm window manager) is a window manager for X11 which contains many
features that concentrate on the efficiency and transparency of window
management, while maintaining the simplest and most pleasant aesthetic.

This package contains a Linux port of the official project, which changes the
source for the port portion but doesn't touches the original functionality
provided by the original OpenBSD's project.

%prep
%setup
%autopatch -p1

%build
export CFLAGS="%optflags"
%make_build

%install
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
* Sun May 01 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 7.1-alt1
- Updated to v7.1.
- Added dependency to /usr/bin/xvt.
- Fixed CFLAGS.

* Wed Jul 14 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.7.0.3.gitce65ff3-alt1
- Updated to v6.7-3-gce65ff3.
- Made xvt a default terminal.

* Sat May 23 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.7-alt1
- Updated to 6.7.

* Wed Feb 19 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.6-alt1
- Initial build for ALT Sisyphus based on Fedora spec.
