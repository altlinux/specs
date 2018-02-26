%define version 0.8.1c
%define release alt1.1
%setup_python_module vobject

Name: %packagename
Version: %version
Release: %release.1
Packager: Alexey Shabalin <shaba at altlinux.ru>

Summary: Python module for parsing and generating vCard files
License: ASL 1.1
Group: Development/Python
Url: http://vobject.skyhouseconsulting.com
BuildArch: noarch

Source0: http://vobject.skyhouseconsulting.com/%modulename-%version.tar.gz
Patch1: python-module-vobject-no-ez-setup.patch

BuildRequires:  python-module-setuptools

%description
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%prep
%setup -q -n %modulename-%version
%patch1 -p1
# remove win32 files
rm -f vobject/win32tz.py

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc LICENSE-2.0.txt ACKNOWLEDGEMENTS.txt README.txt

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1c-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1c-alt1.1
- Rebuilt with python 2.6

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.1c-alt1
- 0.8.1c

* Sun Aug 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- initial build for ALTLinux

