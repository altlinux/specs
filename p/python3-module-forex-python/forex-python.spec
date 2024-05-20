%define oname forex-python

%def_without check

Name: python3-module-%oname
Version: 1.8
Release: alt1

Summary: Foreign exchange rates, Bitcoin price index and currency conversion using ratesapi.io
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/forex-python
VCS: https://github.com/MicroPyramid/forex-python
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-simplejson
BuildRequires: python3-module-requests
%endif

%description
The currency module of the Tryton application platform.

%prep
%setup

sed -i 's/1.6/%version/' setup.py

%build
%pyproject_build

%install
%pyproject_install

rm -rv %buildroot%python3_sitelibdir/docs

%check
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%python3_sitelibdir/forex_python
%python3_sitelibdir/forex_python-%version.dist-info

%changelog
* Mon May 20 2024 Grigory Ustinov <grenka@altlinux.org> 1.8-alt1
- Build new version.

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt1
- Initial build.
