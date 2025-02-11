%define _unpackaged_files_terminate_build 1
%define pypi_name robotframework-debuglibrary
%define mod_name DebugLibrary

%def_with check

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1
Summary: RobotFramework debug library and an interactive shell
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/robotframework-debuglibrary/
Vcs: https://github.com/xyb/robotframework-debuglibrary/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: %pypi_name-2.2.2-tests-Drop-dependency-on-coverage.patch
Patch3: %pypi_name-2.2.2-tests-Make-selenium-tests-conditional.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: /dev/pts
BuildRequires: python3-module-pexpect
%endif

%description
Robotframework-DebugLibrary is A debug library for RobotFramework, which
can be used as an interactive shell(REPL) also.

%prep
%setup
%autopatch1 -p1
%python3_fix_shebang .
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export TERM=xterm
%pyproject_run_unittest tests.test_debuglibrary.suite

%files
%doc README.*
%_bindir/*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 10 2025 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.2.2 -> 2.5.0.

* Fri Feb 07 2025 Stanislav Levin <slev@altlinux.org> 2.2.2-alt2.1
- NMU: fixed FTBFS (tox 4).

* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 2.2.2-alt2
- Moved on modern pyproject macros.

* Thu Mar 31 2022 Stanislav Levin <slev@altlinux.org> 2.2.2-alt1
- 2.2.1 -> 2.2.2.

* Tue Sep 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.git20130806.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.git20130806
- Added module for Python 3

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20130806
- Initial build for Sisyphus

