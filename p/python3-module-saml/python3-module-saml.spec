%define pypi_name saml

%def_without check

Name:    python3-module-%pypi_name
Version: 1.15.0
Release: alt1

Summary: Add SAML support to your Python software using this library
License: MIT
Group:   Development/Python3
URL:     https://github.com/SAML-Toolkits/python3-saml

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: libxmlsec1-openssl-devel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-lxml
BuildRequires: python3-module-isodate
BuildRequires: python3-module-xmlsec
BuildRequires: python3-module-freezegun
%endif

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
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/onelogin/
%python3_sitelibdir/%{pyproject_distinfo python3_%pypi_name}

%changelog
* Tue Oct 03 2023 Alexander Burmatov <thatman@altlinux.org> 1.15.0-alt1
- Initial build for Sisyphus.
