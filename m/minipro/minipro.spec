%define _unpackaged_files_terminate_build 1

Name: minipro
Version: 0.7.4
Release: alt1
Summary: Program for controlling the MiniPRO TL866xx series of chip programmers
License: GPL-3.0-or-later
Group: Engineering
Packager: Dmitriy Voropaev <voropaevdmtr@altlinux.org>
URL: https://gitlab.com/DavidGriffith/minipro
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildRequires: libusb-devel
BuildRequires: pkgconfig(zlib)

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
%_bindir/dump-alg-minipro.bash
%_man1dir/%name.*
%_udevrulesdir/60-minipro.rules
%_udevrulesdir/61-minipro-uaccess.rules
%_datadir/%name/
%_sysconfdir/bash_completion.d/*
%doc LICENSE


%changelog
* Mon Aug 10 2026 Anton Meleshnikov <alton@altlinux.org> 0.7.4-alt1
- new version

* Thu Apr 08 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.5-alt2
- fixed paths, so that the/usr/share/minipro/directory is not left when
  the package is removed

* Thu Feb 04 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.5-alt1
- initial build

