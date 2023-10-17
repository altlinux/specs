%define modname python-distutils-extra
%define pypi_name python_distutils_extra
%define ver_major 3.0

%def_disable check

Name: python3-module-distutils-extra
Version: %ver_major
Release: alt1

Summary: Integrate more support into Python's distutils
Group: Development/Python3
License: GPLv2+
Url: https://salsa.debian.org/python-team/packages/python-distutils-extra

Vcs: https://salsa.debian.org/python-team/packages/python-distutils-extra.git
Source: %modname-%version.tar

BuildArch: noarch
Requires: python3-module-setuptools >= 54.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: /proc python3-module-pytest python3-module-httplib2
BuildRequires: python3-module-pygobject3 intltool python3-module-pyflakes}

%description
Enables you to easily integrate gettext support, themed icons and
documentation into Python's distutils.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

chmod a+x %buildroot%python3_sitelibdir/DistUtilsExtra/command/build_extra.py

%check
#export PYTHONPATH=%buildroot%python3_sitelibdir
export PYTHONPATH=./
%__python3 -v test/auto.py
%_bindir/pyflakes-py3  DistUtilsExtra/ test/

%files
%python3_sitelibdir/DistUtilsExtra/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc doc/*


%changelog
* Tue Oct 17 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0
- ported to %%pyproject macros

* Mon Jun 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.47-alt1
- 2.47

* Sat Mar 26 2022 Yuri N. Sedunov <aris@altlinux.org> 2.45-alt2
- disabled %%check broken with Python-3.10

* Wed Jan 12 2022 Yuri N. Sedunov <aris@altlinux.org> 2.45-alt1
- 2.45 (new Debian upstream)
- enabled %%check

* Fri Jul 23 2021 Yuri N. Sedunov <aris@altlinux.org> 2.39-alt2
- python3-only build

* Tue Mar 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.39-alt1
- 2.39

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.38-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.38-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38-alt1
- 2.38
- new python3 module

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.29-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Andrey Cherepanov <cas@altlinux.org> 2.29-alt1
- New verion 2.29

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.1
- Rebuilt with python 2.6

* Fri Aug 04 2009 Paul Wolneykien <manowar@altlinux.ru> 2.6-alt1
- Initial build for ALTLinux

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 2.6-2
- Bump release

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 2.6-1
- Minor spec file changes
- Changed source to launchpad
- Updated to new upstream version 2.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Fabian Affolter <fabian@bernewireless.net> - 1.91.2-2
- Changed license to GPLv2+

* Sat Nov 18 2008 Fabian Affolter <fabian@bernewireless.net> - 1.91.2-1
- Initial package for Fedora

