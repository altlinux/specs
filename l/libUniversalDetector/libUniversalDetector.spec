Name:       libUniversalDetector
Version:    10.9
Release:    alt1
License:    LGPLv2
Source:     %name-%version.tar.gz
# wget --content-disposition https://codeload.github.com/MacPaw/universal-detector/tar.gz/refs/heads/master
Group:      Development/Objective-C
Summary:    A library for character set autodetection
URL:        https://github.com/MacPaw/universal-detector

# Automatically added by buildreq on Wed Aug 25 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgnustep-base libobjc-devel libp11-kit libstdc++-devel python3-base sh4
BuildRequires: gcc-c++ gcc-objc gnustep-base-devel python3

%description
Universal Detector is a library for character set autodetection.

%package devel-static
Summary:    %summary, development files
Group:      Development/Objective-C
%description devel-static
Universal Detector is a library for character set autodetection.

This is an Objective-C wrapper for universalchardet by Mozilla
It is used by XADMaster library for filenames encoding detection


This is an Objective-C wrapper for universalchardet by Mozilla
It is used by XADMaster library for filenames encoding detection

%prep
%setup

%build
%make_build -f Makefile.linux

%install
install -D libUniversalDetector.a %buildroot/%_libdir/libUniversalDetector.a
install -D UniversalDetector.h  %buildroot/%_includedir/UniversalDetector.h

%check
./DetectorTest

%files devel-static
%doc *.md
%_libdir/*
%_includedir/*

%changelog
* Wed Aug 25 2021 Fr. Br. George <george@altlinux.ru> 10.9-alt1
- Initial build for ALT
