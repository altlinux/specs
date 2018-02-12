Name: mpv
Version: 0.27.1
Release: alt1

Summary: mpv is a free and open-source general-purpose video player based on MPlayer and mplayer2.
Summary(ru_RU.UTF8): MPV - это медиапроигрыватель с открытыми исходниками, основанный на проектах MPlayer и mplayer2.
License: GPLv2+
Group: Video

URL: http://mpv.io/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Packager: %packager

# Automatically added by buildreq on Fri Feb 14 2014
BuildRequires: libGL-devel libXext-devel libalsa-devel libass-devel libavformat-devel libavresample-devel libjpeg-devel libswscale-devel patool perl-Encode perl-Math-BigRat python-module-docutils time zlib-devel libva-devel

BuildRequires: libpulseaudio-devel libenca-devel libXScrnSaver-devel libXv-devel libXinerama-devel libXrandr-devel libdvdnav-devel libbluray-devel libavfilter-devel libsmbclient-devel libswresample-devel libwayland-client-devel libwayland-cursor-devel libxkbcommon-devel libEGL-devel libwayland-egl-devel libdrm-devel libv4l-devel libarchive-devel liblcms2-devel

%ifnarch e2k
BuildRequires: liblua5.3-devel libluajit-devel
%endif

%description
mpv is a movie player based on MPlayer and mplayer2.
It supports a wide variety of video file formats,
audio and video codecs, and subtitle types.

%description -l ru_RU.UTF-8
mpv - это медиапроигрыватель, основанный на проектах
MPlayer и mplayer2. Он поддерживает большое количество
видеоформатов, аудио и видео кодеков и форматов субтитров.

%package -n zsh-completion-%name
Summary: Zsh completion for mpv
Group: Shells
BuildArch: noarch
Requires: %name = %version-%release

%description -n zsh-completion-%name
Zsh completion for %name.

%package -n libmpv-devel
Summary: Header files for %name
Group: Development/C
Requires: %name = %version-%release

%description -n libmpv-devel
Header files for %name

%package -n libmpv1
Summary: %name shared library
Group: System/Libraries

%description -n libmpv1
This package contains %name shared library

%prep
%setup -n %name-%version
%patch0 -p1

ls
chmod ugo+rx waf
./waf configure --bindir=%_bindir --mandir=%_mandir --datadir=%_datadir --libdir=%_libdir --incdir=%_includedir --prefix= \
--enable-pulse \
--enable-xv \
--enable-vaapi \
--enable-alsa \
--enable-gl-x11 \
%ifnarch e2k
--enable-lua \
%endif
--enable-zsh-comp \
--enable-libbluray \
--enable-dvdnav \
--enable-libsmbclient \
--enable-libmpv-shared \

%build
./waf build

%install
./waf install --destdir=%buildroot

%files
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/encoding-profiles.conf
%_bindir/%name
%_man1dir/%name.1.*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_desktopdir/%name.desktop
%doc LICENSE Copyright README.md RELEASE_NOTES etc/input.conf etc/mplayer-input.conf etc/mpv.conf etc/restore-old-bindings.conf

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/_mpv

%files -n libmpv-devel
%_libdir/libmpv.so
%_includedir/%name
%_pkgconfigdir/*.pc

%files -n libmpv1
%_libdir/libmpv.so.*

%changelog
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

