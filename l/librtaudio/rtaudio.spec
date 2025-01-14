%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%add_optflags %optflags_shared
%define oldname rtaudio
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%define soversion 7

Name: librtaudio
Version: 6.0.1
Release: alt1

Summary: Real-time Audio I/O Library
License: MIT
Group: System/Libraries
URL: http://www.music.mcgill.ca/~gary/rtaudio/
VCS: https://github.com/thestk/rtaudio

Source0: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libpulse-simple)

Patch: rtaudio-pipewire-jack.patch

%description
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:
* object-oriented C++ design.
* simple, common API across all supported platforms.
* allow simultaneous multi-api support.
* support dynamic connection of devices.
* provide extensive audio device parameter control.
* allow audio device capability probing.
* automatic internal conversion for data format, channel number compensation,
  (de)interleaving, and byte-swapping.

%package devel
Summary:  Development headers and libraries for rtaudio
Group: Development/C
Requires: %name%soversion = %EVR

%description devel
The %name-devel package contains development files for %name.

%package -n %name%soversion
Summary: Real-time Audio I/O Library
Group: System/Libraries

%description -n %name%soversion
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:
* object-oriented C++ design.
* simple, common API across all supported platforms.
* allow simultaneous multi-api support.
* support dynamic connection of devices.
* provide extensive audio device parameter control.
* allow audio device capability probing.
* automatic internal conversion for data format, channel number compensation,
  (de)interleaving, and byte-swapping.

%prep
%setup
%patch -p1

%build
%autoreconf
export CFLAGS="%optflags -fPIC"
%configure --with-jack --with-alsa --with-pulse --enable-shared --disable-static --verbose
%make_build

%install
%makeinstall_std

%files -n %name%soversion
%doc README.* LICENSE doc/release.txt
%_libdir/lib%oldname.so.*

%files devel
%doc doc/images
%_includedir/%oldname/*.h
%_libdir/lib%oldname.so
%_libdir/pkgconfig/%oldname.pc

%changelog
* Mon Dec 09 2024 Denis Rastyogin <gerben@altlinux.org> 6.0.1-alt1
- Updated to 6.0.1.

* Sun Nov 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 5.2.0-alt1_2
- NMU: fixed FTBFS with pipewire-jack

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.2.0-alt1_1
- update to new release by fcimport

* Sat Oct 12 2019 Michael Shigorin <mike@altlinux.org> 5.0.0-alt2_2
- E2K: strip UTF-8 BOM for lcc < 1.24

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_11
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_5
- update to new release by fcimport

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_4
- fc update

* Mon Jan 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_3
- initial fc import

