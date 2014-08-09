%define oname igakit

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2.hg20130902
Summary: Toolkit for IsoGeometric Analysis (IGA)
License: BSD
Group: Development/Python
Url: https://petiga-igakit.readthedocs.org/en/latest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/dalcinl/igakit
Source: %name-%version.tar

BuildPreReq: python-devel libnumpy-devel gcc-fortran
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel
%endif

%description
igakit: Toolkit for IsoGeometric Analysis (IGA).

%package -n python3-module-%oname
Summary: Toolkit for IsoGeometric Analysis (IGA)
Group: Development/Python3

%description -n python3-module-%oname
igakit: Toolkit for IsoGeometric Analysis (IGA).

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags %optflags_shared
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.hg20130902
- Added module for Python 3

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.hg20130902
- Initial build for Sisyphus

