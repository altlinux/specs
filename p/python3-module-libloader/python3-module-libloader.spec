%define _unpackaged_files_terminate_build 1
%define pypi_name libloader

Name:    python3-module-%pypi_name
Version: 0.21
Release: alt1

Summary: Cross-platform shared library loader which expects a certain path structure
License: MIT
Group:   Development/Python3
URL:     https://github.com/accessibleapps/libloader

%add_python3_req_skip pywintypes
%add_python3_req_skip win32com.client

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

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 21 2025 Artem Semenov <savoptik@altlinux.org> 0.21-alt1
- Initial build for Sisyphus
