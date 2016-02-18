%define module_name django-reversion

%def_with python3

Name: python-module-%module_name
Version: 1.8.4
Release: alt1.git20140907.1

Summary: Comprehensive version control facilities for Django

License: BSD
Group: Development/Python
Url: http://code.google.com/p/django-reversion

# https://github.com/etianen/django-reversion.git
Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv rpm-build-python3 time

%description
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

%package tests
Summary: Tests for Django Reversion
Group: Development/Python
Requires: %name = %version-%release

%description tests
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

This package contains tests for Django Reversion.

%package docs
Summary: Documentation for Django Reversion
Group: Development/Documentation

%description docs
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

This package contains documentation for Django Reversion.

%package -n python3-module-%module_name
Summary: Comprehensive version control facilities for Django
Group: Development/Python3

%description -n python3-module-%module_name
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

%package -n python3-module-%module_name-tests
Summary: Tests for Django Reversion
Group: Development/Python3
Requires: python3-module-%module_name = %version-%release

%description -n python3-module-%module_name-tests
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

This package contains tests for Django Reversion.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc *.rst
%python_sitelibdir/django_reversion-*
%python_sitelibdir/reversion
#exclude %python_sitelibdir/reversion/tests*

#files tests
#python_sitelibdir/reversion/tests*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc *.rst
%python3_sitelibdir/django_reversion-*
%python3_sitelibdir/reversion
#exclude %python_sitelibdir/reversion/tests*
#exclude %python_sitelibdir/reversion/*/tests*

#files -n python3-module-%module_name-tests
#python_sitelibdir/reversion/tests*
#python_sitelibdir/reversion/*/tests*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.8.4-alt1.git20140907.1
- NMU: Use buildreq for BR.

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.4-alt1.git20140907
- Version 1.8.4
- Added module for Python 3

* Sun Jan 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git91bd6b
- Version 1.5.1 (ALT #26818)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.alpha.gitd9655b.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.alpha.gitd9655b
- Version 1.4 alpha

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git64bd63
- Version 1.3.2
- Extracted tests into separate package

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2.1-alt1.svn273
- Initial build for ALT Linux

