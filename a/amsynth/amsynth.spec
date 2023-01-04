#define gcc_version 5.0

Name: amsynth
Version: 1.13.0
Release: alt1.2
Summary: A classic synthesizer with dual oscillators

License: GPLv2+
Group: Sound
Url: https://github.com/amsynth/amsynth
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: release-%version/%name-%version.tar
Source1: %name.appdata.xml
Source2: lv2-%name-plugin.metainfo.xml
Source3: dssi-%name-plugin.metainfo.xml
Source4: vst-%name-plugin.metainfo.xml
Source5: amsynth_ru.po

# Automatically added by buildreq on Sat Dec 10 2022
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 ladspa_sdk libX11-devel libalsa-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libjack-devel libpango-devel libstdc++-devel libuuid-devel perl perl-Encode perl-XML-Parser perl-parent pkg-config python3 python3-base sh4 xorg-proto-devel
BuildRequires: dssi-devel gcc-c++ glibc-devel-static intltool libgtk+2-devel liblash-devel liblo-devel lv2-devel pandoc

BuildRequires: liblo-devel libsndfile-devel
BuildRequires:  autoconf-archive libX11-devel

BuildRequires:  appliance-base-glibc glibc-utils
BuildRequires:  libgtk2-devel libgtkmm3-devel
BuildRequires:  libjack-devel liblash-devel libsndfile-devel libsndfile-utils
BuildRequires:  libGL-devel libEGL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       jack-audio-connection-kit libsndfile-utils lash 
Requires:       %name-data = %EVR


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
Requires: %name
Group: Sound
Obsoletes: lv2-amsynth-plugins

%description -n lv2-amsynth-plugin
Amsynth plugin for the lv2 audio standard

%package -n dssi-amsynth-plugin
Summary: Amsynth dssi plugin
Requires: dssi
Group: Sound
Requires: %name
Obsoletes: dssi-amsynth-plugins

%description -n dssi-amsynth-plugin
Amsynth plugin for the dssi audio API

%package -n vst-amsynth-plugin
Summary: Amsynth lv2 plugin
Requires: %name
Group: Sound
Obsoletes: vst-amsynth-plugins

%description -n vst-amsynth-plugin
Amsynth plugin for the vst protocl

%prep
%setup
install -m644 %SOURCE5 po/ru.po 
echo ru >> po/LINGUAS


%build
%add_optflags -std=gnu++11
%autoreconf

intltoolize --force

#./autogen.sh

#%__aclocal
#%__automake -a


%configure \
--with-gnu-ld \
--with-jack \
--with-gui \
--with-alsa \
--with-jack \
--with-sndfile \
--with-lash \
--with-lv2 \
--with-pandoc \
--with-dssi


# Build in C++11 mode as glibmm headers use C++11 features. This can be dropped
# when GCC in Fedora switches to C++11 by default (with GCC 6, most likely).
%make

%make_build

%install
%makeinstall_std

DESTDIR=%buildroot %makeinstall

# Install appdata files
install -d -m 755  %buildroot%_datadir/appdata/
install -pDm644 %SOURCE1 %buildroot%_datadir/appdata/
install -pDm644 %SOURCE2 %buildroot%_datadir/appdata/
install -pDm644 %SOURCE3 %buildroot%_datadir/appdata/
install -pDm644 %SOURCE4 %buildroot%_datadir/appdata/

# desktop-file-validate %buildroot%_desktopdir/%name.desktop
# appstream-util validate-relax --nonet %buildroot%_datadir/appdata/*%name.*.xml

%find_lang --with-man --with-qt %name

%files -f %name.lang
%doc README AUTHORS
%doc COPYING
%_bindir/%name
%_man1dir/*
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/amsynth.svg
%dir %_datadir/%name
%_datadir/%name/rc

%files data
%dir %_datadir/%name/skins
%_datadir/%name/skins/*
%dir %_datadir/%name/banks
%_datadir/%name/banks/*


%files -n lv2-amsynth-plugin
%_libdir/lv2/%name.lv2/*
%_datadir/appdata/lv2-%name-plugin.metainfo.xml

%files -n dssi-amsynth-plugin
%_libdir/dssi/%{name}_dssi.so
%_libdir/dssi/%{name}_dssi/*
%_datadir/appdata/dssi-%name-plugin.metainfo.xml

%files -n vst-amsynth-plugin
%_libdir/vst/%{name}_vst.so
%_libdir/vst/*
%_datadir/appdata/vst-%name-plugin.metainfo.xml

%changelog
* Wed Jan 04 2023 Ivan A. Melnikov <iv@altlinux.org> 1.13.0-alt1.2
- NMU: main package should require data subpackage
  (closes: #44800).

* Sat Dec 10 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.13.0-alt1.1
- Fix install sections
- Add ru.po

* Fri Dec 09 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.13.0-alt1
- Version 1.13.0 (closes: #40317)

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1.1
- NMU: rebuild with new lv2

* Sat May 28 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.6.4-alt1
- Version 1.6.4

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

