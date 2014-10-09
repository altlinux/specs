%define native iperf
%define abiversion 0

Name: iperf3
Version: 3.0.8
Release: alt1

Summary: A TCP, UDP, and SCTP network bandwidth measurement tool
License: %bsd
Group: Monitoring

Url: http://software.es.net/iperf
Source0: http://downloads.es.net/pub/iperf/%native-%version.tar.gz
Source1: iperf3-tcp.init
Source2: iperf3-udp.init
Source3: iperf3.sysconfig
Source4: iperf3-tcp.service
Source5: iperf3-udp.service

# Milestone-future Milestone-3.1a1
Patch100: iperf-3.0.8-pidfile.patch

BuildRequires: rpm-build-licenses

Requires: lib%name-%abiversion = %version-%release

%package -n lib%name-%abiversion
Summary: iperf shared library
Group: System/Libraries
Provides: lib%name = %version-%release

%package -n lib%name-devel
Summary: iperf's development files
Group: Development/C
Requires: lib%name-%abiversion = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description
iperf is a tool for active measurements of the maximum achievable
bandwidth on IP networks.  It supports tuning of various parameters
related to timing, protocols, and buffers.  For each test it reports
the bandwidth, loss, and other parameters.

This version, sometimes referred to as iperf3, is a redesign of an
original version developed at NLANR/DAST.  iperf3 is a new
implementation from scratch, with the goal of a smaller, simpler code
base, and a library version of the functionality that can be used in
other programs. iperf3 also a number of features found in other tools
such as nuttcp and netperf, but were missing from the original iperf.
These include, for example, a zero-copy mode and optional JSON output.

Note that iperf3 is NOT backwards compatible with the original iperf.

%description -n lib%name-%abiversion
Librairies for iperf3

%description -n lib%name-devel
This package contains development files of iperf3

%prep
%setup -q -n %native-%version

%patch100 -p1

%build

# fixed RPATH issue
libtoolize --copy --force --automake
aclocal -I config
autoheader
automake --foreign --add-missing --copy
autoconf

%configure
%make_build

%install
%makeinstall

rm -f %buildroot/%_libdir/*.a

install -pDm0755 %SOURCE1 %buildroot/%_initdir/%name-tcp
install -pDm0755 %SOURCE2 %buildroot/%_initdir/%name-udp

install -pDm0644 %SOURCE4 %buildroot/%_unitdir/%name-tcp.service
install -pDm0644 %SOURCE5 %buildroot/%_unitdir/%name-udp.service

install -pDm0644 %SOURCE3 %buildroot/%_sysconfdir/sysconfig/%name

%post
%post_service %name-tcp
%post_service %name-udp

%preun
%preun_service %name-tcp
%preun_service %name-udp


%files
%_bindir/*
%_mandir/man?/*
%_initdir/%name-*
%_unitdir/%name-*.service
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc AUTHORS LICENSE README.md RELEASE_NOTES

%files -n lib%name-%abiversion
/%_libdir/lib%native.so.*

%files -n lib%name-devel
%_includedir/%{native}_api.h
%_libdir/lib%native.so


%changelog
* Thu Oct 09 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.0.8-alt1
- Initial build for ALTLinux
