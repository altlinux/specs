%ifarch %luajit_arches
%def_enable lua
%endif

%define oname mpv

Name: mpv034
Version: 0.34.1
Release: alt3

Summary: mpv is a free and open-source general-purpose video player based on MPlayer and mplayer2.
License: GPLv2+
Group: Video

Url: http://mpv.io/
Source: %oname-%version.tar
Patch: %oname-%version-alt.patch

Packager: %packager

# for %%luajit_arches macro
BuildRequires(pre): rpm-macros-luajit

# Automatically added by buildreq on Fri Feb 14 2014
BuildRequires: libGL-devel libXext-devel libalsa-devel libass-devel libavformat-devel libavresample-devel libjpeg-devel libswscale-devel zlib-devel libva-devel

BuildRequires: libpulseaudio-devel libXScrnSaver-devel libXv-devel libXinerama-devel libXrandr-devel libdvdnav-devel libbluray-devel libavfilter-devel

BuildRequires: libsmbclient-devel libswresample-devel libxkbcommon-devel libdrm-devel libv4l-devel libarchive-devel liblcms2-devel libjack-devel

BuildRequires: libenca-devel libuchardet-devel libvulkan-devel libwayland-egl-devel libwayland-cursor-devel libwayland-client-devel wayland-protocols python3-base

BuildRequires: libgbm-devel libplacebo-devel libSDL2-devel libavdevice-devel

BuildRequires: libzimg-devel vapoursynth-devel libshaderc-devel nv-codec-headers

BuildRequires: /usr/bin/rst2man

%if_enabled lua
BuildRequires: liblua5.3-devel libluajit-devel
%endif

Summary(ru_RU.UTF-8): MPV - это медиапроигрыватель с открытыми исходниками, основанный на проектах MPlayer и mplayer2.

%description
mpv is a movie player based on MPlayer and mplayer2.
It supports a wide variety of video file formats,
audio and video codecs, and subtitle types.

%description -l ru_RU.UTF-8
mpv - это медиапроигрыватель, основанный на проектах
MPlayer и mplayer2. Он поддерживает большое количество
видеоформатов, аудио и видео кодеков и форматов субтитров.

%package -n libmpv1
Summary: %oname shared library
Group: System/Libraries

%description -n libmpv1
This package contains %oname shared library

%prep
%setup -n %oname-%version
%patch -p1

ls
chmod ugo+rx waf
./waf configure --bindir=%_bindir --mandir=%_mandir --datadir=%_datadir --libdir=%_libdir --includedir=%_includedir --prefix= \
--enable-pulse \
--enable-xv \
--enable-vaapi \
--enable-alsa \
--enable-gl-x11 \
%{subst_enable lua} \
--enable-libbluray \
--enable-dvdnav \
--enable-libmpv-shared \
--enable-jack \
--enable-vulkan \
--enable-sdl2 \
--enable-vapoursynth \
#

%build
./waf build %_smp_mflags

%install
./waf install --destdir=%buildroot

rm -rfv %buildroot/share/
rm -rfv %buildroot%_iconsdir/hicolor/symbolic/

%files -n libmpv1
%_libdir/libmpv.so.*

%changelog
* Sat Nov 12 2022 L.A. Kostis <lakostis@altlinux.ru> 0.34.1-alt3
- Compat build to ease transition to libmpv2 library.

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 0.34.1-alt2
- BR: added nv-codec-headers (for CUDA support).

* Mon Jun 06 2022 Leontiy Volodin <lvol@altlinux.org> 0.34.1-alt1
- 0.34.1.
- Fix build with python3-module-docutils.

* Tue Nov 16 2021 L.A. Kostis <lakostis@altlinux.ru> 0.34.0-alt2
- use shaderc.

* Fri Nov 12 2021 L.A. Kostis <lakostis@altlinux.ru> 0.34.0-alt1
- 0.34.0.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.33.1-alt3
- NMU: drop unused BR, use /usr/bin/rst2man.py

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 0.33.1-alt2
- Apply build fix for new libplacebo.

