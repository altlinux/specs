%define pkgname boto
%def_with python3

Summary: A simple lightweight interface to Amazon Web Services
Name: python-module-%{pkgname}
Version: 2.38.0
Release: alt1.1
License: MIT
Group: Development/Python
Url: https://github.com/boto/boto

Source: %name-%version.tar
Patch0: python-boto.vendored.six-remove.patch

BuildRequires: python-devel
BuildRequires: python-module-nose
BuildRequires: python-module-mock
BuildRequires: python-module-httpretty
BuildRequires: python-module-requests
BuildArch: noarch

%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports S3 (Simple Storage Service), SQS (Simple Queue Service) via
the REST API's provided by those services and EC2 (Elastic Compute Cloud)
via the Query API. The goal of boto is to provide a very simple, easy to
use, lightweight wrapper around the Amazon services.


%if_with python3
%package -n python3-module-%{pkgname}
Summary:        A simple lightweight interface to Amazon Web Services
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-nose
BuildRequires:  python3-module-mock
BuildRequires:  python3-module-httpretty
BuildRequires:  python3-module-requests
BuildRequires:  python-tools-2to3

%description -n python3-module-%{pkgname}
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports S3 (Simple Storage Service), SQS (Simple Queue Service) via
the REST API's provided by those services and EC2 (Elastic Compute Cloud)
via the Query API. The goal of boto is to provide a very simple, easy to
use, lightweight wrapper around the Amazon services.

%endif

%prep
%setup
%patch0 -p1

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
2to3 --write --nobackups .
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -fv %buildroot/usr/bin/*

%python_install

%check
%{__python} tests/test.py default
%if_with python3
pushd ../python3
%{__python3} tests/test.py default
popd
%endif

%files
%doc README.rst
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
%{python_sitelibdir}/boto*

%if_with python3
%files -n python3-module-boto
%{python3_sitelibdir}/boto*
%endif

%changelog
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
