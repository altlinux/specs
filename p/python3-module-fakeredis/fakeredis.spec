%define _unpackaged_files_terminate_build 1
%define pypi_name fakeredis
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 2.36.1
Release: alt1
Summary: Fake implementation of redis API for testing purposes
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/fakeredis/
Vcs: https://github.com/cunla/fakeredis-py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
fakeredis is a pure-Python implementation of the redis-py python client that
simulates talking to a redis server. This was created for a single purpose: to
write unittests. Setting up redis is not hard, but many times you want to write
unittests that do not talk to an external server (such as redis). This module
now allows tests to simply use this module as a reasonable substitute for
redis.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
# deduplicate packaging of common license
rm %buildroot%python3_sitelibdir/%mod_name/LICENSE

%check
# requires redis for most tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 08 2026 Stanislav Levin <slev@altlinux.org> 2.36.1-alt1
- 2.35.1 -> 2.36.1

* Mon Apr 13 2026 Stanislav Levin <slev@altlinux.org> 2.35.1-alt1
- 2.35.0 -> 2.35.1.

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 2.35.0-alt1
- 2.34.1 -> 2.35.0.

* Tue Mar 03 2026 Stanislav Levin <slev@altlinux.org> 2.34.1-alt1
- 2.34.0 -> 2.34.1.

* Tue Feb 17 2026 Stanislav Levin <slev@altlinux.org> 2.34.0-alt1
- 2.33.0 -> 2.34.0.

* Wed Dec 17 2025 Stanislav Levin <slev@altlinux.org> 2.33.0-alt1
- 2.32.1 -> 2.33.0.

* Mon Dec 15 2025 Stanislav Levin <slev@altlinux.org> 2.32.1-alt1
- 2.31.1 -> 2.32.1.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 2.31.1-alt1
- 2.31.0 -> 2.31.1.

* Tue Aug 12 2025 Stanislav Levin <slev@altlinux.org> 2.31.0-alt1
- 2.30.3 -> 2.31.0.

* Wed Jul 30 2025 Stanislav Levin <slev@altlinux.org> 2.30.3-alt1
- 2.30.2 -> 2.30.3.

* Tue Jul 29 2025 Stanislav Levin <slev@altlinux.org> 2.30.2-alt1
- 2.30.1 -> 2.30.2.

* Wed Jul 02 2025 Stanislav Levin <slev@altlinux.org> 2.30.1-alt1
- 2.30.0 -> 2.30.1.

* Tue Jun 17 2025 Stanislav Levin <slev@altlinux.org> 2.30.0-alt1
- 2.18.0 -> 2.30.0.

* Tue Aug 15 2023 Stanislav Levin <slev@altlinux.org> 2.18.0-alt1
- 2.14.1 -> 2.18.0.

* Fri Jun 09 2023 Stanislav Levin <slev@altlinux.org> 2.14.1-alt1
- 2.13.0 -> 2.14.1.

* Mon May 22 2023 Stanislav Levin <slev@altlinux.org> 2.13.0-alt1
- 2.12.1 -> 2.13.0.

* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 2.12.1-alt1
- 1.4.3 -> 2.12.1.

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- Initial build for Sisyphus.
