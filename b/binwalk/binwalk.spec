Name: binwalk
Version: 1.2.1
Release: alt1

Summary: Firmware Analysis Tool

License: MIT License
Group: File tools
Url: http://code.google.com/p/binwalk/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://binwalk.googlecode.com/files/%name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 14 2013
# optimized out: python-base python-devel python-module-dateutil python-module-distribute python-module-imaging python-module-numpy python-module-numpy-testing python-module-pyparsing python-module-zope python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-tkinter python-modules-unittest python3-base
BuildRequires: python-module-cmd2 python-module-magic python-module-matplotlib python-module-mwlib python-module-protobuf

# TODO (see https://bugzilla.altlinux.org/show_bug.cgi?id=19293):
#BuildPreReq: python-module-magic > 5.0.0

Requires: python-module-matplotlib python-module-numpy

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

# HACK before we will have new python-module-magic (from file package) > 5.0.x
# https://bugzilla.altlinux.org/show_bug.cgi?id=19293
#%__subst "s|^\(import magic\)|\1\n		magic.MAGIC_NO_CHECK_TEXT = 0|g" src/setup.py
# Note! changed direct in the repo

%build
cd src
%python_build

%install
cd src
%python_install

%files
%doc docs/*
%_bindir/*
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info

%changelog
* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

