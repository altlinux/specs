%define module_name	 evdi
%define module_version 1.14.1
%define stage %nil
%define rel 63.33

%ifarch x86_64
%define dl_dir x64-ubuntu-1604
%endif
%ifarch %ix86
%define dl_dir x86-ubuntu-1604
%endif
%ifarch aarch64
%define dl_dir aarch64-linux-gnu
%endif
%ifarch armh
%define dl_dir arm-linux-gnueabihf
%endif

Name: displaylink-driver
Version: 5.8.0
Release: alt4.%rel
Summary: DisplayLink library and tools
Group: System/Kernel and hardware

URL: https://www.synaptics.com/products/displaylink-graphics/
License: Proprietary

Packager: L.A. Kostis <lakostis@altlinux.org>

ExclusiveArch: %ix86 x86_64 aarch64 armh

BuildRequires: libdrm-devel libusb
BuildRequires: libgomp-devel chrpath

Source1: %name-%version-%{stage}%{rel}.run
Source2: %module_name.modprobe
Source3: %name.service
Source4: %name.sleep.sh
Source5: %name-udev.sh
Source6: %name.rules

Requires: %name-firmware = %EVR
Obsoletes: lib%{module_name}0 lib%{module_name}1

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
BuildArch: noarch
Provides: kernel-source-%module_name = %module_version

%description -n kernel-source-%module_name-%module_version
%module_name modules sources for Linux kernel

%prep
%setup -T -c
sh %SOURCE1 --nodiskspace --noexec --keep --target . ||:
%setup -D -T

%build
tar -xf %{module_name}.tar.gz && pushd library
CFLAGS="%optflags" \
%make_build
popd

%install
%brp_strip_none %_bindir/DisplayLinkManager
%set_debuginfo_skiplist %_bindir/DisplayLinkManager

# TODO maybe create separate kernel-conf- package for this?
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/modprobe.d/%module_name.conf
mkdir -p %buildroot%_sysconfdir/modules-load.d
echo %module_name > %buildroot%_sysconfdir/modules-load.d/%module_name.conf

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
mkdir -p %buildroot{%_bindir,%_unitdir,%_udev_rulesdir,%_systemd_dir,%_datadir/%name,%_logdir/displaylink}
install -m0755 %dl_dir/DisplayLinkManager %buildroot%_bindir/

chrpath -d %buildroot%_bindir/DisplayLinkManager

install -m 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -pD -m 0755 %SOURCE4 %buildroot%_systemd_dir/system-sleep/displaylink.sh
install -m 0755 %SOURCE5 %buildroot%_bindir/
install -m 0644 %SOURCE6 %buildroot%_udev_rulesdir/99-displaylink.rules

# firmware files
install -m 0644 *.spkg %buildroot%_datadir/%name/

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%doc LICENSE 3rd_party_licences.txt
%_bindir/*
%_unitdir/*
%_sysconfdir/modprobe.d/%module_name.conf
%_sysconfdir/modules-load.d/%module_name.conf
%_udev_rulesdir/99-displaylink.rules
%_systemd_dir/system-sleep/displaylink.sh
%dir %attr(0700,root,root) %_logdir/displaylink
%_libdir/*.so*

%files firmware
%_datadir/%name

%files -n kernel-source-%module_name-%module_version
%_usrsrc/kernel/sources/kernel-source-%module_name-%module_version.tar.bz2

%changelog
* Sat Sep 16 2023 L.A. Kostis <lakostis@altlinux.ru> 5.8.0-alt4.63.33
- Use LD_PRELOAD instead of hacks (finally closes #47448).
- remove libevdi as DisplayLinkManager rely on exact library name
  (libevdi.so) so anyway correct soname transition not possible.
- udev.sh: use --no-block for starting the service (to reduce the
  boot time stall).

* Sat Sep 16 2023 L.A. Kostis <lakostis@altlinux.ru> 5.8.0-alt3.63.33
- move firmware files to _libdir due ugly libevdi requires.
- libevdi: bump sover.

* Fri Sep 15 2023 L.A. Kostis <lakostis@altlinux.ru> 5.8.0-alt2.63.33
- Don't run chrpath as it breaks DisplayLinkManager (first try).
- udev.rules: fix disable_u1_u2.
- evdi: added to modules-load.d.

* Tue Sep 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.8.0-alt1.63.33
- New release (5.8.0).
- Update evdi drivers version to 1.14.1.

* Wed Apr 26 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt1.61.129
- New release (5.7.0).
- Update evdi drivers version to 1.13.1.
- Update udev rules.

* Thu Aug 11 2022 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt1.59.184
- New release (5.6.1).
- Update evdi drivers version to 1.12.0.
- Update udev rules.

* Sun May 22 2022 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt1.59.176
- New release (5.6).
- Update evdi drivers version to 1.11.0.
- Update udev rules.

* Mon Mar 21 2022 L.A. Kostis <lakostis@altlinux.ru> 5.5.0-alt3.59.151
- New release (5.5).
- Update evdi drivers version to 1.10.1.
- Update udev.rules.

* Thu Feb 03 2022 L.A. Kostis <lakostis@altlinux.ru> 5.5.0-alt2.59.118
- Restrict access to logs directory.

* Sat Jan 29 2022 L.A. Kostis <lakostis@altlinux.ru> 5.5.0-alt1.59.118
- New beta release.
- Enable aarch64 support.
- Bump evdi version.

* Mon Nov 29 2021 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt4.55.174
- kernel-source: make package noarch.

* Fri Nov 26 2021 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt3.55.174
- Update udev script:
  + fix add/remove actions
  + code cleanups.

* Thu Nov 25 2021 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt2.55.174
- Add logdir.
- Add armh support.
- Improve udev and service scripts.
- Handle service changes.

* Mon Nov 22 2021 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt1.55.174
- Initial build for ALTLinux.
