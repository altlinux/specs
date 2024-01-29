%define _unpackaged_files_terminate_build 1

%define pypi_name kdcproxy
%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt2
Summary: A kerberos KDC HTTP proxy WSGI module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/kdcproxy
Vcs: https://github.com/latchset/kdcproxy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra tests
BuildRequires: libkrb5
%endif

%description
This package contains a Python 3.x WSGI module for proxying KDC requests
over HTTP by following the MS-KKDCP protocol. It aims to be simple
to deploy, with minimal configuration.

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
%pyproject_run_pytest -vra

%files
%doc README
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jan 29 2024 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fixed FTBFS (Python 3.12).

* Fri Jan 22 2021 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.4.2 -> 1.0.0.

* Fri Oct 04 2019 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- 0.4.1 -> 0.4.2.
- Dropped Python2 package.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 0.4.1-alt2
- Added missing dep on Pytest.

* Tue Feb 12 2019 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4 -> 0.4.1.

* Tue Aug 14 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1
- 0.3.3 -> 0.4.

* Thu Jul 26 2018 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- 0.3.2 -> 0.3.3
- Build package for Python3

* Wed Sep 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Initial build.

