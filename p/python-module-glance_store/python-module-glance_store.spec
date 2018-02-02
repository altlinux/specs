%define oname glance_store
%def_with python3

Name: python-module-%oname
Version: 0.20.0
Release: alt1.1
Summary: OpenStack Image Service Store Library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-enum34
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-keystoneauth1 >= 2.17.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-requests >= 2.10.0

BuildRequires: python-module-boto >= 2.32.1
BuildRequires: python-module-oslo.vmware >= 2.15.0
BuildRequires: python-module-httplib2 >= 0.7.5
BuildRequires: python-module-swiftclient >= 3.2.0
BuildRequires: python-module-cinderclient >= 1.6.0
BuildRequires: python-module-os-brick >= 1.8.0
BuildRequires: python-module-oslo.rootwrap >= 5.0.0
BuildRequires: python-module-oslotest
BuildRequires: python-module-requests-mock

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.config >= 3.7.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-stevedore >= 1.17.1
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-jsonschema >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 2.17.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-requests >= 2.10.0

BuildRequires: python3-module-boto >= 2.32.1
BuildRequires: python3-module-oslo.vmware >= 2.15.0
BuildRequires: python3-module-httplib2 >= 0.7.5
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-cinderclient >= 1.6.0
BuildRequires: python3-module-os-brick >= 1.8.0
BuildRequires: python3-module-oslo.rootwrap >= 5.0.0
%endif

BuildArch: noarch

%description
OpenStack Image Service Store Library

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack Image Service Store Library
Group: Development/Python3

%description -n python3-module-%oname
OpenStack Image Service Store Library

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_findreq_skiplist %python3_sitelibdir/glance_store/tests/functional/hooks/post_test_hook.sh

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Image Service Store Library
Group: Development/Documentation

%description doc
Documentation for OpenStack Image Service Store Library

%prep
%setup -n %oname-%version

# Remove bundled egg-info
#rm -rf %oname.egg-info
sed 's/requests.packages.urllib3.util/urllib3.util/' -i glance_store/_drivers/vmware_datastore.py

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
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif
%python_install

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%_bindir/glance-rootwrap
%python_sitelibdir/*/tests/fakes.py
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/tests/fakes.py

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%python3_sitelibdir/*/tests/fakes.py
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/tests/fakes.py
%endif

%files doc
%doc doc/build/html

%changelog
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
