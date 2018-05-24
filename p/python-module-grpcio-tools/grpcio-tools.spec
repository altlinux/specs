%define _unpackaged_files_terminate_build 1

%define oname grpcio-tools

%def_with python3

Name: python-module-%oname
Version: 1.12.0
Release: alt1%ubt
Summary: HTTP/2-based RPC framework
License: Apache 2.0
Group: Development/Python
Url: https://pypi.org/project/grpcio

Source: %oname-%version.tar
Patch1: %oname-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libprotobuf-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(Cython) python-module-protobuf
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(Cython) python3-module-protobuf
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
%patch1 -p1

# remove bundled libraries
rm -rf third_party/protobuf

%if_with python3
cp -a . ../python3
%endif

%build
export GRPC_PYTHON_BUILD_WITH_CYTHON=1

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export GRPC_PYTHON_BUILD_WITH_CYTHON=1

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
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
* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1%ubt
- Initial build for ALT.
