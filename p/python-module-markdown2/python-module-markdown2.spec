%define modulename markdown2

%def_with python3

Name: python-module-%modulename
Version: 1.4.3
Release: alt1.git20120427

Summary: Another implementation of Markdown in Python
Group: Development/Python
License: %gpl2plus | %bsd
Url: http://code.google.com/p/python-markdown2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/trentm/python-markdown2.git
Source: %modulename-%version.zip

BuildArch: noarch
BuildPreReq: rpm-build-licenses unzip

# Automatically added by buildreq on Sun Feb 17 2008
BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
This project provides a converter written in Python that closely matches
the behaviour of the original Perl-implemented Markdown.pl. There is
another Python markdown.py, but markdown2.py is faster and, to my
knowledge, more correct.

%if_with python3
%package -n python3-module-%modulename
Summary: Another implementation of Markdown in Python 3
Group: Development/Python3

%description -n python3-module-%modulename
This project provides a converter written in Python that closely matches
the behaviour of the original Perl-implemented Markdown.pl. There is
another Python markdown.py, but markdown2.py is faster and, to my
knowledge, more correct.
%endif

%package tests
Summary: Tests for markdown2
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description tests
This project provides a converter written in Python that closely matches
the behaviour of the original Perl-implemented Markdown.pl. There is
another Python markdown.py, but markdown2.py is faster and, to my
knowledge, more correct.

This package contains tests for markdown2.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
sed -i 's|%_bindir/env python|%_bindir/env python3|' lib/markdown2.py
%python3_build
popd
%endif

%install

%if_with python3
pushd ../python3
%python3_install
popd
%endif
mv %buildroot%_bindir/markdown2 %buildroot%_bindir/py3_markdown2
rm -f %buildroot%python3_sitelibdir/*.pyo

%python_install --optimize=2
rm -f %buildroot%python_sitelibdir/*.pyo

%files
%doc *.txt
%_bindir/markdown2
%python_sitelibdir/*

%files tests
%doc test/*

%if_with python3
%files -n python3-module-%modulename
%doc *.txt
%_bindir/py3_markdown2
%python3_sitelibdir/*
%endif

%changelog
* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20120427
- Version 1.4.3
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1.19-alt1.git20110718
- Version 1.0.1.19

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1.17-alt1.1
- Rebuild with Python-2.7

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1.17-alt1
- Initial build for Sisyphus

