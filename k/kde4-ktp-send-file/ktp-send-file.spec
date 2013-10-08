%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define rname ktp-send-file
Name: kde4-ktp-send-file
Version: 0.6.3
Release: alt1

Group: Graphical desktop/KDE
Summary: File manager plugin to launch file transfer jobs
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
#%K4find_lang --with-kde --append --output=%rname.lang ktp-send-file

%files -f %rname.lang
%_kde4_bindir/ktp-send-file
%_K4srv/ServiceMenus/ktp-send-file.desktop

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt1
- new version

* Tue Jun 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Fri May 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- new version

* Wed Apr 10 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt1
- new version

* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Wed Aug 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- new version

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
