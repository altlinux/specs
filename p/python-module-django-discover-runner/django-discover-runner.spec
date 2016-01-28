%define oname django-discover-runner

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20130615.1
Summary: A Django test runner based on unittest2's test discovery
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-discover-runner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jezdez/django-discover-runner.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-django-tests python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-django-tests python3-module-unittest2
%endif

%py_provides discover_runner
%py_requires django.test

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-psycopg2 python-module-pytest python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-psycopg2 python3-module-pytest python3-module-setuptools python3-module-yaml
BuildRequires: python-module-django python-module-setuptools-tests python-module-unittest2 python3-module-django python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3

%description
An alternative Django TEST_RUNNER which uses the unittest2 test
discovery from a base path specified in the settings, or any other
module or package specified to the test management command -- including
app tests.

If you just run './manage.py test', it'll discover and run all tests
underneath the current working directory. E.g. if you run
'./manage.py test full.dotted.path.to.test_module', it'll run the tests
in that module (you can also pass multiple modules). If you give it a
single dotted path to a package (like a Django app) like
'./manage.py test myapp' and that package does not itself directly
contain any tests, it'll do test discovery in all submodules of that
package.

%package -n python3-module-%oname
Summary: A Django test runner based on unittest2's test discovery
Group: Development/Python3
%py3_provides discover_runner
%py3_requires django.test

%description -n python3-module-%oname
An alternative Django TEST_RUNNER which uses the unittest2 test
discovery from a base path specified in the settings, or any other
module or package specified to the test management command -- including
app tests.

If you just run './manage.py test', it'll discover and run all tests
underneath the current working directory. E.g. if you run
'./manage.py test full.dotted.path.to.test_module', it'll run the tests
in that module (you can also pass multiple modules). If you give it a
single dotted path to a package (like a Django app) like
'./manage.py test myapp' and that package does not itself directly
contain any tests, it'll do test discovery in all submodules of that
package.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt1.git20130615.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20130615
- Initial build for Sisyphus

