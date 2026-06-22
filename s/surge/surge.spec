Name: surge
Version: 1.3.4
Release: alt3

Summary: Hybrid synthesizer
License: GPLv3
Group: Sound
Url: https://github.com/surge-synthesizer/surge

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++ rack-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(luajit)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%package -n surge-xt
Summary: Standalone Surge XT synthesizer
Group: Sound
Requires: surge-common = %version-%release

%package -n lv2-surge-plugin
Summary: Surge XT synthesizer as LV2 plugin
Group: Sound
Requires: surge-common = %version-%release

%package -n vst3-surge-plugin
Summary: Surge XT synthesizer as VST3 plugin
Group: Sound
Requires: surge-common = %version-%release

%package -n rack-plugin-surge-xt
Summary: Surge XT synthesizer as VCV Rack plugin
Group: Sound
Requires: surge-common = %version-%release

%package common
Summary: Common data for Surge XT synthesizer
Group: Sound
BuildArch: noarch

%description
%summary

%description -n surge-xt
Standalone Surge XT synthesizer.

%description -n lv2-surge-plugin
Surge XT synthesizer as LV2 plugin.

%description -n vst3-surge-plugin
Surge XT synthesizer as VST3 plugin.

%description -n rack-plugin-surge-xt
Surge XT synthesizer as VCV Rack plugin

%description common
Common data for Surge XT synthesizer.

%prep
%setup -a1
printf '\n%%s\n%%s\n' release-xt/%version %release > VERSION_GIT_INFO

%build
%cmake  -DCMAKE_INSTALL_LIBDIR=%_libdir \
        -DSURGE_BUILD_LV2=ON \
        -DSURGE_BUILD_CLAP=OFF \
        -DSURGE_COPY_TO_PRODUCTS=OFF \
        -DSURGE_SKIP_PIE_CHANGE=ON \
        -DSURGE_BUILD_TESTRUNNER=OFF \
        -DSURGE_RELIABLE_VERSION_INFO=OFF
%cmake_build

%make_build -C src/surge-rack RACK_DIR=%_datadir/rack/sdk rack_plugin

%install
%cmake_install
mkdir -p %buildroot%_desktopdir
cp -pv scripts/installer_linux/assets/applications/*.desktop %buildroot%_desktopdir
cp -prv scripts/installer_linux/assets/icons %buildroot%_datadir
mv %buildroot%_iconsdir/scalable %buildroot%_iconsdir/hicolor
make install -C src/surge-rack RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%global _customdocdir %_defaultdocdir/surge-xt

%files common
%doc LICENSE* README* doc/*
%_datadir/surge-xt

%files -n surge-xt
%_bindir/surge-*
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.*

%files -n lv2-surge-plugin
%_libdir/lv2/*

%files -n vst3-surge-plugin
%_libdir/vst3/*

%files -n rack-plugin-surge-xt
%_libdir/rack/*

%changelog
* Mon Jun 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.4-alt3
- rebuilt with vendored fmt

* Fri Oct 31 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.4-alt2
- added vcvrack plugin

* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.4-alt1
- 1.3.4 released

* Thu May 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.2-alt1
- 1.3.2 released

* Fri Mar  1 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- initial
