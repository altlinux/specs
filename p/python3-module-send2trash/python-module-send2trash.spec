%define _unpackaged_files_terminate_build 1
%define pypi_name send2trash
%define mod_name send2trash
%def_with check

Name: python3-module-%pypi_name
Version: 1.8.3
Release: alt1
Summary: Python library to natively send files to Trash
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/Send2Trash/
Vcs: https://github.com/hsoft/send2trash
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# manage dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
Send2Trash is a small package that sends files to the Trash
natively and on all platforms.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%_bindir/send2trash
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/Send2Trash-%version.dist-info/

%changelog
* Fri Feb 07 2025 Stanislav Levin <slev@altlinux.org> 1.8.3-alt1
- 1.8.0 -> 1.8.3.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Tue Dec 06 2022 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- new version 1.8.0
- enabled tests

* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0.0.2.1c32-alt3
- Build for python2 disabled.

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.0.0.2.1c32-alt2
- NMU: build python3-module-send2trash

* Fri Jan 04 2019 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.0.2.1c32-alt1
- 1.5.0-2-g1c32d47.
