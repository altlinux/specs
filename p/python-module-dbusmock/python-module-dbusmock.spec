%define modname dbusmock
%define _name python-%modname
%def_enable python2
%def_enable check

Name: python-module-dbusmock
Version: 0.19
Release: alt1

Summary: mock D-Bus objects for tests
License: LGPLv3
Group: Development/Python
Url: https://github.com/martinpitt/python-dbusmock
# https://pypi.python.org/pypi/%_name

Source: %url/releases/download/%version/%_name-%version.tar.gz
#Source: https://pypi.io/packages/source/p/%_name/%_name-%version.tar.gz

BuildArch: noarch

%setup_python_module %modname

Requires: dbus

# for python3
BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-setuptools
%if_enabled python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
%endif
%if_enabled check
BuildRequires: /proc dbus-tools-gui %_bindir/notify-send %_bindir/nmcli upower bluez
BuildRequires: python3-module-setuptools python3-module-nose python3-module-dbus-gobject
BuildRequires: python3-module-pyflakes python3-module-pycodestyle
%if_enabled python2
BuildRequires: python-module-setuptools python-module-nose python-module-dbus-gobject
BuildRequires: python-modules-json python-module-pycodestyle
%endif
# polkit tests fail since 0.115-alt4
#BuildRequires: polkit
%endif

%description
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to D-Bus
services such as upower, systemd, ConsoleKit, gnome-session or others,
and it is hard (or impossible without root privileges) to set the state
of the real services to what you expect in your tests.

See %_docdir/%name-%version/README.rst for more information.

%package -n python3-module-%modname
Summary: mock D-Bus objects for tests (python3 version)
Group: Development/Python3

%description -n python3-module-%modname
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to D-Bus
services such as upower, systemd, ConsoleKit, gnome-session or others,
and it is hard (or impossible without root privileges) to set the state
of the real services to what you expect in your tests.

See %_docdir/%name-%version/README.rst for more information.

%prep
%setup -n %_name-%version %{?_enable_python2:-a0
mv %_name-%version py2build}

%build
%python3_build
%if_enabled python2
pushd py2build
%python_build
popd
%endif

%install
%python3_install
%if_enabled python2
pushd py2build
%python_install
popd
%endif

%check
python3 setup.py test
%if_enabled python2
pushd py2build
python setup.py test
popd
%endif

%files
%if_enabled python2
%python_sitelibdir_noarch/%modname/
%doc NEWS README.* PKG-INFO
%endif

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/


%changelog
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

