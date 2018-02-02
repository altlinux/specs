# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20140409.1.1.1.1
%define oname zc.customdoctests

%def_with python3

Name: python-module-%oname
Version: 1.0.2
#Release: alt1.dev0.git20140409.1.1
Summary: Leverage doctest / manuel hooks to support other languages, such as JavaScript
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.customdoctests/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zc.customdoctests.git
Source: %name-%version.tar

#BuildPreReq: python-module-setuptools
#BuildPreReq: python-module-spidermonkey
#BuildPreReq: python-module-manuel-tests python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-module-setuptools
#BuildPreReq: python3-module-manuel-tests python3-module-zope.testing
%endif

%py_provides %oname
%py_requires zc manuel.testing zope.testing

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-manuel python-module-pytest python-module-setuptools python-module-six python-module-zc python-module-zope.exceptions python-module-zope.interface python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools python3-module-zc python3-module-zope python3-module-zope.exceptions python3-module-zope.interface
BuildRequires: python-module-manuel-tests python-module-setuptools python-module-spidermonkey python3-module-manuel python3-module-setuptools python3-module-zope.testing rpm-build-python3

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

%if "%_libexecdir" != "%_libdir"
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.dev0.git20140409.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20140409.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20140409.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.dev0.git20140409.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20140409
- Initial build for Sisyphus

