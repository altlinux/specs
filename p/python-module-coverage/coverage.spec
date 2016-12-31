%define oname coverage

%def_with python3

Name: python-module-%oname
Version: 4.0
Release: alt1.a7.git20150730.1.2
Summary: A tool for measuring code coverage of Python programs
License: BSD
Group: Development/Python
Url: http://nedbatchelder.com/code/coverage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://bitbucket.org/ned/coveragepy
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-sphinx python-module-Pygments
#BuildPreReq: python-module-enchant libenchant
#BuildPreReq: python-module-sphinxcontrib-napoleon
#BuildPreReq: python-module-sphinxcontrib-spelling

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: bzr elfutils python-base python-devel python-module-Paver python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-docutils python-module-enchant python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mimeparse python-module-pbr python-module-pyasn1 python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sphinxcontrib python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base
BuildRequires: libenchant python-module-alabaster python-module-html5lib python-module-sphinxcontrib-napoleon python-module-sphinxcontrib-spelling time

%if_with python3
BuildRequires: python3-devel python3-module-setuptools rpm-build-python3
%endif

%description
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

Coverage measurement is typically used to gauge the effectiveness of
tests. It can show which parts of your product code are being exercised
by tests, and which are not.

%package doc
Summary: Documentation for Coverage python module
Group: Development/Documentation
BuildArch: noarch

%description doc
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

This package contains documentation for Coverage.py.

%package pickles
Summary: Pickles for Coverage python module
Group: Development/Python

%description pickles
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

This package contains pickles for Coverage.py.

%if_with python3
%package -n python3-module-%oname
Summary: A tool for measuring code coverage of Python3 programs
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute

%description -n python3-module-%oname
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

Coverage measurement is typically used to gauge the effectiveness of
tests. It can show which parts of your product code are being exercised
by tests, and which are not.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

export PYTHONPATH=$PWD
%make_build dochtml
%make_build pickle

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
mv %buildroot%_bindir/coverage %buildroot%_bindir/coverage3
%endif

%python_install

install -d %buildroot%python_sitelibdir/%oname/lab
install -p -m644 lab/* %buildroot%python_sitelibdir/%oname/lab

install -d %buildroot%_docdir/%name
cp -fR doc/_build/html/* %buildroot%_docdir/%name/
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGES.txt README.txt TODO.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%_bindir/*
%exclude %_bindir/coverage3
%exclude %_bindir/coverage-%_python3_version

%files doc
%_docdir/%name

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%_bindir/coverage3
%_bindir/coverage-%_python3_version
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%oname
%endif

%changelog
* Sun Jan 01 2017 Michael Shigorin <mike@altlinux.org> 4.0-alt1.a7.git20150730.1.2
- BOOTSTRAP: made python3 knob actually work

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0-alt1.a7.git20150730.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0-alt1.a7.git20150730.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a7.git20150730
- Version 4.0a7

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a6.git20150216
- Version 4.0a6

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a0.hg20140719
- New snapshot

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a0.hg20140708
- Version 4.0a0

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1.hg20131027
- Version 3.7.1

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2.a1.hg20130915
- Version 3.6.1a1

* Sun Feb 17 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.a0.hg20130202
- Fix build with Python3-3.3.x

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.a0.hg20130202
- Version 3.6.1a0

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2.b1.hg20120329
- New snapshot
- Avoid requirement for %name on Python 3

* Wed Feb 08 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.b1.hg20111031
- Build with Python3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1.b1.hg20111031
- Version 3.5.2b1
- Added pickles subpackage

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5-alt1.a1.hg20110502.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20110502
- New snapshot

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20101120.1
- Rebuilt for debuginfo

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20101120
- Version 3.5a1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.a1.hg20100725
- Version 3.4a1

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0b1-alt1.hg20090922.1
- Rebuilt with python 2.6

* Wed Sep 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0b1-alt1.hg20090922
- Initial build for Sisyphus

