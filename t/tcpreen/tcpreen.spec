Name: tcpreen
Version: 1.4.4
Release: alt1

Summary: TCP network re-engineering tool
License: GPLv2 only
Group: Monitoring

URL: http://www.remlab.net/tcpreen/
Source0: http://www.remlab.net/files/tcpreen/current/tcpreen-%version.tar.bz2

# Automatically added by buildreq on Mon Dec 24 2007
BuildRequires: gcc-c++

%description
A tool to monitor and analyse data transmitted between a client and a server
via a TCP connection. This tool focuses on the data stream (software layer),
not on the lower level transmission protocol as packet sniffers do.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README THANKS
%_bindir/*
%_man1dir/*

%changelog
* Mon Dec 24 2007 Victor Forsyuk <force@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Mon Mar 14 2005 Victor Forsyuk <force@altlinux.ru> 1.4.2-alt1
- Initial build for Sisyphus.
