%define oname yapps2

%def_with python3

Name: python-module-%oname
Version: 2.1.1
Release: alt3
Summary: Yet Another Python Parser System

Group: Development/Python
License: MIT
URL: http://theory.stanford.edu/~amitp/yapps/
Source: %name-%version.tar
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Patch0: 0001-fix-indexdation-t.patch
Patch1: 0002-Bring-closer-to-Python-3-keep-Pytho2-compatibile.patch
Patch2: 0003-bring-closer-to-Python-3-support-compatible-with-new.patch
Patch3: 0004-full-Python3-port-no-backward-compatibile.patch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%py_provides yapps

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

%if_with python3
%package -n python3-module-%oname
Summary: Yet Another Python 3 Parser System
Group: Development/Python3
%py3_provides yapps

%description -n python3-module-%oname
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
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
popd
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%doc changelog doc/*.html examples test
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc changelog doc/*.html examples test
%python3_sitelibdir/*
%endif

%changelog
* Sat Jun 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt3
- Applied repocop patch

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt2
- Added module for Python 3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus

