%define oname translationstring

Name: python3-module-%oname
Version: 1.4
Release: alt2

Summary: Utility library for i18n relied on by various Repoze packages
License: BSD-like
Group: Development/Python3
Url: http://pypi.python.org/pypi/translationstring
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: pylons_sphinx_theme python3-module-sphinx


%description
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

%package tests
Summary: Tests for translationstring
Group: Development/Python3
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
Group: Development/Python3

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

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build

pushd docs
%make pickle
%make html
popd

%install
%python3_install

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/pickle

%files tests
%python3_sitelibdir/%oname/tests

%files docs
%doc docs/_build/html/*

%files pickles
%python3_sitelibdir/%oname/pickle


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4-alt2
- build for python2 disabled

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

