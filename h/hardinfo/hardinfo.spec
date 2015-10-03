Name: hardinfo
Version: 0.5.1
Release: alt2

Summary: A system profiler for Linux
License: GPLv2+
Group: System/Kernel and hardware

Url: http://wiki.hardinfo.org/HomePage
Source: http://download.berlios.de/hardinfo/%name-%version.tar.bz2
Patch0: 01-truncated_description.patch
Patch1: 02-fix-distro-crash.patch
Patch2: 03-detect-lxde.patch
Patch3: 04-fix-usb.patch
Patch4: 05-fix-sensors-output.patch
Patch10: hardinfo-0.5.1-alt-makefile.patch
Patch11: hardinfo-0.5.1-debian-makefile.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pciutils
BuildRequires: libsoup-devel
BuildRequires: libgtk+2-devel
BuildRequires: zlib-devel
BuildRequires: libffi-devel
BuildRequires: libffi-devel
BuildRequires: desktop-file-utils
#BuildRequires: pkgconfig(usbutils)

Requires: pciids
Requires: pciutils
Requires: usbutils

%description
HardInfo is a system profiler for Linux systems.
It can display information about the hardware, software,
and perform simple benchmarks.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch10 -p1
%patch11 -p1

%build
%configure
%make_build

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Settings;HardwareSettings;" \
  --dir %buildroot%_desktopdir %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_libdir/%name/modules/*so
%_datadir/%name/pixmaps/*
%_datadir/%name/benchmark.conf
%_datadir/%name/benchmark.data
%_desktopdir/%name.desktop

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.5.1-alt2
- added debian patch to fix FTBFS (see bdo#757525)

* Mon Nov 03 2014 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- initial build for ALT Linux Sisyphus
  + based on mageia's 0.5.1-8.mga5 (spec) and rosa's 0.5.1-6 (patches)
  + fixed broken linking

