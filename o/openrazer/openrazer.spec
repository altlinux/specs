%def_with check
%define dkms_name openrazer-driver
%define dkms_version 3.8.0

Name: openrazer
Version: 3.8.0
Release: alt2

Summary: Open source driver and user-space daemon for managing Razer devices
License: GPL-2.0
Group: System/Kernel and hardware
URL: https://openrazer.github.io
Vcs: https://github.com/openrazer/openrazer
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt-skip-check-plugdev.patch
Patch1: %name-%version-alt-fake_driver-include.patch

Requires: openrazer-kernel-modules-dkms
Requires: openrazer-daemon
Requires: python3-module-openrazer
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: dbus-tools-gui
BuildRequires: python3-module-setproctitle
BuildRequires: python3-module-dbus
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-pyudev
BuildRequires: python3-module-daemonize
%endif

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
%autopatch -p1

%build
# noop

%install
make DESTDIR=%buildroot setup_dkms udev_install daemon_install python_library_install

cp -v ./pylib/%name/_fake_driver/*.cfg %buildroot%python3_sitelibdir/%name/_fake_driver/
install -D -m 0755 ./scripts/create_fake_device.py %buildroot%python3_sitelibdir/%name/scripts/create_fake_device.py

%check
# functional test
export OR_SKIP_CHECK_PLUGDEV_FOR_TESTS=1
eval $(dbus-launch --sh-syntax)
./scripts/ci/setup-fakedriver.sh
./scripts/ci/launch-daemon.sh
sleep 5
./scripts/ci/test-daemon.sh

%pre -n %name-kernel-modules-dkms
#!/bin/sh
set -e
getent group plugdev >/dev/null || groupadd -r plugdev

%post -n %name-kernel-modules-dkms
#!/bin/sh
set -e
dkms install %dkms_name/%dkms_version || {
echo "Failed to install openrazer-driver! Update your kernel and install"
echo "kernel-headers-modules matching your kernel type std-def/un-def."
}

%preun -n %name-kernel-modules-dkms
#!/bin/sh
if [ "$(dkms status -m %dkms_name -v %dkms_version)" ]; then
  dkms remove -m %dkms_name -v %dkms_version --all
fi

%files
# meta package is empty

%files -n %name-kernel-modules-dkms
%_udevrulesdir/99-razer.rules
%_udevdir/razer_mount
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
* Mon Jun 24 2024 Anton Kurachenko <srebrov@altlinux.org> 3.8.0-alt2
- Fix FTBFS.

* Wed Apr 17 2024 Anton Kurachenko <srebrov@altlinux.org> 3.8.0-alt1
- New version 3.8.0.

* Wed Feb 14 2024 Anton Kurachenko <srebrov@altlinux.org> 3.7.0-alt2
- Functional tests added in the spec.

* Tue Nov 14 2023 Anton Kurachenko <srebrov@altlinux.org> 3.7.0-alt1
- New version 3.7.0.

* Sat Jul 1 2023 Anton Kurachenko <srebrov@altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus.
