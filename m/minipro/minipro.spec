%define _unpackaged_files_terminate_build 1

Name: minipro
Version: 0.5
Release: alt2
Summary: Program for controlling the MiniPRO TL866xx series of chip programmers
License: GPLv3
Group: Engineering
Packager: Dmitriy Voropaev <voropaevdmtr@altlinux.org>
URL: https://gitlab.com/DavidGriffith/minipro
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildRequires: libusb-devel

%description
Software for Minipro TL866XX series of programmers from autoelectric.cn.
Used to program flash, EEPROM, etc.

%prep
%setup
%autopatch -p1

%build
%make_build PREFIX=%_prefix

%install
make install DESTDIR=%buildroot PREFIX=%_prefix
install -D -p -m 0644 udev/60-minipro.rules %buildroot%_udevrulesdir/60-minipro.rules
install -D -p -m 0644 udev/61-minipro-uaccess.rules %buildroot%_udevrulesdir/61-minipro-uaccess.rules
# see https://gitlab.com/DavidGriffith/minipro/-/issues/161
install -D -p -m 0644 bash_completion.d/minipro %buildroot%_sysconfdir/bash_completion.d/minipro


%files
%_bindir/minipro
%_bindir/miniprohex
%_man1dir/%name.*
%_udevrulesdir/60-minipro.rules
%_udevrulesdir/61-minipro-uaccess.rules
%_datadir/%name/
%_sysconfdir/bash_completion.d/*


%changelog
* Thu Apr 08 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.5-alt2
- fixed paths, so that the/usr/share/minipro/directory is not left when
  the package is removed

* Thu Feb 04 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.5-alt1
- initial build

