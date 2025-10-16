Name: python3-module-frozenlist
Version: 1.8.0
Release: alt1

Summary: A list-like structure which implements collections.abc.MutableSequence 
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/frozenlist
VCS: https://github.com/aio-libs/frozenlist

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements/test.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/frozenlist
%python3_sitelibdir/frozenlist-%version.dist-info

%changelog
* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.0-alt1
- 1.8.0 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt1
- 1.5.0 released

* Tue May 07 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt1
- 1.4.1 released

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.3-alt1
- 1.3.3 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released
