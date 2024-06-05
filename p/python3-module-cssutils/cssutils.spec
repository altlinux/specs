%define _unpackaged_files_terminate_build 1
%define pypi_name cssutils
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.11.1
Release: alt1
Summary: CSS Cascading Style Sheets library for Python
License: LGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/cssutils/
Vcs: https://github.com/jaraco/cssutils
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage extras dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities!

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore -m 'not internet'

%files
%_bindir/csscapture
%_bindir/csscombine
%_bindir/cssparse
%python3_sitelibdir/%mod_name/
%exclude %python3_sitelibdir/%mod_name/tests/
%python3_sitelibdir/encutils/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jun 05 2024 Stanislav Levin <slev@altlinux.org> 2.11.1-alt1
- 2.11.0 -> 2.11.1.

* Wed May 15 2024 Stanislav Levin <slev@altlinux.org> 2.11.0-alt1
- 2.10.3 -> 2.11.0.

* Tue May 14 2024 Stanislav Levin <slev@altlinux.org> 2.10.3-alt1
- 2.10.2 -> 2.10.3.

* Mon Apr 01 2024 Stanislav Levin <slev@altlinux.org> 2.10.2-alt1
- 2.9.0 -> 2.10.2.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 2.9.0-alt1
- 2.7.1 -> 2.9.0.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1
- 2.3.0 -> 2.7.1.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 2.3.0-alt2
- Fixed FTBFS (Python3.10).

* Fri Jan 14 2022 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 1.0.2 -> 2.3.0.

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- build python3 package only

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- switch to build from tarball
- enable python3 module
- new version (1.0.2) with rpmgs script

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt2
- exclude tests from package

* Tue Jul 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7b1-alt1.1
- Rebuild with Python-2.7

* Tue Jun 01 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.9.7b1-alt1
- 1st build for ALTLinux
- thanks to real@ fr spec skeleton
