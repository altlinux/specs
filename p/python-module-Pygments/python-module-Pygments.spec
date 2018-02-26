%define oname Pygments

%def_with python3

Name: python-module-Pygments
Version: 1.5
Release: alt2

Summary: Pygments is a syntax highlighting package written in Python

License: BSD
Group: Development/Python
Url: http://pygments.org/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Source: http://pypi.python.org/packages/source/P/%oname/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# manually removed: pybliographic python-module-Rabbyt python-module-pybliographer
# Automatically added by buildreq on Sat Jan 05 2008
BuildRequires: python-module-MySQLdb python-module-Pyrex python-module-lxml
BuildPreReq: python-module-RuleDispatch python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
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
%setup -q -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .

%build
%python_build

%generate_pickles $PWD $PWD/docs/build pygments

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
install -d %buildroot%_docdir/%name/html
	
install -p -m644 AUTHORS CHANGES LICENSE TODO \
	%buildroot%_docdir/%name
install -p -m644 docs/build/* %buildroot%_docdir/%name/html

install -p -m644 docs/pygmentize.1 %buildroot%_man1dir
cp -fR tests %buildroot%python_sitelibdir/pygments/
cp -fR pickle %buildroot%python_sitelibdir/pygments/

%files
%doc %dir %_docdir/%name
%doc %_docdir/%name/*
%exclude %_docdir/%name/html
%_bindir/pygmentize
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle
%_man1dir/*

%files tests
%python_sitelibdir/*/tests

%files doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/html

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%_bindir/pygmentize3
%python3_sitelibdir/*
%endif

%changelog
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
