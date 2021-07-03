Name:       encled
Version:    2018
Release:    alt4

Summary:    utility to change location / fault LED for enclosure
License:    GPLv2+
Group:      System/Configuration/Hardware
Url:        https://github.com/amarao/sdled

BuildArch:  noarch

Source0:    %name-%version.tar
Patch0:     port-on-python3.patch

BuildRequires: rpm-build-python3

%description
Encled - utility to change location / fault LED for enclosure.

I'm not sure if it works with every avaible enclosures, but at least it
works with Supermicro chases with SAS enclosures (LSI).

Encled heavily depends on linux kernel's /sys/class/enclosure

Previous name was sdled, but now it supports not only 'sd' devices
but empty disk slots too.

%prep
%setup
%patch0 -p1

%build

%install
install -p -m 755 -D encled %buildroot%_sbindir/encled
install -p -m 755 -D sdled %buildroot%_sbindir/sdled
install -p -m 644 -D encled.8 %buildroot%_man8dir/encled.8

%files
%doc README
%_man8dir/encled.8*
%_sbindir/encled
%_sbindir/sdled


%changelog
* Sat Jul 03 2021 Vitaly Lipatov <lav@altlinux.ru> 2018-alt4
- NMU: add BR: rpm-build-python3

* Tue Jan 28 2020 Andrey Bychkov <mrdrew@altlinux.org> 2018-alt3
- Porting on Python3.

* Sat Nov 23 2019 Terechkov Evgenii <evg@altlinux.org> 2018-alt2
- /usr/bin/python -> /usr/bin/python2

* Sun Apr 14 2019 Terechkov Evgenii <evg@altlinux.org> 2018-alt1
- git-185372e

* Sat Oct  8 2016 Terechkov Evgenii <evg@altlinux.org> 2016-alt1
- git-5527aff

* Sun Aug 30 2015 Terechkov Evgenii <evg@altlinux.org> 2015-alt2
- git-8833f2b
- man page added

* Sun Apr  5 2015 Terechkov Evgenii <evg@altlinux.org> 2015-alt1
- Initial build for ALT Linux Sisyphus
