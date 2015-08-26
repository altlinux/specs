Name: mnt
Summary: Mount hotplug devices as normal user
Version: 1.0.2
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

%files
%_bindir/mnt
%_bindir/umnt

%changelog
* Wed Aug 26 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt1
- add fusermount -u support for umnt

* Fri Aug 07 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt1
- fix unmount with udiskctl

* Sun Aug 17 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build
