%define oname pytest

%def_with python3

Name: python-module-%oname
Version: 2.8.0
Release: alt1.dev4.git20150807.1
Summary: Simple and popular testing tool for Python
License: MIT
Group: Development/Python
Url: http://pytest.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# https://github.com/pytest-dev/pytest.git
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-py python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires py

%description
py.test is a command line tool to collect, run and report about
automated tests. It runs well on Linux, Windows and OSX and on Python
2.4 through to 3.1 versions. It is used in many projects, ranging from
running 10 thousands of tests to a few inlined tests on a command line
script. As of version 1.2 you can also generate a
no-dependency py.test-equivalent standalone script that you can
distribute along with your application.

%if_with python3
%package -n python3-module-%oname
Summary: Simple and popular testing tool for Python 3
Group: Development/Python3
%py3_requires py
%add_python3_req_skip compiler

%description -n python3-module-%oname
py.test is a command line tool to collect, run and report about
automated tests. It runs well on Linux, Windows and OSX and on Python
2.4 through to 3.1 versions. It is used in many projects, ranging from
running 10 thousands of tests to a few inlined tests on a command line
script. As of version 1.2 you can also generate a
no-dependency py.test-equivalent standalone script that you can
distribute along with your application.
%endif

%package docs
Summary: Documentation for py.test
Group: Development/Documentation

%description docs
py.test is a command line tool to collect, run and report about
automated tests. It runs well on Linux, Windows and OSX and on Python
2.4 through to 3.1 versions. It is used in many projects, ranging from
running 10 thousands of tests to a few inlined tests on a command line
script. As of version 1.2 you can also generate a
no-dependency py.test-equivalent standalone script that you can
distribute along with your application.

This package contains documentation for py.test.

%package pickles
Summary: Pickles for py.test
Group: Development/Python

%description pickles
py.test is a command line tool to collect, run and report about
automated tests. It runs well on Linux, Windows and OSX and on Python
2.4 through to 3.1 versions. It is used in many projects, ranging from
running 10 thousands of tests to a few inlined tests on a command line
script. As of version 1.2 you can also generate a
no-dependency py.test-equivalent standalone script that you can
distribute along with your application.

This package contains pickles for py.test.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/en/

%build
%python_build
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
rm -f %buildroot%_bindir/py.test
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc/en
%make html
%make pickle
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/en/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS CHANGELOG LICENSE *.txt
%_bindir/*
%exclude %_bindir/py.test-%_python3_version
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/en/_build/html/*

%if_with python3
%files -n python3-module-%oname
%_bindir/py.test-%_python3_version
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.0-alt1.dev4.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.dev4.git20150807
- New snapshot

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.dev4.git20150726
- Version 2.8.0.dev4

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.dev1.hg20141030
- Version 2.7.0.dev1

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt2.dev1.hg20141025
- New snapshot

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt2.dev1.hg20141009
- Added requirement on py

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.dev1.hg20141009
- Version 2.6.4.dev1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.dev1.hg20140109
- Version 2.5.2.dev1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.dev2.hg20131122
- Version 2.4.3.dev2

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.dev12.hg20130909
- Version 2.4.0.dev12

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.5.dev8-alt1.hg20130328
- Version 2.3.5.dev8

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.0.dev10-alt1.hg20120813.1
- Rebuild with Python-3.3

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0.dev10-alt1.hg20120813
- Version 2.3.0.dev10

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4.dev2-alt1.hg20120331
- Version 2.2.4.dev2
- Added module for Python 3

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2.dev6-alt1.hg20110120
- Version 2.2.2.dev6

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.hg20111119
- Fixed buildreq

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.hg20111119
- Version 2.2.0
- Disabled conflict with py

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt1.hg20110501.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.hg20110501
- Version 2.0.3

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120.2
- Rebuilt with python-module-sphinx-devel

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120.1
- Added explicit conflict with py

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120
- Initial build for Sisyphus

