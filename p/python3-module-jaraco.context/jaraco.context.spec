%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.context

%def_with check

Name: python3-module-%pypi_name
Version: 4.3.0
Release: alt2
Summary: Context managers by Jaraco
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.context/
VCS: https://github.com/jaraco/jaraco.context.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%py3_provides %pypi_name
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
%pypi_name provides context managers by Jaraco.

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
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/jaraco/__pycache__/context.cpython-*.py*
%python3_sitelibdir/jaraco/context.py
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 4.3.0-alt2
- Mapped PyPI name to distro's one.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 4.3.0-alt1
- 4.2.0 -> 4.3.0.

* Mon Nov 21 2022 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1
- 4.1.2 -> 4.2.0.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 4.1.2-alt1
- 4.1.1 -> 4.1.2.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 4.0.0 -> 4.1.1.

* Sat Mar 27 2021 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus.
