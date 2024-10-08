%define _unpackaged_files_terminate_build 1
%define pypi_name vcrpy
%define mod_name vcr

%def_with check

Name: python3-module-%pypi_name
Version: 6.0.2
Release: alt1
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/vcrpy/
Vcs: https://github.com/kevin1024/vcrpy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
Automatically mock your HTTP interactions to simplify and speed up
testing.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export REQUESTS_CA_BUNDLE=`python3 -m pytest_httpbin.certs`
# TODO: integrations tests are failing atm, need some investigation
%pyproject_run_pytest -ra -m 'not online' tests/unit/

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 6.0.2-alt1
- 6.0.1 -> 6.0.2.

* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 4.1.1 -> 6.0.1.

* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 4.1.1-alt2
- Dropped dependency on unmaintained and unused boto.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 1.2.0 -> 4.1.1.

* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2.git20150108
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1.git20150108.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150108.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20150108.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150108
- Version 1.2.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141103
- Initial build for Sisyphus

