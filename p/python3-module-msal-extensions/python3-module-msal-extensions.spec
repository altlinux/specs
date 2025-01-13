%define _unpackaged_files_terminate_build 1
%define pypi_name msal-extensions
%define mod_name msal_extensions
%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1
Summary: Microsoft Authentication Library extensions (MSAL EX)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/msal-extensions/
Vcs: https://github.com/AzureAD/microsoft-authentication-extensions-for-python.git

BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%EVR.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# .github/workflows/python-package.yml
BuildRequires: python3(gi)
BuildRequires: libsecret-gir
BuildRequires: /usr/bin/gnome-keyring-daemon
BuildRequires: /bin/dbus-run-session
%endif

%description
Microsoft Authentication Library extensions (MSAL EX) provides a persistence API
that can save your data on disk, encrypted on Windows, macOS and Linux.
Concurrent data access will be coordinated by a file lock mechanism.

The Microsoft Authentication Extensions for Python offers secure mechanisms for
client applications to perform cross-platform token cache serialization and
persistence. It gives additional support to the Microsoft Authentication Library
for Python (MSAL).

MSAL Python supports an in-memory cache by default and provides the
SerializableTokenCache to perform cache serialization. You can read more about
this in the MSAL Python documentation. Developers are required to implement
their own cache persistance across multiple platforms and Microsoft
Authentication Extensions makes this simpler.

The supported platforms are Windows, Mac and Linux.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/python-package.yml
echo 'echo secret_placeholder | gnome-keyring-daemon --unlock ; pytest -vra' > linux_test.sh
chmod +x linux_test.sh
%pyproject_run -- dbus-run-session -- ./linux_test.sh

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jan 10 2025 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.0.0 -> 1.2.0 (closes: #52422).

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
