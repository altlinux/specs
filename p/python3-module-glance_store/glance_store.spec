%define oname glance_store
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 4.1.0
Release: alt1.1

Summary: OpenStack Image Service Store Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/glance_store

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 4.7.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-jsonschema >= 3.2.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-requests >= 2.14.2

%if_with check
BuildRequires: python3-module-oslo.vmware >= 3.6.0
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-os-brick >= 2.6.0
BuildRequires: python3-module-oslo.privsep >= 1.23.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-retrying >= 1.3.3
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-boto3 >= 1.9.199
BuildRequires: python3-module-httplib2 >= 0.9.1
BuildRequires: python3-module-oslo.rootwrap >= 5.8.0
BuildRequires: python3-module-os-service-types
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-doc8 >= 0.6.0
%endif

%description
Glance's stores library

This library has been extracted from the Glance source code for the specific
use of the Glance and Glare projects.

The API it exposes is not stable, has some shortcomings, and is not a general
purpose interface. We would eventually like to change this, but for now using
this library outside of Glance or Glare will not be supported by the core team.

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

sed 's/requests.packages.urllib3.util/urllib3.util/' -i glance_store/_drivers/vmware_datastore.py

%build
%pyproject_build

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
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/glance/rootwrap.d
mv %buildroot/usr/etc/glance/rootwrap.conf %buildroot%_sysconfdir/glance/rootwrap.conf
mv %buildroot/usr/etc/glance/rootwrap.d/glance_cinder_store.filters \
  %buildroot%_sysconfdir/glance/rootwrap.d/glance_cinder_store.filters

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/glance-rootwrap
%dir %_sysconfdir/glance
%dir %_sysconfdir/glance/rootwrap.d
%config(noreplace) %_sysconfdir/glance/rootwrap.conf
%config(noreplace) %_sysconfdir/glance/rootwrap.d/glance_cinder_store.filters
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1.1
- Moved on modern pyproject macros.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.
- Renamed spec file.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 0.26.1-alt4
- Build without python2.

* Mon Apr 22 2019 Lenar Shakirov <snejok@altlinux.ru> 0.26.1-alt3
- Move tests/__init__.py* to main package

* Fri Apr 19 2019 Lenar Shakirov <snejok@altlinux.ru> 0.26.1-alt2
- Move tests.fakes to main package

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 0.26.1-alt1
- 0.26.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.20.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 0.20.0-alt1
- 0.20.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Thu Jun 16 2016 Lenar Shakirov <snejok@altlinux.ru> 0.13.1-alt3
- tests.fakes packed: needed for glance-{api,registry}

* Thu Jun 16 2016 Lenar Shakirov <snejok@altlinux.ru> 0.13.1-alt2
- Fix urllib3.util import in vmware_datastore.py

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial release
