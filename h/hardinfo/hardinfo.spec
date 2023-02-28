Name: hardinfo
Version: 0.6
Release: alt0_0_git_3c42646

Epoch: 1
Summary: A system profiler for Linux
License: GPLv2+
Group: System/Kernel and hardware

Url: http://hardinfo.org
Source: %name-%version.tar
Patch0: 00-fix-cmake.patch
Patch1: 01-fix-impldecl.patch

BuildRequires(pre): cmake rpm-macros-cmake

BuildRequires: gcc-c++
BuildRequires: gettext-tools
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libgtk+3-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libdrm-devel
BuildRequires: libexpat-devel
BuildRequires: libpixman-devel
BuildRequires: libharfbuzz-devel
BuildRequires: desktop-file-utils
BuildRequires: libsoup-devel
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: libsensors3-devel

Requires: pciids
Requires: pciutils
Requires: usbutils

%description
HardInfo is a system profiler for Linux systems.
It can display information about the hardware, software,
and perform simple benchmarks.

%prep
%setup
%autopatch -p1

%build
%cmake -DHARDINFO_GTK3=on \
	-DHARDINFO_NOSYNC=1

%cmake_build

%install
%cmakeinstall_std
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
%_datadir/%name
%dir %_datadir/%name/doc
%doc %_datadir/%name/doc/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.*
%_desktopdir/%name.desktop

%changelog
* Tue Feb 28 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.6-alt0_0_git_3c42646
- Update from git commit 3c42646b196d4c5dc8466c4cdd1fb16538b7ff9a

* Sat Jun 04 2022 Anton Midyukov <antohami@altlinux.org> 0.6-alt2.20220113
- New snapshot
- Fix locale path (Closes: 42936)

* Sun Apr 11 2021 Anton Midyukov <antohami@altlinux.org> 0.6-alt1.20210404
- New snapshot

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

