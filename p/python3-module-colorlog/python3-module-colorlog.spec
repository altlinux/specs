%define modname colorlog

%def_enable check

Name: python3-module-%modname
Version: 6.6.0
Release: alt1

Summary: Python 3 module for log formatting with colors
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%modname
Source: http://pypi.io/packages/source/c/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
colorlog.ColoredFormatter is a formatter for use with Python's logging
module that outputs records using terminal colors.

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
%doc README.md


%changelog
* Wed Nov 17 2021 Yuri N. Sedunov <aris@altlinux.org> 6.6.0-alt1
- 6.6.0

* Sun Oct 17 2021 Yuri N. Sedunov <aris@altlinux.org> 6.5.0-alt1
- 6.5.0

* Sat Apr 17 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- 5.0.1

* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 4.8.0-alt1
- 4.8.0

* Tue Jan 19 2021 Yuri N. Sedunov <aris@altlinux.org> 4.7.2-alt1
- 4.7.2
- enabled %%check

* Tue Nov 10 2020 Yuri N. Sedunov <aris@altlinux.org> 4.6.2-alt1
- 4.6.2

* Mon Nov 09 2020 Yuri N. Sedunov <aris@altlinux.org> 4.5.0-alt1
- 4.5.0

* Thu Oct 29 2020 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

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


