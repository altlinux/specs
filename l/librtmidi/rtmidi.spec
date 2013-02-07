# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ gromacs-devel
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
%define oldname rtmidi
Name:       librtmidi
Version:    1.0.15
Release:    alt1_4.1
Summary:    Library for realtime MIDI input/output (ALSA support)
# Request to send in changes is considered optional.
License:    MIT
URL:        http://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:    http://www.music.mcgill.ca/~gary/rtmidi/release/%{oldname}-%{version}.tar.gz
# Build shared object, sent upstream via email 20111008
Patch0:     rtmidi-1.0.15-shared-linux-only.patch
BuildRequires:  libalsa-devel libjack-devel
BuildRequires:  autoconf /usr/bin/dos2unix
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

This package contains the RtMidi library compiled for ALSA support.

%package devel
Group: Development/C
Summary:    Development headers and libraries for rtmidi
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-jack%{?_isa} = %{version}-%{release}
Provides: rtmidi-devel = %{version}-%{release}

%description devel
Development headers and libraries for rtmidi.

%package jack
Group: Development/C
Summary:    Library for realtime MIDI input/output (JACK support)
Provides: rtmidi-jack = %{version}-%{release}

%description jack
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

This package contains the RtMidi library compiled for Jack support.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -b .shared
autoconf -f
# fix end of line
dos2unix doc/release.txt doc/doxygen/tutorial.txt
sed -i -e 's,$(LIBS) $(SOURCE),$(SOURCE) $(LIBS),' Makefile*

%build
# First pass, jack.
%configure --docdir=%{_docdir}/%{oldname}-devel-%{version} --with-jack
make
mv Makefile Makefile-jack

# Second pass, alsa
%configure --docdir=%{_docdir}/%{oldname}-devel-%{version}
make

%install
# First pass, jack.
make -f Makefile-jack install DESTDIR=%{buildroot}

# Second pass, alsa
make install DESTDIR=%{buildroot}

# Include the readme in non-devel packages
rm -f %{buildroot}%{_docdir}/%{oldname}-devel-%{version}/readme

%files
%doc readme
%{_libdir}/lib%{oldname}.so.*

%files devel
%{_docdir}/%{oldname}-devel-%{version}/
%{_includedir}/RtMidi.h
%{_includedir}/RtError.h
%{_libdir}/lib%{oldname}.so
%{_libdir}/lib%{oldname}-jack.so
%{_libdir}/pkgconfig/%{oldname}.pc
%{_libdir}/pkgconfig/%{oldname}-jack.pc

%files jack
%doc readme
%{_libdir}/lib%{oldname}-jack.so.*

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1_4.1
- initial fc import

