Name: systemd-shim
Version: 9
Release: alt1

Summary: shim for systemd
License: %gpl2plus
Group: System/Base

URL: https://launchpad.net/ubuntu/utopic/+source/systemd-shim
Source: %name-%version.tar
Source1: org.freedesktop.systemd1.conf
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgio-devel systemd-devel

Requires: cgmanager

%define libexec_dir /lib

%description
This package emulates the systemd function that are required to run
the systemd helpers without using the init service.

%prep
%setup
%patch -p1

sed -i 's;ntpunitsdir = \$(prefix);ntpunitsdir = ;' data/Makefile.am

%build
%autoreconf
chmod +x configure
%configure \
	--libexecdir=%libexec_dir

%make_build

%install
%makeinstall_std

# Install dbus policy from systemd package
install -pDm0644 %SOURCE1 %buildroot%_sysconfdir/dbus-1/system.d/org.freedesktop.systemd1.conf

%files
%_sysconfdir/dbus-1/system.d/org.freedesktop.systemd1.conf
%libexec_dir/systemd-shim
%libexec_dir/systemd/ntp-units.d/systemd-shim.list
%libexec_dir/systemd-shim-cgroup-release-agent
%_datadir/dbus-1/system-services/org.freedesktop.systemd1.service

%changelog
* Wed Nov 12 2014 Mikhail Efremov <sem@altlinux.org> 9-alt1
- Add DBus policy from systemd package.
- Drop obsoleted patch.
- Updated to 9.

* Wed Oct 15 2014 Mikhail Efremov <sem@altlinux.org> 8-alt2
- Update dbus policy to match that from systemd 215.

* Wed Sep 24 2014 Mikhail Efremov <sem@altlinux.org> 8-alt1
- Initial build.

