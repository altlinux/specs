%define _kde_alternate_placement 1


%define rname DropboxServiceMenu
Name: kde4-dropbox-service-menu
Version: 0.5.13
Release: alt3.1

%add_findpackage_path %_kde4_bindir
#add_findreq_skiplist %_K4apps/%rname/*.py

Group:     Networking/File transfer
Summary:   Dropbox service menu
License:   GPL
URL:       http://kde-apps.org/content/show.php/Dropbox+ServiceMenu?content=124416

BuildArch: noarch
Requires: kde4-kfilebox

Source:  %rname-%version.tar.bz2

# Automatically added by buildreq on Fri Jun 24 2011 (-bi)
# optimized out: python-base
#BuildRequires: rpm-build-gir sqlite3 xdg-utils
BuildRequires: kde-common-devel xdg-utils

%description
Dropbox service menu for KDE desktops

%prep
%setup -qn %rname-%version

%build

%install
mkdir -p %buildroot/%_K4apps/%rname

install -m 755 dropbox-scripts/* %buildroot/%_K4apps/%rname/
sed -i 's|#SCRIPTS_PATH.*|SCRIPTS_PATH=%_K4apps/%rname/|g' %buildroot/%_K4apps/%rname/dropbox_menu.sh

mkdir -p %buildroot/%_K4srv/ServiceMenus/

install -m 644 dropbox_all.desktop %buildroot/%_K4srv/ServiceMenus/
install -m 644 dropbox_files.desktop %buildroot/%_K4srv/ServiceMenus/
install -m 644 dropbox_directories.desktop %buildroot/%_K4srv/ServiceMenus/

pushd %buildroot/%_K4srv/ServiceMenus/
sed -i 's|=dropbox_menu.sh|=%_K4apps/%rname/dropbox_menu.sh|g' dropbox_all.desktop
sed -i 's|=dropbox_menu.sh|=%_K4apps/%rname/dropbox_menu.sh|g' dropbox_files.desktop
sed -i 's|=dropbox_menu.sh|=%_K4apps/%rname/dropbox_menu.sh|g' dropbox_directories.desktop
popd

%files
%_K4apps/%rname
%_K4srv/ServiceMenus/*.desktop

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.13-alt3.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.13-alt3
- don't start dropbox, require kfilebox

* Fri Jun 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.13-alt2
- install dropbox

* Fri Jun 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.13-alt1
- initial build

