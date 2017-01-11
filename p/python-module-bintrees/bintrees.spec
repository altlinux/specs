%define oname bintrees

%def_with python3

Name: python-module-%oname
Version: 2.0.4
Release: alt1
Summary: Package provides Binary-, RedBlack- and AVL-Trees in Python and Cython
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bintrees/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/7b/77/7e13390e242c72a460cdf4a4f878d3605d7490cea156e5991156458d2ffb/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname

%description
This package provides Binary- RedBlack- and AVL-Trees written in Python
and Cython/C.

This Classes are much slower than the built-in dict class, but all
iterators/generators yielding data in sorted key order. Trees can be
uses as drop in replacement for dicts in most cases.

%package -n python3-module-%oname
Summary: Package provides Binary-, RedBlack- and AVL-Trees in Python and Cython
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package provides Binary- RedBlack- and AVL-Trees written in Python
and Cython/C.

This Classes are much slower than the built-in dict class, but all
iterators/generators yielding data in sorted key order. Trees can be
uses as drop in replacement for dicts in most cases.

%prep
%setup -q -n %{oname}-%{version}

rm -f %oname/cython_trees.c

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

%check
python setup.py test
python setup.py build_ext -i
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
python3 setup.py build_ext -i
py.test-%_python3_version -vv
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus

