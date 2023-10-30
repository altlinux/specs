%define pypi_name csscompressor

%def_with check

Name:    python3-module-%pypi_name
Version: 0.9.5
Release: alt1

Summary: Port of YUI CSS Compressor to Python
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/sprymix/csscompressor

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

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
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 26 2023 Alexander Burmatov <thatman@altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus.
