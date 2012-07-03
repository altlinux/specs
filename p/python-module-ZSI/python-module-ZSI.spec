%define rname ZSI
Name: python-module-ZSI
Version: 2.0
Release: alt2.1.1.1

BuildArch: noarch

Summary: A pure-Python module that provides an implementation of SOAP messaging.
License: PSF
Group: Development/Python
Url: http://pywebsvcs.sourceforge.net

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

BuildRequires: python-module-setuptools python-dev >= 2.4
Requires:python >= 2.4 python-module-PyXML

%description
ZSI, the Zolera SOAP Infrastructure, is a pure-Python module that
provides an implementation of SOAP messaging, as described in SOAP 1.1
Specification (see http://www.w3.org/TR/soap).  It can also be used to
build applications using SOAP Messages with Attachments (see
http://www.w3.org/TR/SOAP-attachments).  ZSI is intended to make it
easier to write web services in Python.

%prep
%setup -q

%build

%install
%__python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,root,root)
%python_sitelibdir/%rname/
%python_sitelibdir/%rname-%version-py%__python_version.egg-info/
%_bindir/*


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.1.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.1.1
- Rebuilt with python 2.6

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 2.0-alt2.1
- Rebuilt with python-2.5.

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 2.0-alt2
- Use __python macro while building and __python_version while packaging.

* Thu Jan 17 2008 Alexey Morsov <swi@altlinux.ru> 2.0-alt1
- initial build

