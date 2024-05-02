Name: mnt
Summary: Mount hotplug devices as normal user
Version: 1.0.5
Release: alt1
License: GPLv2
Group: System/Base
BuildArch: noarch
Url: https://github.com/mithraen/mnt

Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
install -D -m 755 mnt %buildroot%_bindir/mnt
install -D -m 755 umnt %buildroot%_bindir/umnt
install -D -m 755 alsblk %buildroot%_bindir/alsblk

%files
%_bindir/mnt
%_bindir/umnt
%_bindir/alsblk

%changelog
* Tue Apr 16 2024 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.5-alt1
- Add alsblk

* Tue Dec 26 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.4-alt1
- Add mnt -a and alsblk

* Mon Dec 05 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.3-alt1.1
- fix mnt with udiskctl

* Sat Nov 12 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.3-alt1
- remove hmount ; correct scripts

* Wed Aug 26 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt1
- add fusermount -u support for umnt

* Fri Aug 07 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt1
- fix unmount with udiskctl

* Sun Aug 17 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build
