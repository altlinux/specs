%define _unpackaged_files_terminate_build 1

%define pypi_name pyzbar

%def_without check

Name: python3-module-%pypi_name
Version: 0.1.9
Release: alt1

Summary: Read one-dimensional barcodes and QR codes from Python 2 and 3.
License: MIT
Group: Development/Python3
URL: https://github.com/NaturalHistoryMuseum/pyzbar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc CHANGELOG.md DEVELOPING.md LICENSE.txt README.rst
%_bindir/read_zbar
%exclude %_bindir/read_zbar.py
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Nov 02 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.9-alt1
- Initial build for Sisyphus
