%define _unpackaged_files_terminate_build 1
%define pypi_name cachetools

%def_with check

Name: python3-module-%pypi_name
Version: 5.2.0
Release: alt1

Summary: Extensible memoizing collections and decorators
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cachetools
VCS: https://github.com/tkem/cachetools

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache function
decorator.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# override upstream's config (too much to patch)
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/cachetools/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 09 2022 Stanislav Levin <slev@altlinux.org> 5.2.0-alt1
- 3.1.1 -> 5.2.0.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1.1-alt2
- Build for python2 disabled.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20141230.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141230
- Initial build for Sisyphus

