%define _unpackaged_files_terminate_build 1
%define pypi_name parse
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.20.2
Release: alt1
Summary: parse() is the opposite of format()
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/parse/
Vcs: https://github.com/r1chardj0n3s/parse
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Parse strings using a specification based on the Python format() syntax.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# override coverage cli options
%pyproject_run_pytest -ra -o=addopts=''

%files
%doc README.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 11 2024 Stanislav Levin <slev@altlinux.org> 1.20.2-alt1
- 1.20.1 -> 1.20.2.

* Tue Mar 05 2024 Stanislav Levin <slev@altlinux.org> 1.20.1-alt1
- 1.19.0 -> 1.20.1.

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 1.19.0-alt2
- Moved on modern pyproject macros.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.19.0-alt1
- 1.8.2 -> 1.19.0.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt1
- Updated to upstream version 1.8.2.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.6-alt2
- Fixed tests.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.6-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1.git20141117
- Initial build for Sisyphus

