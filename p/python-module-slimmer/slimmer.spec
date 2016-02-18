%define oname slimmer

%def_with python3

Name: python-module-%oname
Version: 0.1.31
Release: alt1.git20120510.1
Summary: HTML,XHTML,CSS,JavaScript optimizer
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/slimmer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/peterbe/slimmer.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-CommandLineApp
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires CommandLineApp

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

%description
slimmer.py is a whitespace optimizer for CSS, HTML and XHTML output.
It's written by Peter Bengtsson, peter@fry-it.com in 2004-2005. Still
maintained in 2008.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
slimmer.py is a whitespace optimizer for CSS, HTML and XHTML output.
It's written by Peter Bengtsson, peter@fry-it.com in 2004-2005. Still
maintained in 2008.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: HTML,XHTML,CSS,JavaScript optimizer
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip commandlineapp

%description -n python3-module-%oname
slimmer.py is a whitespace optimizer for CSS, HTML and XHTML output.
It's written by Peter Bengtsson, peter@fry-it.com in 2004-2005. Still
maintained in 2008.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
slimmer.py is a whitespace optimizer for CSS, HTML and XHTML output.
It's written by Peter Bengtsson, peter@fry-it.com in 2004-2005. Still
maintained in 2008.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' '{}' +
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
install -p -m644 %oname/tests/*.html \
	%buildroot%python_sitelibdir/%oname/tests/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 %oname/tests/*.html \
	%buildroot%python3_sitelibdir/%oname/tests/
popd
%endif

%check
export PYTHONPATH=$PWD
python setup.py test
pushd %oname/tests
python testSlimmer.py --verbose
popd
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test-3.3 -vv %oname/tests/testSlimmer.py
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.31-alt1.git20120510.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.31-alt1.git20120510
- Initial build for Sisyphus

