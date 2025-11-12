%define sover_gig  13
%define sover_akai 0
Name: libgig
Version: 4.5.1
Release: alt1
Summary: Library for loading Gigasampler and DLS Level 1/2 files
License: GPLv2 and LGPLv2+
Group: Sound
URL: https://linuxsampler.org/
Source0: http://download.linuxsampler.org/packages/libgig-%{version}.tar.bz2
Patch0: libdir.patch

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
Provides: %name = %EVR

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
Requires: libakai%sover_akai = %EVR

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
%autopatch -p1
# Fix non-utf8 warnings
iconv --from=ISO-8859-1 --to=UTF-8 README > README.new
mv README.new README

%build
%autoreconf
%configure --disable-static
%make_build
make docs

%install
%makeinstall_std

find %buildroot -type f -name "*.la" -delete -print

%check
%make_build check

%files -n %name%sover_gig
%doc COPYING
%_libdir/%name.so.%sover_gig
%_libdir/%name.so.%sover_gig.*

%files -n libakai%sover_akai
%doc COPYING
%_libdir/libakai.so.%sover_akai
%_libdir/libakai.so.%sover_akai.*

%files -n %name-devel
%doc ChangeLog COPYING NEWS README
%_libdir/*.so
%_includedir/%name/
%_libdir/pkgconfig/*.pc

%files -n %name-tools
%doc ChangeLog COPYING NEWS README
%_bindir/*
%_man1dir/*.1*

%changelog
* Wed Nov 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.5.1-alt1
- 4.5.1

* Fri Jun 06 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.5.0-alt1
- 4.5.0
- place libraries to %%_libdir

* Mon Apr 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 4.4.1-alt1
- Initial build for ALT.
