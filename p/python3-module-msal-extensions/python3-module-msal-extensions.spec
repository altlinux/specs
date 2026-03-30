%define _unpackaged_files_terminate_build 1
%define pypi_name msal-extensions
%define mod_name msal_extensions
%def_with check

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1.1
Summary: Microsoft Authentication Library extensions (MSAL EX)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/msal-extensions/
Vcs: https://github.com/AzureAD/microsoft-authentication-extensions-for-python.git

BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%EVR.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest

BuildRequires: python3-module-msal
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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1.1
- Demodernized packaging.

* Mon Mar 17 2025 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1.

* Fri Mar 14 2025 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Fri Jan 10 2025 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.0.0 -> 1.2.0 (closes: #52422).

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
