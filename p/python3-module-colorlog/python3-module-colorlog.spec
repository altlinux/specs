%define modname colorlog

Name: python3-module-%modname
Version: 4.2.1
Release: alt1

Summary: Python 3 module for log formatting with colors
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
colorlog.ColoredFormatter is a formatter for use with Python's logging
module that outputs records using terminal colors.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.md


%changelog
* Mon Jul 27 2020 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Sat Jan 04 2020 Yuri N. Sedunov <aris@altlinux.org> 4.1.0-alt1
- 4.1.0
- disabled python2 build

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.1.4-alt1
- 3.1.4

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt1
- 3.1.2

* Mon Sep 25 2017 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Jul 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Jul 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- first build for Sisyphus


