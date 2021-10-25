%def_without check
%define modulename olefile
Name: python3-module-olefile
Version: 0.46
Release: alt2

Summary: Python package to parse, read and write Microsoft OLE2 files

Url: https://pypi.python.org/pypi/olefile
License: BSD
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/o/%modulename/%modulename-%version.zip
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
olefile is a Python package to parse,
read and write Microsoft OLE2 files
(also called Structured Storage,
Compound File Binary Format or Compound Document File Format),
such as Microsoft Office 97-2003 documents,
vbaProject.bin in MS Office 2007+ files,
Image Composer and FlashPix files, Outlook messages,
StickyNotes, several Microscopy file formats,
McAfee antivirus quarantine files, etc.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Mon Oct 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.46-alt2
- Drop python2 support.

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt1
- new version 0.46 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.45.1-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.45.1-alt1
- new version 0.45.1 (with rpmrb script)

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.44-alt1
- initial build for ALT Sisyphus

