Name: librtmidi5
Version: 4.0.0
Release: alt2

Summary: Library for realtime MIDI input/output
License: MIT
Group: System/Legacy libraries
Url: https://github.com/thestk/rtmidi

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)

%define desc\
RtMidi is a set of C++ classes (RtMidiIn and RtMidiOut) that provides a common\
API (Application Programming Interface) for realtime MIDI input/output across \
Linux (ALSA & Jack), Macintosh OS X, Windows (Multimedia Library), and SGI \
operating systems. RtMidi significantly simplifies the process of interacting \
with computer MIDI hardware and software. It was designed with the following \
goals:\
* object oriented C++ design\
* simple, common API across all supported platforms\
* only two header files and one source file for easy inclusion in programming \
  projects\
* MIDI device enumeration

%description %desc
This package contains the shared library.

%prep
%setup

%build
%autoreconf
%configure --disable-static --with-alsa --with-jack

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/librtmidi.so.*

%changelog
* Wed Feb 21 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt2
- rebuilt as legacy library

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

