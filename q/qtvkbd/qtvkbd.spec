
%define		rname qtvkbd
Name:		%rname
Version:	0.8.3
Release:	alt1
%K5init no_altplace

Group:		Accessibility
Summary:	Virtual Keyboard
Summary(ru_RU.UTF8): Виртуальная (экранная) клавиатура
License: LGPL-3.0
Url: https://github.com/Alexander-r/qtvkbd

Provides: %{rname}5 = %version-%release
Provides: kde4-kvkbd = %EVR
Obsoletes: kde4-kvkbd < %EVR

Source0:	%rname-%version.tar
#Patch1: alt-hide-extent.patch
#Patch2: alt-def-geometry.patch
#Patch3: alt-visibility.patch
#Patch4: alt-empty-label-text.patch
#Patch5: alt-close-label-color.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake qt5-base-devel qt5-x11extras-devel libxslt-devel

%description
Kvkbd is a virtual keyboard, it contains many
feature like system tray and dock support, autodetection
and on the fly change of the keyboard layout, scripting
with DBus, etc.

%description -l ru_RU.UTF8
Kvkbd - виртуальная клавиатура, обладающая множеством
функций, таких как поддержка системного лотка и стыковки к
окнам других приложений, автоматическое определение раскладки
и смена её на лету, поддержка скриптов для работы с DBus, и т.п.

%prep
%setup -n %rname-%version
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1

# swap standart and light color themes
#mv src/standart.css src/standart-old.css
#mv colors/light.css src/standart.css
#mv src/standart-old.css colors/light.css

%build
%K5build

%install
%K5install
ln -s %rname %buildroot/%_bindir/kvkbd

%find_lang --with-kde %rname

%files -f %rname.lang
%doc AUTHORS TODO README.md ChangeLog
%_bindir/%rname
%_bindir/kvkbd
%_desktopdir/%rname.desktop
%_datadir/%rname/

%changelog
* Thu Jun 03 2021 Sergey V Turchin <zerg@altlinux.org> 0.8.3-alt1
- initial build
