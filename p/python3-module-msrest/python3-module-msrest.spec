%define        _unpackaged_files_terminate_build 1
%define        pypiname msrest
%define        modname %pypiname
%define        distname %pypiname
%def_disable   check

Name:          python3-module-%pypiname
Version:       0.7.1
Release:       alt1.1
Summary:       The runtime library "msrest" for AutoRest generated Python clients
License:       MIT
Group:         Development/Python3
Url:           https://github.com/Azure/msrest-for-python
Vcs:           https://github.com/Azure/msrest-for-python.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%{?!_disable_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(azure)
BuildRequires: python3(azure-core)
BuildRequires: python3(certifi)
BuildRequires: python3(isodate)
BuildRequires: python3(requests_oauthlib)
BuildRequires: python3(requests)
%endif

%description
AutoRest swagger generator Python client runtime.

This package is deprecated and no longer receives updates

* The authentication part of this package has been moved to azure-identity
* The serialization part of this package is now vendored inside SDKs themselves
* The other parts of this library are covered by azure-core

As such, we will no longer accept PR and fix issues on this project, and this
repo will be soon archived.


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
%doc *.md *.txt
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- Initial build v0.7.1 for Sisyphus.
