%def_disable rpath
%def_with pic
%def_enable deprecated
%def_enable lirc
%def_with dbus
%def_without xinerama
%def_with browser_plugin
%define jstype lib
#----------------------------------------------------------------------
%define subst_with_to() %{expand:%%{?_with_%{1}:--with-%{2}}} %{expand:%%{?_without_%{1}:--without-%{2}}}

Name: gxine
Summary: Mediaplayer - GTK-based GUI for xine libraries
Summary(uk_UA.CP1251): Медіапрогравач - GTK+ GUI для бібліотек xine
Summary(ru_RU.CP1251): Медиапроигрыватель - GTK+ GUI для библиотек xine
Version: 0.5.11
Release: alt10.3
License: %gpl2plus
Group: Video
URL: http://xinehq.de
Source: %name-%version.tar
Patch: gxine-0.5.11-alt-glib2.patch
Patch1: gxine-0.5.11-alt-DSO.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: imake libgtk+2-devel libxine-devel zlib-devel
BuildRequires: libXtst-devel libXaw-devel libXrandr-devel xorg-cf-files
BuildRequires: libXext-devel xorg-inputproto-devel xorg-sdk
BuildRequires: desktop-file-utils ImageMagick-tools

%{?_enable_lirc:BuildRequires: liblirc-devel}
%{?_with_dbus:BuildRequires: libdbus-glib-devel}
%{?_with_xinerama:BuildRequires: libXinerama-devel}
%{?_with_browser_plugin:BuildRequires: browser-plugins-npapi-devel libnspr-devel}
%{!?jstype:%define jstype moz}
%if %jstype == moz
BuildRequires: xulrunner-devel
%endif
%if %jstype == sea
BuildRequires: seamonkey-devel
%endif
%if %jstype == ff
BuildRequires: firefox-devel
%endif
%if %jstype == lib
BuildRequires: libjs-devel
%endif

%description
%name is a GTK+ based GUI for the libxine video player library.
It provides %name, a  media player that can play all the audio/video
formats that libxine supports. Currently, this includes MPEG1/2, some
AVI and Quicktime files, some network streaming methods and disc based
media (VCD, SVCD, DVD).

%description -l uk_UA.CP1251
%name - GTK+ GUI для бібліотеки відеопрогравання libxine.
Він надає %name - медіа-програвач для програвання аудіо/відео форматів,
які підтримує libxine. В даний час це MPEG1/2, деякі файли AVI та
Quicktime, деякі мережеві потокові способи і дискові засоби (VCD, SVCD,
DVD).

%description -l ru_RU.CP1251
%name - GTK+ GUI для библиотеки видеопроигрывания libxine.
Он предоставляет %name - медиа-проигрыватель для проигрывания
аудио/видео форматов, поддерживаемых libxine. В данное время это
MPEG1/2, некоторые файлы AVI и Quicktime, некоторые сетевые потоковые
способы и дисковые средства (VCD, SVCD, DVD).


%package -n mozilla-plugin-%name
Summary: gxine browser plugin
Group: Video
Requires: %name = %version-%release
Requires: browser-plugins-npapi

%description -n mozilla-plugin-%name
Browser plugin for mozilla and other browsers using the same plugin
infrastructure.

%description -n mozilla-plugin-%name -l uk_UA.CP1251
Плагін для mozilla та інших браузерів з такою ж інфраструктурою
плагінів.

%description -n mozilla-plugin-%name -l ru_RU.CP1251
Плагин для mozilla и других браузеров с такой же инфраструктурой
плагинов.


%prep
%setup
%patch -p0
%patch1 -p0
sed -i \
    -e '/^Encoding=/d' \
    -e '/^Exec=/s/$/ %%U/' \
    -e '/^Categories=/ s/=.*$/=GTK;AudioVideo;Video;Player;TV;/' \
    -e '/^MimeType=/ s|=.*$|='"$(cat %_datadir/mimetypes-devel/libxine)|" \
    %name.desktop
iconv -f cp1251 -t utf-8 >> %name.desktop <<__MENU__
GenericName[ru]=Проигрыватель видео
GenericName[uk]=Програвач відео
Comment[ru]=Проигрывание фильмов и песен, или просмотр цифрового телевидения
Comment[uk]=Програвання фільмів та пісень, або перегляд цифрового телебачення
__MENU__


%build
# need for make configure with proper xine.m4
%autoreconf
%configure \
    %{subst_enable rpath} \
    %{subst_with pic} \
    --enable-defeat-screensaver-via-xtest \
    %{subst_enable lirc} \
    --enable-%{jstype}js \
    --with-spidermonkey=%_includedir/js \
    %{subst_with dbus} \
    %{subst_with xinerama} \
    %{subst_with_to browser_plugin browser-plugin} \
    --disable-integration-wizard \
    %{subst_enable deprecated}

%make_build
convert -border 0x8 -bordercolor none -depth 8 pixmaps/%name{,-64}.png
for s in 48 36 32 24 22 16; do
    convert -depth 8 -resize ${s}x$s pixmaps/%name{-64,-$s}.png
