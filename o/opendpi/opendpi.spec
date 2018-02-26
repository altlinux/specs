Name: opendpi
Version: 1.3.0
%define w_version 1.2
Release: alt1
Summary: OpenDPI is a software component for traffic classification based on deep packet inspection
Group: System/Libraries

URL: http://opendpi.org/
License: GPLv3

Source0: %name-%version.tar.gz
Source1: opendpi-netfilter-wrapper-%w_version.tar.gz
Patch: opendpi-netfilter-wrapper-1.1_2.6.35_v3.patch
Patch1: opendpi-netfilter-wrapper-1.1_2.6.36.patch

BuildRequires: iptables-devel >= 1.4.3 libpcap-devel

%description
OpenDPI is a software component for traffic classification based on deep packet inspection

%package -n iptables-%name
Summary: OpenDPI wrapper for iptables
License: GPLv3
Group: System/Libraries
Requires: iptables

%description -n iptables-%name
OpenDPI wrapper for iptables

%package -n lib%name
Summary: library for OpenDPI
License: GPLv3
Group: System/Libraries

%description -n lib%name
OpenDPI library

%package -n lib%name-devel
Summary: Headers for libOpenDPI
License: GPLv3
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Headers for libOpenDPI

%package demo
Summary: Demo for OpenDPI
License: GPLv3
Group: System/Libraries

%description demo
Demo for OpenDPI

%package -n kernel-source-%name
Summary: %name module sources
Group: Development/Kernel
BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description -n kernel-source-%name
%name addons module sources for Linux kernel

%prep
%setup -q
tar -xzf %SOURCE1 -C ../
rm -rf ../opendpi-netfilter-wrapper-%w_version/README
mv -f ../opendpi-netfilter-wrapper-%w_version/* .
rm -rf ../opendpi-netfilter-wrapper-%w_version

%patch -p2
%patch1 -p2

mkdir -p ../kernel-source-opendpi-%version
cp -r . ../kernel-source-opendpi-%version

%build
%autoreconf
%configure
%make_build

export OPENDPI_PATH=$(pwd)
%make -C wrapper/ipt

%install
%makeinstall_std

install -D wrapper/ipt/libxt_opendpi.so %buildroot/%_lib/iptables/libxt_opendpi.so

mkdir -p %kernel_srcdir
tar cjf %kernel_srcdir/kernel-source-%name-%version.tar.bz2 ../kernel-source-%name-%version

%files -n lib%name
%_libdir/*.so.*

%files -n iptables-%name
/%_lib/iptables/*.so

%files -n lib%name-devel
%doc README COPYING NEWS
%_libdir/*.so
%_includedir/lib%name-*

%files demo
%_bindir/*

%files -n kernel-source-%name
%kernel_src/*

%changelog
* Mon Aug 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1
- New version
- Remove all patches

* Sun Apr 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- Build for ALT
