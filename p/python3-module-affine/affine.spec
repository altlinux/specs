%define _unpackaged_files_terminate_build 1
%define oname affine

%def_with check

Name: python3-module-%oname
Version: 2.4.0
Release: alt1

Summary: Affine transformation matrices

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/affine/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-responses
%endif

BuildArch: noarch

%py3_provides %oname

%description
Matrices describing affine transformation of the plane.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%check
%tox_check_pyproject

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Fri Apr 07 2023 Anton Vyatkin <toni@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- build python3 module separately, clean spec
- new version (2.3.0) with rpmgs script

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0.post1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0.post1-alt2
- Import upstream sources and updated spec
- Fix build with new python3-module-pytest

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0.post1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150601.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150601
- Version 1.2.0

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141113
- Initial build for Sisyphus

