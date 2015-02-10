%define mname tw2
%define oname %mname.wysihtml5

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20130924
Summary: WYSIHTML5 widget for ToscaWidgets2
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.wysihtml5/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.wysihtml5.git
# branch: master
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.forms
BuildPreReq: python-module-mako python-module-tw2.bootstrap.forms
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.forms
BuildPreReq: python3-module-mako python3-module-tw2.bootstrap.forms
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.forms mako tw2.bootstrap.forms

%description
WYSIHTML5 widget for ToscaWidgets2.

WYSIHTML5 is a lightweight HTML5 rich text editing plugin developed by
xing.

%package -n python3-module-%oname
Summary: WYSIHTML5 widget for ToscaWidgets2
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.forms mako tw2.bootstrap.forms

%description -n python3-module-%oname
WYSIHTML5 widget for ToscaWidgets2.

WYSIHTML5 is a lightweight HTML5 rich text editing plugin developed by
xing.

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
%doc *.md docs/*.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20130924
- Initial build for Sisyphus

