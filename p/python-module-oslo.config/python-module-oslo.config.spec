%define oname oslo.config

%def_with python3

Name:       python-module-%oname
Version:    3.22.1
Release:    alt1.1
Summary:    OpenStack common configuration library

Group:      Development/Python
License:    ASL 2.0
URL: http://docs.openstack.org/developer/oslo.config/
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch:  noarch

Provides: python-module-oslo-config = %EVR
Obsoletes: python-module-oslo-config < %EVR
%py_provides oslo

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx >= 1.2.1
BuildRequires: python-module-oslosphinx >= 4.7.0
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-rfc3986 >= 0.3.1
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-mock >= 2.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.3
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-argparse
BuildRequires: python3-module-netaddr >= 0.7.13
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-stevedore >= 1.17.1
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    OpenStack common configuration library
Group: Development/Python3
Provides: python3-module-oslo-config = %EVR
%py3_provides oslo

%description -n python3-module-%oname
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary:    Documentation for OpenStack common configuration library
Group: Development/Documentation
Provides: python-module-oslo-config-doc = %EVR
Obsoletes: python-module-oslo-config-doc < %EVR

%description doc
Documentation for the oslo-config library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
#rm -rf %{oname}.egg-info

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/oslo-config-generator \
   %buildroot%_bindir/python3-oslo-config-generator
popd
%endif

%python_install

#%check

%files
%doc README.rst
%_bindir/oslo-config-generator
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-oslo-config-generator
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc LICENSE doc/build/html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.22.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.1-alt1
- 3.22.1

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.0-alt1
- 3.22.0
- add test package

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 3.17.1-alt1
- 3.17.1

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.17.0-alt1
- 3.17.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1
- 3.9.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0
- rename from python-module-oslo-config to python-module-oslo.config
- add python3 package

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2.1-alt1
- First build for ALT
