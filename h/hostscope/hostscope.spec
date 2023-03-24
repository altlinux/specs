Name: hostscope
Version: 8.0
Release: alt1

Summary: System monitoring tool for multiple hosts
License: GPLv3
Group: Monitoring
Url: https://www.maier-komor.de/hostscope.html

Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %{name}-V%{version}.tar
Patch: %{name}-alt.patch

BuildRequires: gcc-c++ libncurses-devel wfc

%description
HostScope displays key system metrics of Linux hosts, such as detailed CPU
load, speed and temperature, I/O rates of network interfaces, I/O rates of
disks, and user process summary information. All metrics are multicast on the
LAN, if wanted, and clients can switch between multiple hosts on the network.

%prep
%setup -n %{name}-V%{version}
%patch -p2

%build
%autoreconf
%configure
%make_build

%install
mkdir -p %buildroot{%_sysconfdir,%_man1dir}
make install PREFIX=%buildroot%_prefix
cp -a %name.1 %buildroot%_man1dir/
cp -a %name.conf %buildroot%_sysconfdir/

%files
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/%name
%_sbindir/%{name}*
%_man1dir/*

%changelog
* Fri Mar 24 2023 L.A. Kostis <lakostis@altlinux.ru> 8.0-alt1
- Initial build for ALTLinux.
