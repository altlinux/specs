%define _unpackaged_files_terminate_build 1

%define oname grpcio

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
BuildRequires: gcc-c++ zlib-devel libcares-devel
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
%patch1 -p1

# remove some bundled libraries. TODO: try unbundling all libraries.
rm -rf third_party/zlib
rm -rf third_party/cares

sed -i \
	-e '/third_party\/cares/d' \
	-e '/third_party\/zlib/d' \
	src/python/grpcio/grpc_core_dependencies.py

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
%doc README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1%ubt
- Initial build for ALT.
