%define mname tw2
%define oname %mname.sqla

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 2.1.0
Release: alt1.git20131108
Summary: SQLAlchemy database layer for ToscaWidgets 2, a web widget toolkit
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.sqla/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.sqla.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-cheetah python-module-turbocheetah
BuildPreReq: python-module-genshi python-module-kid
BuildPreReq: python-module-turbokid python-module-mako
BuildPreReq: python-module-tw2.forms python-module-tw2.dynforms
BuildPreReq: python-module-SQLAlchemy python-module-zope.sqlalchemy
BuildPreReq: python-module-BeautifulSoup python-module-strainer
BuildPreReq: python-module-nose python-module-FormEncode
BuildPreReq: python-module-webtest python-module-elixir
BuildPreReq: python-module-sieve python-module-markdown
BuildPreReq: python-module-tw2.core-tests python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cheetah python3-module-turbocheetah
BuildPreReq: python3-module-genshi python3-module-kid
BuildPreReq: python3-module-turbokid python3-module-mako
BuildPreReq: python3-module-tw2.forms python3-module-tw2.dynforms
BuildPreReq: python3-module-SQLAlchemy python3-module-zope.sqlalchemy
BuildPreReq: python3-module-BeautifulSoup python3-module-strainer
BuildPreReq: python3-module-nose python3-module-FormEncode
BuildPreReq: python3-module-webtest python3-module-elixir
BuildPreReq: python3-module-sieve python3-module-markdown
BuildPreReq: python3-module-tw2.core-tests python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires %mname Cheetah turbocheetah genshi kid turbokid mako
%py_requires tw2.forms tw2.dynforms sqlalchemy

%description
tw2.sqla is a database layer for ToscaWidgets 2 and SQLAlchemy. It
allows common database tasks to be achieved with minimal code.

%package -n python3-module-%oname
Summary: SQLAlchemy database layer for ToscaWidgets 2, a web widget toolkit
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname Cheetah turbocheetah genshi kid turbokid mako
%py3_requires tw2.forms tw2.dynforms sqlalchemy

%description -n python3-module-%oname
tw2.sqla is a database layer for ToscaWidgets 2 and SQLAlchemy. It
allows common database tasks to be achieved with minimal code.

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
%doc *.rst docs/*.rst
%python_sitelibdir/%mname/sqla
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/%mname/sqla
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20131108
- Initial build for Sisyphus

