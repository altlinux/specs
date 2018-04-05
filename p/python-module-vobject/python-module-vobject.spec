%define version 0.9.5
%define release alt1
%setup_python_module vobject

Name: python-module-vobject
Version: %version
Release: %release
Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: Python module for parsing and generating vCard files
License: ASL 1.1
Group: Development/Python
Url: http://vobject.skyhouseconsulting.com
BuildArch: noarch

Source0: %modulename-%version.tar
#VCS: https://github.com/eventable/vobject

BuildRequires:  python-module-setuptools
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%package -n python3-module-%modulename
Summary: Python module for parsing and generating vCard files
Group: Development/Python3

%description -n python3-module-%modulename
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%prep
%setup -n %modulename-%version
# remove win32 files
rm -f vobject/win32tz.py
rm -rf ../python3
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install 
pushd ../python3
%python3_install
popd

%files
%doc ACKNOWLEDGEMENTS.txt LICENSE-2.0.txt README.md
%python_sitelibdir/%{modulename}*

%files -n python3-module-%modulename
%python3_sitelibdir/%{modulename}*

%changelog
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

