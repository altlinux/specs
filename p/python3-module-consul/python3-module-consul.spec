%define pypi_name consul

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Python client for Consul (http://www.consul.io/)
License: MIT
Group:   Development/Python3
URL:     https://github.com/cablehead/python-consul

Packager: Andrey Cherepanov <cas@altlinux.org>

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
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/python_consul-*.dist-info

%changelog
* Sat Mar 18 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
