%define modname evdev

Name: python3-module-%modname
Version: 1.6.1
Release: alt1

Summary: Python3 bindings to the generic input event interface
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%modname
Vcs: https://github.com/gvalkov/python-evdev.git

Source: https://pypi.io/packages/source/e/%modname/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: glibc-kernheaders
BuildRequires: python3-devel python3-module-distribute

%description
This package provides bindings to the generic input event interface in
Linux. The evdev interface serves the purpose of passing events generated
in the kernel directly to userspace through character devices that are
typically located in /dev/input/

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modname/
%exclude %python3_sitelibdir/*.egg-info
%doc README*

%changelog
* Sat Jan 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Jul 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Mar 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sat Jan 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0 (python3-only)

* Sun Jan 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Apr 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Mar 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1.1
- exclude %%python*_sitelibdir/*.egg-info

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- first build for Sisyphus



