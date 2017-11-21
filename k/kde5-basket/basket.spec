%define libbasket_soname 5
%define libbasketcommon libbasketcommon%libbasket_soname
%define rname basket

Name: 	 kde5-%rname
Version: 2.49
Release: alt1%ubt
%K5init no_altplace

Summary: multi-purpose note-taking application
License: GPLv2+
Group:   Graphical desktop/KDE
Url:     https://github.com/basket-notepads/basket

Requires: %libbasketcommon = %version-%release
Provides: basket = %version-%release
Provides: kde4-basket = %version-%release
Obsoletes: kde4-basket < %version-%release

Source:  %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: glib2-devel glibc-devel kde5-libkdepim-devel
BuildRequires: kf5-karchive-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdoctools-devel
BuildRequires: kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kcmutils-devel kf5-kio-devel kf5-knotifications-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: qt5-base-devel qt5-phonon-devel

%description
This multi-purpose note-taking application can helps you to:

* Easily take all sort of notes
* Collect research results and share them
* Centralize your project data and re-use them
* Quickly organize your toughts in idea boxes
* Keep track of your information in a smart way
* Make intelligent To Do lists
* And a lot more...

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libbasketcommon
Summary: Library for %name
Group: System/Libraries
%description -n %libbasketcommon
Library for %name

%prep
%setup -q -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data basket
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc AUTHORS TODO README.md
%_K5bin/*
%_K5plug/basketthumbcreator.so
%_K5plug/kcm_basket.so
%_K5xdgapp/basket.desktop
%_K5data/basket
%_K5icon/hicolor/*/apps/basket.*
%_K5icon/hicolor/*/actions/likeback_*.png
%_K5icon/hicolor/*/actions/tag_*.png
%_K5srv/basket_config_*.desktop
%_K5srv/basketthumbcreator.desktop
%_K5xmlgui/basket

#%files devel
#%_K5link/libbasketcommon.so

%files -n %libbasketcommon
%_K5lib/libbasketcommon.so.%libbasket_soname
%_K5lib/libbasketcommon.so.%libbasket_soname.*.*

%changelog
* Tue Nov 21 2017 Oleg Solovyov <mcpain@altlinux.org> 2.49-alt1%ubt
- port from kde4 to kde5

* Fri Nov 10 2017 Oleg Solovyov <mcpain@altlinux.org> 2.10-alt0_4beta.gite93519c
- fix build

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 2.10-alt0_3beta.gite93519c
- Build without nepomuk

* Wed May 06 2015 Andrey Cherepanov <cas@altlinux.org> 2.10-alt0_2beta.gite93519c
- New snapshot
- Implement user configurable plaintext pasting
- Do not collapse empty lines when toggling a note tag

* Tue Nov 18 2014 Andrey Cherepanov <cas@altlinux.org> 2.10-alt0_1beta.git43890d6
- New beta version
- Set Url to github page

* Wed May 21 2014 Andrey Cherepanov <cas@altlinux.org> 1.90-alt3.gita91eb93
- Fix bugs

* Thu Apr 03 2014 Andrey Cherepanov <cas@altlinux.org> 1.90-alt2.git79c422a
- Fix Link note bugs
- Append creation time to basket and note files

* Wed Mar 19 2014 Andrey Cherepanov <cas@altlinux.org> 1.90-alt1.git372776a
- New version with changes from https://github.com/gl-bars/basket.git
- Provides basket

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.81-alt2
- fix build requires

* Tue Oct 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.81-alt1
- new beta

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 1.80-alt0.M51.1
- build for M51

* Thu Apr 29 2010 Sergey V Turchin <zerg@altlinux.org> 1.80-alt1
- initial specfile

