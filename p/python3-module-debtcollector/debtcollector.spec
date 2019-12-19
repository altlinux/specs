%define oname debtcollector

Name: python3-module-%oname
Version: 1.22.0
Release: alt2
Summary: A collection of Python deprecation patterns and strategies
Group: Development/Python3

License: ASL 2.0
Url: http://docs.openstack.org/developer/debtcollector
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-wrapt >= 1.7.0

BuildRequires: python3-module-fixtures

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx >= 4.7.0
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-doc8 >= 0.6.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

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
Group: Development/Python3
BuildArch: noarch

%description tests
Tests for %oname library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

rm -rf {test-,}requirements.txt

%build
%python3_build

# doc
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc README.rst CONTRIBUTING.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html
%doc LICENSE

%changelog
* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.22.0-alt2
- Build without python2.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.22.0-alt1
- Automatically updated to 1.22.0.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.21.0-alt1
- Automatically updated to 1.21.0

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.20.0-alt1
- 1.20.0

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
