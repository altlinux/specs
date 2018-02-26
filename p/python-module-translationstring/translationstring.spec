%define oname translationstring

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1
Summary: Utility library for i18n relied on by various Repoze packages
License: BSD-like
Group: Development/Python
Url: http://pypi.python.org/pypi/translationstring
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
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
* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Version 1.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

