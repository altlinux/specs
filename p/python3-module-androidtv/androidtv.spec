Name: python3-module-androidtv
Version: 0.0.75
Release: alt1

Summary: State information and control of Android TV devices via ADB
License: MIT
Group: Development/Python
URL: https://pypi.org/project/androidtv
VCS: https://github.com/JeffLIrion/python-androidtv

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
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
%pyproject_deps_resync_check_pipreqfile venv_requirements.txt

%build
%pyproject_build

%install
%pyproject_install

%check
# test_no_underscores needs a real git checkout (git grep); the gear
# tarball has no .git, so it can never run in the build env
%pyproject_run_pytest -o addopts= -k "not test_no_underscores" tests

%files
%python3_sitelibdir/androidtv
%python3_sitelibdir/androidtv-%version.dist-info

%changelog
* Thu Oct 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.75-alt1
- 0.0.75 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.72-alt1
- 0.0.72 released

* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.70-alt1
- 0.0.70 released

* Fri Jul 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.68-alt1
- 0.0.68 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.67-alt1
- 0.0.67 released

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.63-alt1
- 0.0.63 released

* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.60-alt1
- 0.0.60 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.57-alt1
- 0.0.57 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.52-alt1
- 0.0.52 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.47-alt1
- 0.0.47 released

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.45-alt1
- initial
