Name: mpv
Version: 0.7.3
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

BuildRequires: libpulseaudio-devel libenca-devel libXScrnSaver-devel libXv-devel libXinerama-devel libXrandr-devel liblua5-devel

%description
mpv is a movie player based on MPlayer and mplayer2.
It supports a wide variety of video file formats,
audio and video codecs, and subtitle types.

%description -l ru_RU.UTF-8
mpv - это медиапроигрыватель, основанный на проектах
MPlayer и mplayer2. Он поддерживает большое количество
видеоформатов, аудио и видео кодеков и форматов субтитров.

%prep
%setup -n %name-%version
%patch0 -p1

ls
chmod ugo+rx waf
./waf configure --bindir=%buildroot%_bindir --mandir=%buildroot/usr/share/man --datadir=%buildroot%_datadir --prefix=%buildroot \
--enable-pulse \
--enable-enca \
--enable-xss \
--enable-xv \
--enable-xinerama \
--enable-xrandr \
--enable-vaapi \
--enable-alsa \
--enable-gl-x11 \
--enable-lua \

%build

./waf build

%install
./waf install

%files
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/encoding-profiles.conf
%_bindir/%name
%_man1dir/%name.1.*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_desktopdir/%name.desktop
%doc LICENSE Copyright README.md RELEASE_NOTES etc/input.conf etc/mplayer-input.conf etc/example.conf etc/restore-old-bindings.conf

%changelog
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

