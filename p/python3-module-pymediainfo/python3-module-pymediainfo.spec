%define modname pymediainfo

Name: python3-module-%modname
Version: 5.0.2
Release: alt1

Summary: A Python 3 wrapper for the mediainfo library
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%modname
Source: https://pypi.io/packages/source/p/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: libmediainfo

%define python3_ver 3.5

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= %python3_ver python3-module-setuptools_scm

%description
This Python3 module provides a wrapper around the MediaInfo library.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.rst


%changelog
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


