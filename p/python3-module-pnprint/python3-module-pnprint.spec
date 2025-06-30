%define oname pnprint

Name: python3-module-pnprint
Version: 1.3
Release: alt1

Summary: Python3 module providing convenient functions to format, color and print any string
Url: https://pypi.org/project/pnprint/
License: LGPL-3.0
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)

BuildArch: noarch

%description
This is a Python3 module providing convenient functions to format, color and print any string to highlight any contained data structures.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon Jun 30 2025 Ivan Mazhukin <vanomj@altlinux.org> 1.3-alt1
- Initial build for ALT Sisyphus

