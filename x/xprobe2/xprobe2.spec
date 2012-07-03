Name: xprobe2
Version: 0.3
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Active operating system fingerprinting tool
License: GPLv2+
Group: Monitoring

Url: http://xprobe.sourceforge.net/
Source: http://downloads.sourceforge.net/xprobe/xprobe2-%version.tar.gz
Patch0: xprobe2-0.3-gcc43.patch

# Automatically added by buildreq on Thu Apr 10 2008
BuildRequires: gcc-c++ libpcap-devel

%description
Xprobe is an alternative to some tools which are heavily dependent upon the
usage of the TCP protocol for remote active operating system fingerprinting.

Xprobe I combines various remote active operating system fingerprinting methods
using the ICMP protocol, which were discovered during the "ICMP Usage in
Scanning" research project, into a simple, fast, efficient and a powerful way
to detect an underlying operating system a targeted host is using.

Xprobe2 is an active operating system fingerprinting tool with a different
approach to operating system fingerprinting. Xprobe2 rely on fuzzy signature
matching, probabilistic guesses, multiple matches simultaneously, and a
signature database.

%prep
%setup
%patch0 -p0

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%dir %_sysconfdir/xprobe2
%config(noreplace) %_sysconfdir/xprobe2/*
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 27 2008 Victor Forsyuk <force@altlinux.org> 0.3-alt2
- Fix FTBFS with gcc4.3.

* Thu Apr 10 2008 Victor Forsyuk <force@altlinux.org> 0.3-alt1
- Initial build.