* Tue Jun 01 2021 Leontiy Volodin <lvol@altlinux.org> 0.33.1-alt1
- 0.33.1.
- Fixes:
  + CVE-2021-30145.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 0.33.0-alt2
- Added vapoursynth and libzimg support.

* Tue Nov 24 2020 L.A. Kostis <lakostis@altlinux.ru> 0.33.0-alt1.1
- Add libspirv-cross-devel to BR.
- Add missing libavdevice-devel to BR (should fix v4l).

* Mon Nov 23 2020 L.A. Kostis <lakostis@altlinux.ru> 0.33.0-alt1
- 0.33.0.
- remove buggy libsmbclient.
- waf: use python3.
- add bash-completition package.

* Mon Jul 20 2020 L.A. Kostis <lakostis@altlinux.ru> 0.32.0-alt1
- 0.32.0.
- Enabled support:
  + vulkan
  + SDL2
  + gbm (for drm output)

* Mon Jul 20 2020 L.A. Kostis <lakostis@altlinux.ru> 0.29.1-alt10
- Added vulkan vo.
- Fix wayland support.

* Mon Jul 20 2020 L.A. Kostis <lakostis@altlinux.ru> 0.29.1-alt9.1
- Don't exit on fail ABI check (complete a fix from ALT#37106).

