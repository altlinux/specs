%define oname debtcollector
%def_with python3

Name: python-module-%oname
Version: 1.11.0
Release: alt1.1
Summary: A collection of Python deprecation patterns and strategies
Group: Development/Python

License: ASL 2.0
Url: http://docs.openstack.org/developer/debtcollector
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

# fix autoreq
%py_requires funcsigs

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-wrapt >= 1.7.0
BuildRequires: python-module-funcsigs >= 0.4
BuildRequires: python-module-fixtures
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx >= 4.7.0
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-wrapt >= 1.7.0
%endif

%description
It is a collection of functions/decorators which is used to signal a user when
*  a method (static method, class method, or regular instance method) or a class
    or function is going to be removed at some point in the future.
* to move a instance method/property/class from an existing one to a new one
* a keyword is renamed
* further customizing the emitted messages


%package doc
Summary: Documentation for the debtcollector module
Group: Development/Documentation

%description doc
Documentation for the debtcollector module

%package tests
Summary: Tests for %oname library
Group: Development/Python
BuildArch: noarch

%description tests
Tests for %oname library.


%package -n python3-module-%oname
Summary: A collection of Python deprecation patterns and strategies
Group: Development/Python3

%description -n python3-module-%oname
It is a collection of functions/decorators which is used to signal a user when
*  a method (static method, class method, or regular instance method) or a class
    or function is going to be removed at some point in the future.
* to move a instance method/property/class from an existing one to a new one
* a keyword is renamed
* further customizing the emitted messages

%package -n python3-module-%oname-tests
Summary: Tests for futurist library
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%oname-tests
Tests for futurist library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

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

# doc
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst CONTRIBUTING.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html
%doc LICENSE

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0
- add tests package

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial build
