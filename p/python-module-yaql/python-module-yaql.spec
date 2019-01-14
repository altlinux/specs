%define pypi_name yaql
%def_without doc

Name: python-module-%pypi_name
Version: 1.1.3
Release: alt1
Summary: YAQL - Yet Another Query Language
Group: Development/Python

License: ASL 2.0
Url: https://yaql.readthedocs.io
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-ply
BuildRequires: python-module-dateutil >= 2.4.2

BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-ply
BuildRequires: python3-module-dateutil >= 2.4.2

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-reno >= 1.8.0

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query language,
that allows performing complex queries against arbitrary objects.
It has a vast and comprehensive standard library of frequently 
used querying functions and can be extend even further with user-specified functions.

%package -n python3-module-%pypi_name
Summary: YAQL - Yet Another Query Language
Group: Development/Python3

%description -n python3-module-%pypi_name
YAQL (Yet Another Query Language) is an embeddable and extensible query language,
that allows performing complex queries against arbitrary objects.
It has a vast and comprehensive standard library of frequently
used querying functions and can be extend even further with user-specified functions.

%package -n python3-module-%pypi_name-tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: python3-module-%pypi_name = %EVR

%description -n python3-module-%pypi_name-tests
This package contains tests for %pypi_name.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %pypi_name.

%package doc
Summary: yaql documentation
Group: Development/Documentation

%description doc
Documentation for yaql

%prep
%setup -n %pypi_name-%version
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%if_with doc
# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%python_install
mv %buildroot%_bindir/%pypi_name %buildroot%_bindir/%pypi_name.py2

pushd ../python3
%python3_install
popd

%files
%doc README.rst
%_bindir/%pypi_name.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%pypi_name
%doc README.rst
%_bindir/%pypi_name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/*/tests

%if_with doc
%files doc
%doc doc/build/html
%endif

%changelog
* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.3-alt1
- 1.1.3

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- Initial Package
