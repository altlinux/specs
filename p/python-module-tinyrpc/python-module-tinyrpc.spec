
%define oname tinyrpc

Name: python-module-%oname
Version: 0.9.3
Release: alt1
Summary: Modular RPC library
Group: Development/Python
License: MIT
Url: http://github.com/mbr/tinyrpc
Source: %oname-%version.tar.gz
Patch1: tinyrpc-0.9.3-python3.patch
BuildArch: noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
tinyrpc is a library for making and handling RPC calls in python.
Its initial scope is handling jsonrpc,
although it aims to be very well-documented and modular
to make it easy to add support for further protocols.

A feature is support of multiple transports (or none at all)
and providing clever syntactic sugar for writing dispatchers.

%package -n python3-module-%oname
Summary: Modular RPC library
Group: Development/Python3

%description -n python3-module-%oname
tinyrpc is a library for making and handling RPC calls in python.
Its initial scope is handling jsonrpc,
although it aims to be very well-documented and modular
to make it easy to add support for further protocols.

A feature is support of multiple transports (or none at all)
and providing clever syntactic sugar for writing dispatchers.

%prep
%setup -n %oname-%version
%patch1 -p1
find tinyrpc -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Remove bundled egg-info
rm -rf %oname.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*

%changelog
* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.3-alt1
- 0.9.3
- build python3 package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt2
- fix permitions inside egg-info dir

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- Initial package.
