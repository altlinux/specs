%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:    eg25-manager
Version: 0.5.2
Release: alt4

Summary: Manager daemon for the Quectel EG25 mobile broadband modem
License: GPL-3.0-or-later
Group:   Other
Url:     https://gitlab.com/mobian1/eg25-manager

Source: %name-%version.tar
Source1: mobile-tweaks.conf
Source2: 80-%name.preset
Source3: %name.firsttime
Patch0: %name-dirs.patch

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

# For fast on-call wakeups ModemManager needs to be started with
# --test-quick-suspend-resume
install -Dp -m 644 %SOURCE1 %buildroot%_unitdir/ModemManager.service.d/mobile-tweaks.conf

# Start eg25-manager by default
# udev-based rule is useless on pinephone pro, because usb device
# will appear only after eg25-manager is started
install -Dp -m 644 -t %buildroot%_presetdir %SOURCE2

# Disable eg25-manager on unsupported devices during firstinstall
install -Dp -m 755 %SOURCE3 %buildroot%_sysconfdir/firsttime.d/%name

%preun
%preun_service %name

%post
%post_service %name

%triggerin -- %name < 0.5.2-alt3
# Force autostart on supported devices to simplify system upgrade
grep -qi pinephone /proc/device-tree/model 2>/dev/null && systemctl preset eg25-manager || :

%files
%doc *.md
%_bindir/%name
%_unitdir/%name.service
%_unitdir/ModemManager.service.d/mobile-tweaks.conf
%_presetdir/80-%name.preset
%_sysconfdir/firsttime.d/%name
%_udevrulesdir/*.rules
%_datadir/%name

%changelog
* Sat Feb 22 2025 Andrew Savchenko <bircoph@altlinux.org> 0.5.2-alt4
- Fix trigger: return true even when hardware check is negative.

* Thu Feb 20 2025 Andrew Savchenko <bircoph@altlinux.org> 0.5.2-alt3
- Autostart eg25-manager out of the box, but
  disable autostart on firstinstall on unsupported systems.

* Sat Jan 25 2025 Andrew Savchenko <bircoph@altlinux.org> 0.5.2-alt2
- Enable fast wake-up on incoming calls.
- Drop useless udev-based autostart.

* Wed Oct 30 2024 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- New version.

* Mon Oct 28 2024 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- New version.

* Thu Aug 29 2024 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.

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
