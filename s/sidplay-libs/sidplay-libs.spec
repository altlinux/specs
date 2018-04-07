# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ swig
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define spmajor 1
%define libname    libsidplay2_%{spmajor}
%define develname libsidplay2-devel
%define sumajor 0
%define libnamesu libsidutils%{sumajor}
%define bumajor 0
%define libnamebu libsidplay-builders%{bumajor}
%define develnamesu libsidutils-devel
%define staticdevelnamesu libsidutils-devel-static

Summary:        A Commodore 64 music player and SID chip emulator library
Name:           sidplay-libs
Version:        2.1.1
Release:        alt1_22
Source:         http://prdownloads.sourceforge.net/sidplay2/%{name}-%version.tar.bz2
Patch:		sidplay-libs-2.1.1-gcc4.3.patch
#gw from xsidplay 2.0.3
Patch1:		cia1.patch
Patch2:		sidplay-libs-2.1.1-builders-dir.patch
Patch3:         sidplay-libs-2.1.1-pkgconfig.patch
License:        GPLv2+
Group:          System/Libraries
URL:            http://sidplay2.sourceforge.net/
BuildRequires:  chrpath
Source44: import.info

%description
This is a cycle-based version of a C64 music playing library
developed by Simon White. This library provides no internal
SID emulation. Instead a means to drive any external SID hardware or
emulation has been provided using the SID Builder Classes.

A ReSID Builder Class using a modified version of ReSID 0.13
is included in this package. Alternative/updated classes can be
obtained from the SIDPlay2 homepage.

%package -n %libname
Summary:        A Commodore 64 music player and SID chip emulator library
Group:          System/Libraries
Obsoletes:	%{_lib}sidplay2 < %{version}-%{release}

%description -n %libname
This is a cycle-based version of a C64 music playing library
developed by Simon White. This library provides no internal
SID emulation. Instead a means to drive any external SID hardware or
emulation has been provided using the SID Builder Classes.

%package -n %libnamebu
Summary:        A Commodore 64 music player and SID chip emulator library
Group:          System/Libraries

%description -n %libnamebu
This is a cycle-based version of a C64 music playing library
developed by Simon White. This library provides no internal
SID emulation. Instead a means to drive any external SID hardware or
emulation has been provided using the SID Builder Classes.

A ReSID Builder Class using a modified version of ReSID 0.13
is included in this package. Alternative/updated classes can be
obtained from the SIDPlay2 homepage.

%package -n %develname
Summary:        Development headers and libraries for %{libname}
Group:          Development/C++
Requires:       %{libname} = %{version}
Requires:       %{libnamebu} = %{version}
Provides:       libsidplay-devel = %{version}-%release
Provides:	sidplay2-devel = %version-%release
Obsoletes:	%{_lib}sidplay2_1-devel < %version-%release

%description -n %develname
This package includes the header and library files necessary
for developing applications to use %{libname}.

%package -n %libnamesu
Summary:        General utility library for use in sidplayers
Requires:	%libname = %version
Group:          System/Libraries
%description -n %libnamesu
This library provides general utilities that are not considered core
to the C64 emulation.  Utilities include decoding and obtaining tune
lengths from the songlength database, INI file format parser and SID
filter files (types 1 and 2).

%package -n %develnamesu
Summary:        Development headers and libraries for libsidutils
Group:          Development/C++
Requires:       %libnamesu = %{version}
Requires:	%{develname} = %version
Provides:       libsidutils-devel = %{version}-%release
Obsoletes:	libsidutils0-devel

%description -n %develnamesu
This package includes the header and library files necessary
for developing applications to use %libnamesu.

%prep
%setup -q 
%patch -p1 -b .gcc
%patch1 -p1
%patch2 -p1
%patch3 -p1
autoreconf -fi -Iunix
pushd resid
autoreconf -fi
popd

%build
export CFLAGS="%optflags -fPIC"
export CXXFLAGS="%optflags -fPIC"
%configure --disable-static --enable-shared
%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete
rm -f %buildroot%_libdir/lib*.a
chrpath -d %buildroot%_libdir/libsidutils.so

echo #multiarch_includes %buildroot%_includedir/sidplay/sidconfig.h

%files -n %libname
%doc libsidplay/AUTHORS libsidplay/ChangeLog libsidplay/README libsidplay/TODO
%{_libdir}/libsidplay2.so.%{spmajor}
%{_libdir}/libsidplay2.so.%{spmajor}.*

%files -n %libnamebu
%_libdir/libresid-builder.so.%{bumajor}
%_libdir/libresid-builder.so.%{bumajor}.*
%_libdir/libhardsid-builder.so.%{bumajor}
%_libdir/libhardsid-builder.so.%{bumajor}.*


%files -n %develname
%{_includedir}/sidplay/*.h
%{_includedir}/sidplay/builders/*.h
#multiarch %multiarch_includedir/sidplay/
%{_libdir}/libsidplay2.so
%{_libdir}/libresid-builder.so
%{_libdir}/libhardsid-builder.so
%{_libdir}/pkgconfig/libsidplay*.pc

%files -n %libnamesu
%doc libsidutils/AUTHORS libsidutils/ChangeLog libsidutils/README libsidutils/TODO
%{_libdir}/libsidutils.so.%{sumajor}
%{_libdir}/libsidutils.so.%{sumajor}.*

%files -n %develnamesu
%dir %{_includedir}/sidplay/utils/
%{_includedir}/sidplay/utils/*
%{_libdir}/libsidutils*.so
%_libdir/pkgconfig/libsidutils*pc


%changelog
* Sat Apr 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_22
- new version

