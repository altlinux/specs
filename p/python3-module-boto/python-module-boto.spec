%define _unpackaged_files_terminate_build 1

%define oname boto

Summary: A simple lightweight interface to Amazon Web Services
Name: python3-module-%oname
Version: 2.49.0
Release: alt2
License: MIT
Group: Development/Python3
Url: https://github.com/boto/boto

BuildArch: noarch

# https://github.com/boto/boto.git
Source: %name-%version.tar
Patch1: python-boto.vendored.six-remove.patch
Patch2: boto-python3.8-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose
BuildRequires: python3-module-mock
BuildRequires: python3-module-httpretty
BuildRequires: python3-module-requests

%add_findreq_skiplist %python3_sitelibdir/%oname/mashups/order.py
%add_python3_req_skip Queue StringIO httplib urlparse

#Conflicts: python-module-boto
#Obsoletes: python-module-boto

%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports S3 (Simple Storage Service), SQS (Simple Queue Service) via
the REST API's provided by those services and EC2 (Elastic Compute Cloud)
via the Query API. The goal of boto is to provide a very simple, easy to
use, lightweight wrapper around the Amazon services.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%python3_build

%install
%python3_install

rm -fv %buildroot/usr/bin/*

%check
%{__python3} tests/test.py default

%files
%doc README.rst
%if 0
%{_bindir}/asadmin
%{_bindir}/bundle_image
%{_bindir}/cfadmin
%{_bindir}/cq
%{_bindir}/cwutil
%{_bindir}/dynamodb_dump
%{_bindir}/dynamodb_load
%{_bindir}/elbadmin
%{_bindir}/fetch_file
%{_bindir}/glacier
%{_bindir}/instance_events
%{_bindir}/kill_instance
%{_bindir}/launch_instance
%{_bindir}/list_instances
%{_bindir}/lss3
%{_bindir}/mturk
%{_bindir}/pyami_sendmail
%{_bindir}/route53
%{_bindir}/s3put
%{_bindir}/sdbadmin
%{_bindir}/taskadmin
%endif
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.49.0-alt2
- Drop python2 support.

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.49.0-alt1
- Updated to upstream version 2.49.0.

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.38.0-alt2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.38.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.38.0-alt1
- Version 2.38.0

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.36.0-alt1
- Version 2.36.0

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.35.2-alt1
- Version 2.35.2

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.35.1-alt1
- Version 2.35.1

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 2.32.1-alt1
- 2.32.1
- Enable python3

* Mon Jul 30 2012 Mykola Grechukh <gns@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Fri May 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8d-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8d-alt1.1
- Rebuilt with python 2.6

* Tue Oct 13 2009 Boris Savelev <boris@altlinux.org> 1.8d-alt1
- intial build for Sisyphus

* Fri Jul 24 2009 Robert Scheck <robert@fedoraproject.org> 1.8d-1
- Upgrade to 1.8d (#513560)

* Wed Jun 03 2009 Luke Macken <lmacken@redhat.com> 1.7a-2
- Add python-setuptools-devel to our build requirements, for egg-info

* Thu Apr 16 2009 Robert Scheck <robert@fedoraproject.org> 1.7a-1
- Upgrade to 1.7a

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.5c-2
- Rebuild against rpm 4.6

* Sun Dec 07 2008 Robert Scheck <robert@fedoraproject.org> 1.5c-1
- Upgrade to 1.5c

* Fri Dec 05 2008 Jeremy Katz <katzj@redhat.com> 1.2a-2
- Rebuild for python 2.6

* Wed May 07 2008 Robert Scheck <robert@fedoraproject.org> 1.2a-1
- Upgrade to 1.2a

* Sat Feb 09 2008 Robert Scheck <robert@fedoraproject.org> 1.0a-1
- Upgrade to 1.0a

* Sat Dec 08 2007 Robert Scheck <robert@fedoraproject.org> 0.9d-1
- Upgrade to 0.9d

* Thu Aug 30 2007 Robert Scheck <robert@fedoraproject.org> 0.9b-1
- Upgrade to 0.9b
- Initial spec file for Fedora and Red Hat Enterprise Linux
