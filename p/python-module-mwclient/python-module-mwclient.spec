%define modulename mwclient

Name: python-module-mwclient
Version: 0.6.5
Release: alt1.1

Summary: mwclient is a framework to MediaWiki's API

Group: Development/Python

License: MIT
Url: http://sourceforge.net/projects/mwclient/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%modulename/%modulename-%version.tar

BuildPreReq: rpm-build-python

%setup_python_module %modulename

%description
Mwclient is a client to the MediaWiki API
and allows access to almost most implemented API functions.

%prep
%setup -n %modulename-%version

%install
install -d -m755 %buildroot%python_sitelibdir/mwclient/
install -pm 0644 *.py %buildroot%python_sitelibdir/mwclient/

%files
%doc README.txt REFERENCE.txt RELEASE-NOTES.txt
%python_sitelibdir/mwclient*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.6.5-alt1
- initial build for ALT Linux Sisyphus
