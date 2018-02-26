Name: xscope
Version: 1.3.1
Release: alt1
Summary: A program to monitor X11/Client conversations
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Thu Sep 23 2010
BuildRequires: xorg-xproto-devel xorg-xtrans-devel

BuildRequires: xorg-util-macros pkg-config

%description
XSCOPE is a program to monitor the connections between the X11 window
server and a client program.  xscope runs as a separate process.  By
adjusting the host and/or display number that a X11 client attaches
to, the client is attached to xscope instead of X11.  xscope attaches
to X11 as if it were the client.  All bytes from the client are sent
to xscope which passes them on to X11; All bytes from X11 are sent to
xscope which sends them on to the client.  xscope is transparent to
the client and X11.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README NEWS AUTHORS
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Autobuild version bump to 1.3

* Fri Sep 24 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2

