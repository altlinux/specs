%define pypi_name jsmin

%def_with check

Name:    python3-module-%pypi_name
Version: 3.0.1
Release: alt1

Summary: Javascript minifier
License: MIT
Group:   Development/Python3
URL:     https://github.com/tikitu/jsmin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

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
rm -f %buildroot%python3_sitelibdir/%pypi_name/test.py
rm -f %buildroot%python3_sitelibdir/%pypi_name/__pycache__/test*

%check
%pyproject_run_unittest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 26 2023 Alexander Burmatov <thatman@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus.
