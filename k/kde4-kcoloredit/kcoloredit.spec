%define rname kcoloredit

Name: kde4-kcoloredit
Version: 2.0.0
Release: alt1

Group: Graphics
Summary: A color palette Editor
Url: http://www.kde.org/
License: GPLv2+

Source: %rname-%version.tar
Patch1: alt-fix-linking.patch

BuildRequires: cmake gcc-c++ kde4libs-devel kde-common-devel gettext

%description
KColorEdit is a palette files editor. It can be used for editing
color palettes and for color choosing and naming.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname

%files -f %rname.lang
%doc AUTHORS README
%_K4bindir/%rname
%_K4apps/%rname/
%_K4xdg_apps/%rname.desktop
%_K4iconsdir/hicolor/*/*/%rname.*

%changelog
* Wed Dec 25 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- initial build

