Name: vzvalidate
Version: 0.1
Release: alt1

Summary: Check all OpenVZ settings - vzcfgvalidate improvement

License: Public domain
Group: System/Configuration/Other
Url: http://phpsuxx.blogspot.com/2009/12/ubc-openvz.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

%description
vzvalidate check all OpenVZ settings for running containers.
See vzcfgvalidate also.

%prep
%setup -n %name-%version

%install
mkdir -p %buildroot%_sbindir/
install %name %buildroot%_sbindir/

%files
%_sbindir/%name

%changelog
* Fri Apr 29 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
