%define oname autobahn

Name: python3-module-%oname
Version: 18.5.2
Release: alt6

Summary: WebSocket & WAMP for Python/Twisted
License: Apache License 2.0
Group: Development/Python3
Url: https://github.com/tavendo/AutobahnPython

# https://github.com/tavendo/AutobahnPython.git
Source: %name-%version.tar

# https://github.com/crossbario/autobahn-python/commit/9b6fb57e5c87a5e29cd880f752a30b9409d480c6
Patch: ensure-python37-compat.patch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%py3_requires twisted.internet twisted.web twisted.words

%description
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

%prep
%setup
%patch -p1

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc *.md *.rst
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 18.5.2-alt6
- NMU: drop tests subpackage and unitest2 requires

* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 18.5.2-alt5
- Build for python3 only.

* Sat Mar 21 2020 Vitaly Lipatov <lav@altlinux.ru> 18.5.2-alt4
- disable python2 module build

* Sat Sep 21 2019 Anton Midyukov <antohami@altlinux.org> 18.5.2-alt3
- Update BuldRequires
- Drop build pickles
- Add swith disable docs and python2 module build

* Fri May 10 2019 Vitaly Lipatov <lav@altlinux.ru> 18.5.2-alt2.1
- NMU: drop python3 trollius

* Sat Apr 20 2019 Anton Midyukov <antohami@altlinux.org> 18.5.2-alt2
- Fix build with python-3.7

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 18.5.2-alt1.qa1
- NMU: applied repocop patch

* Sun Aug 26 2018 Anton Midyukov <antohami@altlinux.org> 18.5.2-alt1
- new version 18.5.2
- disable check

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 17.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 17.7.1-alt1
- Updated to upstream version 17.7.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.5-alt1.git20150111.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.5-alt1.git20150111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.5-alt1.git20150111.1
- NMU: Use buildreq for BR.

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.git20150111
- Version 0.9.5

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3.3-alt1.git20141115
- Version 0.9.3-3

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20141110
- Version 0.9.3

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20141025
- Version 0.9.2
- Enabled testing

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.10-alt2.git20140710
- Moved tests into separate package

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.10-alt1.git20140710
- Version 0.8.10

* Tue Nov 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20131123
- Version 0.6.5

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20130826
- Version 0.6.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.14-alt2.git20130210
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.14-alt1.git20130210.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.14-alt1.git20130210
- Version 0.5.14

* Sat Sep 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.8-alt1.git20120920
- Version 0.5.8

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20120523
- Initial build for Sisyphus

