%define pypi_name yaql
%def_with python3
%def_without doc

Name: python-module-%pypi_name
Version: 1.1.1
Release: alt1
Summary: YAQL - Yet Another Query Language
Group: Development/Python

License: ASL 2.0
Url: https://launchpad.net/yaql
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.11
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-oslotest
BuildRequires: python-module-ply
BuildRequires: python-module-dateutil

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.11
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-ply
BuildRequires: python3-module-dateutil
%endif

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query language,
that allows performing complex queries against arbitrary objects.
It has a vast and comprehensive standard library of frequently 
used querying functions and can be extend even further with user-specified functions.

%if_with python3
%package -n python3-module-%pypi_name
Summary: YAQL - Yet Another Query Language
Group: Development/Python3

%description -n python3-module-%pypi_name
YAQL (Yet Another Query Language) is an embeddable and extensible query language,
that allows performing complex queries against arbitrary objects.
It has a vast and comprehensive standard library of frequently 
used querying functions and can be extend even further with user-specified functions.

%endif

%package doc
Summary: yaql documentation
Group: Development/Documentation

%description doc
Documentation for yaql

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

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

%if_with doc
# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/%pypi_name %buildroot%_bindir/%pypi_name.py3
popd
%endif
%python_install


# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%doc README.rst
%_bindir/%pypi_name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%_bindir/%pypi_name.py3
%python3_sitelibdir/*
%endif

%if_with doc
%files doc
%doc doc/build/html
%endif

%changelog
* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- Initial Package
