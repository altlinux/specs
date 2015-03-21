%define oname unicore-cms

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 1.7.0
Release: alt3.git20150319
Summary: JSON based CMS for Universal Core
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unicore-cms/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/unicore-cms.git
# https://github.com/universalcore/unicore-cms.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git
BuildPreReq: python-module-pyramid-tests python-module-pyramid_chameleon
BuildPreReq: python-module-pyramid_debugtoolbar python-module-memcached
BuildPreReq: python-module-pyramid_beaker python-module-waitress
BuildPreReq: python-module-webtest python-module-cornice
BuildPreReq: python-module-pyramid_celery python-module-babel
BuildPreReq: python-module-pyramid_redis python-module-lingua
BuildPreReq: python-module-arrow python-module-markdown
BuildPreReq: python-module-raven python-module-elastic-git
BuildPreReq: python-module-slugify python-module-pyramid_mako
BuildPreReq: python-module-GitDB python-module-mako
BuildPreReq: python-module-universal-analytics-python
BuildPreReq: python-module-mock python-module-unicore.content
BuildPreReq: python-module-unicore.google python-module-pycountry
BuildPreReq: python-module-unicore.distribute python-module-libthumbor
BuildPreReq: python-module-unicore.hub.client python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-pyramid_chameleon
BuildPreReq: python3-module-pyramid_debugtoolbar python3-module-memcached
BuildPreReq: python3-module-pyramid_beaker python3-module-waitress
BuildPreReq: python3-module-webtest python3-module-cornice
BuildPreReq: python3-module-pyramid_celery python3-module-babel
BuildPreReq: python3-module-pyramid_redis python3-module-lingua
BuildPreReq: python3-module-arrow python3-module-markdown
BuildPreReq: python3-module-raven python3-module-elastic-git
BuildPreReq: python3-module-slugify python3-module-mock
BuildPreReq: python3-module-universal-analytics-python
BuildPreReq: python3-module-unicore.content python3-module-pycountry
BuildPreReq: python3-module-unicore.google python3-module-libthumbor
BuildPreReq: python3-module-unicore.distribute
BuildPreReq: python3-module-unicore.hub.client python3-module-webtest
%endif

%py_provides cms
Conflicts: python-module-django-cms3.0
Conflicts: python-module-django-cms2.3
Conflicts: python-module-django-cms
%py_requires UniversalAnalytics pyramid_celery unicore.content slugify
%py_requires unicore.google unicore.distribute pycountry raven memcache
%py_requires unicore.hub.client pyramid_redis pyramid_debugtoolbar
%py_requires pyramid_chameleon

%description
JSON based CMS for Universal Core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JSON based CMS for Universal Core.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: JSON based CMS for Universal Core
Group: Development/Python3
%py3_provides cms
Conflicts: python3-module-django-cms3.0
Conflicts: python3-module-django-cms2.3
Conflicts: python3-module-django-cms
%py3_requires UniversalAnalytics pyramid_celery unicore.content slugify
%py3_requires unicore.google unicore.distribute pycountry raven
%py3_requires unicore.hub.client pyramid_redis memcache
%py3_requires pyramid_debugtoolbar pyramid_chameleon

%description -n python3-module-%oname
JSON based CMS for Universal Core.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JSON based CMS for Universal Core.

This package contains tests for %oname.
%endif

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

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3.git20150319
- More requirements

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt2.git20150319
- Added necessary requirements

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20150319
- Version 1.7.0

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1.git20150226
- Version 1.6.5

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1.git20150115
- Version 1.4.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20141127
- Version 1.3.0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20141120
- Version 1.2.2

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141119
- Version 1.1.1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.13-alt1.git20141111
- Version 1.0.13

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.12-alt1.git20141110
- Version 1.0.12

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1
- Version 1.0.10

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt2
- Applied python-module-unicore-cms-1.0.4-alt1.diff

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus

