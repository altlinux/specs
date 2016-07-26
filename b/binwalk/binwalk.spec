Name: binwalk
Version: 2.1.1
Release: alt1

Summary: Firmware Analysis Tool

License: MIT License
Group: File tools
Url: https://github.com/devttys0/binwalk

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/devttys0/binwalk/archive/v%version.tar.gz
Source: %name-%version.tar

# TODO:
%add_python_req_skip lzma
%add_python_req_skip capstone

BuildRequires: libdb4-devel python-module-cmd2 python-module-setuptools

# TODO (see https://bugzilla.altlinux.org/show_bug.cgi?id=19293):
#BuildPreReq: python-module-magic > 5.0.0

#Requires: python-module-matplotlib python-module-numpy

%description
Binwalk is a firmware analysis tool designed to assist in the analysis,
extraction, and reverse engineering of firmware images and other binary blobs.
It is simple to use, fully scriptable,
and can be easily extended via custom signatures, extraction rules, and plugin modules.

Binwalk supports various types of analysis useful
for inspecting and reverse engineering firmware, including:

* Embedded file identification and extraction
* Executable code identification
* Type casting
* Entropy analysis and graphing
* Heuristic data analysis
* "Smart" strings analysis 

Binwalk's file signatures are (mostly) compatible with the magic signatures
used by the Unix file utility, and include customized/improved signatures
for files that are commonly found in firmware images such as compressed/archived files,
firmware headers, kernels, bootloaders, filesystems, etc. 

%prep
%setup

%build
%python_build

%install
%python_install
[ "%_libdir" = "/usr/lib" ] || mv %buildroot/usr/lib %buildroot%_libdir

%files
%_bindir/*
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%changelog
* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Sun Jul 12 2015 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- fix build

* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

