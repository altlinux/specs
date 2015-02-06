%define mname tw2
%define oname %mname.dynforms

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20130829
Summary: Dynamic widgets with JavaScript for ToscaWidgets 2
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.dynforms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.dynforms.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.forms
BuildPreReq: python-module-genshi python-module-nose
BuildPreReq: python-module-FormEncode python-module-BeautifulSoup
BuildPreReq: python-module-strainer python-module-webtest
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.forms
BuildPreReq: python3-module-genshi python3-module-nose
BuildPreReq: python3-module-FormEncode python3-module-BeautifulSoup
BuildPreReq: python3-module-strainer python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.forms genshi

%description
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

tw2.dynforms includes dynamic form building widgets that use JavaScript.

%package -n python3-module-%oname
Summary: Dynamic widgets with JavaScript for ToscaWidgets 2
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.forms genshi

%description -n python3-module-%oname
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

tw2.dynforms includes dynamic form building widgets that use JavaScript.

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
%doc *.rst docs/*.rst examples
%python_sitelibdir/%mname/dynforms
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst examples
%python3_sitelibdir/%mname/dynforms
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20130829
- Initial build for Sisyphus

