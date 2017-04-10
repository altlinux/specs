Name:		LibreOffice-extension-CyrillicTools
Version:	1.3
Release:	alt3
Summary:	A macro library useful for working with Cyrillic documents
Group:		Office
License:	GPLv2+
URL:		http://openoffice.vspu.ac.ru
Source:		cyrtools%version.uno.zip

BuildPreReq:	unzip

%description
CyrillicTools is a macro library for OpenOffice.org 1.1.0 and above,
which provides some utilities useful for working with Cyrillic (Russian,
Ukrainian and Belarusian) documents.

%define lodir %_libdir/LibreOffice

%prep
%setup -c

%install
mkdir -p %buildroot%lodir/share/uno_packages/cache/uno_packages/%{name}_
cp -a . %buildroot%lodir/share/uno_packages/cache/uno_packages/%{name}_/%name

%files
%doc README
%lodir/share/uno_packages/cache/uno_packages/%{name}*

%changelog
* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 1.3-alt3
- Build for new LibreOffice
- Rename package

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt2
- Rename package

* Tue Sep 17 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial separated build
