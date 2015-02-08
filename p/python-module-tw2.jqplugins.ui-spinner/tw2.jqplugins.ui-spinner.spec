%define mname tw2.jqplugins
%define oname %mname.ui-spinner

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20131119
Summary: toscawidgets2 widget for TextField with spinner
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jqplugins.ui-spinner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RobertSudwarts/tw2.jqplugins.ui-spinner.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-tw2.core python-module-tw2.jquery
BuildPreReq: python-module-tw2.jqplugins.ui python-module-BeautifulSoup
BuildPreReq: python-module-nose python-module-FormEncode
BuildPreReq: python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-tw2.core python3-module-tw2.jquery
BuildPreReq: python3-module-tw2.jqplugins.ui python3-module-BeautifulSoup
BuildPreReq: python3-module-nose python3-module-FormEncode
BuildPreReq: python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %mname.ui_spinner
%py_requires %mname genshi mako tw2.core tw2.jquery tw2.jqplugins.ui
%add_findreq_skiplist %python_sitelibdir/tw2/jqplugins/ui_spinner/samples.py

%description
toscawidgets2 widget for TextField with spinner.

%package -n python3-module-%oname
Summary: toscawidgets2 widget for TextField with spinner
Group: Development/Python3
%py3_provides %mname.ui_spinner
%py3_requires %mname genshi mako tw2.core tw2.jquery tw2.jqplugins.ui
%add_findreq_skiplist %python3_sitelibdir/tw2/jqplugins/ui_spinner/samples.py

%description -n python3-module-%oname
toscawidgets2 widget for TextField with spinner.

%prep
%setup

%if_with python3
cp -fR . ../python3
for i in $(find ../python3/tw2 -type f -name '*.py'); do
	2to3 -w -n $i ||:
done
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
install -d %buildroot%python_sitelibdir
cp -fR tw2 *.egg-info %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir
cp -fR tw2 *.egg-info %buildroot%python3_sitelibdir/
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
%doc *.rst
%python_sitelibdir/tw2/jqplugins/ui_spinner
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/jqplugins/ui_spinner
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Feb 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20131119
- Initial build for Sisyphus

