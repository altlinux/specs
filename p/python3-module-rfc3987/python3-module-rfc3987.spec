%define pypi_name rfc3987

%def_with check

Name:    python3-module-%pypi_name
Version: 1.3.8
Release: alt1

Summary: Parsing and validation of URIs (RFC 3896) and IRIs (RFC 3987)
License: GPL-3.0
Group:   Development/Python3
URL:     https://pypi.org/project/rfc3987/
VCS:     https://github.com/dgerber/rfc3987

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Fri Apr 14 2023 Anton Vyatkin <toni@altlinux.org> 1.3.8-alt1
- Initial build for Sisyphus
