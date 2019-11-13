%define oname deliverance

Name: python3-module-%oname
Version: 0.6.1
Release: alt4

Summary: Deliverance transforms HTML to theme pages
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/Deliverance
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Deliverance does transformations of HTML to 'theme' pages, similar in
function to XSLT but using a simpler XML-based language to express the
transformation.

%package tests
Summary: Tests for Deliverance
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Deliverance does transformations of HTML to 'theme' pages, similar in
function to XSLT but using a simpler XML-based language to express the
transformation.

This package contains tests for Deliverance.

%prep
%setup

find ./ -type f -name '*.py' -exec \
    sed -i 's|rfc822|rfc822py3|' '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/*/*/*/test

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/*/*/*/test


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt4
- python2 disabled

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added module for Python 3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Sun Dec 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Extracted test into separate package

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Applied patch from Repocop

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

