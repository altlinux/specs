Name:    pcm
Version: 202405
Release: alt1

Summary: Intel Performance Counter Monitor (Intel PCM)
License: BSD-3-Clause
Group:   Other

Url: https://github.com/intel/pcm

ExclusiveArch: i586 x86_64

# Source-url: https://github.com/intel/pcm/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel

%description
Intel Performance Counter Monitor (Intel PCM) is an application 
programming interface (API) and a set of tools based on the API to 
monitor performance and energy metrics of Intel Core, Xeon, Atom 
and Xeon Phi processors. PCM works on Linux, Windows, Mac OS X,
FreeBSD, DragonFlyBSD and ChromeOS operating systems.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

rm -rv %buildroot%_datadir/licenses/
rm -rv %buildroot%_datadir/doc/PCM

%files
%doc README*
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
%_datadir/pcm/

%changelog
* Sat Jul 06 2024 Anton Palgunov <toxblh@altlinux.org> 202405-alt1
- new version 202405 (with rpmrb script)

* Wed Mar 20 2024 Anton Palgunov <toxblh@altlinux.org> 202403-alt1
- new version 202403 (with rpmrb script)

* Tue Feb 27 2024 Anton Palgunov <toxblh@altlinux.org> 202401-alt1
- new version 202401 (with rpmrb script)

* Sun Oct 29 2023 Anton Palgunov <toxblh@altlinux.org> 202307-alt1
- Initial build for Sisyphus
