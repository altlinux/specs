# Ensure no unpackaged files
%global _unpackaged_files_terminate_build 1

# Stable docs path across the versions
%define _customdocdir %_defaultdocdir/%name

# wc-config --cflags to add -I/usr/include/wx-3.1
# wx-config --libs: https://github.com/audacity/audacity/issues/552
# libmp3lame: https://github.com/audacity/audacity/issues/2166
%add_optflags %(wx-config --cflags || :) -DDISABLE_DYNAMIC_LOADING_LAME=1

%ifarch armh %ix86
%add_optflags -DPFFFT_SIMD_DISABLE=1
%endif

%define add_libs %(wx-config --libs || :) -lmp3lame

Name: audacity
Version: 3.6.3
Release: alt1

Summary: Cross-platform audio editor
Summary(ru_RU.UTF-8): Кроссплатформенный звуковой редактор
License: GPL
Group: Sound

Url: http://audacity.sourceforge.net/
# https://github.com/audacity/audacity/releases
# https://github.com/audacity/audacity-manual
Source0: %name-sources-%version.tar
Source1: %name-manual-%version.tar
# XXX
Source2: loffice-libcxx-wrapper.sh
Source3: README.ALT

# Patch0001: 0001-Desktop-file-fix-exec-command.patch
Patch0002: 0002-Use-home-directory-for-temp-dir-instead-of-var-tmp-t.patch
Patch0003: 0003-Fix-building-with-system-sbsms.patch
Patch0005: 0005-Fix-lv2-external-gui.patch
Patch0006: 0006-Find-modules-in-lib64.patch
Patch0007: 0007-Manual-document-session-path.patch
Patch0008: 0008-Fix-release-build-warning.patch

Source2000: audacity-e2k.patch

BuildRequires: gcc-c++
BuildRequires: cmake
# -Daudacity_conan_enabled=Off is a temporary workaround according to
# https://github.com/audacity/audacity/pull/1030
#BuildRequires: conan
%ifarch %e2k
BuildRequires: chrpath
%endif
BuildRequires: patchelf
BuildRequires: gettext-devel
BuildRequires: ImageMagick-tools
BuildRequires: ladspa_sdk
BuildRequires: liblame-devel
BuildRequires: libportmidi-devel
# Requires wxWidgets built without STL
BuildRequires: libwxGTK3.2-devel
BuildRequires: zip
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(flac++)
BuildRequires: pkgconfig(id3tag)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sbsms)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(soundtouch)
BuildRequires: pkgconfig(soxr)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(suil-0)
BuildRequires: pkgconfig(twolame)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(vamp-hostsdk)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(wavpack)
BuildRequires: pkgconfig(zlib)
# %%autopatch macro appeared in 4.0.4-alt133
BuildRequires: rpm-build >= 4.0.4-alt133

# Dummy dependency from dlopen()'ed library, without ABI tracking, track at least soname
# https://github.com/audacity/audacity/issues/2161
# This makes sure that the latest ffmpeg libraries Audacity supports
# are installed, and won't be removed from the repository without
# us noticing that.
%if "%_lib" == "lib64"
%define soname_suffix ()(64bit)
%else
%define soname_suffix %nil
%endif
Requires: libavformat.so.60%soname_suffix
Requires: libavcodec.so.60%soname_suffix
Requires: libavutil.so.58%soname_suffix

%description
Audacity is a program that lets you manipulate digital audio waveforms.
It imports many sound file formats, including WAV, AIFF, AU, IRCAM,
MP3, and Ogg Vorbis. It supports all common editing operations such
as Cut, Copy, and Paste, plus it will mix tracks and let you apply
plug-in effects to any part of a sound.

%description -l ru_RU.UTF-8
Audacity - программа, которая дает возможность обрабатывать звукозаписи
в цифровом виде. Она может импортировать множество аудиоформатов, в т.ч.
WAV, AIFF, AU, IRCAM, MP3, Ogg Vorbis, и поддерживает все основные
операции редактирования, такие как Вырезать, Скопировать, Вставить,
а также возможность микширования дорожек и применения эффектов,
предоставляемых подключаемыми модулями, к любой части звука.

