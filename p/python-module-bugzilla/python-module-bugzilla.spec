%define oname python-bugzilla


Name: python-module-bugzilla
Version: 0.5.1
Release: alt1.1

Summary: A python library.. for bugzilla!

License: GPL
Group: System/Libraries
Url: https://fedorahosted.org/python-bugzilla/

BuildArch: noarch

Source: %name-%version.tar

# Automatically added by buildreq on Wed Jan 13 2010
BuildRequires: python-devel python-module-PyXML python-module-Reportlab python-modules-email

BuildPreReq: rpm-build-python

%setup_python_module bugzilla

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
%python_build

%install
%python_install

%files
%doc README TODO
%_bindir/bugzilla
%_man1dir/bugzilla.*
%python_sitelibdir/bugzilla/
%python_sitelibdir/python_bugzilla*.egg-info

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux Sisyphus
