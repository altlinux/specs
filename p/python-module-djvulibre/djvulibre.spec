%define oname djvulibre

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Python support for the DjVu image format
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/python-djvulibre
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libdjvu-devel /usr/bin/latex graphviz
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-nose
BuildPreReq: python-module-sphinx-devel texlive-latex-recommended
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-nose
%endif

%py_provides %oname djvu

%description
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open source implementation of DjVu.

%if_with python3
%package -n python3-module-%oname
Summary: Python support for the DjVu image format
Group: Development/Python3
%py3_provides %oname djvu

%description -n python3-module-%oname
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open source implementation of DjVu.
%endif

%prep
%setup

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

python setup.py build_sphinx

%check
python setup.py test -v
export PYTHONPATH=$PWD
python setup.py build_ext -i
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
python3 setup.py build_ext -i
py.test-%_python3_version -vv
popd
%endif

%files
%doc examples build/sphinx/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc examples build/sphinx/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

