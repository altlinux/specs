%define dkms_name hid-xpadneo
%define src_dir %_usrsrc/%dkms_name-%version

Name: xpadneo
Version: 0.10.1
Release: alt1

Summary: Driver for Xbox Wireless Controller

License: GPL-3.0
Group: System/Kernel and hardware
Url: https://github.com/atar-axis/xpadneo

# Source-url: https://github.com/atar-axis/xpadneo/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Requires: dkms-xpadneo = %EVR
BuildArch: noarch

%description
%summary

%package -n dkms-xpadneo
Summary: xpadneo Driver DKMS package
Group: System/Kernel and hardware
Requires: dkms
BuildArch: noarch

%description -n dkms-xpadneo
Advanced Linux Driver for Xbox One Wireless Gamepad (DKMS-variant).

%prep
%setup

echo "%version" > VERSION

%build
%install
make PREFIX="%buildroot" ETC_PREFIX=/usr/lib install

cd "%dkms_name"

# Module source
install -d "%buildroot%_usrsrc/%dkms_name-%version"
cp -a src "%buildroot%_usrsrc/%dkms_name-%version/"

# DKMS files
install -Dm0644 -t "%buildroot%_usrsrc/%dkms_name-%version" Makefile dkms.conf
install -Dm0755 -t "%buildroot%_usrsrc/%dkms_name-%version" dkms.post_{install,remove}

%post -n dkms-xpadneo
#!/bin/sh
set -e
dkms install %dkms_name/%version || {
echo "Failed to install xpadneo Update your kernel and install"
echo "kernel-headers-modules matching your kernel flavour."
}

%preun -n dkms-xpadneo
#!/bin/sh
if [ "$(dkms status -m %dkms_name -v %version)" ]; then
  dkms remove -m %dkms_name -v %version --all
fi

%files
/usr/lib/modprobe.d/xpadneo.conf
%_udevrulesdir/
%dir %_docdir/xpadneo

%files -n dkms-xpadneo
%_usrsrc/%dkms_name-%version/

%changelog
* Sat Mar 28 2026 Boris Yumankulov <boria138@altlinux.org> 0.10.1-alt1
- new version 0.10.1

* Tue Mar 24 2026 Boris Yumankulov <boria138@altlinux.org> 0.10-alt2
- fix dkms package version (ALT bug: 58326)

* Fri Mar 20 2026 Boris Yumankulov <boria138@altlinux.org> 0.10-alt1
- new version 0.10 (ALT bug: 58279)
- use make to build

* Tue Jan 06 2026 Boris Yumankulov <boria138@altlinux.org> 0.9.8-alt2
- rebase DKMS hooks cleanup patch

* Mon Jan 05 2026 Boris Yumankulov <boria138@altlinux.org> 0.9.8-alt1
- new version 0.9.8

* Wed Feb 05 2025 Boris Yumankulov <boria138@altlinux.org> 0.9.7-alt1
- initial build for ALT Sisyphus
