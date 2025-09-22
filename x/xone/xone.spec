%define src_dir %_usrsrc/%name-%version

Name: xone
Version: 0.4.5
Release: alt1

Summary: Driver for Xbox One and Xbox Series X|S accessories

License: GPL-2.0
Group: System/Configuration/Hardware
Url: https://github.com/dlundqvist/xone.git

Source0: %name-%version.tar
Source1: %name.sh

Patch0: xone-0.3.4-alt-firmware-install.patch

Requires: dkms-%name = %EVR
# needed for firmware.sh (download and unpack firmware for the wireless dongle):
Requires: curl cabextract

BuildArch: noarch

%description
%name is a Linux kernel driver for Xbox One and Xbox Series X|S accessories.
It serves as a modern replacement for xpad, aiming to be compatible with
Microsoft's Game Input Protocol (GIP).

Compatibility:
* Wired devices (via USB)
* Wireless devices (with Xbox Wireless Dongle)

Usage:
xone <install | force-install | uninstall>.

%package -n dkms-%name
Summary: Patched %name DKMS package
Group: System/Configuration/Hardware
Requires: dkms
BuildArch: noarch

%description -n dkms-%name
%summary

%prep
%setup
%patch0 -p1

find . -type f \( -name dkms.conf -o -name '*.c' \) -exec sed -i "s/#VERSION#/%version/" {} +
%__subst "s/version=/version=%version/" %SOURCE1

%build

%install
install -Dm 644 install/modprobe.conf %buildroot/etc/modprobe.d/%name-blacklist.conf
install -Dm 755 install/firmware.sh %buildroot%_sbindir/%name-get-firmware
install -Dm 755 %SOURCE1 %buildroot%_sbindir/%name

rm -v install.sh uninstall.sh modules_load.sh
rm -rv install/

mkdir -p %buildroot%src_dir
cp -rv . %buildroot%src_dir

%files
%doc LICENSE *.md
%_sbindir/%name
%_sbindir/%name-get-firmware
/etc/modprobe.d/%name-blacklist.conf

%files -n dkms-%name
%src_dir/

%changelog
* Mon Sep 22 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.5-alt1
- 0.4.5

* Mon Aug 25 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Jul 31 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.5-alt1
- 0.3.5

* Tue Jul 01 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.4-alt1
- 0.3.4
- changed upstream to dlundqvist/xone.git (ALT bug: 54715)
- fixed build on kernel 6.15 (ALT bug: 54979)

* Mon Dec 02 2024 Mikhail Tergoev <fidel@altlinux.org> 0.3-alt4
- fixed build on kernel 6.11+

* Sat Jun 22 2024 L.A. Kostis <lakostis@altlinux.ru> 0.3-alt3
- transport: kernel 6.9+ fixes.

* Thu Sep 21 2023 Mikhail Tergoev <fidel@altlinux.org> 0.3-alt2
- move to git
- update xone.sh
- added patch for firmware.sh (unpack to tmp, check for downloading and unpacking firmware)
- clearing the dkms package

* Fri Aug 04 2023 Mikhail Tergoev <fidel@altlinux.org> 0.3-alt1
- Initial build for ALT Sisyphus
