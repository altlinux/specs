%def_without check
%def_with python3

%define python3_dirsetup \
%if_with python3 \
rm -rf ../python3 \
cp -a . ../python3 \
%endif \
%nil

#find ../python3 -name "*.py" | xargs %__subst "s|^#!/usr/bin/env python$|#!/usr/bin/python3|g"

%define python3_dirbuild \
%if_with python3 \
pushd ../python3 \
%python3_build_debug \
popd \
%endif \
%nil

%define python3_dirinstall \
%if_with python3 \
pushd ../python3 \
%python3_install \
popd \
%endif \
%nil

#TODO: python3_dircheck


%define modulename olefile
Name: python-module-olefile
Version: 0.46
Release: alt1

Summary: Python package to parse, read and write Microsoft OLE2 files

Url: https://pypi.python.org/pypi/olefile
License: BSD
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/o/%modulename/%modulename-%version.zip
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

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

%package -n python3-module-olefile
Summary: Python package to parse, read and write Microsoft OLE2 files
Group: Development/Python3

%description -n python3-module-olefile
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
%setup

%python3_dirsetup

%build
%python_build_debug
%python3_dirbuild

%install
%python_install
%python3_dirinstall

%files
%doc README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-olefile
%doc README.md
%python3_sitelibdir/*
%endif


%changelog
* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt1
- new version 0.46 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.45.1-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.45.1-alt1
- new version 0.45.1 (with rpmrb script)

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.44-alt1
- initial build for ALT Sisyphus

