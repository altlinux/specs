%define modname pymediainfo
%def_enable check

Name: python3-module-%modname
Version: 5.0.4
Release: alt1

Summary: A Python 3 wrapper for the mediainfo library
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%modname
Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz
# skip internet test
Patch: %modname-5.0.3-alt-skip_internet_test.patch

BuildArch: noarch

Requires: libmediainfo

%define python3_ver 3.5

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= %python3_ver python3-module-setuptools_scm
%{?_enable_check:BuildRequires: python3-module-pytest libmediainfo}

%description
This Python3 module provides a wrapper around the MediaInfo library.

%prep
%setup -n %modname-%version
%patch -b .nointernet

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
%doc README.rst


%changelog
* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0.4-alt1
- 5.0.4

* Tue Nov 24 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.3-alt1
- 5.0.3
- enabled %%check

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- 5.0.2

* Sun Nov 08 2020 Yuri N. Sedunov <aris@altlinux.org> 4.3-alt1
- 4.3

* Thu Apr 30 2020 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- 4.1
- disabled python2 module

* Sat Apr 06 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Sat Nov 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Wed May 16 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Mar 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Nov 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- first build for Sisyphus


