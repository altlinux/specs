%define _unpackaged_files_terminate_build 1

%define oname grpcio

Name: python3-module-%oname
Version: 1.26.0
Release: alt1
Summary: HTTP/2-based RPC framework
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/grpcio

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ zlib-devel libcares-devel
BuildRequires: libssl-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(Cython) python3(six)

%description
HTTP/2-based RPC framework.

%prep
%setup -n %oname-%version

# remove some bundled libraries. TODO: try unbundling all libraries.
rm -rf third_party/zlib
rm -rf third_party/cares
rm -rf third_party/boringssl

%build
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1

%python3_build_debug

%install
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1

%python3_install

%check
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1

python3 setup.py test

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.26.0-alt1
- Updated to upstream version 1.26.0 (Closes: #37909)

* Tue Aug 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.22.0-alt1
- Updated to upstream version 1.22.0.
- Disabled build for python-2.

* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19.0-alt1
- Updated to upstream version 1.19.0.

* Wed May 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1
- Initial build for ALT.
