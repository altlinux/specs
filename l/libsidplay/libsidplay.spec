# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: libsidplay
Summary: SID chip music module playing library
Version: 1.36.60
Release: alt2_5
Source: http://home.arcor.de/ms2002sep/bak/%{name}-%{version}.tar.bz2
Patch0: libsidplay-1.36.57-opts.patch
Group: System/Libraries
URL: http://home.arcor.de/ms2002sep/bak/
License: GPLv2+
# Package is relocatable.
Prefix: %{_prefix}
Source44: import.info

%description
This library provides support for playing SID music modules originally
created on Commodore 64 and compatibles. It contains a processing engine
for MOS 6510 machine code and MOS 6581 Sound Interface Device (SID)
chip output. It is used by music player programs like SIDPLAY and
several plug-ins for versatile audio players.

Developers should consider switching to libsidplay version 2 or newer.


%package devel
Summary: Files needed for compiling programs that use libsidplay
Group: System/Libraries
Requires: libsidplay = %{version}-%{release}

%description devel
These are the files needed for compiling programs that use libsidplay.
Developers should consider switching to libsidplay version 2 or newer.


%prep
%setup -q
%patch0 -p1 -b .opts


%build
%configure --disable-static
make %{_smp_mflags}


%install
mkdir -p %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install


%files
%doc COPYING
%{_libdir}/libsidplay.so.*


%files devel
%doc AUTHORS DEVELOPER src/*.txt
%{_libdir}/libsidplay.so
%{_includedir}/sidplay/


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.36.60-alt2_5
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.36.60-alt2_4
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.36.60-alt2_3
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.36.60-alt1_3
- initial import by fcimport

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.36.59-alt1
- fix build with gcc 4.3 (thanks, Mandriva)

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 1.36.59-alt0.1
- initial build for ALT Linux Sisyphus

