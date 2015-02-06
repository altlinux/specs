%define mname tw2.jqplugins
%define oname %mname.ui

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.2.0
Release: alt1.git20130827
Summary: toscawidgets2 wrapper for jquery-ui
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.ui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jqplugins.ui.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-tw2.core-tests python-module-tw2.forms
BuildPreReq: python-module-tw2.jquery python-module-six
BuildPreReq: python-module-nose python-module-webtest
BuildPreReq: python-module-sieve python-module-FormEncode
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.forms
BuildPreReq: python3-module-tw2.jquery python3-module-six
BuildPreReq: python3-module-nose python3-module-webtest
BuildPreReq: python3-module-sieve
%endif

%py_provides %oname
%py_requires %mname genshi mako tw2.core tw2.forms tw2.jquery six

%description
tw2.jqplugins.ui is a toscawidgets2 (tw2) wrapper for jQuery UI.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for jquery-ui
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname genshi mako tw2.core tw2.forms tw2.jquery six

%description -n python3-module-%oname
tw2.jqplugins.ui is a toscawidgets2 (tw2) wrapper for jQuery UI.

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
%python_sitelibdir/tw2/jqplugins/ui
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/jqplugins/ui
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20130827
- Initial build for Sisyphus

