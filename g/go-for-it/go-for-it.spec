%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define realname com.github.jmoerman.go-for-it

Name: go-for-it
Version: 1.9.6
Release: alt2
Summary: A stylish to-do list with built-in productivity timer
License: GPLv3
Group: Office
Url: https://github.com/JMoerman/Go-For-It

Source: %name-%version.tar

Source1000: %name.watch

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: pkgconfig(libpeas-1.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: libayatana-appindicator3-vala
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(granite)
BuildRequires: libgranite-vala
BuildRequires: libcanberra-vala

%description
GoForIt! is a simple and stylish productivity app, featuring a to-do list,
merged with a timer that keeps your focus on the current task.

%package devel
Summary: Development files for go-for-it
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides the development files for go-for-it.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev \
       -DAPP_SYSTEM_NAME:STRING="go-for-it" \
       -DUSE_GRANITE=1 \
       -DDEFAULT_PLUGINS:STRING="['launcherindicator', 'appindicator']"
%cmake_build

%install
%cmakeinstall_std
%find_lang %realname

%files -f %realname.lang
%doc AUTHORS README.md COPYING
%_bindir/*
%_libdir/*.so.*
%_libdir/%name
%_desktopdir/%realname.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/glib-2.0/schemas/%realname.gschema.xml
%_datadir/metainfo/%realname.appdata.xml
%_iconsdir/hicolor/*/apps/%realname.svg
%_iconsdir/hicolor/*/apps/%{realname}-symbolic.svg

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_datadir/vala/vapi/*.deps
%_datadir/vala/vapi/*.vapi

%changelog
* Wed Mar 12 2025 Nikolay Strelkov <snk@altlinux.org> 1.9.6-alt2
- Fixed FTBFS.
- Break BuildRequires to multiple lines.
- Compiled with support of Granite and Ayatana Indicator.

* Mon Jan 17 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.6-alt1
- Updated to upstream version 1.9.6.

* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.5-alt1
- Updated to upstream version 1.6.5.

* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.3-alt1
- Updated to upstream version 1.6.3.

* Sat Dec 19 2015 Konstantin Artyushkin <akv@altlinux.org> 1.4-alt2
- initial build for ALT Linux Sisyphus

