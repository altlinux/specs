%define oldname librtmidi
Group: System/Legacy libraries
%add_optflags %optflags_shared
%define oldname rtmidi
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       librtmidi4
Version:    3.0.0
Release:    alt2_12
Summary:    Library for realtime MIDI input/output (ALSA support)
License:    MIT
URL:        http://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:    http://www.music.mcgill.ca/~gary/rtmidi/release/%{oldname}-%{version}.tar.gz
Patch0:     rtmidi-3.0.0-buildfix.patch
BuildRequires:  libalsa-devel, pkgconfig(jack)
BuildRequires:  autoconf, automake, libtool, /usr/bin/dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc-c++
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
Requires:   librtmidi4 = %{version}-%{release}
Requires:   pkgconfig(jack)
Provides: rtmidi-devel = %{version}-%{release}

%description devel
Development headers and libraries for rtmidi.

%prep
%setup -n %{oldname}-%{version} -q

%patch0 -p1

sed -i.orig -e 's/\/lib/\/%{_lib}/' Makefile.in rtmidi.pc.in
# fix end of line
dos2unix doc/release.txt doc/doxygen/tutorial.txt
sed -i -e 's,$(LIBS) $(SOURCE),$(SOURCE) $(LIBS),' Makefile*

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

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f




%files -n librtmidi4
%doc README.md
%{_libdir}/lib%{oldname}.so.*

%if 0
%files devel
%doc doc/html
%{_bindir}/%{oldname}-config
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/%{oldname}.pc
%endif

%changelog
* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt2_12
- compat library

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

