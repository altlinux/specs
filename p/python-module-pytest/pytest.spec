%define oname pytest

%def_with python3

Name: python-module-%oname
Version: 2.2.4.dev2
Release: alt1.hg20120331
Summary: Simple and popular testing tool for Python
License: MIT
Group: Development/Python
Url: http://pytest.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# hg clone https://bitbucket.org/hpk42/pytest
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

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

%prepare_sphinx .
ln -s ../objects.inv doc/

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
pushd doc
%make html
%make pickle
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

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
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%_bindir/py.test-%_python3_version
%python3_sitelibdir/*
%endif

%changelog
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

