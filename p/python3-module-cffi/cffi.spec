%define _unpackaged_files_terminate_build 1
%define pypi_name cffi

%def_with check

Name: python3-module-%pypi_name
Version: 1.16.0
Release: alt1
Summary: Foreign Function Interface for Python calling C code
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/%pypi_name/
Vcs: https://github.com/python-cffi/cffi
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: cffi-0.8.6-alt-link.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libffi-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: gcc-c++
BuildRequires: python3-module-pytest
%endif

%description
Foreign Function Interface for Python calling C code.

%prep
%setup
%patch -p2
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%add_optflags -fno-strict-aliasing

%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%python3_sitelibdir/_cffi_backend.cpython-%{python_version_nodots python3}.so
%python3_sitelibdir/cffi/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 03 2023 Stanislav Levin <slev@altlinux.org> 1.16.0-alt1
- 1.15.1 -> 1.16.0.

* Thu Nov 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.15.1-alt2
- Bootstrap for python3.11.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 1.15.1-alt1
- 1.15.0 -> 1.15.1.

* Mon Dec 13 2021 Egor Ignatov <egori@altlinux.org> 1.15.0-alt1
- 1.14.5 -> 1.15.0.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 1.14.5-alt2
- Built Python3 package from its ows src.

* Thu Feb 18 2021 Grigory Ustinov <grenka@altlinux.org> 1.14.5-alt1
- Build new version.
- Enable check.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt2
- Disabled check for bootstrap on python3.9.

* Tue Mar 17 2020 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt1
- Build new version.
- Enable check.

* Thu Jan 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.13.2-alt2
- Disabled check for bootstrap on python3.8.
- Removed abi flag, because obsolete.

* Fri Nov 15 2019 Stanislav Levin <slev@altlinux.org> 1.13.2-alt1
- 1.12.3 -> 1.13.2.

* Mon May 06 2019 Stanislav Levin <slev@altlinux.org> 1.12.3-alt1
- 1.10.0 -> 1.12.3.
- Enabled testing.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Jun 8 2017 Vladimir Didenko <cow@altlinux.ru> 1.10.0-alt1
- Version 1.10.0

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Jan 10 2016 Vladimir Didenko <cow@altlinux.ru> 1.4.2-alt1
- Version 1.4.2

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Mon Aug 04 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8.6-alt2
- python{3,}-module-pycparser added to Requires
- Because find-requires script /usr/lib/rpm/python3.req.py says:
  * cffi/cparser.py: line=2 possible relative import from ., UNIMPLEMENTED

* Fri Jul 11 2014 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1
- new version 0.8.6 (with rpmrb script) (ALT bug #30174)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added module for Python3

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- fix packing

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
