Name: python3-module-fnv-hash-fast
Version: 0.5.0
Release: alt1

Summary: CPP implementation of fnv1a
License: MIT
Group: Development/Python
Url: https://pypi.org/project/fnv-hash-fast/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(fnvhash)

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
%python3_sitelibdir/fnv_hash_fast
%python3_sitelibdir/fnv_hash_fast-%version.dist-info

%changelog
* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- 0.5.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released
