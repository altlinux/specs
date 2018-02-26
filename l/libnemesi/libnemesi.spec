%add_optflags %optflags_shared
%define git 20110215

Summary: RTSP/RTP client library
Name: libnemesi
Version: 0.7.0
Release: alt3_0.2.20110215git
License: LGPLv2+
Group: Development/C
%if %{?git:1}0
# http://cgit.lscube.org/cgit.cgi/libnemesi/snapshot/libnemesi-0.6.tar.gz
Source0: libnemesi-%{version}-%{git}.tar.bz2
%else
Source0: http://www.lscube.org/files/downloads/libnemesi/%{name}-%{version}-rc2.tar.bz2
%endif
URL: http://www.lscube.org/projects/libnemesi
BuildRequires: liblksctp-devel
BuildRequires: netembryo-devel >= 0.1.1
Source44: import.info


%description
Libnemesi let you add multimedia streaming playback in your applications in
a quick and straightforward way. This software, derived from the experience
matured with NeMeSi is fully compliant with IETF's standards for real-time
streaming of multimedia contents over Internet. libnemesi implements RTSP a..
Real-Time Streaming Protocol (RFC2326) and RTP/RTCP a.. Real-Time Transport
Protocol/RTP Control Protocol (RFC3550) supporting the RTP Profile for
Audio and Video Conferences with Minimal Control (RFC3551).

The library provides two different API:

    * high level: the simplest abstraction to get the demuxed streams out
      of a resource uri
    * low level: provides access to all the rtp, rtcp, rtsp primitives in
      order to develop advanced applications.

Libnemesi leverages the netembryo network support and provides hooks to
register custom depacketizers (rtp parsers) to have a good compromises
between ease of use and flexibility.

%package devel
Summary: Nemesi development library and headers
Group: Development/C
Requires: libnemesi = %{version}-%{release}

%description devel
The libnemesi-devel package contains the header files and some
documentation needed to develop application with libnemesi.

%package tools
Summary: Simple dump/info programs that use libnemesi
Group: Sound

%description tools
Simple programs that use libnemesi to show network streams' information
and dump them.

%prep
%setup -q

#Bug in upstream configure option
sed -i -e 's/-Werror=return-type//g' configure configure.ac

%build
%configure \
 --disable-dependency-tracking \
 --disable-static \
 --enable-errors=none \
 --program-prefix=nemesi_ \

%if %{!?git:1}0
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%endif
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install
%{__rm} %{buildroot}%{_libdir}/libnemesi.la

#Remove installed docs
%{__rm} -r %{buildroot}/%{_docdir}/%{name}

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/libnemesi.so.*

%files devel
%doc CodingStyle
%{_includedir}/nemesi
%{_libdir}/libnemesi.so
%{_libdir}/pkgconfig/libnemesi.pc

%files tools
%{_bindir}/nemesi_dump_info
%{_bindir}/nemesi_dump_stream
%{_bindir}/nemesi_loop_stream

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt3_0.2.20110215git
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_0.2.20110215git
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_0.1.20110215git
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_0.1.20110215git
- initial import by fcimport

