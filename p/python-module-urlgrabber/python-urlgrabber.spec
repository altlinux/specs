%define real_name urlgrabber

Summary: High-level cross-protocol url-grabber
Name: python-module-urlgrabber
Version: 3.1.0
Release: alt1.1.1
License: LGPL
Group: Development/Python
URL: http://linux.duke.edu/projects/urlgrabber/
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: http://linux.duke.edu/projects/urlgrabber/download/urlgrabber-%{version}.tar.gz
Patch: python-urlgrabber-2.9.6-reget.patch
BuildArch: noarch
Provides: urlgrabber
# Automatically added by buildreq on Mon Dec 17 2007
BuildRequires: python-devel python-modules-compiler python-modules-email python-modules-logging

BuildRequires: python

%description
python-urlgrabber is a high-level cross-protocol url-grabber for python
supporting HTTP, FTP and file locations. Features include keepalive, byte
ranges, throttling, authentication, proxies and more.

%prep
%setup -n %real_name-%version
#patch0 -p1 -b .reget

%build
%__python setup.py build

%install
%__python setup.py install -O1 --skip-build --root="%buildroot" --prefix="%_prefix"

%files
/usr/share/doc/%real_name-%version/*
%_bindir/%real_name
#python_sitelib/urlgrabber/
#_libdir/python%{__python_version}/site-packages/%real_name/*
%python_sitelibdir/%real_name/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.0-alt1.1.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.1
- Rebuilt with python 2.6

* Tue Apr 29 2008 Mikhail Pokidko <pma@altlinux.org> 3.1.0-alt1
- Version up

* Mon Dec 17 2007 Mikhail Pokidko <pma@altlinux.org> 2.9.7-alt1
- Initial ALT build
