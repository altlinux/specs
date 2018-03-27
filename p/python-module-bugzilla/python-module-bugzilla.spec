%define oname bugzilla


Name: python-module-%oname
Version: 2.1.0
Release: alt1

Summary: A python library.. for bugzilla!

License: GPLv2.0
Group: Development/Python
Url: https://fedorahosted.org/python-bugzilla/

BuildArch: noarch

# Source-url: https://fedorahosted.org/releases/p/y/python-bugzilla/python-bugzilla-0.9.0.tar.gz
Source: bugzilla-%version.tar

# Automatically added by buildreq on Wed Jan 13 2010
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-PyXML
BuildRequires: python-module-Reportlab
BuildRequires: python-modules-email
BuildRequires: python-module-requests

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-setuptools


%description
This is a python module that provides a nice, python-ish interface to Bugzilla
over XMLRPC.

It was originally written specifically for Red Hat's Bugzilla instance, but
now supports the Web Services provided by upstream Bugzilla 3.0 and 3.2 also.

It also includes a 'bugzilla' commandline client which can be used for quick,
ad-hoc bugzilla jiggery-pokery.

%package -n python3-module-%oname
Summary: A python library.. for bugzilla!
Group: Development/Python3

%description -n python3-module-%oname
This is a python module that provides a nice, python-ish interface to Bugzilla
over XMLRPC.

It was originally written specifically for Red Hat's Bugzilla instance, but
now supports the Web Services provided by upstream Bugzilla 3.0 and 3.2 also.

It also includes a 'bugzilla' commandline client which can be used for quick,
ad-hoc bugzilla jiggery-pokery.

%prep
%setup -n bugzilla-%version

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot/%_bindir
mv %oname %oname.py3
popd
%python_install

%files
%doc COPYING *.md examples/*
%_bindir/%oname
%_man1dir/bugzilla.*
%python_sitelibdir/bugzilla/
%python_sitelibdir/python_bugzilla*.egg-info

%files -n python3-module-%oname
%doc COPYING *.md examples/*
%_bindir/%oname.py3
%_man1dir/bugzilla.*
%python3_sitelibdir/bugzilla/
%python3_sitelibdir/python_bugzilla*.egg-info


%changelog
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
