%define oname bugzilla

Name: python3-module-%oname
Version: 2.3.0
Release: alt1

Summary: A python library.. for bugzilla!
License: GPLv2.0
Group: Development/Python3
Url: https://github.com/python-bugzilla/python-bugzilla
BuildArch: noarch

# Source-url: https://pypi.io/packages/source/p/python-bugzilla/python-bugzilla-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests


%description
This is a python module that provides a nice, python-ish interface to Bugzilla
over XMLRPC.

It was originally written specifically for Red Hat's Bugzilla instance, but
now supports the Web Services provided by upstream Bugzilla 3.0 and 3.2 also.

It also includes a 'bugzilla' commandline client which can be used for quick,
ad-hoc bugzilla jiggery-pokery.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc COPYING *.md examples/*
%_bindir/*
%_man1dir/bugzilla.*
%python3_sitelibdir/bugzilla/
%python3_sitelibdir/python_bugzilla*.egg-info


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt1
- python2 disabled

* Wed Jun 19 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)
- switch to build from tarball

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.ru> 2.1.0-alt1
- Version 2.1.0

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Thu Sep 04 2014 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux Sisyphus
