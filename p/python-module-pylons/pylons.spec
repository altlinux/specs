%define oname pylons

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2.git20120813.1
Epoch: 1
Summary: Lightweight web framework emphasizing flexibility and rapid development
License: BSD
Group: Development/Python
Url: http://pylonshq.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: Pylons-%version.tar.gz
Source1: http://cdn.pylonshq.com/download/1.0/Pylons.pdf
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

%description
The Pylons web framework is aimed at making webapps and large
programmatic website development in Python easy. Several key points:

* A framework to make writing web applications in Python easy

* Utilizes a minimalist, component-based philosophy that makes it easy
  to expand on

* Harness existing knowledge about Python

%package -n python3-module-%oname
Summary: Lightweight web framework emphasizing flexibility and rapid development
Group: Development/Python3

%description -n python3-module-%oname
The Pylons web framework is aimed at making webapps and large
programmatic website development in Python easy. Several key points:

* A framework to make writing web applications in Python easy

* Utilizes a minimalist, component-based philosophy that makes it easy
  to expand on

* Harness existing knowledge about Python

%package -n python3-module-%oname-tests
Summary: Tests for Pylons
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The Pylons web framework is aimed at making webapps and large
programmatic website development in Python easy.

This package contains tests for Pylons.

%package pickles
Summary: Pickles for Pylons
Group: Development/Python

%description pickles
The Pylons web framework is aimed at making webapps and large
programmatic website development in Python easy.

This package contains pickles for Pylons.

%package tests
Summary: Tests for Pylons
Group: Development/Python
Requires: %name = %EVR

%description tests
The Pylons web framework is aimed at making webapps and large
programmatic website development in Python easy.

This package contains tests for Pylons.

%package doc
Summary: Documentation for Pylons
Group: Development/Documentation
BuildArch: noarch

%description doc
The Pylons web framework is aimed at making webapps and large
programmatic website development in Python easy.

This package contains documentation for Pylons.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

install -p -m644 %SOURCE1 .

#prepare_sphinx .

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

#export PYTHONPATH=$PWD
#pushd pylons/docs/en
#make_build html
#popd

#rm -f conf.py
#ln -s $PWD/pylons/docs/en/conf.py .
#generate_pickles $PWD pylons/docs/en %oname

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

#install -d %buildroot%_docdir/%name
#cp -fR pylons/docs/en/_build/html/* %buildroot%_docdir/%name/
#cp -fR pickle %buildroot%python_sitelibdir/%oname

%files
%doc CHANGELOG LICENSE README.txt UPGRADING
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/test_files

#files pickles
#dir %python_sitelibdir/%oname
#python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/test*
%python_sitelibdir/test_files

%files doc
%doc *.pdf

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG LICENSE README.txt UPGRADING
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/test_files

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/test*
%python3_sitelibdir/test_files
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.0.1-alt2.git20120813.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.1-alt2.git20120813
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.1-alt1.git20120813
- Version 1.0.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.git20110115.1
- Rebuild with Python-2.7

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20110115
- Version 1.2

* Wed Jul 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Pylons 1.0 Released

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20090814.4
- Extracted tests into separate packages
- Added pickles package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20090814.3
- Rebuilt with python 2.6

* Mon Nov 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20090814.2
- Fixed subpackages list for imports by external modules (ALT #22195)

* Mon Nov 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20090814.1
- Fixed imports (ALT #22195)

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20090814
- Initial build for Sisyphus

