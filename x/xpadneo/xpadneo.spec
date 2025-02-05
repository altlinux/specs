%define dkms_name hid-xpadneo
%define src_dir %_usrsrc/%dkms_name-%version

Name: xpadneo
Version: 0.9.7
Release: alt1

Summary: Driver for Xbox Wireless Controller

License: GPL-3.0
Group: System/Kernel and hardware
Url: https://github.com/atar-axis/xpadneo

# Source-url: https://github.com/atar-axis/xpadneo/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Patch: xpadneo-0.9.7-alt-drop-postinstall-and-postremove-files.patch

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
%patch -p1
sed "s/@DO_NOT_CHANGE@/%version/" hid-xpadneo/dkms.conf.in > hid-xpadneo/dkms.conf

%build
%install
cd "%dkms_name"

# Module source
install -Dm0644 -t "%buildroot%_usrsrc/%dkms_name-%version/src" src/*

# DKMS files
install -Dm0644 -t "%buildroot%_usrsrc/%dkms_name-%version" Makefile dkms.conf

# Module dependencies
install -Dm0644 -t "%buildroot/etc/modprobe.d" etc-modprobe.d/*
install -Dm0644 -t "%buildroot%_udevrulesdir" etc-udev-rules.d/*

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
%config(noreplace) /etc/modprobe.d/xpadneo.conf
%_udevrulesdir/

%files -n dkms-xpadneo
%_usrsrc/%dkms_name-%version/

%changelog
* Wed Feb 05 2025 Boris Yumankulov <boria138@altlinux.org> 0.9.7-alt1
- initial build for ALT Sisyphus