* Thu Jul 16 2020 Terechkov Evgenii <evg@altlinux.org> 0.29.1-alt9
- Cherry-pick commit from lakostis@ (ALT#37106)

* Tue Mar 31 2020 Vitaly Lipatov <lav@altlinux.ru> 0.29.1-alt8
- NMU: add BR: libuchardet to fix auto guess of subtitle encoding
- NMU: fix unpacked files

* Sun Mar  1 2020 Terechkov Evgenii <evg@altlinux.org> 0.29.1-alt7
- Fix FTBFS (replace bin/python -> bin/python2 in waf.py)

* Fri Oct 11 2019 Terechkov Evgenii <evg@altlinux.org> 0.29.1-alt6
- Build with JACK support (ALT#37324)

* Sat Jun 29 2019 Michael Shigorin <mike@altlinux.org> 0.29.1-alt5
- Fix build with older libEGL, see upstream issue #5599
  (commit taken from NetBSD)
- Minor spec cleanup

* Fri Apr 12 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.29.1-alt4
- Use %%luajit_arches macro to disable lua support on architectures
  unsupported by luajit.

* Tue Feb 26 2019 Terechkov Evgenii <evg@altlinux.org> 0.29.1-alt3
- Rebuild without libass5

* Fri Nov  9 2018 Terechkov Evgenii <evg@altlinux.org> 0.29.1-alt2
- Rebuild with new ffmpeg

* Thu Nov  1 2018 Terechkov Evgenii <evg@altlinux.org> 0.29.1-alt1
- 0.29.1

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 0.28.2-alt3
- Replace e2k arch name with %%e2k macro (grenka@)

* Sun Sep  9 2018 Terechkov Evgenii <evg@altlinux.org> 0.28.2-alt2
- Build with TV/V4L support (ALT#35370)

* Thu Jun 14 2018 Anton Farygin <rider@altlinux.ru> 0.28.2-alt1
- 0.28.2

* Mon Feb 12 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.27.1-alt1
- 0.27.1
- Fixes:
  + CVE-2018-6360

* Wed Sep 20 2017 Michael Shigorin <mike@altlinux.org> 0.27.0-alt2
- E2K: avoid lua for luajit (not ported yet)

* Wed Sep 13 2017 Terechkov Evgenii <evg@altlinux.org> 0.27.0-alt1
- 0.27.0

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 0.25.0-alt2
- rebuild with debuginfo-enabled ffmpeg

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 0.25.0-alt1
- 0.25.0
- enabled wayland, v4l, egl, drm and libarchive support

* Sun Jan 29 2017 Terechkov Evgenii <evg@altlinux.org> 0.22.0-alt2
- Fix build

* Tue Nov 22 2016 Terechkov Evgenii <evg@altlinux.org> 0.22.0-alt1
- 0.22.0

* Fri Oct 21 2016 Terechkov Evgenii <evg@altlinux.org> 0.21.0-alt1
- 0.21.0

* Tue Aug 16 2016 Terechkov Evgenii <evg@altlinux.org> 0.19.0-alt1
- 0.19.0 (ALT#32382)

* Sat Mar 12 2016 Terechkov Evgenii <evg@altlinux.org> 0.16.0-alt2
- Build libmpv as shared library (ALT#31876)

* Mon Mar  7 2016 Terechkov Evgenii <evg@altlinux.org> 0.16.0-alt1
- 0.16.0

* Sat Jan 30 2016 Terechkov Evgenii <evg@altlinux.org> 0.15.0-alt1
- 0.15.0

* Thu Nov 12 2015 Terechkov Evgenii <evg@altlinux.org> 0.13.0-alt1
- 0.13.0

* Sun Nov  8 2015 Terechkov Evgenii <evg@altlinux.org> 0.12.0-alt1
- 0.12.0

* Fri Oct  9 2015 Terechkov Evgenii <evg@altlinux.org> 0.11.0-alt1
- 0.11.0 (ALT #31345)

* Mon May 25 2015 Terechkov Evgenii <evg@altlinux.org> 0.9.2-alt1
- 0.9.2

* Mon Apr 27 2015 Terechkov Evgenii <evg@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Apr  1 2015 Terechkov Evgenii <evg@altlinux.org> 0.8.3-alt2
- Build with Samba (ALT #30889)

* Sun Mar 29 2015 Terechkov Evgenii <evg@altlinux.org> 0.8.3-alt1
- 0.8.3
- Enable dvdnav/bluray/avfilter (ALT #30873)
- Enable Zsh completion subpackage (ALT #30874)

* Sat Feb 21 2015 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt1
- 0.8.0

* Sun Feb  8 2015 Terechkov Evgenii <evg@altlinux.org> 0.7.3-alt1
- 0.7.3
- Build from upstream git
- Spec cleanup

* Sun Jan 11 2015 Terechkov Evgenii <evg@altlinux.org> 0.7.2-alt1
- Version update

* Sat Dec 20 2014 Andrey Bergman <vkni@altlinux.org> 0.7.1-alt1
- Version update. Added VAAPI support.

* Thu Nov 13 2014 Andrey Bergman <vkni@altlinux.org> 0.6.2-alt1.1
- Added examples.

* Thu Nov 13 2014 Andrey Bergman <vkni@altlinux.org> 0.6.2-alt1
- Version update.

* Wed Oct 08 2014 Andrey Bergman <vkni@altlinux.org> 0.6.0-alt1
- Version update.

* Tue Sep 16 2014 Andrey Bergman <vkni@altlinux.org> 0.5.3-alt1.1
- Rebuild.

* Tue Sep 16 2014 Andrey Bergman <vkni@altlinux.org> 0.5.3-alt1
- Version update.

* Mon Jun 23 2014 Andrey Bergman <vkni@altlinux.org> 0.3.11-alt1
- Version update.

* Sat Apr 05 2014 Andrey Bergman <vkni@altlinux.org> 0.3.7-alt1.1
- Added docdir ownership.

* Sat Apr 05 2014 Andrey Bergman <vkni@altlinux.org> 0.3.7-alt1
- Version update.

* Fri Feb 14 2014 Andrey Bergman <vkni@altlinux.org> 0.3.5-alt1.2
- Enabled support for libass and libquvi.

* Fri Feb 14 2014 Andrey Bergman <vkni@altlinux.org> 0.3.5-alt1.1
- Removed intersections with system packages.

* Fri Feb 14 2014 Andrey Bergman <vkni@altlinux.org> 0.3.5-alt1
- Inital build for Sisyphus.

