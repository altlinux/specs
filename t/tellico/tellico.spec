Name: 	 tellico
Version: 2.3.11
Release: alt2

Summary: A collection manager for KDE
License: GPLv2+
Group:   Graphical desktop/KDE
Url:     http://tellico-project.org/
# VCS:	 git://anongit.kde.org/tellico

Source:  %name-%version.tar
Source1: %name.watch
Source2: FindKSane.cmake

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++
BuildRequires: kde4multimedia-devel
BuildRequires: kde4pimlibs-devel
BuildRequires: libexempi-devel
BuildRequires: libksane4-devel
BuildRequires: libpoppler-qt4-devel
BuildRequires: libqimageblitz-devel
BuildRequires: libtag-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libyaz-devel
BuildRequires: qjson-devel

%description
Tellico is a KDE application for organizing your collections. It
provides default templates for books, bibliographies, videos, music,
video games, coins, stamps, trading cards, comic books, and wines.

%prep
%setup -q
# See https://bugzilla.altlinux.org/show_bug.cgi?id=30814
cp %SOURCE2 cmake/modules/FindKSane.cmake

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS README
%_K4bindir/*
%_datadir/appdata/%name.appdata.xml
%_desktopdir/kde4/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/mimetypes/application-x-%name.png
%_K4conf_update/*
%_K4apps/%name/*
%_K4cfg/*.kcfg
%_K4conf/*
%_K4xdg_mime/%name.xml

%changelog
* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.11-alt2
- Build without Nepomuk support

* Tue Dec 08 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.11-alt1
- New version

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 2.3.10-alt2
- rebuild with new libyaz 5.13

* Sun Mar 08 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.10-alt1
 Initial build in Sisyphus
