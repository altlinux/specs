Name: dnsflood
Version: 1.20
Release: alt1
Summary: DNS Flood Detector was developed to detect abusive usage levels on high traffic nameservers
License: %gpl2plus
Group: Monitoring
URL: http://www.adotout.com/dnsflood.html
Source: http://www.adotout.com/%name-%version.tgz
Patch0: dont-strip-alt.patch
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libpcap-devel

%description
DNS Flood Detector was developed to detect abusive usage levels on high traffic nameservers and
to enable quick response in halting the use of one's nameserver to facilitate spam

%prep
%setup -n dns_flood_detector_1.2
%patch0 -p1

%build
./configure.pl Linux
%make_build

%install
install -pD -m755 dns_flood_detector %buildroot%_sbindir/dns_flood_detector

#post
#post_service %name ||:

#preun
#preun_service %name ||:

%files
%doc LICENSE README
#%dir %_sysconfdir/%name
#%config(noreplace) %_sysconfdir/%name/*
#%ghost %config(noreplace) %_sysconfdir/%{name}rc
%_sbindir/*
#%_man1dir/*
#%_man5dir/*
#%_initdir/*


%changelog
* Tue Jan  8 2013 Terechkov Evgenii <evg@altlinux.org> 1.20-alt1
- 1.20
- Apply patch to generate debuginfo

* Fri Dec 23 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.10-alt1
- built for ALT Linux
