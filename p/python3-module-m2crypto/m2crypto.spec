%define _unpackaged_files_terminate_build 1

%define oname m2crypto

%ifnarch %ix86 armh
%def_with check
%else
%def_without check
%endif

Name: python3-module-%oname
Version: 0.42.0
Release: alt1

Summary: Support for using OpenSSL in python scripts.

License: BSD
Group: Development/Python3
URL: http://wiki.osafoundation.org/bin/view/Projects/MeTooCrypto

# https://gitlab.com/m2crypto/m2crypto.git
Source: %name-%version.tar

BuildRequires: libssl-devel swig
BuildRequires: /usr/bin/openssl
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-py libnumpy-py3-devel

%add_python3_req_skip M2Crypto.six.moves.http_client
%add_python3_req_skip M2Crypto.six.moves.http_cookies
%add_python3_req_skip M2Crypto.six.moves.socketserver
%add_python3_req_skip M2Crypto.six.moves.urllib_parse
%add_python3_req_skip M2Crypto.six.moves.urllib_response
%add_python3_req_skip M2Crypto.six.moves.xmlrpc_client
%py3_requires typing

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-parameterized
%endif

%description
This package allows you to call OpenSSL functions from python scripts.

%prep
%setup

%build
if pkg-config openssl ; then
	FLAGS="$(pkg-config --cflags openssl)"
	%add_optflags $FLAGS
	LDFLAGS="$LDFLAGS`pkg-config --libs-only-L openssl`" ; export LDFLAGS
fi

%python3_build

%install
if pkg-config openssl ; then
	FLAGS="$(pkg-config --cflags openssl)"
	%add_optflags $FLAGS
	LDFLAGS="$LDFLAGS`pkg-config --libs-only-L openssl`" ; export LDFLAGS
fi

%python3_build_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc CHANGES LICENCE README.rst tests doc/*
%python3_sitelibdir/M2Crypto
%python3_sitelibdir/M2Crypto-%version-py%_python3_version.egg-info

%changelog
* Thu Aug 15 2024 Grigory Ustinov <grenka@altlinux.org> 0.42.0-alt1
- Automatically updated to 0.42.0.

* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 0.41.0-alt1
- Automatically updated to 0.41.0.

* Tue Oct 31 2023 Grigory Ustinov <grenka@altlinux.org> 0.40.1-alt1
- Automatically updated to 0.40.1.

* Wed Oct 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.39.0.0.11.git.ce75069-alt1
- Fixed build with python3.12.

* Tue Jul 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.39.0-alt1
- Automatically updated to 0.39.0.

* Sat Sep 17 2022 Grigory Ustinov <grenka@altlinux.org> 0.38.0-alt1
- Automatically updated to 0.38.0.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.30.1-alt3
- Drop python2 support.

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.30.1-alt2
- Updated runtime dependencies.

* Thu Sep 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.30.1-alt1
- Updated to upstream version 0.30.1
- Enabled python3 build from same sources.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.22-alt2.git20140728.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt2.git20140728
- Snapthot from git

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1.r739
- Version 0.22

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.21-alt1.r724.1.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1.r724.1
- Rebuilt for debuginfo

* Mon Dec 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1.r724
- Pre-release of 0.21 (svn revision 724 for fix build with openssl 1.0.0x)

* Thu Aug 26 2010 Fr. Br. George <george@altlinux.ru> 0.20.2-alt2
- Check phase dependency fixed

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20.2-alt1.1
- Added BuildPreReq: python-module-setuptools-tests

* Sun Apr 11 2010 Fr. Br. George <george@altlinux.ru> 0.20.2-alt1
- Version up

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19.1-alt2
- Rebuilt with python 2.6

* Sat Nov 01 2008 Fr. Br. George <george@altlinux.ru> 0.19.1-alt1
- Version up

* Sun Mar 16 2008 Fr. Br. George <george@altlinux.ru> 0.18.2-alt1
- New version

* Wed Dec 27 2006 Fr. Br. George <george@altlinux.ru> 0.17-alt1
- New version, #10479 fixed

* Sat Jul 29 2006 Fr. Br. George <george@altlinux.ru> 0.16-alt1
- Initial ALT build from FC

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.16-2.1
- rebuild

* Thu Jul  6 2006 Miloslav Trmac <mitr@redhat.com> - 0.16-2
- Fix build with rawhide swig

* Thu Jul  6 2006 Miloslav Trmac <mitr@redhat.com> - 0.16-1
- Update to m2crypto-0.16

* Wed Apr 19 2006 Miloslav Trmac <mitr@redhat.com> - 0.15-4
- Fix SSL.Connection.accept (#188742)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.15-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.15-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan  3 2006 Miloslav Trmac <mitr@redhat.com> - 0.15-3
- Add BuildRequires: swig

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Miloslav Trmac <mitr@redhat.com> - 0.15-2
- Rebuild with newer openssl

* Mon Aug 29 2005 Miloslav Trmac <mitr@redhat.com> - 0.15-1
- Update to m2crypto-0.15
- Drop bundled swig

* Tue Jun 14 2005 Miloslav Trmac <mitr@redhat.com> - 0.13-5
- Better fix for #159898, by Dan Williams

* Thu Jun  9 2005 Miloslav Trmac <mitr@redhat.com> - 0.13-4
- Fix invalid handle_error override in SSL.SSLServer (#159898, patch by Dan
  Williams)

* Tue May 31 2005 Miloslav Trmac <mitr@redhat.com> - 0.13-3
- Fix invalid Python version comparisons in M2Crypto.httpslib (#156979)
- Don't ship obsolete xmlrpclib.py.patch
- Clean up the build process a bit

* Wed Mar 16 2005 Nalin Dahyabhai <nalin@redhat.com> 0.13-2
- rebuild

* Tue Nov 23 2004 Karsten Hopp <karsten@redhat.de> 0.13-1
- update, remove now obsolete patches

* Mon Nov 22 2004 Karsten Hopp <karsten@redhat.de> 0.09-7
- changed pythonver from 2.3 to 2.4

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Harald Hoyer <harald@redhat.com> - 0.09-5
- changed pythonver from 2.2 to 2.3
- patched setup.py to cope with include path

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 14 2003 Nalin Dahyabhai <nalin@redhat.com> 0.09-1
- Update to version 0.09
- Build using bundled copy of SWIG
- Pick up additional CFLAGS and LDFLAGS from OpenSSL's pkgconfig data, if
  there is any
- Handle const changes in new OpenSSL
- Remove unnecessary ldconfig calls in post/postun

* Thu Dec 12 2002 Elliot Lee <sopwith@redhat.com> 0.07_snap3-2
- Update to version 0.07_snap3

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Nalin Dahyabhai <nalin@redhat.com> 0.05_snap4-4
- rebuild with Python 2.2

* Wed Apr 24 2002 Nalin Dahyabhai <nalin@redhat.com> 0.05_snap4-3
- remove a stray -L at link-time which prevented linking with libssl (#59985)

* Thu Aug 23 2001 Nalin Dahyabhai <nalin@redhat.com> 0.05_snap4-2
- drop patch which isn't needed because we know swig is installed

* Mon Apr  9 2001 Nalin Dahyabhai <nalin@redhat.com> 0.05_snap4-1
- break off from openssl-python
