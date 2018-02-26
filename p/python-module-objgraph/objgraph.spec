%define oname objgraph
Name: python-module-%oname
Version: 1.7.1
Release: alt1
Summary: Draws Python object reference graphs with graphviz
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/objgraph/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
objgraph is a module that lets you visually explore Python object
graphs.

You'll need graphviz if you want to draw the pretty graphs.

I recommend xdot for interactive use. pip install xdot should suffice;
objgraph will automatically look for it in your PATH.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs
%python_sitelibdir/*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1
- Version 1.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus

