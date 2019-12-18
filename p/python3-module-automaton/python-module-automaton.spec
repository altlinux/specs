%define sname automaton

Name: python3-module-%sname
Version: 1.15.0
Release: alt2
Summary: Friendly state machines for python
Group: Development/Python3
License: ASL 2.0
Url: https://wiki.openstack.org/wiki/Oslo#automaton
Source: %sname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-prettytable >= 0.7.2

BuildArch: noarch

%description
Friendly state machines for python.

%package tests
Summary: Tests for %sname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %sname.

%package doc
Summary: Friendly state machines for python - documentation
Group: Development/Documentation

%description doc
Friendly state machines for python (documentation)

%prep
%setup -n %sname-%version

# Remove bundled egg-info
rm -rf %sname.egg-info

%build
%python3_build

%install
%python3_install

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

#%check
#python setup.py test

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html README.rst

%changelog
* Wed Dec 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.15.0-alt2
- Build without python2.

* Sat Dec 08 2018 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- 1.15.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- Initial release
