%define version 0.9.6.1
%define modulename vobject

Name: python3-module-vobject
Version: %version
Release: alt2
Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: Python module for parsing and generating vCard files
License: ASL 1.1
Group: Development/Python3
Url: http://vobject.skyhouseconsulting.com
BuildArch: noarch

Source0: %modulename-%version.tar
#VCS: https://github.com/eventable/vobject

BuildRequires(pre): rpm-build-python3

%description
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%prep
%setup -n %modulename-%version
# remove win32 files
rm -f vobject/win32tz.py

%build
%python3_build

%install
%python3_install

%files
%doc ACKNOWLEDGEMENTS.txt LICENSE-2.0.txt README.md
%python3_sitelibdir/%{modulename}*

%changelog
* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.6.1-alt2
- Drop python2 support.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.6.1-alt1
- New version.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt1
- New version.

* Mon Aug 01 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt2
- vcard: Fix ORG fields with multiple components (commit fe78218)

* Tue Jul 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- New version 0.9.2

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1d-alt1.git20140128
- Version 0.8.1d

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1c-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1c-alt1.1
- Rebuilt with python 2.6

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.1c-alt1
- 0.8.1c

* Sun Aug 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- initial build for ALTLinux

