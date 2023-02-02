%def_disable check
%define xdg_name in.lsp_plug.lsp_plugins

Name: lsp-plugins
Version: 1.2.5
Release: alt1.1

Summary: Linux Studio Plugins
Group: Sound
License: LGPL-3.0
Url: https://lsp-plug.in/

Vcs: https://github.com/sadko4u/lsp-plugins
Source: https://github.com/sadko4u/%name/releases/download/%version/%name-src-%version.tar.gz

BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++
BuildRequires: lv2-devel libjack-devel ladspa_sdk
BuildRequires: libsndfile-devel libcairo-devel
BuildRequires: libGL-devel libXrandr-devel
BuildRequires: %_bindir/php

ExclusiveArch: %ix86 x86_64 aarch64 %e2k

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

%package -n jack-%name
Summary: LSP (Linux Studio Plugins) JACK plugins
Group: Sound

%description -n jack-%name
LSP (Linux Studio Plugins) JACK plugins.

%package -n ladspa-%name
Summary: LSP (Linux Studio Plugins) LADSPA plugins
Group: Sound

%description -n ladspa-%name
LSP (Linux Studio Plugins) LADSPA plugins.

%package -n lv2-%name
Summary: LSP (Linux Studio Plugins) LV2 plugins
Group: Sound

%description -n lv2-%name
LSP (Linux Studio Plugins) LV2 plugins.

%package -n vst-%name
Summary: LSP (Linux Studio Plugins) LinuxVST plugins
Group: Sound

%description -n vst-%name
LSP (Linux Studio Plugins) LinuxVST plugins.

%package doc
Summary: Documentation for LSP (Linux Studio Plugins) plugins
Group: Sound
BuildArch: noarch

%description doc
Documentation for LSP (Linux Studio Plugins) plugins.

%package devel
Summary: Headers for LSP (Linux Studio Plugins) plugins
Group: Development/C++
Requires: lv2-%name = %EVR

%description devel
This package provides headers for LSP-developers.

%prep
%setup -n %name
%ifarch %e2k
sed -i "s|VSTCALLBACK __cdecl|VSTCALLBACK|" \
	modules/lsp-3rd-party/include/steinberg/vst2.h
%endif

%build
export PLATFORM=Linux BUILD_SYSTEM=Linux
export VERSION=%version
%make PREFIX=%_prefix \
    LIBDIR=%_libdir \
    FEATURES="jack ladspa lv2 vst2 doc xdg" \
    CXXFLAGS_EXT="%optflags_default %(getconf LFS_CFLAGS)" \
    CFLAGS_EXT="%optflags_default %(getconf LFS_CFLAGS)" \
    config
%make_build VERBOSE=1

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.a

%check
%make check

%files -n jack-%name
%_bindir/*
%_libdir/liblsp-r3d-glx-lib*.so
%dir %_libdir/%name
%_libdir/%name/lib%name-jack-%version.so
%_desktopdir/%{xdg_name}_*.desktop
%_datadir/desktop-directories/%name.directory
%_xdgmenusdir/applications-merged/%name.menu
%_iconsdir/hicolor/*/apps/%name.*
%doc CHANGELOG* README*

%exclude %_pkgconfigdir/lsp-r3d-glx-lib.pc

%files -n ladspa-%name
%_libdir/ladspa/*
%doc CHANGELOG* README*

%files -n lv2-%name
%_libdir/lv2/*
%doc CHANGELOG* README*

%files -n vst-%name
%_libdir/vst/*
%doc CHANGELOG* README*

%files doc
%_defaultdocdir/%name/

%changelog
* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1.1
- fixed build for %e2k (mike@)

* Sun Jan 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Thu Dec 22 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1.1
- fixed build for %%e2k (mike@)

* Thu Jun 23 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu May 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Dec 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.31-alt1
- 1.1.31

* Mon Aug 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.30-alt2
- fixed build for %%e2k (ilyakurdyukov@)

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.30-alt1
- 1.1.30

* Tue Jan 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.29-alt1
- 1.1.29

* Mon Dec 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.28-alt1
- 1.1.28

* Thu Sep 17 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.26-alt1
- 1.1.26

* Thu Jul 16 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.24-alt1
- 1.1.24

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.21-alt1
- 1.1.21

* Mon Apr 20 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.19-alt1
- 1.1.19

* Sun Apr 05 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.17-alt1
- 1.1.17

* Sun Mar 29 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.15-alt1
- 1.1.15

* Sat Mar 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1.1.14-alt1
- 1.1.14

* Tue Dec 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.13-alt1
- 1.1.13
- removed rpath.patch

* Sun Dec 22 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.11-alt1
- 1.1.11
- enabled build for aarch64

* Wed Jul 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.10-alt1
- 1.1.10

* Thu Apr 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.9-alt1
- 1.1.9

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- 1.1.7

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- first build for Sisyphus

