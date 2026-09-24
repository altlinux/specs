%define _unpackaged_files_terminate_build 1
%define pypi_name mohawk

Name:           python3-module-mohawk
Version:        1.1.0
Release:        alt1

Summary:        Python library for Hawk HTTP authentication
Group:          Development/Python3
License:        BSD-3-Clause
URL:            https://github.com/kumar303/mohawk

BuildArch:      noarch

Source:         %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools
Requires:       python3-module-six

%description
Mohawk is a Python library for Hawk HTTP authentication scheme.
It implements the Hawk protocol which allows clients to authenticate
HTTP requests using a shared secret.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install --exclude-paths %pypi_name/tests.py

#disable tests
#reason: module nose (python3-module-nose) is outdated
#%check

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.1.0-alt1
- Initial build for ALT.