done
bzip2 --keep --best --force ChangeLog


%install
%make DESTDIR=%buildroot install
%if_with browser_plugin
install -d %buildroot%browser_plugins_path
mv %buildroot%_libdir/%name/%{name}plugin.* %buildroot%browser_plugins_path/
%endif
for s in 64 48 36 32 24 22 16; do
    install -D -m 0644 {pixmaps/%name-$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name}.png
done
rm -rf %buildroot%_pixmapsdir

%find_lang --with-man %name
%find_lang --with-man --append --output=%name.lang %name.theme
%find_lang --with-man --append --output=%name.lang %{name}_client

%files -f %name.lang
%doc AUTHORS ChangeLog.* README TODO doc/Keybindings-HOWTO
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_bindir/*
%_man1dir/*
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*


%if_with browser_plugin
%files -n mozilla-plugin-%name
%browser_plugins_path/*
%endif


%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.11-alt10.3
- Fixed build

* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.11-alt10.2
- NMU: dropped obsolete macros, updated desktop categories

* Fri Oct 02 2009 Alexey Gladkov <legion@altlinux.ru> 0.5.11-alt10.1
- NMU: Rebuilt with browser-plugins-npapi.

* Tue Dec 02 2008 Led <led@altlinux.ru> 0.5.11-alt10
- updated BuildRequires
- cleaned up spec

* Mon Aug 11 2008 Led <led@altlinux.ru> 0.5.11-alt9
- added icons
- fixed %name.desktop

* Thu Aug 07 2008 Led <led@altlinux.ru> 0.5.11-alt8
- fixed %%files
- fixed %name.desktop
- added icons

* Fri Apr 04 2008 Led <led@altlinux.ru> 0.5.11-alt7
- fixes desktop-mime-entry

* Mon Mar 17 2008 Led <led@altlinux.ru> 0.5.11-alt6
- fixed License
- fixed Requires

* Tue Feb 12 2008 Led <led@altlinux.ru> 0.5.11-alt5
- build with SpiderMonkey libjs
- fixed spec
- updated BuildRequires

* Thu Sep 20 2007 Led <led@altlinux.ru> 0.5.11-alt4
- fixed %name.desktop

* Sat Jun 23 2007 Led <led@altlinux.ru> 0.5.11-alt3
- fixed %name.desktop

* Wed Jun 06 2007 Led <led@altlinux.ru> 0.5.11-alt2
- fised and cleaned up spec

* Fri Feb 02 2007 Led <led@altlinux.ru> 0.5.11-alt1
- 0.5.11: bugfix release

* Tue Jan 09 2007 Led <led@altlinux.ru> 0.5.10-alt1
- 0.5.10: SECURITY FIX (local exploit)

* Mon Dec 18 2006 Led <led@altlinux.ru> 0.5.9-alt1
- 0.5.9:
  + prevent screen blanking in windowed mode
  + show time remaining
  + some minor fixes

* Mon Oct 09 2006 Led <led@altlinux.ru> 0.5.8-alt1
- 0.5.8
- removed gxine-0.5.7-uk.patch
- fixed BuildRequires

* Mon Jul 24 2006 Led <led@altlinux.ru> 0.5.7-alt3
- fixed %%files
- cleaned up spec
- fixed BuildRequires

* Tue Jul 11 2006 Led <led@altlinux.ru> 0.5.7-alt2
- fixed ukrainian translation (gxine-0.5.7-uk.patch)
- cleaned up spec

* Fri Jul 07 2006 Led <led@altlinux.ru> 0.5.7-alt1
- 0.5.7
- fixed spec
- enable dbus support (for screansavers)
- cleaned up BuildRequires and Requres

* Wed May 03 2006 Led <led@altlinux.ru> 0.5.6-alt1
- 0.5.6
- cleanup spec
- removed %name-0.5.5-i18n.patch and uk.po because they in upstream now
- fixed spec

* Tue Mar 21 2006 Led <led@altlinux.ru> 0.5.5-alt3
- fix %name.desktop

* Tue Mar 14 2006 Led <led@altlinux.ru> 0.5.5-alt2
- added %name-0.5.5-i18n.patch
- added uk.po
- removed redundant BuildRequires
- fix spec

* Fri Mar 10 2006 Led <led@altlinux.ru> 0.5.5-alt1
- 0.5.5
- updated %name-0.5.5-wizards.patch
- disabled %name-0.5.5-wizards.patch, used --disable-integration-wizard instead
- fix spec

* Mon Jan 30 2006 Led <led@altlinux.ru> 0.4.9-alt4
- fix %%doc
- fix spec

* Mon Jan 23 2006 Led <led@altlinux.ru> 0.4.9-alt3
- fix spec
- fix %name.desktop
- uk and ru Summary and description
- added patch for wizards

* Thu Dec 22 2005 Led <led@altlinux.ru> 0.4.9-alt2
- fix menu

* Mon Nov 28 2005 Led <led@altlinux.ru> 0.4.9-alt1
- initial build
