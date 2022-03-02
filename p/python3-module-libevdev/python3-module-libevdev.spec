%define modname libevdev
%def_enable check

Name: python3-module-%modname
Version: 0.10
Release: alt1

Summary: Python wrapper around the libevdev C library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

BuildArch: noarch

Vcs: https://gitlab.freedesktop.org/libevdev/python-libevdev
Source: https://pypi.io/packages/source/l/%modname/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-pytest libevdev}

%description
python-libevdev is a Python wrapper around the libevdev C library. It
provides a Pythonic API to read events from the Linux kernel's input
device nodes and to read and/or modify the device's state and
capabilities.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3


%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README*

%changelog
* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Mon Nov 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt2
- fixed %%check

* Mon Aug 3 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- first build for Sisyphus



