%define _unpackaged_files_terminate_build 1

%define oname grpcio-tools

Name: python3-module-%oname
Version: 1.26.0
Release: alt1
Summary: HTTP/2-based RPC framework
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/grpcio-tools

Source: %oname-%version.tar
Patch1: %oname-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libprotobuf-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(Cython) python3-module-protobuf

%description
HTTP/2-based RPC framework.

%prep
%setup -n %oname-%version
%patch1 -p1

# remove bundled libraries
rm -rf third_party/protobuf

%build
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
%python3_build_debug

%install
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
%python3_install

%check
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
python3 setup.py test

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.26.0-alt1
- Updated to upstream version 1.26.0.

* Tue Aug 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.22.0-alt1
- Updated to upstream version 1.22.0 (Closes: #37081).
- Disabled build for python-2.

* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19.0-alt1
- Updated to upstream version 1.19.0.

* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1
- Initial build for ALT.
