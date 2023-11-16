%define dkms_name openrazer-driver
%define dkms_version 3.7.0

Name: openrazer
Version: 3.7.0
Release: alt1

Summary: Open source driver and user-space daemon for managing Razer devices
License: GPL-2.0
Group: System/Kernel and hardware
URL: https://github.com/openrazer/openrazer
BuildArch: noarch

Source0: %name-%version.tar

Requires: openrazer-kernel-modules-dkms
Requires: openrazer-daemon
Requires: python3-module-openrazer
BuildRequires: python3-module-setuptools

%description
Meta package for installing all required openrazer packages.

%package -n %name-kernel-modules-dkms
Summary: OpenRazer Driver DKMS package
Group: System/Kernel and hardware

%description -n %name-kernel-modules-dkms
Kernel driver for Razer devices (DKMS-variant).

%package -n %name-daemon
Summary: OpenRazer Service package
Group: System/Kernel and hardware
Requires: openrazer-kernel-modules-dkms

%description -n %name-daemon
Userspace daemon that abstracts access to the kernel driver. Provides a DBus service for applications to use.

%package -n python3-module-%name
Summary: OpenRazer Python library
Group: System/Libraries
Requires: openrazer-daemon

%description -n python3-module-%name
Python library for accessing the daemon from Python.

%prep
%setup

%build
# noop

%install
make DESTDIR=%buildroot setup_dkms udev_install daemon_install python_library_install

mkdir -p %buildroot/lib/udev/
for f in %buildroot%_libexecdir/udev/*
do
mv -v "$f" %buildroot/lib/udev/
done

%pre -n %name-kernel-modules-dkms
#!/bin/sh
set -e
getent group plugdev >/dev/null || groupadd -r plugdev

%post -n openrazer-kernel-modules-dkms
#!/bin/sh
set -e
dkms install %dkms_name/%dkms_version || {
echo "Failed to install openrazer-driver! Update your kernel and install"
echo "kernel-headers-modules matching your kernel type std-def/un-def."
}

%preun -n openrazer-kernel-modules-dkms
#!/bin/sh
if [ "$(dkms status -m %dkms_name -v %dkms_version)" ]; then
  dkms remove -m %dkms_name -v %dkms_version --all
fi

%files
# meta package is empty

%files -n %name-kernel-modules-dkms
%_udevrulesdir/99-razer.rules
/lib/udev/razer_mount
%_usrsrc/%dkms_name-%dkms_version/

%files -n %name-daemon
%_bindir/%name-daemon
%python3_sitelibdir/%{name}_daemon/
%python3_sitelibdir/%{name}_daemon-%version-py%_python3_version.egg-info/
%_datadir/%name/
%_datadir/dbus-1/services/org.razer.service
%_prefix/lib/systemd/user/%name-daemon.service
%_man5dir/razer.conf.5*
%_man8dir/%name-daemon.8*

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version-py%_python3_version.egg-info/

%changelog
* Tue Nov 14 2023 Anton Kurachenko <srebrov@altlinux.org> 3.7.0-alt1
- New version 3.7.0.

* Sat Jul 1 2023 Anton Kurachenko <srebrov@altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus.
