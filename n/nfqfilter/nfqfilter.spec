Name: nfqfilter
Version: 0.2
Release: alt20.git20160913
Summary: Pattern-based packet filtering system
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv3
Url: https://github.com/max197616/nfqfilter
Source0: %name-%version.tar

BuildRequires: gcc-c++ libnetfilter_queue-devel libnfnetlink-devel
BuildRequires: libpoco-devel >= 1.6
BuildRequires: libnDPI-devel >= 1.7

# Temporary, while upstream fix
ExclusiveArch: x86_64

%description
Pattern-based packet filtering system

%prep
%setup

%build
%autoreconf

%configure

%make_build

%install
%makeinstall

install -m 0644 -D etc/%name.ini %buildroot%_sysconfdir/%name/%name.ini
install -m 0644 -D etc/systemd/%name.service %buildroot%_unitdir/%name.service

install -m 0755 -D nfqfilter.init        %buildroot%_initdir/%name
install -m 0644 -D nfqfilter.sysconfig   %buildroot%_sysconfdir/sysconfig/%name

install -m 0644 -D contrib/domains   %buildroot%_localstatedir/%name/domains
install -m 0644 -D contrib/hosts     %buildroot%_localstatedir/%name/hosts
install -m 0644 -D contrib/protos    %buildroot%_localstatedir/%name/protos
install -m 0644 -D contrib/ssl_host  %buildroot%_localstatedir/%name/ssl_host
install -m 0644 -D contrib/urls      %buildroot%_localstatedir/%name/urls


%files
%doc README COPYING
%_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.ini
%_sysconfdir/sysconfig/%name
%_initdir/%name
%_unitdir/*
%_bindir/*
%_localstatedir/%name

%changelog
* Fri Nov 11 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt20.git20160913
- Rebuild with new nDPI

* Sat Oct 22 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt19.git20160913
- update to git:6b902d1930a067a64221f2c1a91034f56f080835

* Mon Sep 05 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt19.git20160905
- analyzed only 'client hello' SSL packets

* Mon Aug 29 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt19.git20160818
- Rebuild with 1.7.5-alt1

* Mon Aug 29 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt18.git20160818
- Rebuild with 1.7.3-alt2

* Fri Aug 19 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt17.git20160818
- Add domain mask
- Fix url inclide "http://"

* Mon Aug 01 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt17.git20160801
- Optimized search algorithm url in the block list
- The speed-up search on the lists ssl ip

* Sat Jul 30 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt17.git20160616
- Add custom ssl_ips networks

* Tue May 31 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt17
- update to git:94c56b761655c13b8c77f7e5fe7d4ad533a503a5

* Wed May 04 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt16
- Rebuild with poco 1.7.3

* Fri Apr 29 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt15
- update to git:c910f71520e54d3e7e5029a981e17d37e4f576c8

* Wed Apr 20 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt14
- update to git:682029bb4ef2163e8a2ee111dbdf7e1426aaeb87

* Mon Mar 28 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt13
- update to git:1e79b0229a2870a15c7e18cfa3722da7a35e5c2a
- Add multithread's

* Mon Mar 21 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt11
- Rebuild with poco 1.7.2

* Wed Mar 16 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt10
- update to git:05cd8a51e92ccbf807b682cd3f6da4a20b26ee9c

* Tue Mar 15 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt9
- update to git:e650bdb44c42d2c975765cd31697a4c6d9adc360
- Rebuild with poco 1.7.1

* Tue Mar 08 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt8
- Rebuild with poco 1.7.0

* Tue Mar 01 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt7
- update to git:01a639d6a8dc3040db1c4cf876df15001bb85839

* Sat Feb 27 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt6
- update to git:ea6ca1e96aeb72b26444804c5ca1e274c4d22dc6

* Thu Feb 18 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt5
- update to git:bacd85c4cb4c20dc7a68c228a61f3152c4f291f9

* Mon Jan 25 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt4
- update to git:f9f292a7f73e7378e3ce46c3ce0b61aa17c62897

* Thu Jan 21 2016 Alexei Takaseev <taf@altlinux.org> 0.2-alt3
- update to git:1a4aea56d49e7d43f7dcfc7cebdd9be947b52c15

* Tue Dec 22 2015 Alexei Takaseev <taf@altlinux.org> 0.2-alt2
- update to git:85992b9d957848d99b1192c2b6bad550ec49ed54

* Tue Nov 24 2015 Alexei Takaseev <taf@altlinux.org> 0.2-alt1
- 0.2
    * use send rst for https without iptables
    * IPv6 support

* Mon Nov 09 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt4
- update to git:c308c8eaff3f320adc3c96d0ef6940d69631ebd3

* Wed Oct 28 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt3
- Added error handler

* Fri Oct 02 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt2
- Correct License LGPL3 -> GPL3

* Wed Sep 30 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt1
- Initial RPM release
