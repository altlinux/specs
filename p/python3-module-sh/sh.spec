%define _unpackaged_files_terminate_build 1
%define pypi_name sh
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.7
Release: alt1
Summary: Python subprocess replacement
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sh/
Vcs: https://github.com/amoffat/sh
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter rstcheck
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: /dev/pts
BuildRequires: /proc
%endif

%description
sh is a full-fledged subprocess replacement for Python that allows you to call
any program as if it were a function:

  from sh import ifconfig
  print(ifconfig("eth0"))

sh is not a collection of system commands implemented in Python.

sh relies on various Unix system calls and only works on Unix-like operating
systems - Linux, macOS, BSDs etc. Specifically, Windows is not supported.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export SH_TESTS_RUNNING=1
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 03 2024 Stanislav Levin <slev@altlinux.org> 2.0.7-alt1
- 2.0.6 -> 2.0.7.

* Thu Aug 10 2023 Stanislav Levin <slev@altlinux.org> 2.0.6-alt1
- 2.0.5 -> 2.0.6.

* Wed Aug 09 2023 Stanislav Levin <slev@altlinux.org> 2.0.5-alt1
- 2.0.4 -> 2.0.5.

* Wed May 17 2023 Stanislav Levin <slev@altlinux.org> 2.0.4-alt1
- 1.12.14 -> 2.0.4.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.12.14-alt6
- Built Python3 package from its ows src.

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1.12.14-alt5
- Fixed FTBFS.

* Tue Jan 22 2019 Stanislav Levin <slev@altlinux.org> 1.12.14-alt4
- Fixed build.

* Tue Jan 15 2019 Stanislav Levin <slev@altlinux.org> 1.12.14-alt3
- Fixed build.

* Wed Sep 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.14-alt2
- Fixed build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.12.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.14-alt1
- Updated to upstream release 1.12.14.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.git20150211
- Version 1.11

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2.git20141230
- Fixed Group

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1.git20141230
- Version 1.10

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.09-alt1.git20130908
- Initial build for Sisyphus

