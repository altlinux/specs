%define modulename markdown2

%def_disable check

Name: python3-module-%modulename
Version: 2.3.1
Release: alt2

Summary: Another implementation of Markdown in Python
License: %gpl2plus | %bsd
Group: Development/Python3
Url: http://code.google.com/p/python-markdown2/
BuildArch: noarch

# https://github.com/trentm/python-markdown2.git
Source: %modulename-%version.zip

BuildRequires(pre): rpm-build-python3 rpm-build-licenses
BuildRequires: unzip python3-module-pytest

%py3_provides %modulename
%py3_requires logging pygments


%description
This project provides a converter written in Python that closely matches
the behaviour of the original Perl-implemented Markdown.pl. There is
another Python markdown.py, but markdown2.py is faster and, to my
knowledge, more correct.

%package tests
Summary: Tests for markdown2
Group: Development/Python3
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

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install
rm -f %buildroot%python3_sitelibdir/*.pyo

%check
%__python3 setup.py test
export PYTHONPATH=$PWD/lib
py.test-%_python3_version -vv

%files
%doc *.txt
%_bindir/markdown2
%python3_sitelibdir/*

%files tests
%doc test/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.1-alt1.git20141222.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.git20141222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.3.1-alt1.git20141222.1
- NMU: Use buildreq for BR.

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.git20141222
- Version 2.3.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.git20140306
- Version 2.2.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20131127
- Version 2.1.1

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.0-alt1
- Version 2.1.0

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20120427
- Version 1.4.3
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1.19-alt1.git20110718
- Version 1.0.1.19

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1.17-alt1.1
- Rebuild with Python-2.7

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1.17-alt1
- Initial build for Sisyphus

