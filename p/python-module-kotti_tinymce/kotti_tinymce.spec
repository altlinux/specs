%define oname kotti_tinymce

%def_without python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1.dev.git20141130
Summary: TinyMCE plugins for Kotti
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_tinymce/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/kotti_tinymce.git
Source: %name-%version.tar
# git://github.com/dnouri/Products.TinyMCE.git
Source1: Products.TinyMCE.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%add_python_req_skip kotti

%description
TinyMCE plugins for Kotti.

%package -n python3-module-%oname
Summary: TinyMCE plugins for Kotti
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip kotti

%description -n python3-module-%oname
TinyMCE plugins for Kotti.

%prep
%setup

pushd %oname
tar -xf %SOURCE1
popd

%if_with python3
cp -fR . ../python3
%endif

%build
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
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.dev.git20141130
- Version 0.6.0-dev

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.a1.git20140513
- Initial build for Sisyphus

