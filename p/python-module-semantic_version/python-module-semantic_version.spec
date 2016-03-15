%define pypi_name semantic_version

%def_with python3

Name: python-module-%pypi_name
Version: 2.3.1
Release: alt1.1
Summary: A library implementing the 'SemVer' scheme.

Group: Development/Python
License: BSD
URL:  https://github.com/rbarrois/python-semanticversion
Source: %name-%version.tar
BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

%description
This small python library provides a few tools to handle `SemVer`_ in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.


%if_with python3
%package -n python3-module-%pypi_name
Summary: A library implementing the 'SemVer' scheme.
Group: Development/Python3

%description -n python3-module-%pypi_name
This small python library provides a few tools to handle `SemVer`_ in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.
%endif

%package doc
Summary: Documentation for the semantic_version library
Group: Development/Documentation

%description doc
Documentation for the semantic_version library.


%prep
%setup

# Remove bundled egg-info
#rm -rf %pypi_name.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- Initial build
