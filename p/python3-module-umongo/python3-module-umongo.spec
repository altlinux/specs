%define pypi_name umongo

# need network
%def_without check

Name:    python3-module-%pypi_name
Version: 3.1.0
Release: alt1

Summary: sync/async MongoDB ODM
License: MIT
Group:   Development/Python3
URL:     https://github.com/Scille/umongo

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
uMongo is a Python MongoDB ODM. It inception comes from two needs: the lack of
async ODM and the difficulty to do document (un)serialization with existing ODMs.

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
* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus.
