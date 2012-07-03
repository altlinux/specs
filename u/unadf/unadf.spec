Summary: unzip like for .adf files (Amiga devices dumps)
Name: unadf
Version: 0.7.12
Release: alt1
URL: http://lclevy.free.fr/adflib
Source0: http://lclevy.free.fr/adflib/adflib-%version.tar.bz2
Patch: %name-doublecomm-alt.patch
License: GPL
Group: Archiving/Other
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Nov 04 2010
BuildRequires: gcc-c++

%description
unzip like for .adf files (Amiga devices dumps)
powered by ADFLib

%package -n libadf
Summary: unzip like for .adf files (Amiga devices dumps) -- the library
License: GPL
Group: Development/C

%description -n libadf
The ADFlib is a portable C library designed to manage Amiga formatted devices like harddisks and ZIP disks, or dump files of this kind of media via the .ADF format.

%package -n libadf-devel
Summary: unzip like for .adf files (Amiga devices dumps) -- development suite
License: GPL
Group: Development/C

%description -n libadf-devel
Development suite for ADFLib

%prep
%setup -n adflib-%version
#patch -p1

%build
%autoreconf
%configure --includedir=%_includedir/adflib
%make_build

%install
#mkdir -p %buildroot%_bindir %buildroot%_libdir %buildroot%_includedir/%name %buildroot%_datadir/libadf
#install Demo/%name %buildroot%_bindir/
#install Lib/libadf.a %buildroot%_libdir/
#install Lib/*.h %buildroot%_includedir/%name/
%makeinstall
mkdir -p %buildroot%_datadir/libadf
cp -rp boot %buildroot%_datadir/libadf
mkdir -p %buildroot%_includedir/adflib
mv %buildroot%_includedir/*.* %buildroot%_includedir/adflib

%files
%_bindir/%name
%doc README

%files -n libadf
%_libdir/libadf.so.*
%dir %_datadir/libadf
%dir %_datadir/libadf/boot
%_datadir/libadf/boot/*

%files -n libadf-devel
%doc %_datadir/doc/adflib
%dir %_includedir/adflib
%_includedir/adflib/*
%_libdir/lib*
%_pkgconfigdir/*
%exclude %_libdir/libadf.so.*

%changelog
* Thu Nov 04 2010 Fr. Br. George <george@altlinux.ru> 0.7.12-alt1
- Version up

* Tue Oct 13 2009 Fr. Br. George <george@altlinux.ru> 0.7.11-alt2
- Test rebuild failure fix

* Wed May 28 2008 Fr. Br. George <george@altlinux.ru> 0.7.11-alt1
- Initial build from scratch

* Sat Jan 20 2007 Laurent Clevy <lclevy@club-internet.fr> 1.0:
  - stable version of unadf

