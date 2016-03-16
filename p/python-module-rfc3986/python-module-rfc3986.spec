%define pypi_name rfc3986

%def_with python3

Name: python-module-%pypi_name
Version: 0.2.0
Release: alt1.1
Summary: Validating URI References per RFC 3986
Group: Development/Python
License: ASL 2.0
Url: https://pypi.python.org/pypi/rfc3986
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

%description
A Python implementation of RFC 3986 including validation and authority parsing.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Validating URI References per RFC 3986
Group: Development/Python3

%description -n python3-module-%pypi_name
A Python implementation of RFC 3986 including validation and authority parsing.
%endif


%prep
%setup

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
export LANG=en_US.UTF-8
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
export LANG=en_US.UTF-8
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif


%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial package
