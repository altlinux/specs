
%define _kde_alternate_placement 1
%def_enable mp4v2

%define rname soundKonverter
%define tname soundkonverter
Name: kde4-soundkonverter
Version: 1.6.2
Release: alt1

Summary: A frontend to various audio converters
License: GPLv2
Group: Sound

Url: http://www.kde-apps.org/content/show.php/content=29024
Source: %tname-%version.tar
Source1: ru.po
Patch1: alt-fix-linking.patch

Requires: /usr/bin/ffmpeg vorbis-tools vorbisgain flac lame mp3gain cdparanoia speex wavpack faad mppenc
#Requires: faac
Requires: kde4libs >= %{get_version kde4libs}

# Automatically added by buildreq on Mon Mar 15 2010 (-bi)
#BuildRequires: gcc-c++ glib2-devel glibc-devel-static kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libcdparanoia-devel libqt3-devel libtag-devel libxkbfile-devel qt4-assistant qt4-designer rpm-build-ruby xorg-xf86vidmodeproto-devel
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ kde4multimedia-devel libcdparanoia-devel libtag-devel
#BuildRequires: libmediainfo-devel libzen-devel
BuildRequires: glib2-devel glibc-devel

%description
%rname project is a frontend to various audio converters.
Currently supported backends are oggenc, oggdec, flac, lame, ffmpeg
(partly), mplayer (partly).
With %rname you can convert between various audio file formats.
Supported formats are: (encode/decode)
    ogg (e/d)
    flac (e/d)
    mp3 (e/d)
    wav (e/d)
    wma (d)

%prep
%setup -qn %tname-%version
#%patch1 -p0

[ -e po/ru.po ] || install -m 0644 %SOURCE1 po/

for f in po/*/*.po; do
    newname=`echo $f| sed 's|\(.*/\)[[:alpha:]]*\(\.po\)|\1%tname\2|'`
    [ "$f" == "$newname" ] || mv $f $newname
done

%build
%K4build


%install
%K4install
%K4find_lang --with-kde %tname


%files -f %tname.lang
%doc README CHANGELOG
#%_K4doc/*/%tname
%_kde4_bindir/%tname
%_K4libdir/libsoundkonvertercore.so*
%_K4lib/%{tname}_*.so
%_kde4_xdg_apps/*.desktop
%_kde4_iconsdir/hicolor/*/*/*.*
%_K4apps/%tname
%_K4apps/solid/actions/soundkonverter-*.desktop
%_K4srv/%{tname}_*.desktop
%_K4srvtyp/%{tname}_*.desktop

%changelog
* Thu Jul 12 2012 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt1
- new version

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt0.M60P.1
- build for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- new version

* Fri Feb 17 2012 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt0.M60P.1
- built for M60P

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt1
- new version

* Sat Feb 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt2
- fix requires

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt0.M60P.1
- built for M60P

* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Thu Sep 08 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.90-alt0.M60P.1
- built for M60P

* Thu Sep 08 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.90-alt1
- 1.1.0 RC1

* Wed Jun 01 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- 1.0.0 release

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.7
- 1.0.0-rc3 (0.9.95)

* Tue Dec 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.6
- 1.0.0-rc2 (0.9.94)

* Fri Nov 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.4.M51.1
- built for M51

* Fri Nov 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.5
- 1.0.0-rc1 (0.9.93)

* Fri Sep 10 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.3.M51.1
- built for M51

* Thu Sep 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.4
- 1.0.0-beta3 (0.9.92)

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.3
- 1.0.0-beta2

* Wed May 05 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.1.M51.1
- build for M51

* Wed May 05 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.2
- 1.0.0-beta1

* Mon Mar 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.0.M51.1
- build for M51

* Mon Mar 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.1
- 1.0.0-alpha2
- initial specfile

