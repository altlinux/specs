%define oname zope.testbrowser

%def_disable check

Name: python3-module-%oname
Version: 5.0.0
Release: alt3

Summary: Programmable browser for functional black-box tests
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.testbrowser/

# https://github.com/zopefoundation/zope.testbrowser.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
zope.testbrowser provides an easy-to-use programmable web browser with
special focus on testing. It is used in Zope, but it's not Zope specific
at all. For instance, it can be used to test or otherwise interact with
any web site.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' + 

ln -s README.rst README.txt

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.0.0-alt3
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2.dev0.git20150220.2
- Rebuild with python3.7.

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.0-alt2.dev0.git20150220.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.0-alt2.dev0.git20150220.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 5.0.0-alt2.dev0.git20150220.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt2.dev0.git20150220
- New snapshot

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt2.dev0.git20140125
- Restored zope.testbrowser.connection

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1.dev0.git20140125
- Version 5.0.0.dev0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.1-alt1.1
- Rebuild with Python-2.7

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

