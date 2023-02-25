Name: binwalk
Version: 2.3.4
Release: alt1

Summary: Firmware Analysis Tool

License: MIT License
Group: File tools
Url: https://github.com/ReFirmLabs/binwalk

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ReFirmLabs/binwalk/archive/v%version.tar.gz
Source: %name-%version.tar

# TODO:
%add_python3_req_skip lzma
%add_python3_req_skip capstone

BuildRequires(pre): rpm-build-python3
BuildRequires: libdb4-devel python3-module-cmd2 python3-module-setuptools

# TODO (see https://bugzilla.altlinux.org/show_bug.cgi?id=19293):
#BuildPreReq: python3-module-magic > 5.0.0

#Requires: python3-module-matplotlib python3-module-numpy

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
%python3_build

%install
%python3_install
[ "%_libdir" = "/usr/lib" ] || mv %buildroot/usr/lib %buildroot%_libdir

%files
%_bindir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- new version 2.3.4 (with rpmrb script)

* Sat Dec 18 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)

* Mon Nov 11 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt2
- Transfer on python3.

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sat Feb 16 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.1.1-alt3.git2e0ccfbf
- new version based on Git commit 2e0ccfbf3eff09c310cf3c8cbff3a72e8b41a845
- update project URL

* Sat May 05 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.1.1-alt2.git298cc28d
- new Git version based on 298cc28d493df7fa71236aac4f2b71d79763a435

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Sun Jul 12 2015 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- fix build

* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

