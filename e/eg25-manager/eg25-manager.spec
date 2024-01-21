Name:    eg25-manager
Version: 0.4.6
Release: alt2

Summary: Manager daemon for the Quectel EG25 mobile broadband modem
License: GPL-3.0+
Group:   Other
Url:     https://gitlab.com/mobian1/eg25-manager

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: %name-dirs.patch

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: glib2-devel
BuildRequires: libmm-glib-devel
BuildRequires: libgudev-devel
BuildRequires: libgpiod-devel
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
%patch0 -p1

%build
%meson
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
* Sun Jan 21 2024 Anton Midyukov <antohami@altlinux.org> 0.4.6-alt2
- Enable service automatically if modem found

* Mon May 22 2023 Andrey Cherepanov <cas@altlinux.org> 0.4.6-alt1
- Initial build for Sisyphus.
