%define mname tw2
%define oname %mname.jquery

%def_with python3

Name: python-module-%oname
Version: 2.2.0.2
Release: alt1.git20130829
Summary: toscawidgets2 wrapper for jQuery
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jquery.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core python-module-tw2.forms
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-FormEncode
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core python3-module-tw2.forms
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname %mname.jqplugins
%py_requires %mname tw2.core tw2.forms genshi mako

%description
tw2.jquery is a ToscaWidgets2 (tw2) wrapper for jquery.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for jQuery
Group: Development/Python3
%py3_provides %oname %mname.jqplugins
%py3_requires %mname tw2.core tw2.forms genshi mako

%description -n python3-module-%oname
tw2.jquery is a ToscaWidgets2 (tw2) wrapper for jquery.

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

install -d %buildroot%python_sitelibdir/%mname/jqplugins
install -p -m644 %mname/jqplugins/__init__.py \
	%buildroot%python_sitelibdir/%mname/jqplugins/
%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir/%mname/jqplugins
install -p -m644 %mname/jqplugins/__init__.py \
	%buildroot%python3_sitelibdir/%mname/jqplugins/
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
%python_sitelibdir/%mname/jquery
%python_sitelibdir/%mname/jqplugins
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/jquery
%python3_sitelibdir/%mname/jqplugins
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0.2-alt1.git20130829
- Initial build for Sisyphus

