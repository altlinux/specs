%define oname ujson

%def_with python3

Name: python-module-%oname
Version: 1.34
Release: alt1.git20140416
Summary: Ultra fast JSON encoder and decoder for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ujson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/esnme/ultrajson.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 2.5+ and 3.

%package -n python3-module-%oname
Summary: Ultra fast JSON encoder and decoder for Pytho
Group: Development/Python3

%description -n python3-module-%oname
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 2.5+ and 3.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%install
%add_optflags -fno-strict-aliasing
%python_build_install

%if_with python3
pushd ../python3
%python3_build_install
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
* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.34-alt1.git20140416
- Initial build for Sisyphus

