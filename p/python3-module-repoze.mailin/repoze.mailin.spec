%define oname repoze.mailin

Name: python3-module-%oname
Version: 0.4
Release: alt3

Summary: Map inbound e-mail onto application-defined handlers
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.mailin

# https://github.com/repoze/repoze.mailin.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires repoze zope.interface


%description
This package provides a framework for mapping inbound e-mail onto
application-defined handlers.

%package tests
Summary: Tests for repoze.mailin
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides a framework for mapping inbound e-mail onto
application-defined handlers.

This package contains tests for repoze.mailin.

%prep
%setup

sed -i 's|implements(|# implements(|' \
        $(find ./ -type f \( -name 'maildir.py' -o -name 'pending.py' \))

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt docs/index.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4-alt2.git20120326.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.git20120326.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.git20120326.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2.git20120326
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20120326
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110225
- Initial build for Sisyphus

