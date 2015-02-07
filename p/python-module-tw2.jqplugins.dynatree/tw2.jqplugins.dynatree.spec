%define mname tw2.jqplugins
%define oname %mname.dynatree

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.1
Release: alt1.git20121107
Summary: toscawidgets2 wrapper for the dynatree jQuery plugin
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.dynatree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jqplugins.dynatree.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-tw2.core python-module-tw2.jqplugins.ui
BuildPreReq: python-module-BeautifulSoup python-module-nose
BuildPreReq: python-module-FormEncode python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-tw2.core python3-module-tw2.jqplugins.ui
BuildPreReq: python3-module-BeautifulSoup python3-module-nose
BuildPreReq: python3-module-FormEncode python3-module-webtest
%endif

%py_provides %oname
%py_requires %mname genshi mako tw2.core tw2.jqplugins.ui

%description
tw2.jqplugins.dynatree is a toscawidgets2 (tw2) wrapper for dynatree.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for the dynatree jQuery plugin
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname genshi mako tw2.core tw2.jqplugins.ui

%description -n python3-module-%oname
tw2.jqplugins.dynatree is a toscawidgets2 (tw2) wrapper for dynatree.

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
%python_sitelibdir/tw2/jqplugins/dynatree
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/jqplugins/dynatree
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.git20121107
- Initial build for Sisyphus

