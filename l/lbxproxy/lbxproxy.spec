Name: lbxproxy
Version: 1.0.3
Release: alt1
License: MIT
Group: System/X11
Summary: Low BandWidth X proxy
Source: %name-%version.tar.bz2
Url: http://cgit.freedesktop.org/xorg/app/%name

# Automatically added by buildreq on Wed Nov 03 2010
BuildRequires: libICE-devel libXext-devel liblbxutil-devel xorg-bigreqsproto-devel xorg-pmproto-devel xorg-xtrans-devel zlib-devel

BuildRequires: xorg-util-macros

%description
Applications that would like to take advantage of the Low Bandwidth
extension to X (LBX) must make their connections to an lbxproxy.
These applications need to know nothing about LBX, they simply connect
to the lbxproxy as if were a regular server.  The lbxproxy accepts
client connections, multiplexes them over a single connection to the X
server, and performs various optimizations on the X protocol to make
it faster over low bandwidth and/or high latency connections.

With regard to authentication/authorization, lbxproxy simply passes
along to the server the credentials presented by the client.  Since X
clients will connect to lbxproxy, it is important that the user's
.Xauthority file contain entries with valid keys associated with the
network ID of the proxy.  lbxproxy does not get involved with how
these entries are added to the .Xauthority file.  The user is
responsible for setting it up.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc README NEWS AUTHORS
%_bindir/*
%_x11sysconfdir/%name
%_man1dir/*

%changelog
* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3
- Fix build

* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build

