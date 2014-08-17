Name: mnt
Summary: Mount hotplug devices as normal user
Version: 1.0
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
* Sun Aug 17 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build
