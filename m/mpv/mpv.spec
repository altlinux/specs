Name: mpv
Version: 0.7.1
Release: alt1

Summary: mpv is a free and open-source general-purpose video player based on MPlayer and mplayer2.
Summary(ru_RU.UTF8): MPV - это медиапроигрыватель с открытыми исходниками, основанный на проектах MPlayer и mplayer2.
License: GPLv2+
Group: Video

URL: http://mpv.io/
Source: %name-%version.tar

Packager: %packager

# Automatically added by buildreq on Fri Feb 14 2014
# Внимание: пакет libva-devel добавлен вручную!
BuildRequires: libGL-devel libXext-devel libalsa-devel libass-devel libavformat-devel libavresample-devel libjpeg-devel libquvi0.9-devel libswscale-devel patool perl-Encode perl-Math-BigRat python-module-docutils time zlib-devel libva-devel

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

ls
./waf configure --bindir=%buildroot%_bindir --mandir=%buildroot/usr/share/man --datadir=%buildroot%_datadir --prefix=%buildroot

%build

./waf build

%install
./waf install

# Добавляем нехитрую документацию.
%define docdir %_docdir/%name-%version

mkdir -p %buildroot/%docdir
install -pm644 LICENSE %buildroot%docdir/
install -pm644 Copyright %buildroot%docdir/
install -pm644 README.md %buildroot%docdir/
install -pm644 RELEASE_NOTES %buildroot%docdir/

# Бравые mpv'шники залили документацию не в тот каталог. Исправляем.
install -pm644 %buildroot/usr/share/doc/mpv/* %buildroot%docdir/
rm -rf %buildroot/usr/share/doc/mpv/

%files

%dir %docdir
%doc %docdir/*
%config /etc/mpv/encoding-profiles.conf
%_bindir/*
%_man1dir/*
%_iconsdir/hicolor/16x16/apps/mpv.png
%_iconsdir/hicolor/32x32/apps/mpv.png
%_iconsdir/hicolor/64x64/apps/mpv.png
%_desktopdir/*

%changelog
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

