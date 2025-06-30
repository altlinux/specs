%global _firmwarepath /lib/firmware
%define firmware_name spb3021

Name: firmware-alsa-%firmware_name
Version: 1
Release: alt1

Summary: Alsa firmware for the Rikor RN NINO 203.2/IC-025

License: Distributable
Group: Sound
Url: https://rikor.com/support/

# spb 302.1 alse audio drivers.tgz
Source0: spb-3021-fw-1.tgz

BuildArch: noarch

%description
This package contains the alsa sound driver
for laptops such as Rikor RN NINO 203.2/IC-025.

%prep
%setup -n spb-3021-fw

%install
install -d %buildroot%_sysconfdir/modprobe.d/
install -d %buildroot%_firmwarepath/

install -p *.conf %buildroot%_sysconfdir/modprobe.d/
install -p *.fw %buildroot%_firmwarepath/

%files
%_sysconfdir/modprobe.d/hda-jack-retask.conf
%_firmwarepath/hda-jack-retask.fw

%changelog
* Mon Jun 30 2025 Leontiy Volodin <lvol@altlinux.org> 1-alt1
- Initial build for ALT Sisyphus (ALT #54659).
