%define mname tw2
%define oname %mname.etc

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.1.0
Release: alt1.git20121126
Summary: Random extra widgets for ToscaWidgets 2
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.etc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.etc.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-webtest
BuildPreReq: python-module-BeautifulSoup python-module-nose
BuildPreReq: python-module-FormEncode python-module-strainer
BuildPreReq: python-module-mako python-module-genshi
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-webtest
BuildPreReq: python3-module-BeautifulSoup python3-module-nose
BuildPreReq: python3-module-FormEncode python3-module-strainer
BuildPreReq: python3-module-mako python3-module-genshi
%endif

%py_provides %oname
%py_requires %mname tw2.core

%description
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

tw2.etc contains 'etcetera' widgets. random stuff you might want.

%package -n python3-module-%oname
Summary: Random extra widgets for ToscaWidgets 2
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core

%description -n python3-module-%oname
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

tw2.etc contains 'etcetera' widgets. random stuff you might want.

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
%doc *.rst
%python_sitelibdir/%mname/etc
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/etc
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20121126
- Initial build for Sisyphus

