Name: miraclecast
Version: 20250608
Release: alt2

Summary: Connect external monitors to your system via Wifi-Display specification also known as Miracast

License: LGPL-2.1-or-later and GPL-2.0-only
Group: Other

Url: https://github.com/albfan/miraclecast
Vcs: https://github.com/albfan/miraclecast

Source: %name-%version.tar

BuildRequires(Pre): rpm-build-python3
BuildRequires: gcc-c++ libsystemd-devel pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpcre2-8) libudev-devel libreadline-devel

%description
The MiracleCast project provides software to connect external monitors to your system via Wi-Fi. 
It is compatible to the Wifi-Display specification also known as Miracast. MiracleCast implements 
the Display-Source as well as Display-Sink side.

%prep
%setup

%build
%autoreconf
%configure --prefix=/usr --sysconfdir=/etc --enable-rely-udev
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_sysconfdir/dbus-1/system.d/*.miracle.conf
%_datadir/bash-completion/completions/miracle*
%doc *.md LICENSE*

%changelog
* Tue Sep 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250608-alt2
- rebuild with make

* Mon Sep 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250608-alt1
- Initial build for ALT Linux.
