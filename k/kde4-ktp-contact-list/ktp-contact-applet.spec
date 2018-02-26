%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-contact-list
Name: kde4-ktp-contact-list
Version: 0.4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Telepathy contact list application
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar

BuildRequires: gcc-c++
BuildRequires: kde4-ktp-common-internals-devel kde4libs-devel
BuildRequires: kde-common-devel

%description
%summary

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
Common empty package for %rname

%package -n libktpaccountskcminternal4
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n libktpaccountskcminternal4
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libtelepathy-qt4-devel
%description devel
%summary.

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang ktp-contactlist

%files -f %rname.lang
%_kde4_bindir/ktp-contactlist
#%_K4apps/ktelepathy/
%_kde4_xdg_apps/ktp-contactlist.desktop
#%_kde4_iconsdir/hicolor/*/*/*.*

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
