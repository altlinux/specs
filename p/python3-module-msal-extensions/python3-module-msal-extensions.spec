%define        _unpackaged_files_terminate_build 1
%define        pypiname msal-extensions
%define        modname msal_extensions
%define        distname %modname
%def_disable   check

Name:          python3-module-%pypiname
Version:       1.0.0
Release:       alt1.1
Summary:       Microsoft Authentication Library extensions (MSAL EX)
License:       MIT
Group:         Development/Python3
Url:           https://github.com/AzureAD/microsoft-authentication-extensions-for-python
Vcs:           https://github.com/AzureAD/microsoft-authentication-extensions-for-python.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%{?!_disable_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(msal)
BuildRequires: python3(portalocker)
BuildRequires: python3(gi)
BuildRequires: python3-module-pygobject
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
%pyproject_run_pytest
%pyproject_run_unittest

%files
%doc *.md
%python3_sitelibdir/%{distname}/
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
