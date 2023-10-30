%define pypi_name htmlmin

%def_with check

Name:    python3-module-%pypi_name
Version: 0.1.12
Release: alt1

Summary: A configurable HTML Minifier with safety features
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/mankyd/htmlmin

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
rm -fr %buildroot%python3_sitelibdir/%pypi_name/tests

%check
%pyproject_run_unittest

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 26 2023 Alexander Burmatov <thatman@altlinux.org> 0.1.12-alt1
- Initial build for Sisyphus.
