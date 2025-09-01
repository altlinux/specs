Name: miraclecast
Version: 20250608
Release: alt1

Summary: Connect external monitors to your system via Wifi-Display specification also known as Miracast

License: LGPL-2.1-or-later and GPL-2.0-only
Group: Other

Url: https://github.com/albfan/miraclecast
Vcs: https://github.com/albfan/miraclecast

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake gcc-c++ libsystemd-devel pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpcre2-8) libudev-devel libreadline-devel

%description
The MiracleCast project provides software to connect external monitors to your system via Wi-Fi. 
It is compatible to the Wifi-Display specification also known as Miracast. MiracleCast implements 
the Display-Source as well as Display-Sink side.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_sysconfdir/dbus-1/system.d/*.miracle.conf
%_datadir/bash-completion/completions/miracle*
%doc *.md LICENSE*

%changelog
* Mon Sep 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 20250608-alt1
- Initial build for ALT Linux.