%package manual
Summary: Audacity manual (offline install)
Group: Documentation
BuildArch: noarch

%description manual
Audacity Manual can be installed locally if preferred, or accessed
on-line if internet connection is available.

For the most up to date manual content, use the on-line manual.

%prep
%setup -n %name-sources-%version
mkdir manual
tar -xf %SOURCE1 --strip-components=1 -C manual
%autopatch -p1
cp %SOURCE3 .

sed -i 's/"lv2 >= .* >= 0.10.6"//' cmake-proxies/CMakeLists.txt
%add_optflags -isystem /usr/include/suil-0 -lsuil-0

%ifarch %e2k
# EDG frontend bug workaround
sed -i "/std::initializer_list/s/static//" src/prefs/GUIPrefs.cpp
sed -i "s/.*\[ upstream, downstream \].*/\
for (auto \&fix : mDecoratedSources) {\
auto \&upstream = fix.upstream; auto \&downstream = fix.downstream;/" \
  libraries/lib-mixer/Mix.cpp
sed -i "s/mAdjustPolicy{}/mAdjustPolicy/" \
  src/tracks/playabletrack/wavetrack/ui/WaveClipAdjustBorderHandle.h
patch -p2 -i %SOURCE2000
%endif

%build
export ADD_LIBS="%add_libs"
install -m0755 %SOURCE2 ./g++
export CXX="$PWD/g++"
export CC="$(command -v gcc)"

# disable assertions checked via wxASSERT
%add_optflags -DwxDEBUG_LEVEL=0

%cmake \
%ifarch %e2k
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH:PATH='$ORIGIN/../' \
%endif
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -Daudacity_lib_preference:STRING=system \
  -Daudacity_has_networking=no \
  -Daudacity_conan_enabled=Off \
  -Daudacity_has_vst3=Off \
  -Daudacity_obey_system_dependencies=On \
  -Daudacity_use_ffmpeg:STRING=loaded \
  -Daudacity_use_libavcodec:STRING=system \
  -Daudacity_use_libavformat:STRING=system \
  -Daudacity_use_libavutil:STRING=system \
  -Daudacity_use_libmp3lame:STRING=system \
  -Daudacity_use_libflac:STRING=system \
  -Daudacity_use_libid3tag:STRING=system \
  -Daudacity_use_libsndfile:STRING=system \
  -Daudacity_use_libsoxr:STRING=system \
  -Daudacity_use_libtwolame:STRING=system \
  -Daudacity_use_libuuid:STRING=system \
  -Daudacity_use_libvamp:STRING=system \
  -Daudacity_use_libvorbis:STRING=system \
  -Daudacity_use_lv2:STRING=system \
  -Daudacity_use_sbsms:STRING=system \
  -Daudacity_use_soundtouch:STRING=system \
  -Daudacity_use_portaudio:STRING=system \
  -Daudacity_use_portsmf:STRING=local \
  -Daudacity_use_midi:STRING=system \
  -DAUDACITY_BUILD_LEVEL=2 \
  -DAUDACITY_SUFFIX:STRING=""

%cmake_build

%install
%cmakeinstall_std
cp -a manual/manual %buildroot%_datadir/%name/help
rm -rf %buildroot%_defaultdocdir/%name
rm -rf %buildroot%_datadir/%name/include
# Remove a helper script that runs audacity in GitHub CI builds
rm -rf %buildroot%_prefix/%name

