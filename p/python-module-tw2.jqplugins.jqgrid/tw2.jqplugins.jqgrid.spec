%define mname tw2.jqplugins
%define oname %mname.jqgrid

%def_with python3

Name: python-module-%oname
Version: 2.2.0
Release: alt1.git20130827
Summary: toscawidgets2 wrapper for the jQuery grid plugin
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.jqgrid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jqplugins.jqgrid.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-tw2.core-tests python-module-tw2.jquery
BuildPreReq: python-module-tw2.jqplugins.ui python-module-tw2.sqla
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-sieve python-module-webtest
BuildPreReq: python-module-FormEncode python-module-zope.sqlalchemy
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.jquery
BuildPreReq: python3-module-tw2.jqplugins.ui
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-sieve python3-module-webtest
BuildPreReq: python3-module-zope.sqlalchemy python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname genshi mako tw2.core tw2.jquery tw2.sqla six

%description
tw2.jqplugins.jqgrid is a toscawidgets2 (tw2) wrapper for the jQuery
Grid Plugin.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for the jQuery grid plugin
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname genshi mako tw2.core tw2.jquery six

%description -n python3-module-%oname
tw2.jqplugins.jqgrid is a toscawidgets2 (tw2) wrapper for the jQuery
Grid Plugin.

%prep
%setup

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/tw2/jqplugins/jqgrid
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/jqplugins/jqgrid
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.git20130827
- Initial build for Sisyphus

