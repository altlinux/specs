%def_with python3

Name: python-module-swiftclient
Version: 2.6.0
Release: alt1
Summary: Client Library for OpenStack Object Storage API
License: ASL 2.0
Url: http://pypi.python.org/pypi/%name
Source0: %name-%version.tar
Group: Development/Python

BuildArch: noarch

Requires: python-module-futures
Requires: python-module-requests

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-futures >= 2.1.3
BuildRequires: python-module-requests >= 1.1
BuildRequires: python-module-six >= 1.5.2

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-requests >= 1.1
BuildRequires: python3-module-six >= 1.5.2
%endif

# /usr/bin/swift collision with older swift-im rhbz#857900
Conflicts: swift < 2.0-alt1

%description
Client library and command line utility for interacting with Openstack
Object Storage API.

%if_with python3
%package -n python3-module-swiftclient
Summary: Client Library for OpenStack Object Storage API
Group: Development/Python3
Requires: python3-module-requests

%description -n python3-module-swiftclient
Client library and command line utility for interacting with Openstack
Object Storage API.
%endif


%package doc
Summary: Documentation for OpenStack Object Storage API Client
Group: Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_swiftclient.egg-info
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
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/swift %buildroot%_bindir/python3-swift
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
make html
popd

install -p -D -m 644 doc/manpages/swift.1 %buildroot%_man1dir/swift.1

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/swift
%python_sitelibdir/*
%_man1dir/swift.1*

%if_with python3
%files -n python3-module-swiftclient
%_bindir/python3-swift
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE doc/build/html

%changelog
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
