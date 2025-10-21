Name: python3-module-marshmallow
Version: 4.0.1
Release: alt1

Summary: Simplified object serialization
License: MIT
Group: Development/Python
Url: https://pypi.org/project/marshmallow
VCS: https://github.com/marshmallow-code/marshmallow

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra tests

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/marshmallow
%python3_sitelibdir/marshmallow-%version.dist-info

%changelog
* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.1-alt1
- 4.0.1 released

* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.19.0-alt1
- 3.19.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.0-alt1
- 3.17.0 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.0-alt1
- initial
