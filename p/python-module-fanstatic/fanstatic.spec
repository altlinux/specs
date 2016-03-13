%define oname fanstatic

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt2.a5.1.1
Summary: Flexible static resources for web applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/fanstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%py_requires shutilwhich

%description
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

%if_with python3
%package -n python3-module-%oname
Summary: Flexible static resources for web applications (Python 3)
Group: Development/Python3
%py3_requires shutilwhich

%description -n python3-module-%oname
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

%package -n python3-module-%oname-tests
Summary: Tests for fanstatic (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains tests for fanstatic.
%endif

%package tests
Summary: Tests for fanstatic
Group: Development/Python
Requires: %name = %version-%release

%description tests
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains tests for fanstatic.

%package docs
Summary: Documentation for fanstatic
Group: Development/Documentation

%description docs
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains documentation for fanstatic.

%package pickles
Summary: Pickles for fanstatic
Group: Development/Python

%description pickles
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains pickles for fanstatic.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
export LC_ALL=en_US.UTF-8

%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
pushd ../python3
%python3_install
popd
%endif
mv %buildroot%_bindir/fanstatic-compile \
	%buildroot%_bindir/fanstatic-compile3

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc html
%make -C doc pickle

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/fanstatic/

%files
%doc *.txt
%_bindir/fanstatic-compile
%python_sitelibdir/*
#exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

#files tests
#python_sitelibdir/*/test*

%files docs
%doc doc/_build/html/*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/fanstatic-compile3
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/test*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.a5.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt2.a5.1
- NMU: Use buildreq for BR.

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.a5
- Added necessary requirements

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a5
- Version 1.0a5

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a4
- Version 1.0a4

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a3
- Version 1.0a3

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.16-alt1.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1
- Version 0.16
- Added docs and pickles

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.4-alt1
- Version 0.11.4
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3-alt1
- Version 0.11.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.2-alt1.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1
- Initial build for Sisyphus

