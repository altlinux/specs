%define _unpackaged_files_terminate_build 1
%define pypi_name babelfish

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.1
Release: alt1

Summary: A module to work with countries and languages
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/babelfish
VCS: https://github.com/Diaoul/babelfish

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: python3(pkg_resources)
%endif

%description
BabelFish is a Python library to work with countries and languages.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/babelfish/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 31 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Automatically updated to 0.6.1.

* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt2.1
- NMU: fixed FTBFS.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 0.6.0-alt2
- Modernized packaging (fixes FTBFS due to poetry-core 1.1.0).

* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.5 -> 0.6.0.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.5-alt4
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.5-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.5-alt3
- Updated to upstream release version 0.5.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.5-alt2.dev.git20150124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.5-alt2.dev.git20150124
- Delete unnecessary dependens

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev.git20150124
- Version 0.5.5-dev

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.dev.git20140622
- Initial build for Sisyphus

