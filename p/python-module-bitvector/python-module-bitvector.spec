%define oname bitvector
%def_without python3

Summary: A pure-Python memory-efficient packed representation for bit arrays
Name: python-module-%oname
Version: 3.4.4
Release: alt1
Url: https://engineering.purdue.edu/kak/dist/BitVector-3.4.4.html
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: Python Software Foundation License
Group: Development/Python

BuildArch: noarch
BuildRequires: python-devel python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
The BitVector.py module is for a memory-efficient packed
representation of bit vectors and for the processing of such
vectors.

%package -n python3-module-%oname
Summary: A pure-Python memory-efficient packed representation for bit arrays
Group: Development/Python3

%description -n python3-module-%oname
The BitVector.py module is for a memory-efficient packed
representation of bit vectors and for the processing of such
vectors.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif


%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_build_install --prefix=/usr

%if_with python3
pushd ../python3
%python3_install
popd
%endif



%files
%doc README
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif


%changelog
* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 3.4.4-alt1
- Initial build for ALT

