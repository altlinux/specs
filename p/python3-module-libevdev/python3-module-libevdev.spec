%define pypi_name libevdev
%def_enable check

Name: python3-module-%pypi_name
Version: 0.13.1
Release: alt1

Summary: Python wrapper around the libevdev C library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%pypi_name

Vcs: https://gitlab.freedesktop.org/libevdev/python-libevdev

Source: https://pypi.io/packages/source/l/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(hatchling)
%{?_enable_check:BuildRequires: python3(pytest) libevdev}

%description
python-libevdev is a Python wrapper around the libevdev C library. It
provides a Pythonic API to read events from the Linux kernel's input
device nodes and to read and/or modify the device's state and
capabilities.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3


%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%doc README*

%changelog
* Sat Nov 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Fri Nov 14 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13

* Thu May 29 2025 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Mon May 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Mon Nov 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt2
- fixed %%check

* Mon Aug 3 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- first build for Sisyphus



