%define _unpackaged_files_terminate_build 1
%define pypi_name dbus-next
%define mod_name dbus_next

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.3
Release: alt3
Summary: The next great DBus library for Python with asyncio support
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dbus-next/
Vcs: https://github.com/altdesktop/python-dbus-next
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-timeout
BuildRequires: dbus
%endif

%description
The next great DBus library for Python.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# flaky and order-dependent test
# https://github.com/altdesktop/python-dbus-next/issues/161
%pyproject_run -- /bin/dbus-run-session \
    python -m pytest --ignore=test/test_disconnect.py

%pyproject_run -- /bin/dbus-run-session \
    python -m pytest test/test_disconnect.py

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 20 2024 Stanislav Levin <slev@altlinux.org> 0.2.3-alt3
- Fixed FTBFS (Pytest 8.2.0).

* Sun Mar 26 2023 Egor Ignatov <egori@altlinux.org> 0.2.3-alt2
- Fix FTBFS: change dbus session daemon socket path for tests

* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.2.3-alt1
- First build for ALT
