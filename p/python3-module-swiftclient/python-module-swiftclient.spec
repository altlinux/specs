%define oname swiftclient

Name: python3-module-%oname
Version: 3.8.1
Release: alt1

Summary: Client Library for OpenStack Object Storage API

License: ASL 2.0
Group: Development/Python3
Url: http://docs.openstack.org/developer/python-%oname

Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

Requires: python3-module-requests >= 1.1.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-requests >= 1.1.0
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

%build
%python3_build

%install
%python3_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
%make SPHINXBUILD="sphinx-build-3" html
popd

install -p -D -m 644 doc/manpages/swift.1 %buildroot%_man1dir/swift.1

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/swift
%python3_sitelibdir/*
%_man1dir/swift.1*

%files doc
%doc LICENSE doc/build/html

%changelog
* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.8.1-alt1
- Automatically updated to 3.8.1.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 3.7.0-alt1
- Automatically updated to 3.7.0

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
