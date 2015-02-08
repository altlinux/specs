%define mname tw2.jqplugins
%define oname %mname.fullcalendar

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20120727
Summary: toscawidgets2 wrapper for the FullCalendar jQuery plugin
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.fullcalendar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jqplugins.fullcalendar.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-tw2.core-tests python-module-tw2.jquery
BuildPreReq: python-module-tw2.jqplugins.ui python-module-BeautifulSoup
BuildPreReq: python-module-nose python-module-FormEncode
BuildPreReq: python-module-webtest
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.jquery
BuildPreReq: python3-module-tw2.jqplugins.ui python3-module-BeautifulSoup
BuildPreReq: python3-module-nose python3-module-FormEncode
BuildPreReq: python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname genshi mako tw2.core tw2.jquery tw2.jqplugins.ui

%description
A toscawidgets2 wrapper for the FullCalendar jquery plugin library.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for the FullCalendar jQuery plugin
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname genshi mako tw2.core tw2.jquery tw2.jqplugins.ui

%description -n python3-module-%oname
A toscawidgets2 wrapper for the FullCalendar jquery plugin library.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/tw2/jqplugins/fullcalendar
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/jqplugins/fullcalendar
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Feb 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20120727
- Initial build for Sisyphus

