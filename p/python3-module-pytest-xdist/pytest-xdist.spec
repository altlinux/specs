%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-xdist
%define mod_name xdist

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.0
Release: alt1
Summary: pytest xdist plugin for distributed testing, most importantly across multiple CPUs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-xdist/
Vcs: https://github.com/pytest-dev/pytest-xdist
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
The pytest-xdist plugin extends pytest with new test execution modes, the most
used being distributing tests across multiple CPUs to speed up test execution:

pytest -n auto

With this call, pytest will spawn a number of workers processes equal to the
number of available CPUs, and distribute the tests randomly across them.

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 14 2023 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Mon May 22 2023 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.3.0 -> 3.3.1.

* Mon May 15 2023 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 2.5.0 -> 3.3.0.

* Mon Feb 28 2022 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.1.0 -> 2.5.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 1.29.0 -> 2.1.0.
- Stopped Python2 package build(Python2 EOL).

* Wed Apr 29 2020 Stanislav Levin <slev@altlinux.org> 1.29.0-alt3
- Fixed FTBFS.

* Fri Dec 06 2019 Stanislav Levin <slev@altlinux.org> 1.29.0-alt2
- Fixed testing against Pytest 5.3+.

* Tue Aug 13 2019 Stanislav Levin <slev@altlinux.org> 1.29.0-alt1
- 1.27.0 -> 1.29.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 1.27.0-alt2
- Fixed testing against Pytest 5.

* Tue Mar 26 2019 Stanislav Levin <slev@altlinux.org> 1.27.0-alt1
- 1.26.1 -> 1.27.0.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.26.1-alt1
- 1.26.0 -> 1.26.1.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 1.26.0-alt1
- 1.25.0 -> 1.26.0.

* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 1.25.0-alt1
- 1.23.2 -> 1.25.0.

* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 1.23.2-alt1
- 1.22.5 -> 1.23.2.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 1.22.5-alt1
- 1.22.2 -> 1.22.5.

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.22.2-alt2
- rebuild with python3.6

* Fri Apr 13 2018 Stanislav Levin <slev@altlinux.org> 1.22.2-alt1
- 1.11 -> 1.22.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt1.hg20140924.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.hg20140924
- Initial build for Sisyphus

