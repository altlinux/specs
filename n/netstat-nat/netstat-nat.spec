# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: netstat-nat
Version: 1.4.9
Release: alt1

Summary: A tool that displays NAT connections
License: %gpl2plus
Group: Networking/Other
Url: http://www.tweegy.nl/projects/netstat-nat/

Packager: Artem Zolochevskiy <azol@altlinux.ru>

Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-licenses

%description
Netstat-nat is a small program written in C. It displays NAT connections,
managed by netfilter/iptables which comes with the > 2.4.x linux kernels.
The program reads its information from '/proc/net/ip_conntrack' or
'/proc/net/nf_conntrack', which is the temporary conntrack-storage of
netfilter.

%prep
%setup

%build
%configure
%make_build --silent --no-print-directory

%install
%make_install DESTDIR=%buildroot install --silent --no-print-directory
ln -sf %_licensedir/GPL-2 COPYING

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%doc -d COPYING
%_bindir/*
%_man1dir/*

%changelog
* Sun Dec 09 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.4.9-alt1
- new version
- use macro for License tag

* Wed Jul 11 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.4.8-alt2
- fixed typo in Summary

* Tue Jul 10 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.4.8-alt1
- initial build for Sisyphus

