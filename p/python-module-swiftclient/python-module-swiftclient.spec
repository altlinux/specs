%define oname swiftclient

Name: python-module-%oname
Version: 3.6.0
Release: alt1
Summary: Client Library for OpenStack Object Storage API
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz
Group: Development/Python

BuildArch: noarch

Requires: python-module-futures
Requires: python-module-requests

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-futures >= 3.0.0
BuildRequires: python-module-requests >= 1.1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-keystoneclient >= 0.7.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-mock >= 1.2.0
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-requests >= 1.1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-keystoneclient >= 0.7.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-mock >= 1.2.0
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

# /usr/bin/swift collision with older swift-im rhbz#857900
Conflicts: swift < 2.0-alt1

%description
Client library and command line utility for interacting with Openstack
Object Storage API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Client Library for OpenStack Object Storage API
Group: Development/Python3
Requires: python3-module-requests

%description -n python3-module-%oname
Client library and command line utility for interacting with Openstack
Object Storage API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Object Storage API Client
Group: Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_swiftclient.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/swift %buildroot%_bindir/swift.py2

pushd ../python3
%python3_install
popd


export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
make html
popd

install -p -D -m 644 doc/manpages/swift.1 %buildroot%_man1dir/swift.1

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/swift.py2
%python_sitelibdir/*
%_man1dir/swift.1*
#%%exclude %python_sitelibdir/*/tests
#
#%files tests
#%%python_sitelibdir/*/tests

%files -n python3-module-swiftclient
%_bindir/swift
%python3_sitelibdir/*
%_man1dir/swift.1*
#%%exclude %python3_sitelibdir/*/tests
#
#%files -n python3-module-%oname-tests
#%%python3_sitelibdir/*/tests

%files doc
%doc LICENSE doc/build/html

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt1
- 3.6.0

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- new version 3.5.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem at altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1
- add python3 package

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.0-alt1
- New version (based on Fedora 2.1.0-1.fc21.src)

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt1
- Initial release for Sisyphus (based on Fedora)
