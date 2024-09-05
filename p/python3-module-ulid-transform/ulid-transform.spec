Name: python3-module-ulid-transform
Version: 1.0.2
Release: alt1

Summary: Fast ULID transformations
License: MIT
Group: Development/Python
Url: https://pypi.org/project/uld-transform/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildRequires(pre): rpm-build-pyproject
BuildRequires: gcc-c++
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/ulid_transform
%python3_sitelibdir/ulid_transform-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt1
- 0.7.2 released
