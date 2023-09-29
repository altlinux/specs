# SPEC-file for PinePhone Keyboard Case user-space driver

Name: pinephone-keyboard
Version: 1.3
Release: alt1

Summary: PinePhone Keyboard case userspace input device daemon

License: %gpl3plus
Group: System/Configuration/Hardware
URL: https://xff.cz/git/pinephone-keyboard/
#URL: https://wiki.mobian.org/doku.php?id=pine-phone-keyboard-case-ppkc

Packager: Nikolay A. Fetisov <naf@altlinux.org>

# PPKB is intended for PinePhone / PinePhone Pro only,
# firmware utils could be used from desktop systemd.
# No much sense to build for aarch32 / ppc64le:
ExcludeArch: armh ppc64le

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name.service
Source2: %name.blacklist

Source3: switch-keyboard.sh
Source4: switch-keyboard.desktop

Source5: firmware-alt-note.txt

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Fri Sep 15 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error php8.2-libs python-modules python2-base python3-base sh4
BuildRequires: git-core php sdcc

%description
PinePhone Keyboard daemon (ppkbd) is a user-space driver
for PinePhone Keyboard case hardware.

PPKBD replaces a kernel driver and provides additional
functionality like working function keys, Fn combinations and
configurable layouts that matched keyboard's on-keys prints.


%package firmware
Summary: FOSS Pinephone Keyboard Firmware and Tools
Group: System/Configuration/Hardware
Requires: %name = %version-%release

ExcludeArch: armh ppc64le

%description firmware
This package contains firmware tools to upload/download
firmware from the PinePhone Keyboard case (PPKB).


%package doc
Summary: Pinephone Keyboard case documentation
Group: Development/Documentation
Requires: %name = %version-%release

ExcludeArch: armh ppc64le

%description doc
This package contains documentation and scheme for
PinePhone Keyboard case.


%prep
%setup
%patch0 -p1

mv -f COPYING COPYING.GPL.orig
ln -s $(relative %_licensedir/GPL-3 %_docdir/%name/COPYING.GPL) COPYING.GPL

cp  %SOURCE5 .

%build
%make_build

# Make firmware:
cd firmware/
./build.sh


%install
# PPKB daemon:
install -Dm 0755 build/ppkb-i2c-inputd %buildroot/%_sbindir/ppkb-i2c-inputd
install -Dm 0644 -- %SOURCE1 %buildroot%_unitdir/%name.service

# PPKB charger control utility:
install -Dm 0775 build/ppkb-i2c-charger-ctl %buildroot%_bindir/ppkb-i2c-charger-ctl

# modprobe blacklist
install -Dm 0644 -- %SOURCE2 %buildroot%_modprobedir/blacklist-pinephone_keyboard.conf

# Switch onscreen keyboard script
install -Dm 0755 -- %SOURCE3 %buildroot%_bindir/switch-keyboard.sh
install -Dm 0644 -- %SOURCE4 %buildroot%_desktopdir/switch-keyboard.desktop

# Debuger/flasher utilities:
install -Dm 0775 build/ppkb-i2c-debugger %buildroot%_bindir/ppkb-i2c-debugger
install -Dm 0775 build/ppkb-i2c-flasher  %buildroot%_bindir/ppkb-i2c-flasher
install -Dm 0775 build/ppkb-usb-debugger %buildroot%_bindir/ppkb-usb-debugger
install -Dm 0775 build/ppkb-usb-flasher  %buildroot%_bindir/ppkb-usb-flasher

install -Dm 0664 -- firmware/build/fw-stock.bin %buildroot%_datadir/%name/fw-stock.bin
install -Dm 0664 -- firmware/build/fw-user.bin %buildroot%_datadir/%name/fw-user.bin

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README
%doc --no-dereference COPYING.GPL

%_sbindir/ppkb-i2c-inputd
%_unitdir/%name.service
%_modprobedir/blacklist-pinephone_keyboard.conf

%_bindir/ppkb-i2c-charger-ctl

%_bindir/switch-keyboard.sh
%_desktopdir/switch-keyboard.desktop


%files firmware
%doc HACKING README README.flashing README.i2c-intf README.testing TODO

%doc firmware-alt-note.txt

%_bindir/ppkb-i2c-flasher
%_bindir/ppkb-i2c-debugger
%_bindir/ppkb-usb-flasher
%_bindir/ppkb-usb-debugger

%dir %_datadir/%name/
%_datadir/%name/*


%files doc
%doc docs/


%changelog
* Fri Sep 29 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.3-alt1
- Initial build for ALT Linux Sisyphus

