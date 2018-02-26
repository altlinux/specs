%define		__kde4_alternate_placement 1

%define		content 94374

%define		rname kvkbd
Name:		kde4-%rname
Version:	0.6
Release:	alt1.1

Group:		Accessibility
Summary:	Virtual Keyboard for KDE4
Summary(ru_RU.UTF8): Виртуальная (экранная) клавиатура для KDE4
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.kde-apps.org/content/show.php/Kvkbd+-+KDE4?content=%content

Provides:	%rname = %version-%release
Requires:	kde4libs >= %{get_version kde4libs}

Source0:	http://www.kde-apps.org/CONTENT/content-files/%content-%rname-%version.tar.bz2

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

%build
%K4cmake \
    -DCMAKE_CXX_FLAGS:STRING="%optflags" \
    -DCMAKE_C_FLAGS:STRING="%optflags"
%K4make

%install
%K4install

%K4find_lang --with-kde %rname

%files -f %rname.lang
%doc AUTHORS TODO README ChangeLog
%__kde4_bindir/%rname
%__kde4_xdg_apps/%rname.desktop
%_K4apps/%rname

%changelog
* Sat Nov 21 2009 Motsyo Gennadi <drool@altlinux.ru> 0.6-alt1.1
- added russian description and summary (fixed #22160). Thanks to Phantom.

* Wed Aug 26 2009 Motsyo Gennadi <drool@altlinux.ru> 0.6-alt1
- initial build for ALT Linux
