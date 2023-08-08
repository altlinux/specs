%define _unpackaged_files_terminate_build 1
%define oname Fabric
%define pypi_name fabric
%define mod_name %pypi_name

%def_with check

Name: python3-module-%oname
Version: 3.2.1
Release: alt1
Summary: High level SSH command execution
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/fabric/
Vcs: https://github.com/fabric/fabric
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
Conflicts: python-module-%oname

%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
%add_pyproject_deps_check_filter codecov alabaster
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell
commands remotely over SSH, yielding useful Python objects in return. It builds
on top of Invoke (subprocess command execution and command-line features) and
Paramiko (SSH protocol implementation), extending their APIs to complement one
another and provide additional functionality.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name

%description tests
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell
commands remotely over SSH, yielding useful Python objects in return. It builds
on top of Invoke (subprocess command execution and command-line features) and
Paramiko (SSH protocol implementation), extending their APIs to complement one
another and provide additional functionality.

This package contains tests for %oname.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- inv test

%files
%doc README.rst
%_bindir/fab
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/testing

%files tests
%python3_sitelibdir/%mod_name/testing/

%changelog
* Mon Aug 07 2023 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 3.0.1 -> 3.2.1.

* Wed May 03 2023 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 2.5.1 -> 3.0.1.

* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version (2.5.1) with rpmgs script
- return tests subpackage with testing module (for test Fabric based code)

* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- cleaup spec, don't pack tests (useless)

* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.5.0-alt1
- Version updated to 2.5.0
- build for python2 disabled.

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.0-alt1
- Updated to upstream version 1.14.0.
- Disabled python-3 build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt1
- automated PyPI update

* Wed Apr 27 2016 Denis Medvedev <nbr@altlinux.org> 1.11.1-alt1
- 1.11.1. Removed changelog.rst from www since new sphinx chokes on that
file.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.10.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Version 1.10.1

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

