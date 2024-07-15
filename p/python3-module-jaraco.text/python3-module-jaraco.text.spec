%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.text

%def_with check

Name: python3-module-%pypi_name
Version: 3.14.0
Release: alt1
Summary: Module for text manipulation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.text/
VCS: https://github.com/jaraco/jaraco.text
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-%release.patch

%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary

%prep
%setup
%patch0 -p1
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
%python3_sitelibdir/jaraco/*
%python3_sitelibdir/jaraco.text-%version.dist-info/

%changelog
* Mon Jul 15 2024 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.12.1 -> 3.14.0.

* Tue Jun 18 2024 Stanislav Levin <slev@altlinux.org> 3.12.1-alt1
- 3.12.0 -> 3.12.1.

* Thu Mar 14 2024 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1
- 3.11.1 -> 3.12.0.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 3.11.1-alt2
- Mapped PyPI name to distro's one.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 3.11.1-alt1
- 3.11.0 -> 3.11.1.

* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.2.0 -> 3.11.0.

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 3.2.0-alt2
- install missing in previous build Lorem\ ipsum.txt

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 3.2.0-alt1
- first build for ALT

