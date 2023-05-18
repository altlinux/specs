%define _unpackaged_files_terminate_build 1
%define pypi_name lazy-object-proxy

%def_with check

Name: python3-module-%pypi_name
Version: 1.9.0
Release: alt1
Summary: A fast and thorough lazy object proxy
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/lazy-object-proxy/
VCS: https://github.com/ionelmc/python-lazy-object-proxy.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
Provides: python3-module-lazy_object_proxy = %EVR
Obsoletes: python3-module-lazy_object_proxy < %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter objproxies hunter
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This Python module is based on wrapt's ObjectProxy with one big change: it
calls a function the first time the proxy object is used, while
wrapt.ObjectProxy just forwards the method calls to the target object.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%python3_sitelibdir/lazy_object_proxy/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.8.0 -> 1.9.0.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- 1.7.1 -> 1.8.0.

* Thu Jan 27 2022 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1
- 1.6.0 -> 1.7.1.

* Wed Jul 28 2021 Stanislav Levin <slev@altlinux.org> 1.6.0-alt3
- Obsoleted previously duplicated package.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt2
- Added conflict to old package.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.5.1 -> 1.6.0.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.4.2 -> 1.5.1.

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.4.1 -> 1.4.2.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.4.1-alt2
- Fixed testing against Pytest 5.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.3.1 -> 1.4.1.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build.
