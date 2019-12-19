%define oname repoze.who.plugins.beaker_tkt

Name: python3-module-%oname
Version: 0.1
Release: alt7

Summary: Identifier (auth_tkt) plugin with beaker.session cache implementation
License: Free
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.who.plugins.beaker_tkt/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

# For more precise deps:
%python3_req_hier
# which unfortunately doesn't auto-detect precisely the following:
%py3_requires repoze.who.plugins paste.script beaker


%description
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

%package tests
Summary: Tests for repoze.who.plugins.beaker_tkt
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires webob webtest nose

%description -n python3-module-%oname-tests
BeakerAuthTktPlugin acts the same way as CookieAuthTktPlugin, but
instead of caching identity through cookie, it stores it in Beaker
session.

This package contains tests for repoze.who.plugins.beaker_tkt.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

# rm is a better way to do
#
#   %%exclude %%python3_sitelibdir/some/thing.py
#
# because it will also remove the compiled stuff from __pycache__ automatically
# (by means of brp-compileall).
pushd %buildroot%python3_sitelibdir
rm -v ./*/__init__.*
rm -v ./*/*/__init__.*
rm -v ./*/*/*/__init__.*
popd

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt7
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.1-alt6.1
- Rebuild with python3.7.

* Mon Oct 31 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt6
- %%python3_req_hier for more precise deps.

* Tue Jun 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt5
- (.spec) Python3 packaging fixes: exclude extra __pycache__/* junk.
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt3.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Avoid conflict with python-module-repoze.who (previous stage doesn't
  completed)

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Avoid conflict with python-module-repoze.who

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

