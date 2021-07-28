%define oname yapps2

Name: python3-module-%oname
Version: 2.2.0
Release: alt2
Summary: Yet Another Python Parser System

Group: Development/Python3
License: MIT
URL: http://theory.stanford.edu/~amitp/yapps/
Source: %name-%version.tar
BuildArch: noarch

Patch0: 0001-fix-indexdation-t.patch
Patch1: 0002-Bring-closer-to-Python-3-keep-Pytho2-compatibile.patch
Patch2: 0003-bring-closer-to-Python-3-support-compatible-with-new.patch
Patch3: 0004-full-Python3-port-no-backward-compatibile.patch

BuildRequires(pre): rpm-build-python3

%py3_provides yapps

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
YAPPS is an easy to use parser generator that is written in Python and
generates Python code.  There are several parser generator systems
already available for Python, but this parser has different goals:
Yapps is simple, very easy to use, and produces human-readable parsers.

It is not the fastest or most powerful parser.  Yapps is designed to be
used when regular expressions are not enough and other parser systems
are too much: situations where you might otherwise write your own
recursive descent parser.

This package contains several upward-compatible enhancements to the
original YAPPS source:
- Handle stacked input ("include files")
- augmented ignore-able patterns (can parse multi-line C comments
  correctly)
- better error reporting
- read input incrementally

%prep
%setup
#patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p1

%build
%python3_build

%install
%python3_install

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%doc ChangeLog NOTES README.md doc/*.html doc/yapps_grammar.g examples test
%_bindir/*
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.1-alt3.1
- Rebuild with Python-3.3

* Sat Jun 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt3
- Applied repocop patch

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt2
- Added module for Python 3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus

