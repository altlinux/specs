%define mname tw2
%define oname %mname.codemirror

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20150105
Summary: ToscaWidgets2 widget for CodeMirror, a JavaScript-based source code editor
License: WTFPL-2
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.codemirror/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/moschlar/tw2.codemirror.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.forms
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.forms
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.forms

%description
tw2.codemirror is a widget library for the ToscaWidgets 2 framework,
which provides a JavaScript-based source code editor using the
CodeMirror JavaScript component.

%package -n python3-module-%oname
Summary: ToscaWidgets2 widget for CodeMirror, a JavaScript-based source code editor
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.forms

%description -n python3-module-%oname
tw2.codemirror is a widget library for the ToscaWidgets 2 framework,
which provides a JavaScript-based source code editor using the
CodeMirror JavaScript component.

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
%doc LICENSE *.rst
%python_sitelibdir/%mname/codemirror
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/%mname/codemirror
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150105
- Initial build for Sisyphus

