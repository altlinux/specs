# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: libgnutls-devel
%add_optflags %optflags_shared
%define oldname obby
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libobby
Version:        0.4.8
Release:        alt2_15
Summary:        A library which provides synced document buffers

Group:          Development/Other
License:        GPLv2+
URL:            http://releases.0x539.de/obby
Source0:        http://releases.0x539.de/obby/%{oldname}-%{version}.tar.gz

BuildRequires:  libnet6-1.3-devel libgmp-devel libgmpxx-devel gettext-tools libasprintf-devel, libavahi-devel
Source44: import.info
Provides: obby = %{version}-%{release}

%description
libobby is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.


%package devel
Summary:        Development libraries for obby
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       pkg-config
Provides: obby-devel = %{version}-%{release}

%description devel
libobby is a library which provides synced document buffers. This package
contains the header files and library required to link against libobby.


%prep
%setup -n %{oldname}-%{version} -q


%build
%add_optflags -std=c++11
%configure --disable-static --enable-ipv6 --with-zeroconf
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %oldname

%files -f %{oldname}.lang
%doc README NEWS COPYING AUTHORS
%{_libdir}/*.so.*

%files devel
%{_includedir}/obby
%{_libdir}/pkgconfig/*
%{_libdir}/*.so


%changelog
* Fri Oct 27 2023 Igor Vlasenko <viy@altlinux.org> 0.4.8-alt2_15
- build with new libnet6-1.3-devel

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_12
- update to new release by fcimport

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_11
- new version

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_6
- update to new release by fcimport

* Thu May 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_5
- initial fc import

