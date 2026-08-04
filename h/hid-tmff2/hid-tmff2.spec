Name:    hid-tmff2
Version: 0.83
Release: alt1

Summary: Linux kernel module for Thrustmaster wheels
License: GPL-2.0-or-later
Group:   System/Configuration/Hardware
URL:     https://github.com/Kimplul/hid-tmff2

Source:  %name-%version.tar
Source1: %name-postsubmodules-%version.tar

Requires: dkms-%name = %EVR
Requires: joyutils

BuildArch: noarch

%description
Linux kernel module with support for force feedback in
Thrustmaster T300RS, T248 and (experimental) TX, T128, T598,
T-GT II and TS-XW wheels.

%package -n dkms-%name
Summary: %name DKMS package
Group:   System/Configuration/Hardware
Requires: dkms

%description -n dkms-%name
%summary

%prep
%setup -a1
# dkms.conf carries a stale upstream version, keep it in sync
sed -e 's/^PACKAGE_VERSION=.*/PACKAGE_VERSION="%version"/' -i dkms/dkms.conf

%build

%install
install -dm755 %buildroot%_usrsrc/%name-%version

cp -a Makefile Kbuild src deps %buildroot%_usrsrc/%name-%version/

install -m644 dkms/dkms.conf %buildroot%_usrsrc/%name-%version/dkms.conf

install -Dm644 udev/99-thrustmaster.rules %buildroot%_udevrulesdir/99-thrustmaster.rules

install -Dm644 udev/71-thrustmaster-steamdeck.rules \
    %buildroot%_udevrulesdir/71-thrustmaster-steamdeck.rules

%files
%doc LICENSE README.md
%_udevrulesdir/71-thrustmaster-steamdeck.rules
%_udevrulesdir/99-thrustmaster.rules

%files -n dkms-%name
%_usrsrc/%name-%version/

%changelog
* Tue Aug 04 2026 Sergey Palcheh <minergenon@altlinux.org> 0.83-alt1
- Initial build for Sisyphus

