# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define optflags_lto %nil

Name: guitarix
Version: 0.47.0
Release: alt1
Summary: Modular, virtual amplifier for Linux
Group: Sound
License: GPL-2.0-or-later
Url: https://github.com/brummer10/guitarix
# Source-url: https://github.com/brummer10/guitarix/releases/download/V%version/guitarix2-%version.tar.xz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: faust-devel
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(avahi-gobject)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: libfftw3-devel
BuildRequires: gperf
BuildRequires: intltool
BuildRequires: boost-devel
BuildRequires: eigen3
BuildRequires: ladspa_sdk
BuildRequires: python3
BuildRequires: sassc
BuildRequires: waf
BuildRequires: zita-convolver-devel
BuildRequires: zita-resampler-devel
BuildRequires: pkgconfig(glibmm-2.4)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(gtk+-3.0)
Requires: jack_capture
Requires: jconvolver
Requires: qjackctl
Requires: vorbis-tools
#Requires: google-roboto-condensed-fonts

Obsoletes: libgxw < 0.40
Obsoletes: libgxwmm < 0.40

%description
Guitarix is a modular, virtual amplifier for Linux. With Guitarix you can choose
different preamp and amp models and /or could load *.nam files with the Neural
Amp Modeler modules, or load *.json or .aidax files with the RTNeural modules,
to simulate a specific hardware unit. Combine them with various effects and
speaker cabinet emulations and/or load your own Impulse Response files to come
up with your very own tones. Guitarix comes as a standalone application or as
vst3 plugin. Its modules are also available in the LV2 plugin format, which you
can incorporate into your DAW of choice. Furthermore, it can even be run
headless, so you can turn a Raspberry Pi, or any other such devices, into a
dedicated amp modeler. You can even control Guitarix via a MIDI controller or
foot-board.

Guitarix comes with an extensive list of effects including compression,
distortion, modulation, reverb, delay, EQ, etc. Some of the effects modules
that are included in Guitarix are influenced by some popular hardware units,
for example the Tube Screamer is, not surprisingly, based off of the Ibanez
Tube Screamer. Guitarix can also load up LAPSPA and LV2 plugins to comply the
effect chain.

%package -n lv2-%name-plugins
Summary: Collection of LV2 guitarix plug-ins
Group: Sound
# ladspa/distortion.cpp and ladspa/guitarix-ladspa.cpp are BSD
# The rest of ladspa/* is GPLv+
License: GPL-2.0-or-later
Requires: lv2
Requires: %name = %EVR

%description -n lv2-%name-plugins
This package contains the guitarix amp plug-ins that come together with
guitarix, but can also be used by any other ladspa host.

%prep
%setup
%autopatch -p1

# fix shebang
find . -type f -print0 |
  xargs -0 sed -i 's,/usr/bin/env python,%_bindir/python3,'

# The build system does not use these bundled libraries by default. But
# just to make sure:
rm -fr src/zita-convolver src/zita-resampler
%__subst 's|-O3||' wscript

%build
./waf -vv configure --prefix=%prefix --libdir=%_libdir \
      --cxxflags-release="-DNDEBUG -fomit-frame-pointer \
      -ffinite-math-only -fno-math-errno -fno-signed-zeros -fstrength-reduce \
%ifarch %ix86 x86_64
      -msse \
%endif
%ifarch %ix86
      -mfxsr \
%endif
      %optflags" \
%ifarch %arm
      --disable-sse \
%endif
      --shared-lib \
      --lv2dir=%_libdir/lv2

./waf -vv build %{?_smp_mflags}

%install
./waf -vv install --destdir="%buildroot" --libdir="%_libdir"

desktop-file-install \
    --add-category="X-DigitalProcessing" \
    --dir=%buildroot%_desktopdir \
        %buildroot/%_desktopdir/%name.desktop

#fix links and remove unwanted devel files
chmod 755 %buildroot%_libdir/libgxw*.so.0.1
rm -rf %buildroot%_libdir/libgxw*.so

%find_lang %name

%files -f %name.lang
%doc changelog COPYING README
%_bindir/%name
%_pixmapsdir/*
%_desktopdir/%name.desktop
%_datadir/gx_head/
%_libdir/libgx*.so.0*
%_datadir/metainfo/*.metainfo.xml

%files -n lv2-%name-plugins
%_libdir/lv2/*

%changelog
* Fri Aug 29 2025 Anton Midyukov <antohami@altlinux.org> 0.47.0-alt1
- new version 0.47.0
- remove subpackage ladspa-guitarix-plugins

* Fri Jun 09 2023 Anton Midyukov <antohami@altlinux.org> 0.44.1-alt2
- Add upstream patches for python 3.11 and gcc13 support

* Sat May 07 2022 Anton Midyukov <antohami@altlinux.org> 0.44.1-alt1
- new version (0.44.1) with rpmgs script

* Fri Jan 07 2022 Anton Midyukov <antohami@altlinux.org> 0.43.1-alt1
- new version 0.43.1

* Thu Aug 26 2021 Anton Midyukov <antohami@altlinux.org> 0.42.1-alt2
- disable LTO flag

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 0.42.1-alt1
- new version (0.42.1) with rpmgs script

* Thu May 13 2021 Slava Aseev <ptrnine@altlinux.org> 0.42.0-alt2
- NMU: fix build with GLib 2.68

* Tue Dec 22 2020 Anton Midyukov <antohami@altlinux.org> 0.42.0-alt1
- new version 0.42.0

* Sat Aug 08 2020 Anton Midyukov <antohami@altlinux.org> 0.41.0-alt1
- new version 0.41.0

* Wed Jun 24 2020 Anton Midyukov <antohami@altlinux.org> 0.40.0-alt1
- new version 0.40.0
- switch to Gtk+3
- add a metainfo file
- disable build devel packages
- cleanup spec
- first build on armh

* Mon Apr 20 2020 Anton Midyukov <antohami@altlinux.org> 0.39.0-alt1
- new version 0.39.0

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 0.38.1-alt1
- new version 0.38.1

* Tue Apr 23 2019 Anton Midyukov <antohami@altlinux.org> 0.37.3-alt2
- Add russian translations (Thanks Valeriy Shtobbe, Olesya Gerasimenko)

* Sun Nov 25 2018 Anton Midyukov <antohami@altlinux.org> 0.37.3-alt1
- new version 0.37.3

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.36.1-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun Apr 08 2018 Anton Midyukov <antohami@altlinux.org> 0.36.1-alt1
- new version 0.36.1

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.35.5-alt1.1
- NMU: rebuild with new lv2

* Tue Aug 08 2017 Anton Midyukov <antohami@altlinux.org> 0.35.5-alt1
- new version (0.35.5) with rpmgs script

* Sun May 21 2017 Anton Midyukov <antohami@altlinux.org> 0.35.3-alt1
- Initial build for ALT Linux Sisyphus
