%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-asyncio

%def_with check

Name: python3-module-%pypi_name
Version: 0.23.7
Release: alt1

Summary: Pytest support for asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-asyncio/
VCS: https://github.com/pytest-dev/pytest-asyncio
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
pyee supplies a BaseEventEmitter object that is similar to the EventEmitter
class from Node.js. It also supplies a number of subclasses with added support
for async and threaded programming in python, such as async/await as seen in
python 3.5+.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc *.rst
%python3_sitelibdir/pytest_asyncio/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 20 2024 Stanislav Levin <slev@altlinux.org> 0.23.7-alt1
- 0.23.6 -> 0.23.7.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.23.6-alt1
- 0.23.5 -> 0.23.6.

* Mon Feb 12 2024 Stanislav Levin <slev@altlinux.org> 0.23.5-alt1
- 0.21.1 -> 0.23.5.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 0.21.1-alt1
- 0.21.0 -> 0.21.1.

* Thu May 11 2023 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1
- 0.20.3 -> 0.21.0.

* Thu Feb 09 2023 Stanislav Levin <slev@altlinux.org> 0.20.3-alt1
- 0.20.2 -> 0.20.3.

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 0.20.2-alt1
- 0.20.1 -> 0.20.2.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 0.20.1-alt1
- 0.19.0 -> 0.20.1.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 0.19.0-alt1
- 0.17.2 -> 0.19.0.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 0.17.2-alt1
- 0.15.1 -> 0.17.2.

* Thu Oct 14 2021 Ivan A. Melnikov <iv@altlinux.org> 0.15.1-alt2
- NMU: Fix FTBFS by ignoring warnings in tests.

* Thu Apr 22 2021 Stanislav Levin <slev@altlinux.org> 0.15.1-alt1
- 0.15.0 -> 0.15.1.

* Mon Apr 19 2021 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1
- 0.14.0 -> 0.15.0.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.14.0-alt1
- 0.10.0 -> 0.14.0.

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus

