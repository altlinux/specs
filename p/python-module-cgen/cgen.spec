%define oname cgen

%def_with python3

Name: python-module-%oname
Version: 2013.1.2
Release: alt1.1
Summary: C/C++ source generation from an AST
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/cgen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif
%py_requires decorator

%description
C/C++ source generation from an AST.

%if_with python3
%package -n python3-module-%oname
Summary: C/C++ source generation from an AST (Python 3)
Group: Development/Python3
%py3_requires decorator

%description -n python3-module-%oname
C/C++ source generation from an AST.
%endif

%package pickles
Summary: Pickles for cgen
Group: Development/Python

%description pickles
C/C++ source generation from an AST.

This package contains pickles for cgen.

%package docs
Summary: Documentation for cgen
Group: Development/Documentation

%description docs
C/C++ source generation from an AST.

This package contains documentation for cgen.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source

%build
%python_build_debug
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build_debug
popd
%endif

%make -C doc pickle
%make -C doc html

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.1.2-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1
- Version 2013.1.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 2012.1-alt1.1
- Rebuild with Python-3.3

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt1
- Initial build for Sisyphus

