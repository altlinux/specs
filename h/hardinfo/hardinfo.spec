Name: hardinfo
Version: 0.6
Release: alt0.1.alpha.gitb2991d7

Summary: A system profiler for Linux
License: GPLv2+
Group: System/Kernel and hardware

Url: http://hardinfo.org
Source: %name-%version.tar
Patch0: 00-fix-cmake.patch
Patch1: 01-fix-impldecl.patch
Packager: Leonid Krivoshein <klark@altlinux.org>

BuildRequires(pre): cmake rpm-macros-cmake

BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libgtk+2-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libdrm-devel
BuildRequires: libexpat-devel
BuildRequires: libpixman-devel
BuildRequires: libharfbuzz-devel
BuildRequires: desktop-file-utils
BuildRequires: libsoup-devel

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

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Settings;HardwareSettings;" \
  --dir %buildroot%_desktopdir %buildroot%_desktopdir/%name.desktop

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_libdir/%name/modules/*so
%dir %_datadir/%name
%dir %_datadir/%name/pixmaps
%_datadir/%name/pixmaps/*
%_datadir/%name/benchmark.conf
%_datadir/%name/benchmark.data
%dir %_datadir/%name/doc
%doc %_datadir/%name/doc/*
%_man1dir/%name.*
%_desktopdir/%name.desktop

%changelog
* Thu Sep 07 2017 Leonid Krivoshein <klark@altlinux.org> 0.6-alt0.1.alpha.gitb2991d7
- New alpha version 0.6alpha, thanks Mike Radyuk <torabora@altlinux.org>.
- Repacked upstream sources tree for Sisyphus (ALT: #33806).
- Add patches for suppress implicit declaration warnings.

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.5.1-alt2
- added debian patch to fix FTBFS (see bdo#757525)

* Mon Nov 03 2014 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- initial build for ALT Linux Sisyphus
  + based on mageia's 0.5.1-8.mga5 (spec) and rosa's 0.5.1-6 (patches)
  + fixed broken linking

