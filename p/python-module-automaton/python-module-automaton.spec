%define sname automaton

%def_with python3

Name: python-module-%sname
Version: 1.4.0
Release: alt1.1
Summary: Friendly state machines for python
Group: Development/Python
License: ASL 2.0
Url: https://wiki.openstack.org/wiki/Oslo#automaton
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-prettytable >= 0.7

BuildRequires: python-module-setuptools
BuildRequires: python-module-oslotest >= 1.10.0
BuildRequires: python-module-testrepository >= 0.0.18
BuildRequires: python-module-testscenarios >= 0.4
BuildRequires: python-module-testtools >= 1.4.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-oslosphinx >= 2.5.0
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-prettytable >= 0.7
%endif

BuildArch: noarch

%description
Friendly state machines for python.

%if_with python3
%package -n python3-module-%sname
Summary: Friendly state machines for python.
Group: Development/Python3

%description -n python3-module-%sname
Friendly state machines for python.
%endif


%package doc
Summary: Friendly state machines for python - documentation
Group: Development/Documentation

%description doc
Friendly state machines for python (documentation)

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

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

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

#%check
#python setup.py test

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html README.rst

%changelog
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
