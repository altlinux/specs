%define oname processional

Name: python3-module-processional
Version: 0.1.4
Release: alt1

Summary: Simplifies functional programming in Python's multiprocessing and multithreading

Url: https://pypi.org/project/processional/
License: LGPLv3
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
This module brings the ease and clearity of functionnal programming into the world of multiprocessing and multithreading in Python.

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
* Mon Jun 30 2025 Ivan Mazhukin <vanomj@altlinux.org> 0.1.4-alt1
- Initial build for ALT Sisyphus

