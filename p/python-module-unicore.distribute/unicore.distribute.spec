%define mname unicore
%define oname %mname.distribute

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20150310
Summary: Distribution tools for Universal Core content
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unicore.distribute/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore.distribute.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-elastic-git-tests python-module-unicore.content
BuildPreReq: python-module-waitress python-module-pyramid
BuildPreReq: python-module-pyramid_celery python-module-cornice
BuildPreReq: python-module-colander python-module-pytest-cov
BuildPreReq: python-module-pytest-xdist python-module-slugify
BuildPreReq: python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-elastic-git-tests python3-module-unicore.content
BuildPreReq: python3-module-waitress python3-module-pyramid
BuildPreReq: python3-module-pyramid_celery python3-module-cornice
BuildPreReq: python3-module-colander python3-module-pytest-cov
BuildPreReq: python3-module-pytest-xdist python3-module-slugify
BuildPreReq: python3-module-webtest
%endif

%py_provides %oname
%py_requires %mname elasticgit unicore.content waitress pyramid cornice
%py_requires pyramid_celery colander

%description
APIs & tools for dealing with content repos.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
APIs & tools for dealing with content repos.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Distribution tools for Universal Core content
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname elasticgit unicore.content waitress pyramid cornice
%py3_requires pyramid_celery colander

%description -n python3-module-%oname
APIs & tools for dealing with content repos.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
APIs & tools for dealing with content repos.

This package contains tests for %oname.
%endif

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
#py.test -vv --cov %mname
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version -vv --cov %mname
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/%mname/distribute
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/distribute/tests

%files tests
%python_sitelibdir/%mname/distribute/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/%mname/distribute
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/distribute/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/distribute/tests
%endif

%changelog
* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20150310
- Initial build for Sisyphus

