%define oname zc.customdoctests

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.dev0.git20140409
Summary: Leverage doctest / manuel hooks to support other languages, such as JavaScript
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.customdoctests/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zc.customdoctests.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-spidermonkey
BuildPreReq: python-module-manuel-tests python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests
BuildPreReq: python3-module-manuel-tests python3-module-zope.testing
%endif

%py_provides %oname
%py_requires zc manuel.testing zope.testing

%description
doctest (and recently manuel) provide hooks for using custom doctest
parsers. zc.customdoctests helps to leverage this to support other
languages, such as JavaScript.

%package -n python3-module-%oname
Summary: Leverage doctest / manuel hooks to support other languages, such as JavaScript
Group: Development/Python3
%py3_provides %oname
%py3_requires zc manuel.testing zope.testing

%description -n python3-module-%oname
doctest (and recently manuel) provide hooks for using custom doctest
parsers. zc.customdoctests helps to leverage this to support other
languages, such as JavaScript.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20140409
- Initial build for Sisyphus

