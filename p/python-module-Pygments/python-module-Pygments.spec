%define oname Pygments

%def_with python3

Name: python-module-Pygments
Version: 2.0.2
Release: alt1.1

Summary: Pygments is a syntax highlighting package written in Python

License: BSD
Group: Development/Python
Url: http://pygments.org/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Source: http://pypi.python.org/packages/source/P/%oname/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# manually removed: pybliographic python-module-Rabbyt python-module-pybliographer
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-peak python-module-pyasn1 python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base xz
BuildRequires: python-module-Pyrex python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

#BuildPreReq: python-module-RuleDispatch python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%description
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

%if_with python3
%package -n python3-module-%oname
Summary: Pygments is a syntax highlighting package written in Python 3
Group: Development/Python

%description -n python3-module-%oname
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

%package -n python3-module-%oname-tests
Summary: Tests for %name
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains tests for %name.
%endif

%package tests
Summary: Tests for %name
Group: Development/Python
Requires: %name = %version-%release
AutoReq: yes, nopython

%description tests
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains tests for %name.

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains documentation for %name.

%package pickles
Summary: Pickles for %name
Group: Development/Python
BuildArch: noarch

%description pickles
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

This package contains pickles for %name.

%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%make -C doc pickle
%make -C doc html

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/pygmentize %buildroot%_bindir/pygmentize3
%endif
%python_install

install -d %buildroot%_man1dir
install -d %buildroot%_docdir/%name
	
install -p -m644 AUTHORS CHANGES LICENSE TODO \
	%buildroot%_docdir/%name/
cp -fR doc/_build/html %buildroot%_docdir/%name/

install -p -m644 doc/pygmentize.1 %buildroot%_man1dir
cp -fR tests %buildroot%python_sitelibdir/pygments/
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/pygments/

%files
%doc %dir %_docdir/%name
%doc %_docdir/%name/*
%exclude %_docdir/%name/html
%_bindir/pygmentize
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/pickle
%_man1dir/*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%files doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/html

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%_bindir/pygmentize3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.0.2-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-3.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- VErsion 1.6

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Moved %_bindir/pygmentize for Python 3 into python3-module-%oname

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Version 1.5
- Added module for Python 3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3
- Enabled docs

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Rebuilt with python-module-sphinx-devel

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Tue Mar 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Rebuilt with updated macro %%prepare_sphinx

* Wed Feb 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added pickles package

* Tue Feb 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added documentation and tests

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt with python 2.6

* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0 (with rpmrb script)

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus
