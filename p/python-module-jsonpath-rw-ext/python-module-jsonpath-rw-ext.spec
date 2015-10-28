%global pkgname jsonpath-rw-ext
%def_with python3

Name: python-module-%pkgname
Version: 0.1.9
Release: alt1
Summary: Extensions for JSONPath RW
Group: Development/Python

License: ASL 2.0
Url: https://github.com/kennknowles/python-jsonpath-rw
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.4
BuildRequires: python-module-jsonpath-rw

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-jsonpath-rw
%endif

%description
jsonpath-rw-ext extends json-path-rw capabilities by adding multiple extensions.
'len' that allows one to get the length of a list.
'sorted' that returns a sorted version of a list, 
'arithmetic' that permits one to make math operation between elements and 'filter' to select only certain elements of a list.

%if_with python3
%package -n python3-module-%pkgname
Summary: Extensions for JSONPath RW
Group: Development/Python3

%description -n python3-module-%pkgname
jsonpath-rw-ext extends json-path-rw capabilities by adding multiple extensions.
'len' that allows one to get the length of a list.
'sorted' that returns a sorted version of a list, 
'arithmetic' that permits one to make math operation between elements and 'filter' to select only certain elements of a list.
%endif

%package doc
Summary: Documentation for %name
Group:  Development/Documentation

%description doc
Documentation for %name.

%prep
%setup

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pkgname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.9-alt1
- Initial build.
