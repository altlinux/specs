%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname grpcio

Name: python3-module-%oname
Version: 1.64.0
Release: alt1
Summary: HTTP/2-based RPC framework
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/grpcio

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ zlib-devel libcares-devel
BuildRequires: libssl-devel
BuildRequires: libre2-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(Cython) python3(six) python3(wheel)

%description
HTTP/2-based RPC framework.

%prep
%setup -n %oname-%version
%ifarch %e2k
# EDG frontend fails at this
sed -i "/static_assert(value.empty()/{N;d}" third_party/abseil-cpp/absl/strings/internal/string_constant.h
%endif

# remove some bundled libraries. TODO: try unbundling all libraries.
rm -rf third_party/zlib
rm -rf third_party/cares
rm -rf third_party/boringssl
rm -rf third_party/re2

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%add_optflags -Wno-return-type

export GRPC_PYTHON_CFLAGS="%optflags"
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1
export GRPC_PYTHON_BUILD_SYSTEM_RE2=1

%pyproject_build

%install
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1
export GRPC_PYTHON_BUILD_SYSTEM_RE2=1

%pyproject_install

%check
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1
export GRPC_PYTHON_BUILD_SYSTEM_RE2=1

python3 setup.py test

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Wed May 22 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.64.0-alt1
- Updated to upstream version 1.64.0.

* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 1.60.0-alt1
- Updated to upstream version 1.60.0.

* Sat Jan 28 2023 Grigory Ustinov <grenka@altlinux.org> 1.51.1-alt1
- Updated to upstream version 1.51.1.

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.43.0-alt1
- Updated to upstream version 1.43.0.

* Thu Nov 18 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.39.0-alt2
- Fixed build for Elbrus.

* Fri Aug 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.39.0-alt1
- Updated to upstream version 1.39.0.

* Thu Mar 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.36.1-alt1
- Updated to upstream version 1.36.1.

* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.26.0-alt1
- Updated to upstream version 1.26.0 (Closes: #37909)

* Tue Aug 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.22.0-alt1
- Updated to upstream version 1.22.0.
- Disabled build for python-2.

* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19.0-alt1
- Updated to upstream version 1.19.0.

* Wed May 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1
- Initial build for ALT.
