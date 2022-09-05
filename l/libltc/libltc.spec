
%define _unpackaged_files_terminate_build 1
%define _customdocdir %_docdir/%name

Name:    libltc
Version: 1.3.2
Release: alt1
Summary: Linear/Longitudinal Time Code (LTC) Library

License: LGPLv3+
Group:   Sound
URL:     http://x42.github.io/libltc/

Source: %name-%version.tar
Patch1: libltc-1.1.2-fedora-multilib.patch

BuildRequires: doxygen

%description
Linear (or Longitudinal) Timecode (LTC) is an encoding of
SMPTE timecode data as a Manchester-Biphase encoded audio
signal. The audio signal is commonly recorded on a VTR track
or other storage media.

libltc provides functionality to encode and decode LTC audio
from/to SMPTE or EBU timecode, including SMPTE date support.


%package devel
Summary:  Development files for %name
Group:    Development/C
Requires: %name = %EVR

%description devel
This package contains the libraries and header files needed for
developing with %name.

%package docs
Summary: Developer's documentation for %name
Group:   Development/Documentation

%description docs
This package contains the documentation for %name.


%prep
%setup -q
%patch1 -p1

%build
%autoreconf
%configure
%make_build all dox

%install
%makeinstall_std
rm -f %buildroot%_libdir/libltc.{a,la}

%check
%make_build check

%files
%doc AUTHORS ChangeLog README.md
%_libdir/libltc.so.*

%files devel
%_libdir/libltc.so
%_includedir/ltc.h
%_pkgconfigdir/*
%_man3dir/*

%files docs
%doc doc/html


%changelog
* Mon Sep 05 2022 Ivan A. Melnikov <iv@altlinux.org> 1.3.2-alt1
- 1.3.2

* Thu Jun 03 2021 Ivan A. Melnikov <iv@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
