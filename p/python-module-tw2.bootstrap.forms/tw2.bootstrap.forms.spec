%define mname tw2.bootstrap
%define oname %mname.forms

%def_with python3

Name: python-module-%oname
Version: 2.2.2.1
Release: alt1
Summary: A drop-in replacement for tw2.forms but with bootstrap!
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.bootstrap.forms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-jinja2 python-module-tw2.core
BuildPreReq: python-module-tw2.forms python-module-tw2.jquery
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-sieve python-module-webtest
BuildPreReq: python-module-FormEncode
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-jinja2 python3-module-tw2.core
BuildPreReq: python3-module-tw2.forms python3-module-tw2.jquery
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-sieve python3-module-webtest
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires genshi mako jinja2 tw2.core tw2.forms tw2.jquery six

%description
ToscaWidgets 2 library that makes excessive use of the Twitter Bootstrap
CSS Framework.

%package -n python3-module-%oname
Summary: A drop-in replacement for tw2.forms but with bootstrap!
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires genshi mako jinja2 tw2.core tw2.forms tw2.jquery six

%description -n python3-module-%oname
ToscaWidgets 2 library that makes excessive use of the Twitter Bootstrap
CSS Framework.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires tw2

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname
%py3_requires tw2

%description -n python3-module-%mname
Core files of %mname.

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

install -p -m644 tw2/bootstrap/__init__.py \
	%buildroot%python_sitelibdir/tw2/bootstrap/
%if_with python3
pushd ../python3
install -p -m644 tw2/bootstrap/__init__.py \
	%buildroot%python3_sitelibdir/tw2/bootstrap/
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
%python_sitelibdir/tw2/bootstrap/forms
%python_sitelibdir/*.egg-info

%files -n python-module-%mname
%dir %python_sitelibdir/tw2/bootstrap
%python_sitelibdir/tw2/bootstrap/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/tw2/bootstrap/forms
%python3_sitelibdir/*.egg-info

%files -n python3-module-%mname
%dir %python3_sitelibdir/tw2/bootstrap
%dir %python3_sitelibdir/tw2/bootstrap/__pycache__
%python3_sitelibdir/tw2/bootstrap/__init__.py
%python3_sitelibdir/tw2/bootstrap/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2.1-alt1
- Initial build for Sisyphus

