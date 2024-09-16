%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:    pcm
Version: 202405
Release: alt2

Summary: Intel Performance Counter Monitor (Intel PCM)
License: BSD-3-Clause
Group:   Monitoring

Url: https://github.com/intel/pcm

ExclusiveArch: %ix86 x86_64

# Source-url: https://github.com/intel/pcm/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libsimdjson-devel
BuildRequires: libstdc++-devel

%description
Intel Performance Counter Monitor (Intel PCM) is an application
programming interface (API) and a set of tools based on the API to
monitor performance and energy metrics of Intel Core, Xeon, Atom
and Xeon Phi processors. PCM works on Linux, Windows, Mac OS X,
FreeBSD, DragonFlyBSD and ChromeOS operating systems.

%prep
%setup
# Our compiler has this enabled, and redefining it produces a warning.
sed -i s/-D_FORTIFY_SOURCE=1// CMakeLists.txt

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLINUX_SYSTEMD=TRUE
%cmake_build

%install
%cmake_install

rm -rv %buildroot%_datadir/licenses/
rm -rv %buildroot%_datadir/doc/PCM

%post
%post_systemd pcm-sensor-server

%preun
%preun_systemd pcm-sensor-server

%files
%doc README* LICENSE doc/*.md
%_bindir/pcm-client
%_sbindir/pcm
%_sbindir/pcm-accel
%_sbindir/pcm-bw-histogram
%_sbindir/pcm-core
%_sbindir/pcm-daemon
%_sbindir/pcm-iio
%_sbindir/pcm-latency
%_sbindir/pcm-lspci
%_sbindir/pcm-memory
%_sbindir/pcm-mmio
%_sbindir/pcm-msr
%_sbindir/pcm-numa
%_sbindir/pcm-pcicfg
%_sbindir/pcm-pcie
%_sbindir/pcm-power
%_sbindir/pcm-raw
%_sbindir/pcm-sensor
%_sbindir/pcm-sensor-server
%_sbindir/pcm-tpmi
%_sbindir/pcm-tsx
%_unitdir/pcm-sensor-server.service
%_datadir/pcm/

%changelog
* Sat Sep 14 2024 Vitaly Chikunov <vt@altlinux.org> 202405-alt2
- spec: Build with simdjson.
- spec: Enable building debuginfo.
- spec: Fix LFS support on i586.
- spec: Fix build time hardening-related warnings.
- spec: Enable additional brp QA checks.
- spec: Change Group from Other to Monitoring.
- spec: Install systemd pcm-sensor-server unit.

* Sat Jul 06 2024 Anton Palgunov <toxblh@altlinux.org> 202405-alt1
- new version 202405 (with rpmrb script)

* Wed Mar 20 2024 Anton Palgunov <toxblh@altlinux.org> 202403-alt1
- new version 202403 (with rpmrb script)

* Tue Feb 27 2024 Anton Palgunov <toxblh@altlinux.org> 202401-alt1
- new version 202401 (with rpmrb script)

* Sun Oct 29 2023 Anton Palgunov <toxblh@altlinux.org> 202307-alt1
- Initial build for Sisyphus
