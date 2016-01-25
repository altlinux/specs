%define gcc_version 5.0

Name: amsynth
Version: 1.6.3
Release: alt2
Summary: A classic synthesizer with dual oscillators

License: GPLv2+
Group: Sound
Url: https://github.com/amsynth/amsynth
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: release-%version/%name-%version.tar.gz
Source1: %name.appdata.xml
Source2: lv2-%name-plugin.metainfo.xml
Source3: dssi-%name-plugin.metainfo.xml
Source4: vst-%name-plugin.metainfo.xml

# Automatically added by buildreq on Mon Nov 23 2015
# optimized out: fontconfig fontconfig-devel glib2-devel ladspa_sdk libX11-devel libalsa-devel libatk-devel libatkmm-devel libcairo-devel libcairomm-devel libdbus-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgtk+2-devel libjack-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel libuuid-devel libxml2-devel pkg-config xorg-xproto-devel
BuildRequires: dssi-devel gcc-c++ glibc-devel-static libxcb libgtkmm2-devel liblash-devel liblo-devel libsndfile-devel

BuildRequires: liblo-devel libsndfile-devel

BuildRequires:  appliance-base-glibc glibc-utils
BuildRequires:  libgtk2-devel libgtkmm3-devel
BuildRequires:  libjack-devel liblash-devel libsndfile-devel libsndfile-utils
BuildRequires:  libGL-devel libEGL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       jack-audio-connection-kit libsndfile-utils lash



%description
Amsynth is a software synthesis that provides a
classic subtractive synthesizer topology, with:

- Dual oscillators with classic waveforms - sine / saw / square / noise
- 12/24 dB/octave low/high/band-pass resonant filter
- Independent ADSR envelopes for filter and amplitude
- LFO which can modulate the oscillators, filter, and amplitude
- Distortion
- Reverb

%package data
BuildArch: noarch
Summary: Data files for amsynth
Group: Sound
%description data
Sound banks and skins used in amsynth

%package -n lv2-amsynth-plugin
Summary: Amsynth lv2 plugin
Requires: lv2
Requires: %name-data = %version-%release
Group: Sound
Obsoletes: lv2-amsynth-plugins

%description -n lv2-amsynth-plugin
Amsynth plugin for the lv2 audio standard

%package -n dssi-amsynth-plugin
Summary: Amsynth dssi plugin
BuildRequires: dssi-devel liblo liblo-devel
Requires: dssi
Group: Sound
Requires: %name-data = %version-%release
Obsoletes: dssi-amsynth-plugins

%description -n dssi-amsynth-plugin
Amsynth plugin for the dssi audio API

%package -n vst-amsynth-plugin
Summary: Amsynth lv2 plugin
Requires: %name-data = %version-%release
Group: Sound
Obsoletes: vst-amsynth-plugins

%description -n vst-amsynth-plugin
Amsynth plugin for the vst protocl

%prep
%setup

%autoreconf

#./autogen.sh

%add_optflags -std=c++11

%configure \
--with-jack \
--with-alsa \
--with-jack \
--with-sndfile \
--with-lash \
--with-dssi

%build
# Build in C++11 mode as glibmm headers use C++11 features. This can be dropped
# when GCC in Fedora switches to C++11 by default (with GCC 6, most likely).
%make

%make_build

%install
DESTDIR=%buildroot %makeinstall

# Install appdata files
install -d -m 755  %buildroot%_datadir/appdata/
install -pDm644 %SOURCE1 %buildroot%_datadir/appdata/
install -pDm644 %SOURCE2 %buildroot%_datadir/appdata/
install -pDm644 %SOURCE3 %buildroot%_datadir/appdata/
install -pDm644 %SOURCE4 %buildroot%_datadir/appdata/

# desktop-file-validate %buildroot%_desktopdir/%name.desktop
# appstream-util validate-relax --nonet %buildroot%_datadir/appdata/*%name.*.xml

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/appdata/%name.appdata.xml

%files data
%doc README AUTHORS
%doc COPYING
%_datadir/%name

%files -n lv2-amsynth-plugin
%_libdir/lv2/%name.lv2/
%_datadir/appdata/lv2-%name-plugin.metainfo.xml

%files -n dssi-amsynth-plugin
%_libdir/dssi/%{name}_dssi.so
%_libdir/dssi/%{name}_dssi/
%_datadir/appdata/dssi-%name-plugin.metainfo.xml

%files -n vst-amsynth-plugin
%_libdir/vst/%{name}_vst.so
%_datadir/appdata/vst-%name-plugin.metainfo.xml

%changelog
* Mon Jan 25 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.6.3-alt2
- Fix build

* Mon Nov 23 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.6.3-alt1
- Initial build to Sisyphus

* Sun Nov 1 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.3-1
- Update to new maintenance upstream 1.6.3

* Mon Oct 26 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.2-1
- Update to new maintenance upstream 1.6.2

* Sun Oct 11 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.1-1
- Update to new maintenance upstream 1.6.1

* Mon Sep 28 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.0-1
- Update to new upstream 1.6.0
- Add the new vst plugin in a new sub-package.
- Remove ugly plurals of "plugins". There is only one.
- Fix build with new gtkmm24

* Mon Sep 07 2015 Richard Hughes <richard@hughsie.com> 1.5.1-6
- Remove the invalid ZERO WIDTH SPACE chars from the metainfo files.

* Sat Sep 05 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-5
- Move license files to the -data subpackage.
- Use fully versioned dependency in subpackages.
- Update the description of -the data subpackage.
- Add the skins/README as a doc file.

* Thu Sep 03 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-4
- Each plugins have now their licenses files and docs.
- Data subpackae for data files required by plugins.

* Thu Jun 04 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-3
- CHange the name of the dssi subckage to dssi-amsytnh-plugins.

* Tue Jun 02 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-2
- Add the support of alsa, lash and dssi. Can now export with libsndfile.
- New subpackage for dssi's plugins.
- Use now the right license: GPLv2+

* Sat May 30 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-1
- Initial spec
