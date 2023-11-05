Group: Development/C
%add_optflags %optflags_shared
%define oldname rtmidi
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       librtmidi
Version:    4.0.0
Release:    alt1_2
Summary:    Library for realtime MIDI input/output (ALSA support)
License:    MIT
URL:        https://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:    https://www.music.mcgill.ca/~gary/rtmidi/release/%{oldname}-%{version}.tar.gz
Patch1: rtmidi-pipewire-jack-buildfix.patch
BuildRequires:  libalsa-devel, pkgconfig(jack)
BuildRequires:  autoconf, automake, libtool, /usr/bin/dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc-c++
Obsoletes:  %{oldname}-jack < 2.0.0
Source44: import.info
Provides: rtmidi = %{version}-%{release}

%description
RtMidi is a set of C++ classes (RtMidiIn and RtMidiOut) that provides a common 
API (Application Programming Interface) for realtime MIDI input/output across 
Linux (ALSA & Jack), Macintosh OS X, Windows (Multimedia Library), and SGI 
operating systems. RtMidi significantly simplifies the process of interacting 
with computer MIDI hardware and software. It was designed with the following 
goals:
* object oriented C++ design
* simple, common API across all supported platforms
* only two header files and one source file for easy inclusion in programming 
  projects
* MIDI device enumeration

%package -n librtmidi5
Summary:        Shared library for the %oldname library
Group:          System/Libraries
Provides: rtmidi5 = %{version}-%{release}

%description -n librtmidi5
RtMidi is a set of C++ classes (RtMidiIn and RtMidiOut) that provides a common 
API (Application Programming Interface) for realtime MIDI input/output across 
Linux (ALSA & Jack), Macintosh OS X, Windows (Multimedia Library), and SGI 
operating systems. RtMidi significantly simplifies the process of interacting 
with computer MIDI hardware and software. It was designed with the following 
goals:
* object oriented C++ design
* simple, common API across all supported platforms
* only two header files and one source file for easy inclusion in programming 
  projects
* MIDI device enumeration

This package contains the shared library.

%package -n librtmidi-devel
Group: Development/C
Summary:    Development headers and libraries for rtmidi
Requires:   librtmidi5 = %EVR
Requires:   pkgconfig(jack)
Provides: %oldname-devel = %EVR
Provides: rtmidi-devel = %{version}-%{release}

%description -n librtmidi-devel
Development headers and libraries for rtmidi.

%prep
%setup -n %{oldname}-%{version} -q
%patch1 -p1

sed -i.orig -e 's/\/lib/\/%{_lib}/' Makefile.in rtmidi.pc.in
# fix end of line
dos2unix doc/release.txt doc/doxygen/tutorial.txt

%build
find . -name Makefile.in -delete
./autogen.sh --no-configure
%configure --docdir=%{_docdir}/%{oldname}-devel --with-jack --with-alsa
%make_build AM_DEFAULT_VERBOSITY=1

# Get rid of the -L/usr/lib in the output of this convenience script
sed -i -E 's/-L[^ "]+//' %{oldname}-config

%install
make DESTDIR=%{buildroot} install

install --verbose -D -t %{buildroot}%{_bindir} %{oldname}-config

rm %{buildroot}%{_libdir}/lib%{oldname}.{a,la}



%files -n librtmidi5
%doc README.md
%_libdir/librtmidi.so.5
%_libdir/librtmidi.so.5.*

%files -n librtmidi-devel
%doc doc/html
%{_bindir}/%{oldname}-config
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/%{oldname}.pc

%changelog
* Sun Nov 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.0.0-alt1_2
- NMU: fixed build with pipewire-jack

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_1
- new version

* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_12
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_9
- update to new release by fcimport

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2
- new version

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_9
- update to new release by fcimport

* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.15-alt2_9
- Rebuilt for new gcc abi.

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1_5.1
- update to new release by fcimport

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1_4.1
- initial fc import

