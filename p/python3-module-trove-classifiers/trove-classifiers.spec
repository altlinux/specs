%define _unpackaged_files_terminate_build 1
%define pypi_name trove-classifiers

%def_with check

Name: python3-module-%pypi_name
Version: 2023.10.18
Release: alt1
Summary: Canonical source for classifiers on PyPI
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/trove-classifiers
VCS: https://github.com/pypa/trove-classifiers.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
# unused
%add_pyproject_deps_check_filter jinja2 natsort

%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Canonical source for classifiers on PyPI:
https://pypi.org/classifiers/

Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.

%prep
%setup
%autopatch -p1

# calver doesn't provide means for reproducible builds from source tree
echo '%version' > ./calver_version

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest
%pyproject_run -- python -m tests.lib

%files
%doc README.md
%python3_sitelibdir/trove_classifiers/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2023.10.18-alt1
- 2023.9.19 -> 2023.10.18.

* Thu Oct 05 2023 Stanislav Levin <slev@altlinux.org> 2023.9.19-alt1
- 2023.8.7 -> 2023.9.19.

* Wed Aug 09 2023 Stanislav Levin <slev@altlinux.org> 2023.8.7-alt1
- 2023.7.6 -> 2023.8.7.

* Wed Jul 26 2023 Stanislav Levin <slev@altlinux.org> 2023.7.6-alt1
- 2023.5.24 -> 2023.7.6.

* Thu May 25 2023 Stanislav Levin <slev@altlinux.org> 2023.5.24-alt1
- 2023.5.22 -> 2023.5.24.

* Tue May 23 2023 Stanislav Levin <slev@altlinux.org> 2023.5.22-alt1
- 2023.5.2 -> 2023.5.22.

* Wed May 03 2023 Stanislav Levin <slev@altlinux.org> 2023.5.2-alt1
- 2023.4.29 -> 2023.5.2.

* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 2023.4.29-alt1
- 2023.4.22 -> 2023.4.29.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 2023.4.22-alt1
- 2023.4.18 -> 2023.4.22.

* Wed Apr 19 2023 Stanislav Levin <slev@altlinux.org> 2023.4.18-alt1
- 2023.3.9 -> 2023.4.18.

* Fri Mar 10 2023 Stanislav Levin <slev@altlinux.org> 2023.3.9-alt1
- 2023.2.20 -> 2023.3.9.

* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 2023.2.20-alt1
- 2023.2.8 -> 2023.2.20.

* Mon Feb 20 2023 Stanislav Levin <slev@altlinux.org> 2023.2.8-alt1
- 2023.1.20 -> 2023.2.8.

* Fri Jan 20 2023 Stanislav Levin <slev@altlinux.org> 2023.1.20-alt1
- 2022.12.1 -> 2023.1.20.

* Fri Dec 02 2022 Stanislav Levin <slev@altlinux.org> 2022.12.1-alt1
- 2022.10.19 -> 2022.12.1.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 2022.10.19-alt1
- 2022.9.26 -> 2022.10.19.

* Tue Sep 27 2022 Stanislav Levin <slev@altlinux.org> 2022.9.26-alt1
- 2022.8.31 -> 2022.9.26.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2022.8.31-alt1
- 2022.8.7 -> 2022.8.31.

* Thu Aug 11 2022 Stanislav Levin <slev@altlinux.org> 2022.8.7-alt1
- 2022.3.30 -> 2022.8.7.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 2022.3.30-alt1
- Initial build for Sisyphus.
