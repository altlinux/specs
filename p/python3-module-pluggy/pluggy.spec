%define _unpackaged_files_terminate_build 1
%define pypi_name pluggy
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pluggy/
Vcs: https://github.com/pytest-dev/pluggy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 27 2023 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Fri Jun 23 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.0.0 -> 1.2.0.

* Wed Sep 08 2021 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.13.1 -> 1.0.0.

* Sun May 03 2020 Stanislav Levin <slev@altlinux.org> 0.13.1-alt2
- Dropped BR on importlib_metadata.

* Mon Apr 20 2020 Stanislav Levin <slev@altlinux.org> 0.13.1-alt1
- 0.13.0 -> 0.13.1.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.13.0-alt2
- Build for python2 disabled.

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- 0.12.0 -> 0.13.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.12.0-alt2
- Fixed testing against Pytest 5.

* Thu Jun 06 2019 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.11.0 -> 0.12.0.

* Wed May 08 2019 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.9.0 -> 0.11.0.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.1 -> 0.9.0.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Sat Oct 20 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.1 -> 0.8.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.6.0 -> 0.7.1.

* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.3.0 -> 0.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150528.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1.git20150528.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150528
- Initial build for Sisyphus

