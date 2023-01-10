%define modname dbusmock
%define pypi_name python-%modname
%def_enable check

Name: python3-module-dbusmock
Version: 0.28.7
Release: alt1

Summary: mock D-Bus objects for tests
License: LGPL-3.0-or-later
Group: Development/Python3
Url: https://github.com/martinpitt/python-dbusmock
# https://pypi.python.org/pypi/%pypi_name

Source: %url/releases/download/%version/%pypi_name-%version.tar.gz

BuildArch: noarch
Requires: dbus

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-dbus
%if_enabled check
BuildRequires: /proc dbus-tools-gui %_bindir/notify-send %_bindir/nmcli upower bluez
BuildRequires: polkit iio-sensor-proxy notification-daemon
BuildRequires: python3-module-dbus-gobject python3-module-pycodestyle
BuildRequires: python3-module-pyflakes python3-module-importlib-metadata
BuildRequires: python3-module-mypy
%endif

%description
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to D-Bus
services such as upower, systemd, logind, gnome-session or others,
and it is hard (or impossible without root privileges) to set the state
of the real services to what you expect in your tests.

See %_docdir/%name-%version/README.rst for more information.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
python3 -m unittest

%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc NEWS PKG-INFO README*

%changelog
* Wed Jan 11 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.7-alt1
- 0.28.7

* Tue Nov 15 2022 Michael Shigorin <mike@altlinux.org> 0.28.6-alt2
- fix build --without check (explicit BR: python3-module-dbus)
- minor spec cleanup

* Wed Oct 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.28.6-alt1
- 0.28.6

* Wed Jul 20 2022 Yuri N. Sedunov <aris@altlinux.org> 0.28.4-alt1
- 0.28.4
- ported to %%pyproject macros

* Sun Jul 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.28.3-alt1
- 0.28.3

* Sun Jul 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2 (fixed tests with libnotify 0.8.0)

* Wed Jun 29 2022 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Mon Jun 20 2022 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 0.28.0

* Tue Apr 05 2022 Yuri N. Sedunov <aris@altlinux.org> 0.27.5-alt1
- 0.27.5

* Tue Apr 05 2022 Yuri N. Sedunov <aris@altlinux.org> 0.27.4-alt1
- 0.27.4

* Wed Mar 23 2022 Yuri N. Sedunov <aris@altlinux.org> 0.27.3-alt1
- 0.27.3

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Sat Dec 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Thu Oct 28 2021 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Sat Aug 28 2021 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Wed Jun 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.23.1-alt1
- 0.23.1

* Fri Mar 26 2021 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0

* Sat Jan 02 2021 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Fri Jan 01 2021 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Sun Dec 20 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0 (python3-only)

* Fri May 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.19-alt2
- fixed python2 build

* Fri Jan 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.19-alt1
- 0.19

* Thu Dec 26 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt2
- fixed BR after python-module-dbus split
- made python2 build optional

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3

* Sun Feb 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Thu Jan 10 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1.1
- skipped broken polkit tests

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt1
- 0.18

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1
- 0.17.1

* Thu Feb 01 2018 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt2
- fixed buildreqs

* Mon Nov 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.16.9-alt2
- rebuilt with rpm-build-gir

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.16.9-alt1
- 0.16.9

* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.16.8-alt1
- 0.16.8

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 0.16.7-alt1
- 0.16.7

* Fri Jun 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.16.4-alt1
- first build for Sisyphus

