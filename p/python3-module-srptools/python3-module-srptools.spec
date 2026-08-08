%define pypi_name srptools

Name:    python3-module-%pypi_name
Version: 1.0.1
Release: alt1

Summary: Tools to implement Secure Remote Password (SRP) authentication
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/srptools/
VCS:     https://github.com/idlesign/srptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Requires: python3-module-click

BuildArch: noarch

Source: %name-%version.tar

%description
srptools is a collection of tools to implement Secure Remote Password
(SRP) authentication.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Sat Aug 08 2026 Sergey Palcheh <minergenon@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
