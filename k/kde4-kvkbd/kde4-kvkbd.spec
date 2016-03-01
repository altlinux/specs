%define		__kde4_alternate_placement 1

%define		content 94374

%define		rname kvkbd
Name:		kde4-%rname
Version:	0.7.2
Release:	alt6

Group:		Accessibility
Summary:	Virtual Keyboard for KDE4
Summary(ru_RU.UTF8): Виртуальная (экранная) клавиатура для KDE4
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://kde-apps.org/content/show.php/Kvkbd?content=56019

Provides:	%rname = %version-%release

Source0:	%rname-%version.tar
Patch1: alt-hide-extent.patch
Patch2: alt-def-geometry.patch
Patch3: alt-visibility.patch
Patch4: alt-empty-label-text.patch
Patch5: alt-close-label-color.patch

BuildRequires(pre): kde4libs-devel
# Automatically added by buildreq on Wed Aug 26 2009 (-bi)
BuildRequires: gcc-c++ kde4libs-devel libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libqt4-devel libxkbfile-devel libxslt-devel xorg-xf86vidmodeproto-devel xsltproc

%description
Kvkbd is a virtual keyboard for KDE, it contains many
feature like system tray and dock support, autodetection
and on the fly change of the keyboard layout, scripting
with DBus, etc.

%description -l ru_RU.UTF8
Kvkbd - виртуальная клавиатура для KDE4, обладающая множеством
функций, таких как поддержка системного лотка и стыковки к
окнам других приложений, автоматическое определение раскладки
и смена её на лету, поддержка скриптов для работы с DBus, и т.п.

%prep
%setup -q -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# swap standart and light color themes
mv src/standart.css src/standart-old.css
mv colors/light.css src/standart.css
mv src/standart-old.css colors/light.css

%build
%K4build

%install
%K4install

%K4find_lang --with-kde %rname

%files -f %rname.lang
%doc AUTHORS TODO README ChangeLog
%_kde4_bindir/%rname
%_kde4_xdg_apps/%rname.desktop
%_K4apps/%rname/

%changelog
* Tue Mar 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt6
- reduce height in login helper mode

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt4.M70P.1
- build for M70P

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt5
- update default look

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt4
- fix default visibility

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt3
- fix visibility

* Wed Dec 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt2
- setup defaults

* Tue Dec 15 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt0.M70P.1
- build for M70P

* Mon Dec 14 2015 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.2
- Fixed build

* Sat Nov 21 2009 Motsyo Gennadi <drool@altlinux.ru> 0.6-alt1.1
- added russian description and summary (fixed #22160). Thanks to Phantom.

* Wed Aug 26 2009 Motsyo Gennadi <drool@altlinux.ru> 0.6-alt1
- initial build for ALT Linux
