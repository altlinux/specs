Name: python-module-pyrax
Version: 1.9.0
Release: alt2

Summary: Python language bindings for OpenStack Clouds

License: ASL 2.0
Group: Development/Python
Url: https://github.com/rackspace/pyrax

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://imcleod.fedorapeople.org/src/pyrax/pyrax-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools
BuildRequires: python-module-mock
BuildRequires: python-dev

%description
A library for working with most OpenStack-based cloud deployments, though it
originally targeted the Rackspace public cloud. For example, the code for
cloudfiles contains the ability to publish your content on Rackspace's CDN
network, even though CDN support is not part of OpenStack Swift. But if you
don't use any of the CDN-related code, your app will work fine on any
standard Swift deployment.

%prep
%setup -n pyrax-%version

%build
%python_build

%install
%python_install

%files
%doc README COPYING samples docs
%python_sitelibdir/*

%changelog
* Thu Jun 16 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt2
- Actually do build me. (%%python_build had been forgotten.)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 29 2014 Ian McLeod <imcleod@redhat.com> - 1.9.0-3
- SPEC change to add missing macros for EPEL 6 builds

* Mon Jul 28 2014 Ian McLeod <imcleod@redhat.com> - 1.9.0-2
- Remove obsolete httplib requirement from SPEC file
- Remove #! execution headers for non-executable components [BZ1123044]
- add inline license for slugify() function to satisfy 3-clause BSD requirements from django [BZ1123044]
- misc additional SPEC change to comply with Fedora package guidelines [BZ1123044]

* Thu Jul 24 2014 Ian McLeod <imcleod@redhat.com> - 1.9.0-1
- Pull in upstream 1.9.0 release

* Fri Sep 6 2013 Greg Swift <gregswift@gmail.com> - 1.5.0-1
- Initial spec
