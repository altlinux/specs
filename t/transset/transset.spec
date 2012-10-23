Name:		transset
Version:	1.0.0
Release:	alt1
Group:		System/X11
Summary:	Simple utility to set transparency on a window
License:	MIT
Source:		%{name}-%{version}.tar.gz
URL:		http://cgit.freedesktop.org/xorg/app/transset/

BuildRequires:	xorg-xproto-devel xorg-util-macros

# optimized out: pkg-config xorg-xproto-devel
BuildRequires: libX11-devel

%description
transset is an utility for setting opacity property.

Features:
 * select window by clicking (as transset)
 * select actual focused X11 window
 * select window by pointing
 * select by window name or id
 * force toggle
 * increase or decrease opacity

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Wed Aug 29 2012 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial autobuild version bump

