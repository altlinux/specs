%define modulename markdown2

%def_with python3
%def_disable check

Name: python-module-%modulename
Version: 2.3.1
Release: alt1.git20141222.1.1

Summary: Another implementation of Markdown in Python
Group: Development/Python
License: %gpl2plus | %bsd
Url: http://code.google.com/p/python-markdown2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/trentm/python-markdown2.git
Source: %modulename-%version.zip

BuildArch: noarch
#BuildPreReq: rpm-build-licenses unzip

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Pygments
#BuildPreReq: python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Pygments
%endif

%py_provides %modulename
%py_requires logging pygments

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel rpm-build-python3 unzip python3-module-pytest

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

%python_install
rm -f %buildroot%python_sitelibdir/*.pyo

export PYTHONPATH=$PWD/lib
for i in *.md; do
	fname=$(echo $i |sed 's|\.md||')
	%buildroot%_bindir/markdown2 $i >$fname.html
done

%check
export PYTHONPATH=$PWD/lib
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD/lib
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt *.html
%_bindir/markdown2
%python_sitelibdir/*

%files tests
%doc test/*

%if_with python3
%files -n python3-module-%modulename
%doc *.txt *.html
%_bindir/py3_markdown2
%python3_sitelibdir/*
%endif

%changelog
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

