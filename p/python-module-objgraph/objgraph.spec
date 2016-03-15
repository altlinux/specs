%define oname objgraph

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.1
Summary: Draws Python object reference graphs with graphviz
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/objgraph/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
objgraph is a module that lets you visually explore Python object
graphs.

You'll need graphviz if you want to draw the pretty graphs.

I recommend xdot for interactive use. pip install xdot should suffice;
objgraph will automatically look for it in your PATH.

%package -n python3-module-%oname
Summary: Draws Python object reference graphs with graphviz
Group: Development/Python3

%description -n python3-module-%oname
objgraph is a module that lets you visually explore Python object
graphs.

You'll need graphviz if you want to draw the pretty graphs.

I recommend xdot for interactive use. pip install xdot should suffice;
objgraph will automatically look for it in your PATH.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%doc *.rst docs
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Version 1.7.2

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1
- Version 1.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus

