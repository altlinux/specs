Name: slock
Version: 1.3
Release: alt1

Summary: Simple X display locker

License: MIT/X11
Group: System/X11
Url: http://tools.suckless.org/slock/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %name-%version.tar.gz

# Automatically added by buildreq on Tue Mar 22 2016
# optimized out: libX11-devel libXrender-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXext-devel libXrandr-devel

%description
Simple X display locker.

%prep
%setup

%build
export CFLAGS="%optflags"
make

%install
make DESTDIR=%buildroot PREFIX=%_prefix install

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Mar 22 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3-alt1
- new version

* Mon Dec 07 2015 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.2-alt1
- Initial build.
