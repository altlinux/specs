Name: tcpxtract
Version: 1.0.1
Release: alt1

Summary: Tool for extracting files from network traffic
License: GPL
Group: Monitoring

URL: http://tcpxtract.sourceforge.net/
Source: http://dl.sourceforge.net/tcpxtract/tcpxtract-%version.tar.gz
# Fix path to configfile hardcoded in source
Patch0: tcpxtract-1.0.1-configdir.patch
# Fix bad PNG signature and comment BMP (many false positives)
Patch1: tcpxtract-1.0.1-config.patch

# Automatically added by buildreq on Thu Jun 21 2007
BuildRequires: flex libpcap-devel

%description
tcpxtract is a tool for extracting files from network traffic based on
file signatures. Can be used against a live network or a tcpdump
formatted capture file.

%prep
%setup
%patch0 -p1
%patch1 -p1
echo "rar(10000000, Rar\x21);" >> tcpxtract.conf

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%config(noreplace) /etc/tcpxtract.conf
%_bindir/*
%_man1dir/*

%changelog
* Thu Jun 21 2007 Victor Forsyuk <force@altlinux.org> 1.0.1-alt1
- Initial build.
