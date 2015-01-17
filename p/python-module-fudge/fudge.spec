%define oname fudge

%def_without python3

Name: python-module-%oname
Version: 1.0.3
Release: alt2
Summary: Replace real objects with fakes (mocks, stubs, etc) while testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/fudge/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires nose

%description
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Replace real objects with fakes (mocks, stubs, etc) while testing
Group: Development/Python3
%py3_provides %oname
%py3_requires nose

%description -n python3-module-%oname
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%check
python setup.py test
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt javascript
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt javascript
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2
- Applied repocop's python-module-fudge-1.0.3-alt1.diff

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus

