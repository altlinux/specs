%define native iperf
%define abiversion 0

%define use_chrpath 1

Name: iperf3
Version: 3.17.1
Release: alt1

Summary: A TCP, UDP, and SCTP network bandwidth measurement tool
License: BSD-3-Clause and MIT
Group: Monitoring

Url: http://software.es.net/iperf
Source0: http://downloads.es.net/pub/iperf/%native-%version.tar.gz
Source1: iperf3.sysconfig
Source2: iperf3.init
Source3: iperf3.service

Requires: lib%name-%abiversion = %version-%release

%ifdef use_chrpath
BuildRequires: chrpath
%endif

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

%build

# fixed RPATH issue
# https://lists.altlinux.org/pipermail/community/2014-October/682803.html
%ifndef use_chrpath
libtoolize --copy --force --automake
aclocal -I config
autoheader
automake --foreign --add-missing --copy
autoconf
%endif

%configure
%make_build

%install
%makeinstall

rm -f %buildroot/%_libdir/*.a

install -pDm0644 %SOURCE1 %buildroot/%_sysconfdir/sysconfig/%name

install -pDm0755 %SOURCE2 %buildroot/%_initdir/%name
install -pDm0644 %SOURCE3 %buildroot/%_unitdir/%name.service

# fixed RPATH issue
%ifdef use_chrpath
chrpath -d %buildroot/%_bindir/iperf3
%endif

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%_mandir/man?/*
%_initdir/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc LICENSE README.md RELNOTES.md

%files -n lib%name-%abiversion
/%_libdir/lib%native.so.*

%files -n lib%name-devel
%_includedir/%{native}_api.h
%_libdir/lib%native.so

%changelog
* Thu Sep 26 2024 Sergey Y. Afonin <asy@altlinux.org> 3.17.1-alt1
- New version

* Mon Dec 04 2023 Sergey Y. Afonin <asy@altlinux.org> 3.16-alt1
- New version
- iperf3-3.10-idle-tcp-DoS.patch and iperf3-3.14-issue1554.patch
  isn't needed since 3.15

* Wed Aug 02 2023 Sergey Y. Afonin <asy@altlinux.org> 3.14-alt2
- Added patch for issue #1554 (ALT #47017)

* Tue Jul 18 2023 Sergey Y. Afonin <asy@altlinux.org> 3.14-alt1
- New version (ALT #46964, security fix)

* Sun Nov 06 2022 Sergey Y. Afonin <asy@altlinux.org> 3.12-alt1
- New version

* Sun Oct 31 2021 Sergey Y. Afonin <asy@altlinux.org> 3.10.1-alt1
- New version
- Switched to chrpath for remove RPATH
  (autoconf 2.71 is needed for reconfigure since 3.10.1)

* Wed Aug 19 2020 Sergey Y. Afonin <asy@altlinux.org> 3.9-alt1
- New version

* Wed Jul 22 2020 Sergey Y. Afonin <asy@altlinux.org> 3.8.1-alt1
- New version
- Removed Vcs tag (unsupported in p8 branch)
- Removed --disable-profiling (disabled by default in 3.8)

* Fri Apr 10 2020 Vitaly Chikunov <vt@altlinux.org> 3.7-alt4
- Further systemd iperf3.service hardening

* Mon Dec 09 2019 Vitaly Chikunov <vt@altlinux.org> 3.7-alt3
- Fix systemd iperf3.service type making it forking
- Systemd iperf3.service hardening
- Update package License

* Sat Aug 31 2019 Sergey Y. Afonin <asy@altlinux.org> 3.7-alt2
- added hack for fix DoS by arbitrary connection to tcp port
  (https://github.com/esnet/iperf/issues/788)

* Thu Aug 15 2019 Sergey Y. Afonin <asy@altlinux.org> 3.7-alt1
- New version
- disabled no-iperf3_profile.patch (--disable-profiling can be
  used since 3.7)

* Fri Aug 17 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.6-alt1
- New version
- disabled iperf3_profile building by external patch

* Wed Nov 15 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3-alt2
- do not build profiled iperf

* Tue Nov 14 2017 Sergey Y. Afonin <asy@altlinux.ru> 3.3-alt1
- New version

* Mon Jul 24 2017 Sergey Y. Afonin <asy@altlinux.ru> 3.2-alt1
- New version

* Fri Mar 17 2017 Sergey Y. Afonin <asy@altlinux.ru> 3.1.7-alt1
- New version

* Sat Jul 09 2016 Sergey Y. Afonin <asy@altlinux.ru> 3.1.3-alt1
- New version (CVE-2016-4303)

* Sat Feb 13 2016 Sergey Y. Afonin <asy@altlinux.ru> 3.1.2-alt1
- New version
- Added lsb init header (fixed repocop's warninig)

* Sat Nov 28 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.1.1-alt3
- removed listen port from $ARGS (5201 is default for iperf3)
- removed --displayname from start_daemon in init script

* Thu Nov 26 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.1.1-alt2
- Removed init and service files for udp service:
  one tcp daemon is serves all in Iperf3

* Thu Nov 26 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.1.1-alt1
- New version

* Thu Oct 09 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.0.8-alt1
- Initial build for ALTLinux
