%define oname z3c.javascript

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Javascript libraries Zope 3
License: BSD-like
Group: Development/Python3
Url: http://svn.zope.org/z3c.javascript/?rev=80712#dirlist

# http://z3c-javascript.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires z3c


%description
Javascript libraries Zope 3.

%prep
%setup

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
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.2-alt1.svn20100323.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.svn20100323.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.svn20100323.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20100323
- New snapshot
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.svn20080428.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20080428
- Initial build for Sisyphus

