%define _kde4_alternate_placement 1
%define libbasketcommon libbasketcommon4

%define rname basket
Name: kde4-%rname
Version: 1.81
Release: alt2

Summary: multi-purpose note-taking application
License: GPLv2+
Group: Graphical desktop/KDE
Url: http://basket.kde.org

Requires: %libbasketcommon = %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 30 2010 (-bi)
#BuildRequires: gcc-c++ glib2-devel glibc-devel-static kde4pimlibs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgpgme-devel libpth-devel libqimageblitz-devel libqt3-devel libxkbfile-devel qt4-assistant qt4-designer rpm-build-ruby
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ glib2-devel glibc-devel kde4pimlibs-devel
BuildRequires: libgpgme-devel libpth-devel libqimageblitz-devel

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


%files -f %rname.lang
%doc AUTHORS README TODO
%_kde4_bindir/*
%_K4lib/basketthumbcreator.so
%_K4lib/kcm_basket.so
%_kde4_xdg_apps/basket.desktop
%_K4apps/basket
%_K4conf/magic/basket.magic
%_kde4_iconsdir/hicolor/*/apps/basket.*
%_kde4_iconsdir/hicolor/*/actions/likeback_*.png
%_kde4_iconsdir/hicolor/*/actions/tag_*.png
%_K4srv/basket_config_*.desktop
%_K4srv/basketthumbcreator.desktop

#/usr/share/mimelnk/application/x-basket-archive.desktop
#/usr/share/mimelnk/application/x-basket-template.desktop

%files -n %libbasketcommon
%_K4libdir/libbasketcommon.so.*

%changelog
* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.81-alt2
- fix build requires

* Tue Oct 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.81-alt1
- new beta

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 1.80-alt0.M51.1
- build for M51

* Thu Apr 29 2010 Sergey V Turchin <zerg@altlinux.org> 1.80-alt1
- initial specfile

