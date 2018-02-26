%define oname pylons
Name: python-module-%oname
Version: 1.2
Release: alt1.git20110115.1
Summary: Lightweight web framework emphasizing flexibility and rapid development
License: BSD
Group: Development/Python
Url: http://pylonshq.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: Pylons-%version.tar.gz
Source1: http://cdn.pylonshq.com/download/1.0/Pylons.pdf
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx python-module-Pygments

%description
The Pylons web framework is aimed at making webapps and large
programmatic website development in Python easy. Several key points:

* A framework to make writing web applications in Python easy

* Utilizes a minimalist, component-based philosophy that makes it easy
  to expand on

* Harness existing knowledge about Python

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
Requires: %name = %version-%release

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
install -p -m644 %SOURCE1 .

#prepare_sphinx .

%build
%python_build

#export PYTHONPATH=$PWD
#pushd pylons/docs/en
#make_build html
#popd

#rm -f conf.py
#ln -s $PWD/pylons/docs/en/conf.py .
#generate_pickles $PWD pylons/docs/en %oname

%install
%python_install

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

#files pickles
#dir %python_sitelibdir/%oname
#python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/*/*/*/tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/test*

%files doc
%doc *.pdf

%changelog
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

