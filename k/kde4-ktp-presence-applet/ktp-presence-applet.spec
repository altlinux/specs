%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-presence-applet
Name: kde4-ktp-presence-applet
Version: 0.4.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Plasma applet for managing your Telepathy account presence
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar
# FC
Patch1: ktp-presence-applet-0.3.0-translations.patch

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
%patch1 -p1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang plasma_applet_ktp_presence

%files -f %rname.lang
%_K4lib/plasma_applet_ktp_presence.so
%_K4srv/plasma_applet_ktp_presence.desktop

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
