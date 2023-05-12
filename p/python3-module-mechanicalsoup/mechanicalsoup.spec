Name: python3-module-mechanicalsoup
Version: 1.2.0
Release: alt2

%def_with check

Summary: A Python library for automating website interaction
License: MIT
Group: Development/Python
Url: https://pypi.org/project/MechanicalSoup/
BuildArch: noarch
Source0: %name-%version-%release.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -oaddopts=-Wignore

%files
%python3_sitelibdir/mechanicalsoup
%python3_sitelibdir/MechanicalSoup-%version.dist-info

%changelog
* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Fixed FTBFS (pytest-httpbin 2.0).

* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- 1.1.0 released

* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- initial
