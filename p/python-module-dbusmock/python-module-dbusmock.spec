%define _name python-dbusmock
%def_enable check

Name: python-module-dbusmock
Version: 0.17
Release: alt2

Summary: mock D-Bus objects for tests
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/%_name

Source: https://launchpad.net/%_name/trunk/%version/+download/%_name-%version.tar.gz

BuildArch: noarch

%setup_python_module dbusmock

Requires: dbus

BuildRequires: rpm-build-gir
BuildRequires: python-devel python-module-setuptools
# for python3
BuildRequires: rpm-build-python3 python3-devel python3-module-setuptools
%if_enabled check
BuildRequires: /proc dbus-tools-gui
BuildRequires: python-module-setuptools python-module-nose python-module-dbus python-modules-json
BuildRequires: python3-module-setuptools python3-module-nose python3-module-dbus
BuildRequires: polkit
%endif

%description
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to D-Bus
services such as upower, systemd, ConsoleKit, gnome-session or others,
and it is hard (or impossible without root privileges) to set the state
of the real services to what you expect in your tests.

See %_docdir/%name-%version/README.rst for more information.

%package -n python3-module-dbusmock
Summary: mock D-Bus objects for tests (python3 version)
Group: Development/Python3

%description -n python3-module-dbusmock
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to D-Bus
services such as upower, systemd, ConsoleKit, gnome-session or others,
and it is hard (or impossible without root privileges) to set the state
of the real services to what you expect in your tests.

See %_docdir/%name-%version/README.rst for more information.


%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build

%build
%python_build
pushd py3build
%python3_build
popd

%install
%python_install
pushd py3build
%python3_install
popd

%if_enabled check
%check
python setup.py test
pushd py3build
#python3 setup.py test
popd
%endif

%files
%python_sitelibdir_noarch/dbusmock/
%doc NEWS README.* PKG-INFO

%files -n python3-module-dbusmock
%python3_sitelibdir_noarch/dbusmock/


%changelog
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

