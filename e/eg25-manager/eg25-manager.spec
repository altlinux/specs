%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:    eg25-manager
Version: 0.4.6
Release: alt4

Summary: Manager daemon for the Quectel EG25 mobile broadband modem
License: GPL-3.0-or-later
Group:   Other
Url:     https://gitlab.com/mobian1/eg25-manager

Source: %name-%version.tar
Patch0: %name-dirs.patch
Patch1: %name-libgpiod.patch

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: glib2-devel
BuildRequires: libmm-glib-devel
BuildRequires: libgudev-devel
BuildRequires: libgpiod-devel >= 2.0
BuildRequires: libusb-devel
BuildRequires: libcurl-devel

Requires: ModemManager

%description
eg25-manager is a daemon for managing the Quectel EG25 modem found on the
Pine64 PinePhone.

It implements the following features:
* cleanly power on/off the modem
* configure/check essential parameters (such as the audio format) on startup
* monitor the modem state through ModemManager
* put the modem in low-power mode when suspending the system, and restore it
  back to normal behavior when resuming monitor the modem state on resume and
  recover it if needed

%prep
%setup
%autopatch -p1

%build
%meson \
	-Dudevrulesdir=%_udevrulesdir \
	-Dsystemddir=%_systemd_dir \
	-Dsystemdsystemdir=%_unitdir

%meson_build

%install
%meson_install

# Enable service automatically if modem found
cat>%buildroot%_udevrulesdir/90-eg25-service.rules<<EOF
SUBSYSTEM=="usb", ACTION=="add", ATTRS{idVendor}=="2c7c", ATTRS{idProduct}=="0125", ENV{SYSTEMD_WANTS}="eg25-manager.service", TAG+="systemd"
EOF

%preun
%preun_service %name

%post
%post_service %name

%files
%doc *.md
%_bindir/%name
%_unitdir/%name.service
%_udevrulesdir/*.rules
%_datadir/%name

%changelog
* Sun Jun 23 2024 Anton Midyukov <antohami@altlinux.org> 0.4.6-alt4
- NMU:
  + revert eg25-manager-dirs.patch and fix it for compatible with Sisyphus and
    p11
  + spec: convert License field to modern SPDX format

* Sat Jun 22 2024 Andrew Savchenko <bircoph@altlinux.org> 0.4.6-alt3
- Port to libgpiod-2

* Sun Jan 21 2024 Anton Midyukov <antohami@altlinux.org> 0.4.6-alt2
- Enable service automatically if modem found

* Mon May 22 2023 Andrey Cherepanov <cas@altlinux.org> 0.4.6-alt1
- Initial build for Sisyphus.
