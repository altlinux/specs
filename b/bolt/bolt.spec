%define git %nil
%define _libexec %_prefix/libexec
%def_enable test

Name: bolt
Version: 0.9.5
Release: alt1
Summary: Thunderbolt device manager
Group: System/Libraries
License: LGPLv2+
Url: https://gitlab.freedesktop.org/bolt/bolt
Source0: %url/-/archive/%version/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: asciidoc-a2x
BuildRequires: libudev-devel
BuildRequires: libgio-devel
BuildRequires: libudev-devel
BuildRequires: libsystemd-devel
BuildRequires: libpolkit-devel

# for the integration test (optional)
%if_enabled test
BuildRequires: python3-module-pygobject3-devel
BuildRequires: python3-module-dbus
BuildRequires: python3-module-dbusmock
BuildRequires: libumockdev-devel
%endif

%description
bolt is a system daemon to manage thunderbolt 3 devices via a D-BUS
API.  Thunderbolt 3 features different security modes that require
devices to be authorized before they can be used. The D-Bus API can be
used to list devices, enroll them (authorize and store them in the
local database) and forget them again (remove previously enrolled
devices). It also emits signals if new devices are connected (or
removed). During enrollment devices can be set to be automatically
authorized as soon as they are connected.  A command line tool, called
boltctl, can be used to control the daemon and perform all the above
mentioned tasks.

%prep
%setup
%patch -p1

%build
%meson -Ddb-name=boltd \
       -Dman=true \
       --libexecdir=%_libexec
%meson_build

%if_enabled test
%check
%meson_test
%endif

%install
%meson_install

%files
%doc COPYING README.md
%_bindir/boltctl
%_libexec/boltd
%_unitdir/%name.service
%_udevrulesdir/*-%name.rules
%_datadir/dbus-1/system.d/org.freedesktop.bolt.conf
%_datadir/dbus-1/interfaces/org.freedesktop.bolt.xml
%_datadir/polkit-1/actions/org.freedesktop.bolt.policy
%_datadir/polkit-1/rules.d/org.freedesktop.bolt.rules
%_datadir/dbus-1/system-services/org.freedesktop.bolt.service
%_man1dir/boltctl.1*
%_man8dir/boltd.8*
%ghost %dir %_localstatedir/boltd

%changelog
* Thu Jan 26 2023 L.A. Kostis <lakostis@altlinux.ru> 0.9.5-alt1
- 0.9.5.

* Mon Dec 05 2022 L.A. Kostis <lakostis@altlinux.ru> 0.9.4-alt1
- 0.9.4.

* Mon Sep 26 2022 L.A. Kostis <lakostis@altlinux.ru> 0.9.3-alt1
- 0.9.3.

* Mon May 23 2022 L.A. Kostis <lakostis@altlinux.ru> 0.9.2-alt1
- 0.9.2.

* Tue Oct 26 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1.1
- cherry-picked 130e09d1c7ff02c09e4ad1c9c36e9940b68e58d8 to fix tests
  against libumockdev-0.16.3

* Tue Feb 23 2021 L.A. Kostis <lakostis@altlinux.ru> 0.9.1-alt1
- 0.9.1.

* Tue Jun 02 2020 L.A. Kostis <lakostis@altlinux.ru> 0.8-alt0.211.gfc530dc
- 0.8-211-gfc530dc.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.8-alt0.195.g6b9b6e0
- 0.8-195-g6b9b6e0.

* Mon Jun 03 2019 L.A. Kostis <lakostis@altlinux.ru> 0.8-alt0.1.g55918d9
- Initial build for ALTLinux.
- GIT 55918d9.
