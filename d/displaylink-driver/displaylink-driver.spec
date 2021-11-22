%define module_name	 evdi
%define module_version 1.9.1
%define sover 0
%define rel 55.174

Name: displaylink-driver
Version: 5.4.1
Release: alt1.%rel
Summary: DisplayLink library and tools
Group: System/Kernel and hardware

URL: https://www.synaptics.com/products/displaylink-graphics/
License: Proprietary

Packager: L.A. Kostis <lakostis@altlinux.org>

ExclusiveArch: %ix86 x86_64

BuildRequires: libdrm-devel libusb chrpath
Source1: %name-%version-%rel.run
Source2: %module_name.modprobe
Source3: %name.service
Source4: %name.sleep.sh
Source5: %name-udev.sh
Source6: %name.rules

Requires: %name-firmware = %EVR lib%{module_name}%{sover} = %EVR

%description
DisplayLink technology makes it simple to connect any display to any
computer that supports USB or Wi-Fi and provides universal solutions for a
range of corporate, home and embedded applications where easy connectivity of
displays enhances productivity.

%package firmware
Group: System/Kernel and hardware
Summary: %name firmware
BuildArch: noarch

%description firmware
Firmware files for %name.

%package -n kernel-source-%module_name-%module_version
Group: Development/Kernel
Summary: Linux %module_name modules sources
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildRequires: kernel-build-tools
Provides: kernel-source-%module_name = %module_version

%description -n kernel-source-%module_name-%module_version
%module_name modules sources for Linux kernel

%package -n lib%{module_name}%{sover}
Group: System/Libraries
Summary: %{module_name} support library
Provides: lib%{module_name}%{sover} = %module_version

%description -n lib%{module_name}%{sover}
%{module_name} support library

%prep
%setup -T -c
sh %SOURCE1 --nodiskspace --keep --target tmp ||:
mv tmp/* . && rm -rf tmp
%setup -D -T

%build
tar -xf %{module_name}.tar.gz && pushd library
CFLAGS="%optflags" \
%make_build
popd

%install
%brp_strip_none %_bindir/DisplayLinkManager
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/modprobe.d/%module_name.conf

# kernel-source install
mkdir -p {kernel-source-%module_name-%module_version,%buildroot%_usrsrc/kernel/sources}
install -m644 module/* kernel-source-%module_name-%module_version/
tar -c kernel-source-%module_name-%module_version | bzip2 -c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

# library
pushd library
%makeinstall DESTDIR=%buildroot LIBDIR=%_libdir
popd

# install scripts
mkdir -p %buildroot{%_bindir,%_unitdir,%_udev_rulesdir,%_systemd_dir,%_datadir/%name}
%ifarch x86_64
install -m 0755 x64-ubuntu-1604/DisplayLinkManager %buildroot%_bindir/
%else
install -m 0755 x86-ubuntu-1604/DisplayLinkManager %buildroot%_bindir/
%endif
chrpath -d %buildroot%_bindir/DisplayLinkManager
install -m 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -pD -m 0755 %SOURCE4 %buildroot%_systemd_dir/system-sleep/displaylink.sh
install -m 0755 %SOURCE5 %buildroot%_bindir/
install -m 0644 %SOURCE6 %buildroot%_udev_rulesdir/99-displaylink.rules

# firmware files
install -m 0644 *.spkg %buildroot%_datadir/%name/

%files
%doc LICENSE 3rd_party_licences.txt
%_bindir/*
%_unitdir/*
%_sysconfdir/modprobe.d/%module_name.conf
%_udev_rulesdir/99-displaylink.rules
%_systemd_dir/system-sleep/displaylink.sh

%files -n lib%{module_name}%{sover}
%_libdir/*.so*

%files firmware
%_datadir/%name

%files -n kernel-source-%module_name-%module_version
%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

%changelog
* Mon Nov 22 2021 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt1.55.174
- Initial build for ALTLinux.
