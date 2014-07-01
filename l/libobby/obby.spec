# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(net6-1.3) pkgconfig(sigc++-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname obby
Name:           libobby
Version:        0.4.8
Release:        alt1_7
Summary:        A library which provides synced document buffers

Group:          Development/C
License:        GPLv2+
URL:            http://releases.0x539.de/obby
Source0:        http://releases.0x539.de/obby/%{oldname}-%{version}.tar.gz

BuildRequires:  net6-devel libgmp-devel libgmp_cxx-devel gettext-devel libavahi-devel
Source44: import.info
Provides: obby = %{version}-%{release}

%description
libobby is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.


%package devel
Summary:        Development libraries for obby
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Provides: obby-devel = %{version}-%{release}

%description devel
libobby is a library which provides synced document buffers. This package
contains the header files and library required to link against libobby.


%prep
%setup -n %{oldname}-%{version} -q


%build
%configure --disable-static --enable-ipv6 --with-zeroconf
make %{?_smp_mflags}


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
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_6
- update to new release by fcimport

* Thu May 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_5
- initial fc import

