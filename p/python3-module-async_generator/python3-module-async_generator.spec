%define _unpackaged_files_terminate_build 1
%define pypi_name async_generator
%define modulename %pypi_name

%def_with check

Name: python3-module-%modulename
Version: 1.10
Release: alt3
Summary: Making it easy to write async iterators in Python 3.5
License: MIT or Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/async_generator/
Vcs: https://github.com/python-trio/async_generator
BuildArch: noarch
Source: %modulename-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Python 3.6 added async generators. (What's an async generator?
Check out my 5-minute lightning talk demo from PyCon 2016.)

Python 3.7 adds some more tools to make them usable,
like contextlib.asynccontextmanager.

%package tests
Summary: Making it easy to write async iterators in Python 3.5
Group: Development/Python3
Requires: %name = %EVR

%description tests
Python 3.6 added async generators. (What's an async generator?
Check out my 5-minute lightning talk demo from PyCon 2016.)

Python 3.7 adds some more tools to make them usable,
like contextlib.asynccontextmanager.

This package contains tests for Python-3.

%prep
%setup -n %modulename-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%modulename/_tests

%files tests
%python3_sitelibdir/%modulename/_tests

%changelog
* Thu Apr 27 2023 Stanislav Levin <slev@altlinux.org> 1.10-alt3
- Modernized packaging.
- Mapped PyPI name to distro's one.

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10-alt2
- Moved tests into separate package.

* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.10-alt1
- Initial build for Sisyphus
