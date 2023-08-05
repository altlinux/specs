%define src_dir %_usrsrc/%name-%version

Name: xone
Version: 0.3
Release: alt1

Summary: Driver for Xbox One and Xbox Series X|S accessories

License: GPL-2.0
Group: System/Configuration/Hardware
Url: https://github.com/medusalix/xone

# Source0-url: https://github.com/medusalix/xone/archive/refs/tags/v%version.tar.gz
Source0: %name-%version.tar
Source1: %name.sh

Patch0: xone-03-fix-build-on-kernel-6.3.patch

Requires: dkms-%name = %EVR
Requires: curl
Requires: cabextract

BuildArch: noarch

%description
%name is a Linux kernel driver for Xbox One and Xbox Series X|S accessories.
It serves as a modern replacement for xpad, aiming to be compatible with
Microsoft's Game Input Protocol (GIP).

Compatibility:
* Wired devices (via USB)
* Wireless devices (with Xbox Wireless Dongle)

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
mkdir -p %buildroot%src_dir
cp -rv . %buildroot%src_dir
rm -v install.sh uninstall.sh

install -Dm 644 install/modprobe.conf %buildroot/etc/modprobe.d/%name-blacklist.conf
install -Dm 755 %SOURCE1 %buildroot%_sbindir/%name

%files
%doc LICENSE
%_sbindir/%name
/etc/modprobe.d/%name-blacklist.conf

%files -n dkms-%name
%src_dir/

%changelog
* Fri Aug 04 2023 Mikhail Tergoev <fidel@altlinux.org> 0.3-alt1
- Initial build for ALT Sisyphus
