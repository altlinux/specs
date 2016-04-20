%define sname debtcollector
%def_with python3

Name: python-module-%sname
Version: 1.3.0
Release: alt1
Summary: A collection of Python deprecation patterns and strategies
Group: Development/Python

License: ASL 2.0
Url: https://pypi.python.org/pypi/debtcollector
Source: %name-%version.tar

BuildArch: noarch

# fix autoreq
%py_requires funcsigs

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-wrapt >= 1.7.0
BuildRequires: python-module-funcsigs >= 0.4
BuildRequires: python-module-fixtures
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
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

%if_with python3
%package -n python3-module-%sname
Summary: A collection of Python deprecation patterns and strategies
Group: Development/Python3

%description -n python3-module-%sname
It is a collection of functions/decorators which is used to signal a user when
*  a method (static method, class method, or regular instance method) or a class
    or function is going to be removed at some point in the future.
* to move a instance method/property/class from an existing one to a new one
* a keyword is renamed
* further customizing the emitted messages
%endif

%package doc
Summary: Documentation for the debtcollector module
Group: Development/Documentation

%description doc
Documentation for the debtcollector module


%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

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

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst CONTRIBUTING.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html
%doc LICENSE

%changelog
* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial build
