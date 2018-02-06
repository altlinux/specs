%define oname translationstring

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt1.dev.git20141105.1.1.1
Summary: Utility library for i18n relied on by various Repoze packages
License: BSD-like
Group: Development/Python
Url: http://pypi.python.org/pypi/translationstring
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: pylons_sphinx_theme python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools
%endif

%description
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

%if_with python3
%package -n python3-module-%oname
Summary: Utility library for i18n relied on by various Repoze packages (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

%package -n python3-module-%oname-tests
Summary: Tests for translationstring
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

This package contains tests for translationstring.
%endif

%package tests
Summary: Tests for translationstring
Group: Development/Python
Requires: %name = %version-%release

%description tests
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

This package contains tests for translationstring.

%package pickles
Summary: Pickles for translationstring
Group: Development/Python

%description pickles
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

This package contains pickles for translationstring.

%package docs
Summary: Documentation for translationstring
Group: Development/Documentation

%description docs
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

This package contains documentation for translationstring.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs
rm -fR docs/_themes
cp -fR %_datadir/pylons_sphinx_theme docs/_themes

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

pushd docs
%make pickle
%make html
popd

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/tests

%files docs
%doc docs/_build/html/*

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4-alt1.dev.git20141105.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4-alt1.dev.git20141105.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4-alt1.dev.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20141105
- Version 1.4dev
- Enabled testing

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-3.3

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Version 1.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

