%define pypi_name pyjsparser

Name: python3-module-%pypi_name
Version: 2.7.1
Release: alt1

Summary: Fast JavaScript parser for Python
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/pyjsparser

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.7.1-alt1
- Initial build for ALT Linux.

