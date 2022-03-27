Name: gcovr
Version: 5.1
Release: alt1

Summary: A Python script for summarizing gcov data
License: BSD-3-Clause
Group: Development/Tools
Url: https://pypi.python.org/pypi/gcovr

Source: https://pypi.io/packages/source/g/%name/%name-%version.tar.gz

BuildArch: noarch

Requires: %_bindir/gcov
Requires: python3-module-jinja2 python3-module-Pygments

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results. This command is inspired
by the Python coverage.py package, which provides a similar utility for
Python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/gcovr
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/*.egg-info/
%doc README.rst PKG-INFO

%changelog
* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 5.1-alt1
- 5.1

* Fri Jun 11 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- 5.0
- fixed License tag

* Sat Nov 09 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Wed Jul 04 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- 4.1

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Wed Feb 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4-alt1
- 3.4 with Python3

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1
- 3.3

* Fri Dec 13 2013 Igor Zubkov <icesik@altlinux.org> 3.1-alt1
- 3.1

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 3.0-alt1
- 2.4 -> 3.0

* Mon Sep 02 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt2
- Update Url

* Wed Aug 28 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt1
- build for Sisyphus

