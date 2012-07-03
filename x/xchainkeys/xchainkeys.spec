Name: xchainkeys
Version: 0.10
Release: alt1

Summary: Create chained key bindings for X11
License: GPLv3
Group: System/Configuration/Other

Packager: Terechkov Evgenii <evg@altlinux.org>

URL: http://code.google.com/p/xchainkeys/
Source0: %name-%version.tar

BuildPreReq: libX11-devel

%description
xchainkeys is a standalone X11 program to create chained key bindings
similar to those found in the ratpoison window manager or the screen
terminal multiplexer

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc ChangeLog AUTHORS README NEWS example.conf

%changelog
* Mon Apr 16 2012 Terechkov Evgenii <evg@altlinux.org> 0.10-alt1
- Initial build for ALT Linux Sisyphus
