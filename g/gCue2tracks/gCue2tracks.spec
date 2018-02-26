Name: gCue2tracks
Version: 0.4.6
Release: alt1.1

Summary: Split Compressed Audio CD Image to Tracks
Summary(ru_RU.UTF-8): Разрезает сжатые Audio CD образы на дорожки
License: GPLv2+
Group: Sound
Url: http://gtk-apps.org/content/show.php/gCue2tracks?content=80703

Packager: Maxim Zhukov <mzhukov@altlinux.org>

Source: %name-%version.tar.bz2
# change some codecs options (from OpenSuSe)
Patch0: gCue2tracks-0.4.5-codec_opts.patch
# some fix gCue2tracks.desktop from original package
Patch1: gCue2tracks-0.4.6-desktop.patch

BuildRequires: fdupes python-modules-encodings

Requires: python-module-pygtk python-module-mutagen
Requires: mac apetag lame wavpack vorbis-tools cuetools shntool ffmpeg

BuildArch: noarch

%description
Tool for spliting compressed audio CD image to tracks with filling tags from cue
sheet info.

Authors:
--------
    Denis Fomin <fominde@gmail.com>

%description -l ru_RU.UTF-8
Утилита для разрезания сжатого образа Audio CD на дорожки по информации 
из cue файла.

Авторы:
--------
    Денис Фомин <fominde@gmail.com>


%prep
%setup
%patch0
%patch1

%build
# none

%install
install -Dm 0755 gcue2tracks %buildroot%_bindir/gcue2tracks
install -Dm 0644 gCue2tracks.glade %buildroot%_datadir/gcue2tracks/%name.glade
install -m 0755 config.py decoder.py gCue2tracks.py preference.py %buildroot%_datadir/gcue2tracks
install -m 0644 %name.png %buildroot%_datadir/gcue2tracks
install -Dm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 0644 %name.png %buildroot%_pixmapsdir/%name.png

pushd po
for i in *.mo
do
    install -Dm 0644 $i %buildroot%_datadir/locale/${i%%.mo}/LC_MESSAGES/%name.mo
done
popd

fdupes -s %buildroot

%find_lang %name

%files -f %name.lang
%doc debian/changelog
%_datadir/gcue2tracks
%_bindir/*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.6-alt1.1
- Rebuild with Python-2.7

* Tue Jun 01 2010 Maxim Zhukov <mzhukov@altlinux.org> 0.4.6-alt1
- initial build for ALT Linux Sisyphus

* Wed May 19 2010 lazy.kent.suse@gmail.com
- update to 0.4.6
* Sat Apr  3 2010 lazy.kent.suse@gmail.com
- initial package created
