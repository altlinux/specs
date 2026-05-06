Name: python3-module-orjson
Version: 3.11.8
Release: alt2

Summary: Fast, correct JSON library for Python
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/orjson
VCS: https://github.com/ijl/orjson

Source0: %name-%version.tar
Source1: pyproject_deps.json
Source2: crates.tar

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter python-dateutil
%add_pyproject_deps_check_filter pendulum
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup -a2
%ifdef bootstrap
cargo vendor
tar cf %SOURCE2 .cargo vendor
%endif
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile test/requirements.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= test

%files
%python3_sitelibdir/orjson
%python3_sitelibdir/orjson-%version.dist-info

%changelog
* Wed May 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.8-alt2
- fixed build with rust-1.95

* Wed Apr 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.8-alt1
- 3.11.8 released

* Fri Feb 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.7-alt1
- 3.11.7 released

* Fri Jan 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.6-alt1
- 3.11.6 released

* Tue Dec  9 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.5-alt1
- 3.11.5 released

* Mon Oct 27 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.4-alt1
- 3.11.4 released

* Fri Aug 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.3-alt1
- 3.11.3 released

* Mon Jul 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.1-alt1
- 3.11.1 released

* Thu Jul 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.11.0-alt1
- 3.11.0 released

* Mon May 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.18-alt1
- 3.10.18

* Fri Apr 04 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.16-alt1
- 3.10.16

* Tue Feb 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.15-alt1
- 3.10.15 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.14-alt1
- 3.10.14 released

* Wed Nov 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.12-alt1
- 3.10.12 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.10-alt1
- 3.10.10 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.7-alt1
- 3.10.7 released

* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.6-alt1
- 3.10.6 released

* Mon May 20 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.3-alt1
- 3.10.3 released

* Tue Apr 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.1-alt1
- 3.10.1 released

* Fri Mar 29 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.10.0-alt1
- 3.10.0 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.15-alt1
- 3.9.15 released

* Wed Feb 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.14-alt1
- 3.9.14 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.12-alt1
- 3.9.12 relelased

* Mon Dec 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.10-alt1
- 3.9.10 released

* Mon Oct 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.9-alt1
- 3.9.9 released

* Fri Sep 15 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9.7-alt1
- 3.9.8 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.10-alt1
- 3.8.10 released

* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.5-alt1
- 3.8.5 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.1-alt1
- 3.8.1 released

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt3
- rebuilt as pyproject

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt2
- rebuilt on ppc64le

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7-alt1
- 3.7.7 released
