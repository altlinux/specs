Name: proxychains
Version: 3.1
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: HTTP CONNECT and SOCKS proxy server client
License: GPLv2+
Group: Networking/Other

URL: http://proxychains.sourceforge.net/
Source: http://downloads.sourceforge.net/proxychains/proxychains-%version.tar.gz
Patch: %name-getnameinfo.patch

# Automatically added by buildreq on Wed Oct 07 2009
BuildRequires: gcc-c++

# TODO:
# Improve proxyresolve script. This script should get nameserver from some
# config file, not hardcoded it.

%description
ProxyChains allows to run any program from behind a proxy. This tool forces any
connection made by given application to follow through user-defined list of
proxies (aka proxy chains). This program allows you to use SSH, TELNET, VNC, FTP
and any other Internet application from behind HTTP(HTTPS) and SOCKS(4/5) proxy
servers.

%prep
%setup
%patch0 -p2

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%config(noreplace) %_sysconfdir/*
%_bindir/*
%_libdir/*.so*

%changelog
* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1.1
- Fixed build

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 3.1-alt1
- Initial build.
