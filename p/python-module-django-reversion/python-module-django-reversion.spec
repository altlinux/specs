%define modname django-reversion

Name: python-module-%modname
Version: 2.0.9
Release: alt1

Summary: Comprehensive version control facilities for Django
License: BSD
Group: Development/Python
Url: http://code.google.com/p/django-reversion
# https://github.com/etianen/django-reversion.git
BuildArch: noarch

Source: django-reversion-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-alabaster
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-objects.inv
BuildRequires: time

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: python3-module-setuptools

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base


%description
django-reversion is an extension to the Django web framework that provides version control for model instances.

%package tests
Summary: Tests for Django Reversion
Group: Development/Python
Requires: %name = %version-%release

%description tests
django-reversion is an extension to the Django web framework that provides version control for model instances.

This package contains tests for Django Reversion.

%package docs
Summary: Documentation for Django Reversion
Group: Development/Documentation

%description docs
django-reversion is an extension to the Django web framework that provides version control for model instances.

This package contains documentation for Django Reversion.

%package -n python3-module-%modname
Summary: Comprehensive version control facilities for Django
Group: Development/Python3

%description -n python3-module-%modname
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

%package -n python3-module-%modname-tests
Summary: Tests for Django Reversion
Group: Development/Python3
Requires: python3-module-%modname = %version-%release

%description -n python3-module-%modname-tests
django-reversion is an extension to the Django web framework that provides version control for model instances.

This package contains tests for Django Reversion.

%prep
%setup -n django-reversion-%version

cp -fR . ../python3

#%prepare_sphinx .
#ln -s ../objects.inv docs/

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

export PYTHONPATH=%buildroot%python_sitelibdir
sphinx-build docs/ _build/ docs/*.rst

%files
%doc *.rst LICENSE
%python_sitelibdir/django_reversion-*
%python_sitelibdir/reversion
#exclude %python_sitelibdir/reversion/tests*

#files tests
#python_sitelibdir/reversion/tests*

%files docs
%doc _build/*

%files -n python3-module-%modname
%doc *.rst LICENSE
%python3_sitelibdir/django_reversion-*
%python3_sitelibdir/reversion
#exclude %python_sitelibdir/reversion/tests*
#exclude %python_sitelibdir/reversion/*/tests*

#files -n python3-module-%modname-tests
#python_sitelibdir/reversion/tests*
#python_sitelibdir/reversion/*/tests*


%changelog
* Wed Mar 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.9-alt1
- Version 2.0.9

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.4-alt1.git20140907.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

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
