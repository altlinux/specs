# vim: set ft=spec: -*- rpm-spec -*-

%define adbusersgroup adbusers

Name: udev-android
Version: 20230303
Release: alt1

Summary: Udev rules for adb and fastboot
License: GPL3
Group: System/Configuration/Hardware

Url: https://github.com/M0Rf30/android-udev-rules
BuildArch: noarch

Source: %name-%version.tar

%description
This package provides an UDEV rules enabling adb and fastboot to work
without root access to the host machine.

%prep
%setup

%install
mkdir -p %buildroot%_udevrulesdir
install -p -m644 51-android.rules %buildroot%_udevrulesdir/

%pre
/usr/sbin/groupadd -r -f %adbusersgroup ||:

%files
%doc LICENSE README.md
%_udevrulesdir/*

%changelog
* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 20230303-alt1
- Build new version.

* Mon Jul 13 2020 Grigory Ustinov <grenka@altlinux.org> 0.0.20200613-alt1
- New version: 20200613
- Fix license packaging (Closes: #38521)

* Tue Aug 06 2019 Pavel Nakonechnyi <zorg@altlinux.org> 0.0.20190315-alt1
- New version: 20190315

* Tue Jan 03 2017 Aleksey Avdeev <solo@altlinux.org> 0.0.20170103-alt1
- New version: 20170103

* Tue Jan 03 2017 Aleksey Avdeev <solo@altlinux.org> 0.0.20161014-alt1.gita64df07.1
- Initial build for ALT Linux Sisyphus
