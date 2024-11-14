%define pypi_name dict2xml

%def_with check

Name:    python3-module-%pypi_name
Version: 1.7.6
Release: alt1

Summary: Very random, limited python script to convert a python dictionary into an xml file
License: MIT
Group:   Development/Python3
URL:     https://github.com/delfick/python-dict2xml

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-nose-of-yeti
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Super Simple utility to convert a python dictionary into an xml string.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 14 2024 Alexander Burmatov <thatman@altlinux.org> 1.7.6-alt1
- Initial build for Sisyphus.
