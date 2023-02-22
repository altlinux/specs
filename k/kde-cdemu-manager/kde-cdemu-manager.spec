%define oname kde_cdemu

Summary: A simple KDE front-end for CDemu
Name: kde-cdemu-manager
Version: 0.8.0
Release: alt1
License: LGPLv2+
Group: Graphical desktop/KDE
Url: http://kde-apps.org/content/show.php/KDE+CDEmu+Manager?content=99752
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://dl.opendesktop.org/api/files/download/id/1481242372/%oname-%version.tar.bz2

BuildRequires(pre): rpm-build-kf5 rpm-macros-kde-common-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kauth-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
Requires: cdemu-client

%description
KDE CDemu Manager is a simple front-end for CDemu.

It provides a little manager window that gives you an overview of your virtual
drives and allows you to mount and unmount images.

It also includes a KDE service menu for mounting images directly from
Dolphin/Konqueror (which is what most people will want to use).

Images can be unmounted like any other media through Dolphin or the Device
Notifier widget.

%prep
%setup -n %oname
find . -name '*.cpp' -exec chmod 644 {} \;
find . -name '*.h' -exec chmod 644 {} \;

%build
%K5cmake
%K5make

%install
%K5install

# Add KDE4 service menu
mkdir -p %buildroot%_datadir/kde4/services/ServiceMenus/
cp %buildroot%_K5srv/ServiceMenus/kde_cdemu_mount.desktop \
%buildroot%_datadir/kde4/services/ServiceMenus/kde_cdemu_mount.desktop

%find_lang %oname

%files -f %oname.lang
%_K5xdgapp/org.kde.kde_cdemu.desktop
%_K5bin/kde_cdemu
%_K5srv/ServiceMenus/kde_cdemu_mount.desktop
%_datadir/kde4/services/ServiceMenus/kde_cdemu_mount.desktop

%changelog
* Wed Feb 22 2023 Artyom Bystrov <arbars@altlinux.org> 0.8.0-alt1
- update to new version



* Mon Jan 30 2023 Artyom Bystrov <arbars@altlinux.org> 0.7.2-alt1
- initial build for ALT Sisyphus

