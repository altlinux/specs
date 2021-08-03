%define oname Pygments

Name: python-module-Pygments
Version: 2.4.2
Release: alt4

Summary: Pygments is a syntax highlighting package written in Python

License: BSD
Group: Development/Python
Url: http://pygments.org/

BuildArch: noarch

Source: %name-%version.tar
Source1: autobuild.watch

%description
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

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
%setup

%build
%python_build

%install
%python_install

cp -fR tests %buildroot%python_sitelibdir/pygments/

%files
%_bindir/pygmentize
%python_sitelibdir/*
%exclude %python_sitelibdir/pygments/tests

%files tests
%python_sitelibdir/pygments/tests

%changelog
* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.4.2-alt4
- Built without docs.

* Wed May 06 2020 Stanislav Levin <slev@altlinux.org> 2.4.2-alt3
- Moved Python3 subpackage to its own package.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.4.2-alt2
- Fixed build requires.

* Sat Jun 29 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- rebuild with python3.6

* Tue Jun 06 2017 Fr. Br. George <george@altlinux.ru> 2.2.0-alt1
- Autobuild version bump to 2.2.0
- Move "testing" lexer back to main package
- Introduce Python3 doc and pickle

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

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
