%define _unpackaged_files_terminate_build 1
%define pypi_name crc32c

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.1
Release: alt1
Summary: Exposes the Intel SSE4.2 CRC32C instruction
License: LGPLv2.1
Group: Development/Python3
Url: https://pypi.org/project/crc32c/
VCS: https://github.com/ICRAR/crc32c.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
This package exposes to Python the crc32c algorithm implemented in the SSE 4.2
instruction set of Intel CPUs.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python -u run-tests.py

%files
%doc *.rst
%python3_sitelibdir/crc32c.cpython-*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4 -> 2.4.1.

* Wed Feb 28 2024 Stanislav Levin <slev@altlinux.org> 2.4-alt1
- 2.3 -> 2.4.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 2.3-alt1
- 2.2 -> 2.3.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 2.2-alt1
- 1.7 -> 2.2.
- Stopped build for Python2.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.7-alt2
- Fixed testing against Pytest 5.

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.7-alt1
- Initial build.
