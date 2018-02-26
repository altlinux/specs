Name: ledmon
Version: 0.0.1
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Graphical desktop/Other
Url: https://github.com/jgoerzen/ledmon?a=tree
Source: %name-%version.tar
Summary: Show leds status (for use with xmobar)

# Automatically added by buildreq on Fri Jun 24 2011
# optimized out: xorg-kbproto-devel xorg-xproto-devel
BuildRequires: libX11-devel

%description
%summary

%prep
%setup

%build
gcc -Wall -o ledmon ledmon.c -lX11

%install
install -D -m755 ledmon %buildroot%_bindir/ledmon

%files
%_bindir/ledmon

%changelog
* Fri Jun 24 2011 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

