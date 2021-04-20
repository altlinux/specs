%define modname pyprind
%define Modname PyPrind

Name: python3-module-%modname
Version: 2.11.3
Release: alt1

Summary: Python Progress Bar and Percent Indicator Utility
Group: Development/Python3
License: BSD-3-Clause
Url: http://pypi.python.org/pypi/%Modname

Source: http://pypi.io/packages/source/P/%Modname/%Modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description
The PyPrind (Python Progress Indicator) module provides a **progress bar** and a
**percentage indicator** object that let you track the progress of a loop
structure or other iterative computation.

%prep
%setup -n %Modname-%version

%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modname/
%python3_sitelibdir_noarch/*.egg-info
%doc README.md LICENSE

%changelog
* Tue Apr 20 2021 Yuri N. Sedunov <aris@altlinux.org> 2.11.3-alt1
- 2.11.3 (Python 3 only)

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.11.2-alt1
- 2.11.2

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.11.1-alt1
- first build for Sisyphus