# Remove absolute RPATHs
# https://github.com/audacity/audacity/pull/1030#issuecomment-873630620
# https://github.com/audacity/audacity/issues/2165
%ifarch %e2k
# patchelf damages e2k binaries
setrpath="chrpath -r"
%else
setrpath="patchelf --set-rpath"
%endif
$setrpath '$ORIGIN/../%_lib/audacity' %buildroot%_bindir/audacity
for lib in %buildroot%_libdir/audacity/*.so; do
  $setrpath '$ORIGIN' "$lib"
done
for lib in %buildroot%_libdir/audacity/modules/*.so; do
  $setrpath '$ORIGIN/../' "$lib"
done

%find_lang %name

%check
# upstream seems to assume statically linking bundled libsbsms,
# verify that system one is used
patchelf --print-needed %buildroot/%_bindir/audacity | grep -q sbsms
# mp3lame can be either dlopen'ed or linked explicitly,
# ensure that a system library is linked explicitly
patchelf --print-needed %buildroot/%_libdir/audacity/modules/mod-mp3.so | grep -q libmp3lame

# https://github.com/audacity/audacity/issues/2161
# [...] | grep -q libavcodec

%files -f %name.lang
%doc CHANGELOG.txt CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md README.ALT
%_bindir/audacity
%_libdir/audacity
%_mandir/man?/*
%_iconsdir/*/*/apps/%name.svg
%_iconsdir/hicolor/*/%name.png
%dir %_datadir/%name
%exclude %_datadir/%name/help
%_datadir/%name/*
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml
%_datadir/metainfo/%name.appdata.xml
%_datadir/icons/hicolor/*/apps/%name.*
%_pixmapsdir/*.xpm

%files manual
%dir %_datadir/%name
%_datadir/%name/help

%changelog
* Mon Sep 09 2024 Ivan A. Melnikov <iv@altlinux.org> 3.6.3-alt1
- 3.6.3

* Thu Sep 05 2024 Ivan A. Melnikov <iv@altlinux.org> 3.6.2-alt1
- 3.6.2

* Thu Aug 08 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.6.1-alt1.1
- Fixed build for Elbrus

* Wed Jul 24 2024 Ivan A. Melnikov <iv@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Jul 17 2024 Ivan A. Melnikov <iv@altlinux.org> 3.6.0-alt1
- 3.6.0

* Fri Jul 05 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.5.1-alt1.1
- Fixed build for Elbrus

* Wed Jun 12 2024 Ivan A. Melnikov <iv@altlinux.org> 3.5.1-alt1
- 3.5.1.
- build in release mode, disabling wxASSERT (altbug#44359).

* Mon Apr 22 2024 Ivan A. Melnikov <iv@altlinux.org> 3.5.0-alt0.2
- Disabe certain SIMD optimizations on %%ix86 to fix build.

* Mon Apr 22 2024 Ivan A. Melnikov <iv@altlinux.org> 3.5.0-alt0.1
- 3.5.0

* Fri Apr 12 2024 Michael Shigorin <mike@altlinux.org> 3.4.2-alt1.3
- FTBFS workaround (ilyakurdyukov@)

* Wed Feb 07 2024 Ivan A. Melnikov <iv@altlinux.org> 3.4.2-alt1.2
- Add libturbojpeg build dependency (fixes FTBFS)

* Thu Nov 23 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.4.2-alt1.1
- Fixed build for Elbrus

* Fri Nov 17 2023 Ivan A. Melnikov <iv@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Nov 15 2023 Ivan A. Melnikov <iv@altlinux.org> 3.4.1-alt2
- Backport upstream workaround for wxWidgets 3.2.4 (alt#48434)

* Thu Nov 09 2023 Ivan A. Melnikov <iv@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Nov 06 2023 Ivan A. Melnikov <iv@altlinux.org> 3.4.0-alt1.1
- Fix build on armh by disabling (some) SIMD optimizations there

* Fri Nov 03 2023 Ivan A. Melnikov <iv@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sat Sep 09 2023 Ivan A. Melnikov <iv@altlinux.org> 3.3.3-alt2
- Update ffmpeg dependencies to 6.0

* Fri Jun 09 2023 Ivan A. Melnikov <iv@altlinux.org> 3.3.3-alt1
- 3.3.3

* Thu May 25 2023 Michael Shigorin <mike@altlinux.org> 3.3.2-alt3
- E2K: update sed patch by ilyakurdyukov@ (mcst#8091)

* Wed May 24 2023 Ivan A. Melnikov <iv@altlinux.org> 3.3.2-alt2
- fix load of lv2 external UIs with system libsuil
- restore desktop file fix

* Fri May 19 2023 Ivan A. Melnikov <iv@altlinux.org> 3.3.2-alt1
- 3.3.2
- build with wavpack and w/o vst3sdk

* Mon Sep 19 2022 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- new version 3.1.3
- build with wxGTK3.2

* Thu Mar 10 2022 Michael Shigorin <mike@altlinux.org> 3.1.2-alt2
- E2K: build fix by ilyakurdyukov@ (patchelf is not ported properly yet)

* Fri Nov 19 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 3.1.2-alt1
- Version 3.1.2 (Closes: 40174, 38790, 38662, 41340)
- Do load plugins from /usr/lib/ladspa in addition to /usr/lib64/ladspa
  (this upstream behaviour was incorrectly changed by sed)
- XXX Upstream removed linkage with libffmpeg, so we do not have propper ABI tracking now
  and depend from libavocodec.so.58 manually
  (https://github.com/audacity/audacity/issues/2161)
- Build against system libopus, libportaudio and libmidi (as in upstream spec for Fedora)
- Dropped setting of correct version in the "About" dialog, upstream code changed,
  it is set correctly now by cmake variables like AUDACITY_VERSION
- Dropped no more needed patches:
  + ALT-Remove-warning-about-alpha-version.patch - upstream code changed, using
    "-DAUDACITY_BUILD_LEVEL=2" now
  + 0001-HACK-off-bundled-libmp3lame.patch - libmp3lame is not bundled any more,
    a chack that system one is linked is kept in %%check
  + 0001-update-PO-files-by-update_po_files.sh.patch,
    0002-Fix-fuzzies-in-Russian-transaltion.patch,
    0003-Fix-translation-of-Filter-Curve.patch - dropped in the new version,
    upstream has a special workflow of updating translations
    (see https://github.com/audacity/audacity/pull/558)
- Renamed and rediffed other patches, make all of them git am-able
- Hacked to force GTK+3.0 at build time
- Removed hack with -latomic on MIPS, upstream CMakeLists.txt adds it itself
- Hacked for liblame-devel missing pkgconfig file
  (reported https://bugzilla.altlinux.org/show_bug.cgi?id=40342)
- Explicitly disabled networking (it is disabled by default, make sure that
  we do not send crash reports to Audacity servers, they will not be able
  to read them due to debuginfo available separately and because it is not their build)

* Mon Nov 01 2021 Michael Shigorin <mike@altlinux.org> 2.4.1-alt0.gitd6f841.3
- fixed build for Elbrus (ilyakurdyukov@)

* Sat May 30 2020 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.4.1-alt0.gitd6f841.2
- Version v2.4.1 + git master from 2020-05-30, commit d6f8410d5
  Git has fixes for newest wxWidgets 3.1.3 and some other important bug fixes
- Ensuring that libmp3lame and ffmpeg are linked but not dlopened
- Ensuring that package version and the one in the "About" dialog are the same
- Fixed Russian translation
  PRed to upstream: https://github.com/audacity/audacity/pull/558

* Wed Dec 18 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.3-alt2
- Drop Fedora-libmp3lame-default.patch because dlopen()-ing libmp3lame
  is switched off by --disable-dynamic-loading (system one is linked)
- Drop incorrect replacement libmp3lame.so -> libmp3lame.so.0:
  it replaced libmp3lame.so.0 -> libmp3lame.so.0.0 and had no sense
  due to target code being under false #ifdef
- Drop installing downstream XPM icons near upstream PNGs and SVG
- Use %%mips macro
- Clean up configure options a bit (no functional changes)
- Drop explicit aclocal, %%autoreconf is enough
- Clean up BuildRequires, delete odd ones, use pkgconfig() where possible

* Sun Nov 24 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.3-alt1
- Version 2.3.3
- Keeping and rediffed NetBSD-ALT-Session-directory-in-home.patch:
  * Use $AUDACITY_TMPDIR env to specify a custom temp directory,
    it then will be $AUDACITY_TMPDIR/audacity-$UID.
  * Default temp directory is ~/.audacity-tmp instead of upstream /var/tmp/audacity-$UID.
  * Reading $TMPDIR was previously changed to $AUDACITY_TMPDIR
    because e.g. pam_mktemp is used by default on ALT and breaks the environment
    that Audacity developers expected.
- Dropped patches merged to upstream:
  * 0001-Fix-building-with-wxWidgets-3.1.2.patch
  * 0002-Fix-Ru-translation-of-signed-and-float.patch
- Dropped NetBSD-ffmpeg3.patch (does not make sense)
- Dropped -fno-strict-aliasing
- Chanages in lib-src/sbsms were ported to libsbsms10

* Fri Oct 04 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.2-alt3
- Fix Russian translation of 'signed' and 'float' (Closes: 37238)
  PRed to upstream: https://github.com/audacity/audacity/pull/381

* Mon Aug 19 2019 Anton Midyukov <antohami@altlinux.org> 2.3.2-alt2
- fix build with wxGTK 3.1.2 (Thanks Mikhail Novosyolov)

* Thu May 14 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.2-alt1
- Version 2.3.2
- Fixed NetBSD-ALT-Session-directory-in-home.patch:
  this patch worked incorrectly, fixed it to really move session
  directory from /var/tmp/audacity-$USER to $HOME/.audacity-tmp
  to ensure session data consistency across reboots and after crashes;
  this directory may be overriden with AUDACITY_TMPDIR variable
- Use AUDACITY_TMPDIR env instead of TMPDIR to override session
  directory because TMPDIR is set by default to tmpfs in many cases
  what may lead to data loss
- Removed Fedora-libdir.patch, instead using sed to fix ladspa directory
- Dropped explicit -std=gnu++11 (build scripts set it by themselves)
- Set LDFLAGS as env on mipsel instead of conditional patching
  to not worry that the mipsel patch will become unappliable
  (removed ALT-link-with-libatomic.patch)

* Fri Apr 26 2019 Ivan A. Melnikov <iv@altlinux.org> 2.3.1-alt2
- Fix build on mipsel.

* Fri Apr 26 2019 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt1
- Build new version (no major changes, but (closes: #36354)).
- Cleanup changelog.

* Mon Feb 18 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.0-alt2.git20190217.2345
- Git master from 17.02.2019 23:45 UTC+0300 (commit e609a9d)
- Patch: remove warning that it's an alpha version from the welcome screen
  and don't recommend to install an "official" build

* Fri Jan 25 2019 Ivan A. Melnikov <iv@altlinux.org> 2.3.0-alt1.git20181205.2140.0.mips1
- Link with latomic to fix build on mipsel

* Wed Dec 05 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.0-alt1.git20181205.2140
- New version 2.3.0 + git master from 05.12.2018 21:40 UTC+0300 (release 2.3.0 is officially buggy on Linux, so took git master)
- Now Russian translation is better than in previous versions
- Switched to no-STL wxGTK3.1 and GTK+3
- Reworked and extended build flags (now Audacity supports working with more formats) (Closes: 31852)
- Enable ffmpeg/avconv (Closes: 35366)
- Build with system libsbsms (packaged it seperately, moved audacity-2.2.2-alt-e2k-fft.patch from Audacity to libsbsms)
- Patched to move temporary files from tmpfs /tmp/.private/ to persistend storage in HOME
- Added built-in icons to RPM files list
- Install ALT's icons only if there are no upstream ones
- Install more docs & don't install docs for bundled statically linked libraries

* Fri Nov 23 2018 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt4
- Fixed packaging documentation (Closes: #34427).
- disable SSE for non-x86 and e2k arches.

* Sun Mar 18 2018 Andrew Savchenko <bircoph@altlinux.org> 2.1.1-alt3
- Fix SSE issue on E2K properly, revert SSE removal for non-x86.

* Sat Mar 17 2018 Michael Shigorin <mike@altlinux.org> 2.1.1-alt2
- disable SSE for non-x86
- enable parallel build

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1.2
- Updated build to support gcc-6

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1.1
- rebuilt against libSoundTouch.so.1

* Fri Oct 09 2015 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1
- 2.1.1
- manual moved to a separate subpackage (not unlike fedora)

* Fri Oct 09 2015 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- 2.1.0 (closes: #31343)
- buildreq for libsoxr-devel

* Thu Jun 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.5-alt4.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Apr 24 2014 Michael Shigorin <mike@altlinux.org> 2.0.5-alt4
- try to recover MP3 processing capability (debian configure options)
- tweaked icons installation

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt3
- Restored in Sisyphus

* Tue Jan 07 2014 Michael Shigorin <mike@altlinux.org> 2.0.5-alt2
- build without ffmpeg support (latest one is unsupported so far)

* Tue Jan 07 2014 Michael Shigorin <mike@altlinux.org> 2.0.5-alt1
- 2.0.5
- spec cleanup according to ALT Packaging HOWTO
- converted Summary: in Russian from CP1251 to UTF-8
- added description in Russian

* Wed Jan 23 2013 Alex Karpov <karpov@altlinux.ru> 2.0.3-alt1
- new version
    + no more fullsrc package.

* Sun Sep 02 2012 Alex Karpov <karpov@altlinux.ru> 2.0.2-alt1
- new version

* Thu Mar 15 2012 Alex Karpov <karpov@altlinux.ru> 2.0.0-alt1
- new version. At last - not beta anymore!

* Tue Jan 31 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.3
- russian translation updated

* Sun Jan 22 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.2
- added new russian translation (bug #26841)

* Wed Jan 18 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.1
- export with libav* now works

* Tue Dec 13 2011 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1
- new version

* Wed Nov 09 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt2.1
- rebuild with new libav*

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt2
- fixed build (patch from Debian by Reinhard Tartler)

* Wed Apr 13 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt1
- new version

* Tue Nov 23 2010 Alex Karpov <karpov@altlinux.ru> 1.3.12-alt1.1
- disable portmixer for a while (build workaround)

* Fri Apr 02 2010 Alex Karpov <karpov@altlinux.ru> 1.3.12-alt1
- new version

* Tue Mar 23 2010 Alex Karpov <karpov@altlinux.ru> 1.3.11-alt1
- new version

* Thu Dec 10 2009 Alex Karpov <karpov@altlinux.ru> 1.3.10-alt1
- new version

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.9-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for audacity
  * postclean-05-filetriggers for spec file

* Mon Nov 02 2009 Alex Karpov <karpov@altlinux.ru> 1.3.9-alt1.1
- GSocket declaration conflict fixed

* Wed Sep 02 2009 Alex Karpov <karpov@altlinux.ru> 1.3.9-alt1
- new version
    + build from fullsrc tarball

* Mon Aug 24 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt2.1
- minor spec cleanup

* Mon Aug 24 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt2
- added actual help files

* Fri Aug 14 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt1.1
- updated build requirements
    + spec cleanup

* Thu Aug 13 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt1
- new version

* Tue Aug 11 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt1.1
- rebuild with new libs

* Fri Feb 27 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt1
- now it's stable enough for alt1 release

* Thu Jan 29 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt0.1
- 1.3.7

* Wed Jan 28 2009 Alex Karpov <karpov@altlinux.ru> 1.3.6-alt0.1
- 1.3.6
    + removed obsoleted %post and %postun stuff

* Thu Sep 25 2008 Alex Karpov <karpov@altlinux.ru> 1.3.5-alt0.1
- 1.3.5
    + updated build requirements

* Mon Apr 07 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9.2
- added update_menus

* Thu Mar 27 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9.1
- added desktopdb macros with new build requirements

* Mon Mar 24 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9
- added mimedb macros

* Sat Dec 15 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.M40.7
- build for branch 4.0 with libtwolame

* Fri Dec 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6.1
- build for branch 4.0 (#13689 fix)

* Wed Nov 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6.1
- Vamp disabled for x86_64 build

* Wed Nov 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6
- 1.3.4 release

* Tue Oct 30 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.1
- new 1.3.4 unofficial beta
  + required wxGTK2u-2.6.4 (#13068 and probably #11880 fix)
  + removed desktop-file patch.

* Thu Sep 20 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.3
- audacity.desktop categories fixed (#12843)

* Tue Jun 05 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.2
- updated build requirements (now we can find a sound device)

* Wed May 30 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.1
- 1.3.3

* Tue Feb 20 2007 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.4
- patch for flac-1.1.3 support by Led <led@> (bug #10868) 

* Thu Dec 14 2006 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.3
- fixed bug 10420

* Sat Nov 11 2006 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.2
- initial build of 1.3.x branch for Sisyphus

* Thu Dec 01 2005 Vladimir Lettiev <crux@altlinux.ru> 1.3.0-alt0.1
- 1.3.0 beta ( audacity-1_3_0-branch from cvs )

* Tue Feb 22 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3-alt1.1.1
- Rebuilt with libflac-1.1.2-alt1

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3-alt1.1
- Rebuilt with libstdc++.so.6.

* Sun Nov 21 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Thu Sep 02 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Fri Jun 25 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.1-alt2
- Updated patch from help file location.

* Wed May 12 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Apr 13 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt2
- Updated russian translation.
- Added russian help.
- Fixed build with SoundTouch for gcc 3.3.3.

* Wed Mar 10 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Feb 14 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.9
- 1.2.0-pre4

* Fri Nov 14 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.8
- 1.2.0-pre3
- Fixed build on SMP systems.

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.7
- 1.2.0-pre2

* Sun Sep 28 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.6
- 1.2.0-pre2 testing tarball.

* Sun Sep 14 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.3
- 1.2.0-pre1

* Wed Jun 25 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt3
- Fixed unmet: now requires wxGTK >= 2.4.1.

* Fri Jun 20 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt2
- Rebuilt with new wxGTK.

* Fri Mar 21 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sun Mar 16 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt0.4
- Rebuilt with libid3tag package.

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt0.2
- Developers branch snapshot (CVS 20030306).
- Temprorary without libsamplerate.

* Wed Mar 05 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt6
- Rebuild with wxGTK-2.4.0

* Fri Feb 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt5
- Rebuild with new id3lib (3.8.2)

* Fri Nov 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt4
- Rebuild with new id3lib (3.8.1)

* Wed Nov 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt3
- Rebuild, system id3lib used.

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt2.1
- rebuild with new vorbis

* Mon Jun 24 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt2
- Fixed intersection with basesystem.

* Fri Jun 7 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon May 27 2002 Andrey Astafiev <andrei@altlinux.ru> 1.1-alt0.1.cvs
- cvs snapshot 20020527 of 1.1.x unstable branch especially for Daedalus.

* Wed Feb 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.99-alt0.1.pre1
- cvs snapshot 20020213 with several bugfixes.
- relocated help.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 0.98-alt2
- rebuild with wxGTK 2.2.x branch.

* Fri Feb 01 2002 Andrey Astafiev <andrei@altlinux.ru> 0.98-alt1
- 0.98.

* Tue Jan 08 2002 Andrey Astafiev <andrei@altlinux.ru> 0.97-alt2
- Fixed group tag.

* Thu Oct 11 2001 Andrey Astafiev <andrei@altlinux.ru> 0.97-alt1
- First version of RPM package.l
