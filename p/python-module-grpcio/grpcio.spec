%define _unpackaged_files_terminate_build 1

%define oname grpcio

%def_with python3

Name: python-module-%oname
Version: 1.19.0
Release: alt1
Summary: HTTP/2-based RPC framework
License: Apache 2.0
Group: Development/Python
Url: https://pypi.org/project/grpcio

Source: %oname-%version.tar

BuildRequires: gcc-c++ zlib-devel libcares-devel
BuildRequires: libssl-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(Cython) python2.7(six)
BuildRequires: python2.7(enum34) python-module-futures
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(Cython) python3(six)
%endif

%description
HTTP/2-based RPC framework.

%if_with python3
%package -n python3-module-%oname
Summary: HTTP/2-based RPC framework
Group: Development/Python3

%description -n python3-module-%oname
HTTP/2-based RPC framework.
%endif

%prep
%setup -n %oname-%version

# remove some bundled libraries. TODO: try unbundling all libraries.
rm -rf third_party/zlib
rm -rf third_party/cares
rm -rf third_party/boringssl

%if_with python3
cp -a . ../python3
%endif

%build
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1

python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19.0-alt1
- Updated to upstream version 1.19.0.

* Wed May 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1
- Initial build for ALT.
