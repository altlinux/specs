%define oname SleekXMPP

Name: python3-module-%oname
Version: 1.3.3
Release: alt3

Summary: Python 3.1+ XMPP Library
License: MIT
Group: Development/Python3
Url: http://sleekxmpp.com/
BuildArch: noarch

# Source-git: https://github.com/fritzy/SleekXMPP.git
Source: %name-%version.tar
Patch1: python3-async.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
SleekXMPP is an MIT licensed XMPP library for Python 3.1+.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
SleekXMPP is an MIT licensed XMPP library for Python 3.1+.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
SleekXMPP is an MIT licensed XMPP library for Python 3.1+.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
SleekXMPP is an MIT licensed XMPP library for Python 3.1+.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%__subst "s|\(from sleekxmpp.thirdparty.suelta.util\)|#\1 (https://github.com/fritzy/SleekXMPP/issues/480)|" sleekxmpp/plugins/xep_0138.py

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python3_sitelibdir/*/test


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.3-alt3
- python2 disabled

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt2.1aeefd
- merge with 1aeefd88accf45947c6376e9fac3abae9cbba8aa

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- build 1.3.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.git20140609.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1.git20140609.1
- NMU: Use buildreq for BR.

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140609
- Initial build for Sisyphus

