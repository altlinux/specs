%add_optflags %optflags_shared

Name: dcmtk
Version: 3.5.4
Release: alt3.1

Summary: DCMTK - DICOM Toolkit
License: MIT license
Group: Graphics
Url: http://dcmtk.org/dcmtk.php.en
Packager: Andrey Yurkovsky <anyr@altlinux.org>

# ftp://dicom.offis.de/pub/dicom/offis/software/dcmtk/dcmtk354/%name-%version.tar.gz
Source: %name-%version.tar
Patch: pdcmtk-r27.diff
Patch1: pdcmtk-3.5.4-alt-openssl.patch

Requires: lib%name = %version-%release
BuildPreReq: gcc-c++, zlib-devel, libpng-devel, libtiff-devel
BuildPreReq: libxml2-devel, libwrap-devel, libssl-devel

%description
DCMTK is a collection of libraries and applications implementing large parts 
the DICOM standard. It includes software for examining, constructing and 
converting DICOM image files, handling offline media, sending and receiving 
images over a network connection, as well as demonstrative image storage and 
worklist servers.

Contains patches against latest stable version from http://gna.org/projects/pdcmtk

%package -n lib%name
Summary: %name shared libraries
Group: System/Libraries

%description -n lib%name
%name shared libraries

%package -n lib%name-devel
Summary: Headers for building software that uses %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Headers for building software that uses %name.

%prep
%setup
%patch
%patch1 -p1

%build
%add_optflags -fPIC
%configure
make

%install
%makeinstall_std install-lib

%files
%_bindir/*
%_datadir/dcmtk/
%_docdir/*
%_man1dir/*
%config(noreplace) %_sysconfdir/*

%files -n lib%name
%_libdir/dcm2xml.dtd
%_libdir/dsr2xml.xsd

%files -n lib%name-devel
%_includedir/dcmtk/
%_libdir/*.a

%changelog
* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 3.5.4-alt3.1
- Fixed build with openssl-1.0.

* Fri Feb 05 2010 Andrey Yurkovsky <anyr@altlinux.org> 3.5.4-alt3
- added dcmtk headers

* Wed Nov 25 2009 Andrey Yurkovsky <anyr@altlinux.org> 3.5.4-alt2
- %_sysconfdir/* in spec changed to %%config %_sysconfdir/*

* Fri Nov 13 2009 Andrey Yurkovsky <anyr@altlinux.org> 3.5.4-alt1
- initial build
