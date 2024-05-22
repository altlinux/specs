Name: lsmount
Summary: List all hotplug storage devices
Version: 1.1
Release: alt1
License: GPLv2
Group: System/Base
BuildArch: noarch
Url: https://github.com/mithraen/lsmount

Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

# Automatically added by buildreq on Fri Aug 08 2014 (-bb)
# optimized out: perl-Term-ANSIColor perl-Text-Aligner python-base
BuildRequires: perl-Text-Table

Requires: lsblk

%description
%summary

%prep
%setup

%install
install -D -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Wed May 22 2024 Hihin Ruslan <ruslandh@altlinux.ru> 1.1-alt1
- fix (ALT #43796)

* Sat Aug 09 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt3
- add Url tag

* Fri Aug 08 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt2
- add requires to lsblk (ALT #30222)

* Fri Aug 08 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- first build
