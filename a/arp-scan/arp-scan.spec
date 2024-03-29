# since 1.9 no more releaeses (tarballs) and corresponding tags,
# so we use snapshots. See NEWS and configure.ac for versions.
%def_enable snapshot
%def_enable check

Name: arp-scan
Version: 1.10.0
Release: alt1

Summary: Scanning and fingerprinting tool
License: GPLv3+
Group: Monitoring
Url: http://www.nta-monitor.com/tools-resources/security-tools/arp-scan

%if_disabled snapshot
Source: http://www.nta-monitor.com/files/arp-scan/%name-%version.tar.gz
%else
Vcs: https://github.com/royhills/arp-scan.git
Source: %name-%version.tar
%endif
# File generated by get-oui as replacements of older file
# shipped with arp-scan:
Source2: ieee-oui.txt

Requires(pre): /sbin/setcap

BuildRequires: libpcap-devel >= 1.0 perl-libwww perl-Text-CSV

%description
arp-scan is a command-line tool that uses the ARP protocol to discover
and fingerprint IP hosts on the local network.

%prep
%setup

%build
cp -a %_sourcedir/ieee-oui.txt .
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%post
/sbin/setcap ap_net_raw+p %_bindir/%name 2>/dev/null ||:

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/mac-vendor.txt
%_bindir/arp-fingerprint
%_bindir/%name
%_bindir/get-oui
%_bindir/get-iab
%dir %_datadir/%name
%_datadir/%name/ieee-oui.txt
%_man1dir/*
%_man5dir/*
%doc NEWS README*

%changelog
* Wed Dec 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0
- updated ieee-oui.txt

* Wed Nov 27 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9.7-alt1
- 1.9.7
- updated ieee-{iab,oui}.txt

* Sat Oct 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9.6-alt1
- updated to 1.9.6-9-g36de712
- updated ieee-{iab,oui}.txt
- new %%check section

* Mon Jan 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.5-alt1
- 1.9.5
- updated ieee-{iab,oui}.txt

* Sat Nov 29 2014 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9
- fixed urls
- updated ieee-{iab,oui}.txt

* Wed Dec 28 2011 Victor Forsiuk <force@altlinux.org> 1.8.1-alt1
- Initial build.
