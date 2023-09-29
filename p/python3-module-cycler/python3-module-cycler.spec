%define oname cycler

%def_with check

Name: python3-module-%oname
Version: 0.12.0
Release: alt1

Summary: Composable style cycles

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/cycler

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-wheel
%if_with check
BuildPreReq: python3-module-pytest
BuildPreReq: python3-module-pytest-xdist
%endif

%description
The public API of cycler consists of a class Cycler and a factory
function cycler(). The function provides a simple interface for creating
'base' Cycler objects while the class takes care of the composition and
iteration logic.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -raR -n auto

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Fri Sep 29 2023 Anton Vyatkin <toni@altlinux.org> 0.12.0-alt1
- new version 0.12.0 (add tests from upstream github)

* Fri Apr 07 2023 Anton Vyatkin <toni@altlinux.org> 0.11.0-alt2
- Fix BuildRequires

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- build python3 module separately

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Apr 10 2017 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- New version 0.10.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.post1.git20150822.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.post1.git20150822
- Initial build for Sisyphus
