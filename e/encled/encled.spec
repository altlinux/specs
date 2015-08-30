Summary: utility to change location / fault LED for enclosure
Name: encled
Version: 2015
Release: alt2
License: GPLv2+
Group: System/Configuration/Hardware
Url: https://github.com/amarao/sdled
Source0: %name-%version.tar
BuildArch: noarch

%description
Encled - utility to change location / fault LED for enclosure.

I'm not sure if it works with every avaible enclosures, but at least it
works with Supermicro chases with SAS enclosures (LSI).

Encled heavily depends on linux kernel's /sys/class/enclosure

Previous name was sdled, but now it supports not only 'sd' devices
but empty disk slots too.

%prep
%setup
%build
%install
install -p -m 755 -D encled %buildroot%_sbindir/encled
install -p -m 755 -D sdled %buildroot%_sbindir/sdled
install -p -m 644 -D encled.8 %buildroot%_man8dir/encled.8

%files
%_sbindir/encled
%_sbindir/sdled
%_man8dir/encled.8*
%doc README

%changelog
* Sun Aug 30 2015 Terechkov Evgenii <evg@altlinux.org> 2015-alt2
- git-8833f2b
- man page added

* Sun Apr  5 2015 Terechkov Evgenii <evg@altlinux.org> 2015-alt1
- Initial build for ALT Linux Sisyphus
