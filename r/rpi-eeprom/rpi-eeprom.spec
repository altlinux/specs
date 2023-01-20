%define fw_subpkg firmware-bootloader-rpi4

Name: rpi-eeprom
Version: 2023.01.11
Release: alt1
Summary: Update Raspberry Pi 4 bootloader and VLI USB controller EEPROMs.
License: BSD-3-Clause
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://github.com/raspberrypi/rpi-eeprom
ExclusiveArch: armh aarch64
Source: %name-%version.tar
BuildRequires: rpm-build-python3
Requires: binutils
Requires: rpi-vcgencmd
Requires: firmware-bootloader-rpi4

%description
This package contains the scripts which is used to update
the Raspberry Pi 4 bootloader and VLI USB controller EEPROMs.
The pre-compiled binaries required for this are contained
in the %fw_subpkg package.

%package -n %fw_subpkg
Summary: Raspberry Pi 4 bootloader and VLI USB controller EEPROMs files.
License: Redistributable, no modification permitted
Group: System/Configuration/Other

%description -n %fw_subpkg
This package contains the pre-compiled binaries
which is used to update the Raspberry Pi 4 bootloader and
VLI USB controller EEPROMs.

%prep
%setup

%install
%define eep_rpi4 /lib/firmware/raspberrypi/bootloader
%define bkp_rpi4 /var/lib/raspberrypi/bootloader/backup
%__install -d %buildroot%eep_rpi4
cp -a firmware/* %buildroot%eep_rpi4
%__install -d %buildroot%bkp_rpi4
%__install -d %buildroot%_bindir
%__install -m755 rpi-eeprom-config %buildroot%_bindir
%__install -m755 rpi-eeprom-update %buildroot%_bindir
%__install -m755 rpi-eeprom-digest %buildroot%_bindir
%__install -d %buildroot%_sysconfdir/default
cat rpi-eeprom-update-default | sed 's/^BOOTFS=\/boot$/BOOTFS=\/boot\/efi/' > %buildroot%_sysconfdir/default/rpi-eeprom-update

%files
%bkp_rpi4
%_bindir/rpi-eeprom-config
%_bindir/rpi-eeprom-update
%_bindir/rpi-eeprom-digest
%doc README.md LICENSE releases.md firmware/release-notes.md
%_sysconfdir/default/rpi-eeprom-update

%files -n %fw_subpkg
%eep_rpi4
%doc README.md LICENSE releases.md firmware/release-notes.md

%changelog
* Fri Jan 20 2023 Dmitry Terekhin <jqt4@altlinux.org> 2023.01.11-alt1
- Updated

* Fri Oct 29 2021 Anton Midyukov <antohami@altlinux.org> 2021.04.29-alt2
- fix the packaging of the documentation
- fix License tag

* Wed Jun 02 2021 Dmitry Terekhin <jqt4@altlinux.org> 2021.04.29-alt1
- Initial build
