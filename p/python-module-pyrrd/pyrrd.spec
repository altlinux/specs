%define oname pyrrd

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20120117.1.1
Summary: An Object-Oriented Python Interface for RRDTool
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyRRD/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/oubiwann/pyrrd.git
Source: %name-%version.tar
# fix from https://github.com/kommmy/pyrrd.git
Patch: pyrrd-0.1.1-fix.patch
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests rrd-utils
#BuildPreReq: python-module-docutils python-module-RRDtool
#BuildPreReq: python-modules-xml
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-docutils python3-module-RRDtool
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: rrd-utils
%py_requires xml rrdtool

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-RRDtool python-module-docutils python-module-html5lib python-module-setuptools-tests python3-module-RRDtool python3-module-html5lib python3-module-setuptools-tests python3-module-sphinx rpm-build-python3 time

%description
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An Object-Oriented Python Interface for RRDTool
Group: Development/Python3
%py3_provides %oname
Requires: rrd-utils
%py3_requires xml rrdtool

%description -n python3-module-%oname
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyRRD lets you use RRDTool from Python code that takes advantage of
standard object-oriented patterns. The makes the programmatic usage of
RRDTool much easier and reusable.

This package contains tests for %oname.

%prep
%setup
%patch -p1

%if_with python3
cp -fR . ../python3
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog README TODO docs/* examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README TODO docs/* examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20120117.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20120117.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20120117
- Initial build for Sisyphus

