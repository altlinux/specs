%define mname tw2
%define oname %mname.jit

%def_with python3

Name: python-module-%oname
Version: 2.0.5
Release: alt1.git20120525
Summary: toscawidgets2 wrapper for the javascript infovis toolkit(jit)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.jit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.jit.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.core-tests python-module-tw2.jquery
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-SQLAlchemy python-module-BeautifulSoup
BuildPreReq: python-module-nose python-module-zope.sqlalchemy
BuildPreReq: python-module-tw2.sqla
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.core-tests python3-module-tw2.jquery
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-SQLAlchemy python3-module-BeautifulSoup
BuildPreReq: python3-module-nose python3-module-zope.sqlalchemy
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname tw2.core tw2.jquery genshi mako tw2.sqla
%py_requires sqlalchemy BeautifulSoup

%description
tw2.jit is a toscawidgets2 (tw2) wrapper for thejit.

%package -n python3-module-%oname
Summary: toscawidgets2 wrapper for the javascript infovis toolkit(jit)
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname tw2.core tw2.jquery genshi mako
%py3_requires sqlalchemy BeautifulSoup

%description -n python3-module-%oname
tw2.jit is a toscawidgets2 (tw2) wrapper for thejit.

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
%doc *.rst doc/*
%python_sitelibdir/%mname/jit
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/*
%python3_sitelibdir/%mname/jit
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.git20120525
- Initial build for Sisyphus

