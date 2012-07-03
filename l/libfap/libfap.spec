# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ glib2-devel imlib2-devel libXext-devel libfreetype-devel pkgconfig(freetype2) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libfap
Version:        1.3
Release:        alt1_1
Summary:        An APRS parser written in C

Group:          Communications
License:        GPL+ or Artistic
URL:            http://pakettiradio.net/libfap/
Source0:        http://pakettiradio.net/downloads/%{name}/%{version}/%{name}-%{version}.tar.gz
Source44: import.info

%description
libfap is an APRS (Amateur Packet Reporting System) parser that can decode
normal, mic-e and compressed location packets, NMEA location packets, 
objects, items, messages, telemetry and most weather packets.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING README THANKS licenses/*.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1
- initial import by fcimport

