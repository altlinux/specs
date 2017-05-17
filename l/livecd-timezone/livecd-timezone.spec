Name: livecd-timezone
Version: 0.1.0
Release: alt1

Summary: Try to setup timezone
License: %gpl2plus
Group: System/Configuration/Other

Source0: %name.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: alterator-datetime >= 4.0

%description
Service to setup timezone on live system.
Try to get timezone from:
  1. 'tz' argument in kernel command line
  2. geoip server (if network is up)
  3. guess based on lang in kernel command line

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pDm755 {livecd-timezone,%buildroot%_initdir}/livecd-timezone
install -pDm644 {livecd-timezone,%buildroot%_unitdir}/livecd-timezone.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/livecd-timezone
%_unitdir/livecd-timezone.service

%changelog
* Wed May 03 2017 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.
