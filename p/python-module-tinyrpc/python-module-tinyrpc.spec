%def_without python3

%define oname tinyrpc

Name: python-module-%oname
Version: 0.5
Release: alt2.1
Summary: Modular RPC library
Group: Development/Python
License: MIT
Url: http://github.com/mbr/tinyrpc
Source: %oname-%version.tar.gz
BuildArch: noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

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
# Remove bundled egg-info
rm -rf %oname.egg-info

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

%files
%doc README.rst
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt2
- fix permitions inside egg-info dir

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- Initial package.
