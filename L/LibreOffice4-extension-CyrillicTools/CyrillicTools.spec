Name:		LibreOffice4-extension-CyrillicTools
Version:	1.3
Release:	alt2
Summary:	A macro library useful for working with Cyrillic documents
Group:		Office
License:	GPLv2+
URL:		http://openoffice.vspu.ac.ru
Source:		cyrtools%version.uno.zip
Obsoletes:	LibreOffce4-extension-CyrillicTools

BuildPreReq:	unzip

%description
CyrillicTools is a macro library for OpenOffice.org 1.1.0 and above,
which provides some utilities useful for working with Cyrillic (Russian,
Ukrainian and Belarusian) documents.

%define lodir %_libdir/LibreOffice4

%prep
%setup -c

%install
mkdir -p %buildroot%lodir/share/uno_packages/cache/uno_packages/%{name}_
cp -a . %buildroot%lodir/share/uno_packages/cache/uno_packages/%{name}_/%name

%files
%doc README
%lodir/share/uno_packages/cache/uno_packages/%{name}*

%changelog
* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt2
- Rename package

* Tue Sep 17 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial separated build
