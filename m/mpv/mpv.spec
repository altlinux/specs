Name: mpv
Version: 0.3.5
Release: alt1.1

Summary: mpv is a free and open-source general-purpose video player based on MPlayer and mplayer2.
Summary(ru_RU.UTF8): MPV - это медиапроигрыватель с открытыми исходниками, основанный на проектах MPlayer и mplayer2.
License: GPLv2+
Group: Video

URL: http://mpv.io/
Source: %name-%version.tar
Patch0: %name-alt-matriska-big-rat.patch

Packager: %packager

# Automatically added by buildreq on Fri Feb 14 2014
BuildRequires: libGL-devel libXext-devel libalsa-devel libavformat-devel libavresample-devel libjpeg-devel libswscale-devel patool perl-Encode perl-Math-BigRat python-module-docutils time zlib-devel

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
./waf configure --bindir=%buildroot%_bindir --mandir=%buildroot/usr/share/man --datadir=%buildroot%_datadir --prefix=%buildroot --disable-libass

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

%files

%doc %docdir/*
%config /etc/mpv/encoding-profiles.conf
%_bindir/*
%_man1dir/*
%_iconsdir/hicolor/16x16/apps/mpv.png
%_iconsdir/hicolor/32x32/apps/mpv.png
%_iconsdir/hicolor/64x64/apps/mpv.png
%_desktopdir/*

%changelog
* Fri Feb 14 2014 Andrey Bergman <vkni@altlinux.org> 0.3.5-alt1.1
- Removed intersections with system packages.

* Fri Feb 14 2014 Andrey Bergman <vkni@altlinux.org> 0.3.5-alt1
- Inital build for Sisyphus.

