%define oname regex

%def_with python3

Name: python-module-%oname
Version: 2014.11.13
Release: alt1
Summary: Alternate regular expression module, to replace re
License: PSFL
Group: Development/Python
Url: http://pypi.python.org/pypi/regex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests python-test
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests python3-test
%endif

%description
This new regex implementation is intended eventually to replace Python's
current re module implementation.

%package -n python3-module-%oname
Summary: Alternate regular expression module, to replace re
Group: Development/Python3

%description -n python3-module-%oname
This new regex implementation is intended eventually to replace Python's
current re module implementation.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
export PYTHONPATH=%buildroot%python_sitelibdir
rm -fR build Python3
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
rm -fR build Python2
py.test-%_python3_version
popd
%endif

%files
%doc README docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/test*

%if_with python3
%files -n python3-module-%oname
%doc README docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test*
%exclude %python3_sitelibdir/__pycache__/test*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.11.13-alt1
- Version 2014.11.13

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.11.03-alt1
- Version 2014.11.03
- Enabled testing

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.10.24-alt1
- Version 2014.10.24

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.06.28-alt1
- Version 2014.06.28
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.10.26-alt1
- Version 2013-10-26

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.08.04-alt1
- Version 2013-08-04

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.03.11-alt1
- Version 2013-03-11

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.20111223-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20111223-alt1
- Version 0.1.20111223

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20111103-alt1
- Version 0.1.20111103

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.20110524-alt1.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20110524-alt1
- Initial build for Sisyphus

