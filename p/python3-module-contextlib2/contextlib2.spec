%define _unpackaged_files_terminate_build 1

%define pypi_name contextlib2
%def_with check

Name: python3-module-%pypi_name
Version: 21.6.0
Release: alt1.1

Summary: Backports and enhancements for the contextlib module

Group: Development/Python3
License: LGPLv2+
Url: https://pypi.org/project/contextlib2/

# Source-git: https://github.com/jazzband/contextlib2.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
contextlib2 is a backport of the standard library's contextlib
module to earlier Python versions.

It also serves as a real world proving ground for possible
future enhancements to the standard library version.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/contextlib2/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 31 2023 Ivan A. Melnikov <iv@altlinux.org> 21.6.0-alt1.1
- NMU: fix build with python 3.11

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 21.6.0-alt1
- 0.6.0 -> 21.6.0.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.5 -> 0.6.0.
- Built Python3 package from its ows src.

* Sat Apr 27 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.5-alt2
- separate run tests for python2 and python3 (ALT bug 36666)

* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.5.5-alt1
- 0.4.0 -> 0.5.5.

* Fri Feb 03 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1.1.1.1.1.1
- BOOTSTRAP: avoid python-module-mwlib -> gevent -> greenlet (!e2k)

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.1
- Added module for Python 3

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus
