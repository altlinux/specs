Name: python3-module-watchfiles
Version: 1.2.0
Release: alt1

Summary: Simple, modern file watching and code reload in python.
License: MIT
Group: Development/Python
URL: https://pypi.org/project/watchfiles
VCS: https://github.com/samuelcolvin/watchfiles

Source0: %name-%version.tar
Source1: pyproject_deps.json
Source2: crates.tar

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%python3_set_limited_api

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
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rf watchfiles
%pyproject_run_pytest tests

%files
%_bindir/watchfiles
%python3_sitelibdir/watchfiles
%python3_sitelibdir/watchfiles-%version.dist-info

%changelog
* Mon May 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released

* Tue Feb 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.1-alt1
- 1.1.1 released

* Mon Apr 22 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.21.0-alt2
- NMU: restored LoongArch support

* Fri Apr 19 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.21.0-alt1
- 0.21.0 released

* Thu Oct 26 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.19.0-alt2
- NMU: support LoongArch architecture

* Fri Apr 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.0-alt1
- 0.19.0 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.1-alt1
- 0.18.1 released

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.1-alt1
- 0.16.1 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- initial
