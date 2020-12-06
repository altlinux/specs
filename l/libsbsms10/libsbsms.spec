%define major 10

Summary: C++ library for subband sinusoidal modeling time stretching and pitch scaling
Name: libsbsms%major
Version: 2.0.2
Release: alt4
License: GPLv2
Group: System/Libraries
URL: http://sbsms.sourceforge.net/
Source0: %name-%version.tar

Patch1: DEBIAN-set-library-version.patch
Patch2: ALT-e2k-fft.patch
Patch3: GENTOO-cflags.patch
Patch4: ALT-audacity-bug-955.patch
Patch5: ALT-audacity-bug-1808.patch
# Required for --enable-multithreaded
# https://bugzilla.audacityteam.org/show_bug.cgi?id=2492
Patch6:	ALT-audacity-bug-2492.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(sndfile)

%description
C++ library for subband sinusoidal modeling time stretching and pitch scaling

%package -n libsbsms-devel
Summary: Development files of C++ library for subband sinusoidal modeling time stretching and pitch scaling
Group: Development/C++
Requires: %name = %EVR

%description -n libsbsms-devel
Development files of the C++ library for subband sinusoidal modeling time stretching and pitch scaling
#--------------------------------------

%prep
%setup

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p3
%patch5 -p3
%patch6 -p3

%build
# for multithreading
export LIBS="-lpthread"
%autoreconf

%configure \
	--enable-shared \
	--disable-static \
%ifarch %ix86 x86_64 %e2k
	--enable-sse \
%else
	--disable-sse \
%endif
	--enable-multithreaded
	
%make_build

%install
%makeinstall_std
#--------------------------------------

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_libdir/libsbsms.so.%{major}
%_libdir/libsbsms.so.%{major}.*

%files -n libsbsms-devel
%_pkgconfigdir/*.pc
%_includedir/*
%_libdir/libsbsms.so

#--------------------------------------
%changelog
* Sun Dec 06 2020 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0.2-alt4
- Fixed and enabled multithreded processing
  https://bugzilla.audacityteam.org/show_bug.cgi?id=2492

* Sun Nov 24 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0.2-alt3
- Port from Audacity commit df1d9a0: ALT-audacity-bug-1808.patch
- Some spec clean up

* Sun Dec 02 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0.2-alt2
- Port from Audacity commit 954bb0f: ALT-audacity-bug-955.patch

* Wed Nov 07 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0.2-alt1
- Initial build for ALT Linux (version 2.0.2)
