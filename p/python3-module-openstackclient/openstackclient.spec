%define oname openstackclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 6.0.0
Release: alt2

Summary: OpenStack Command-line Client

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-openstackclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 3.5.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-openstacksdk >= 0.61.0
BuildRequires: python3-module-osc-lib >= 2.3.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneclient >= 3.17.0
BuildRequires: python3-module-novaclient >= 9.1.0
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-stevedore >= 2.0.1

%if_with check
BuildRequires: python3-module-keystoneauth1 >= 3.6.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-mock
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-tempest >= 17.1.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-wrapt >= 1.7.0
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-osc-lib-tests
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
%endif

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack that brings the
command set for Compute, Identity, Image, Network, Object Store and Block Storage
APIs together in a single shell with a uniform command structure.

The primary goal is to provide a unified shell command structure and a common
language to describe operations in OpenStack.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%if_with docs
# install man page
install -pDm 644 man/openstack.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/openstack
%python3_sitelibdir/%oname
%python3_sitelibdir/python_openstackclient-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 6.0.0-alt2
- Build with check.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 6.0.0-alt1
- Automatically updated to 6.0.0.
- Renamed spec file.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Build without docs.

* Fri Nov 01 2019 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- new version 4.0.0
- Build without python2.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 3.16.2-alt1
- 3.16.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 3.8.1-alt1
- 3.8.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1
- add python3 package

* Wed Aug 26 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial package

