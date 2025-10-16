Name: python3-module-hassil
Version: 3.2.1
Release: alt1

Summary: The Home Assistant Intent Language parser
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/hassil
VCS: https://github.com/OHF-Voice/hassil

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check

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
%_bindir/hassil
%python3_sitelibdir/hassil
%python3_sitelibdir/hassil-%version.dist-info

%changelog
* Thu Oct 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.1-alt1
- 3.2.1 released

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.0-alt1
- 2.1.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.4-alt1
- 1.7.4 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.1-alt1
- 1.7.1 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- 1.5.1 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.5-alt1
- 1.2.5 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt1
- initial
