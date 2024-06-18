%define _unpackaged_files_terminate_build 1
%define pypi_name fastjsonschema

%def_with check

Name: python3-module-%pypi_name
Version: 2.20.0
Release: alt1
Summary: Fast JSON schema validator for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/fastjsonschema/
VCS: https://github.com/horejsek/python-fastjsonschema

BuildArch: noarch

Source: %name-%version.tar
Source1: modules.tar
Source2: pyproject_deps.json
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Fast JSON schema validator for Python

%prep
%setup -a1
%autopatch -p1

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -m "not benchmark" -vra

%files
%doc README.rst AUTHORS CHANGELOG.txt
%python3_sitelibdir/fastjsonschema/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 17 2024 Stanislav Levin <slev@altlinux.org> 2.20.0-alt1
- 2.19.1 -> 2.20.0.

* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 2.19.1-alt1
- 2.18.1 -> 2.19.1.

* Sun Feb 11 2024 Grigory Ustinov <grenka@altlinux.org> 2.18.1-alt1.1
- NMU: fixed FTBFS.

* Mon Oct 02 2023 Stanislav Levin <slev@altlinux.org> 2.18.1-alt1
- 2.18.0 -> 2.18.1.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 2.18.0-alt1
- 2.17.1 -> 2.18.0.

* Mon May 22 2023 Stanislav Levin <slev@altlinux.org> 2.17.1-alt1
- 2.16.3 -> 2.17.1.

* Tue Apr 18 2023 Stanislav Levin <slev@altlinux.org> 2.16.3-alt1
- 2.16.2 -> 2.16.3.

* Wed Jan 25 2023 Stanislav Levin <slev@altlinux.org> 2.16.2-alt1
- 2.15.1 -> 2.16.2.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.15.1-alt1
- Initial build for ALT.
