%define oldname librtmidi
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: System/Legacy libraries
%add_optflags %optflags_shared
%define oldname rtmidi
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       librtmidi2
Version:    2.1.0
Release:    alt2_9
Summary:    Library for realtime MIDI input/output (ALSA support)
License:    MIT
URL:        http://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:    http://www.music.mcgill.ca/~gary/rtmidi/release/%{oldname}-%{version}.tar.gz
BuildRequires:  libalsa-devel, libjack-devel
BuildRequires:  autoconf-common, /usr/bin/dos2unix
Source44: import.info

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

%package devel
Group: Development/C
Summary:    Development headers and libraries for rtmidi
Requires:   %{name} = %{version}-%{release}
Provides: rtmidi-devel = %{version}-%{release}

%description devel
Development headers and libraries for rtmidi.

%prep
%setup -n %{oldname}-%{version} -q

# cp -f /usr/lib/rpm/config.{guess,sub} config/
sed -i -e 's/\/lib/\/%{_lib}/' Makefile.in librtmidi.pc.in
sed -i -e 's/RtError\.h//' Makefile.in
autoconf -f
# fix end of line
dos2unix doc/release.txt doc/doxygen/tutorial.txt
sed -i -e 's,$(LIBS) $(SOURCE),$(SOURCE) $(LIBS),' Makefile*

%build
# First pass, jack.
%configure --docdir=%{_docdir}/%{oldname}-devel --with-jack --with-alsa
make CFLAGS="$CXXFLAGS -fPIC"

%install
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_bindir} %{buildroot}%{_includedir}
sed -i -E 's/-L[^ "]+//' %{oldname}-config
make install PREFIX=%{buildroot}%{_prefix}

rm %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -p lib%{oldname}.pc %{buildroot}%{_libdir}/pkgconfig/
rm %{buildroot}%{_libdir}/*.a

rm -rf %buildroot%_bindir %buildroot%{_includedir} %buildroot%{_libdir}/pkgconfig %buildroot%{_libdir}/lib%{oldname}.so

%files
%doc readme
%{_libdir}/lib%{oldname}.so.*

%if 0
%files devel
%doc doc/*
%{_bindir}/%{oldname}-config
#{_docdir}/%{oldname}-devel/
%{_includedir}/RtMidi.h
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/lib%{oldname}.pc
%endif

%changelog
* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2_9
- legacy library

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

