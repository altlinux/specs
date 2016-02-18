Name: nfqfilter
Version: 0.2
Release: alt5
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
