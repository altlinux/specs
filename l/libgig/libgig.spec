%define sover_gig  11
%define sover_akai 0
Name: libgig
Version: 4.4.1
Release: alt1
Summary: Library for loading Gigasampler and DLS Level 1/2 files
License: GPLv2 and LGPLv2+
Group: Sound
URL: https://linuxsampler.org/
Source0: http://download.linuxsampler.org/packages/libgig-%{version}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: pkgconfig(sndfile) >= 1.0.2
BuildRequires: pkgconfig(uuid)

%description
C++ library for accessing Gigasampler/GigaStudio, DLS,
SoundFont and KORG sound files.

%package -n %name%sover_gig
Summary: Library for loading Gigasampler and DLS Level 1/2 files
Group: System/Libraries

%description -n %name%sover_gig
C++ library for loading Gigasampler and DLS Level 1/2 files.

%package -n libakai%sover_akai
Summary: Library for accessing AKAI disk images
Group: System/Libraries

%description -n libakai%sover_akai
C++ library for accessing AKAI disk images

%package -n %name-devel
Summary: Library for loading Gigasampler and DLS Level 1/2 files
Group: Development/C++
Requires: %name%sover_gig = %EVR

%description -n %name-devel
C++ library for loading Gigasampler and DLS Level 1/2 files.

%package -n %name-tools
Summary: Example applications for libgig
Group: Sound
Requires: %name%sover_gig = %EVR
Provides: libgig6-tools = %EVR
Obsoletes: libgig6-tools < %EVR

%description -n %name-tools
Some example applications for the libgig package.

* gigdump: demo app that prints out the content of a .gig file
* gigextract: extracts samples from a .gig file
* dlsdump: demo app that prints out the content of a DLS file
* rifftree: tool that prints out the RIFF tree of an arbitrary RIFF file

%prep
%setup

%build
%configure --disable-static
%make_build
make docs

%install
%makeinstall_std

find %buildroot -type f -name "*.la" -delete -print

mkdir -p %buildroot%_sysconfdir/ld.so.conf.d/
echo "%_libdir/libgig"  > "%buildroot%_sysconfdir/ld.so.conf.d/libgig%sover_gig.conf"
echo "%_libdir/libakai" > "%buildroot%_sysconfdir/ld.so.conf.d/libakai%sover_akai.conf"

%check
%make_build check

%files -n %name%sover_gig
%doc AUTHORS ChangeLog NEWS README TODO COPYING
%dir %_libdir/%name/
%_libdir/%name/%name.so.%sover_gig
%_libdir/%name/%name.so.%sover_gig.*
%config %_sysconfdir/ld.so.conf.d/%name%sover_gig.conf

%files -n libakai%sover_akai
%doc AUTHORS ChangeLog NEWS README TODO COPYING
%_libdir/%name/libakai.so.%sover_akai
%_libdir/%name/libakai.so.%sover_akai.*
%config %_sysconfdir/ld.so.conf.d/libakai%sover_akai.conf

%files -n %name-devel
%doc COPYING
%_libdir/%name/*.so
%_includedir/%name/
%_libdir/pkgconfig/*.pc

%files -n %name-tools
%doc AUTHORS ChangeLog NEWS README TODO COPYING
%_bindir/*
%_man1dir/*.1*

%changelog
* Mon Apr 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.4.1-alt1
- Initial build for ALT.
