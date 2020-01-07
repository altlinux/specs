%define oname oslo.config

Name:       python3-module-%oname
Version:    6.12.0
Release:    alt1

Summary:    OpenStack common configuration library

Group:      Development/Python3
License:    ASL 2.0
URL: http://docs.openstack.org/developer/oslo.config/
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch:  noarch

Provides: python3-module-oslo-config = %EVR
Obsoletes: python3-module-oslo-config < %EVR
%py3_provides oslo

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-rfc3986 >= 1.2.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-mock >= 2.0
BuildRequires: python3-module-requests >= 2.18.0

BuildRequires: python3-module-sphinx >= 1.2.1
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-reno >= 2.5.0

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary:    Documentation for OpenStack common configuration library
Group: Development/Documentation
Provides: python3-module-oslo-config-doc = %EVR
Obsoletes: python3-module-oslo-config-doc < %EVR

%description doc
Documentation for the oslo-config library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
#rm -rf %{oname}.egg-info

%build
%python3_build

# disabling git call for last modification date from git repo
#sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
# generate html docs
#sphinx-build -W -b html doc/source doc/build/html
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc README.rst
%_bindir/oslo-config-generator
%_bindir/oslo-config-validator
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE build/sphinx/html

%changelog
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 6.12.0-alt1
- Automatically updated to 6.12.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 6.11.1-alt1
- Automatically updated to 6.11.1.
- Build without python2.

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 6.4.1-alt1
- 6.4.1

* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.22.1-alt2
- rebuild with python3.6

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
