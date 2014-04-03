%define _kde4_alternate_placement 1
%define libbasketcommon libbasketcommon4
%define rname basket
%define git_rev 79c422a

Name: 	 kde4-%rname
Version: 1.90
Release: alt2.git%git_rev

Summary: multi-purpose note-taking application
License: GPLv2+
Group:   Graphical desktop/KDE
Url:     http://basket.kde.org

Requires: %libbasketcommon = %version-%release
Provides: basket = %version-%release

Source:  %rname-%version.tar

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ glib2-devel glibc-devel kde4pimlibs-devel
BuildRequires: libgpgme-devel
BuildRequires: libpth-devel
BuildRequires: libqimageblitz-devel
BuildRequires: soprano

%description
This multi-purpose note-taking application can helps you to:

* Easily take all sort of notes
* Collect research results and share them
* Centralize your project data and re-use them
* Quickly organize your toughts in idea boxes
* Keep track of your information in a smart way
* Make intelligent To Do lists
* And a lot more...

%package -n %libbasketcommon
Summary: KDE 4 core library
Group: System/Libraries
Requires: %{get_dep kde4libs}
%description -n %libbasketcommon
KDE 4 core library.

%prep
%setup -q -n %rname-%version

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname

# Remove development files
rm -f %buildroot%_K4link/libbasketcommon.so

%files -f %rname.lang
%doc AUTHORS README TODO
%_kde4_bindir/*
%_K4lib/basketthumbcreator.so
%_K4lib/kcm_basket.so
%_kde4_xdg_apps/basket.desktop
%_K4apps/basket
%_kde4_iconsdir/hicolor/*/apps/basket.*
%_kde4_iconsdir/hicolor/*/actions/likeback_*.png
%_kde4_iconsdir/hicolor/*/actions/tag_*.png
%_K4srv/basket_config_*.desktop
%_K4srv/basketthumbcreator.desktop

%files -n %libbasketcommon
%_K4libdir/libbasketcommon.so.*

%changelog
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

