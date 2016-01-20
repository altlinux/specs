%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%def_disable modemman

%define rname ktp-accounts-kcm
Name: kde4-ktp-accounts-kcm
Version: 0.9.0
Release: alt2

Group: Graphical desktop/KDE
Summary: KDE Configuration Module for Telepathy Instant Messaging Accounts
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar

Patch1: 0.7.0-alt-autoconnect.patch

# Automatically added by buildreq on Mon Apr 16 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libtelepathy-qt4 libtelepathy-qt4-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-ktp-common-internals-devel kde4libs-devel libicu libqt3-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4-ktp-common-internals-devel kde4libs-devel
BuildRequires: kde-common-devel
%if_enabled modemman
BuildRequires: libmm-qt-devel
%endif

%description
This is a KControl Module which handles adding/editing/removing Telepathy
Accounts. It interacts with any Telepathy Spec compliant AccountManager
to manipulate the accounts.

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common kde4-ktp-common-internals-common
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
%K4find_lang --with-kde --append --output=%rname.lang kcm_ktp_accounts
find %buildroot/%_K4i18n -type f -name kcmtelepathyaccounts_\*.mo | sed "s|\.mo$||" | \
while read f; do echo `basename "$f"`; done | sort -u | \
while read n
do
    %K4find_lang --with-kde --append --output=%rname.lang "$n"
done

%files common
%files -f %rname.lang
%_K4lib/kcm_ktp_accounts.so
%_K4lib/ktpaccountskcm_plugin_*.so
%_K4srv/*.desktop
%_K4srvtyp/*.desktop
%_datadir/telepathy/profiles/

%files -n libktpaccountskcminternal4
%_K4libdir/libktpaccountskcminternal.so.*

#%files devel
#%_K4link/lib*.so
#%_K4includedir/KTp/

%changelog
* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt2
- fix requires

* Fri Oct 31 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M70P.1
- built for M70P

* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Wed May 21 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt0.M70P.1
- built for M70P

* Tue May 20 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- new version

* Thu Apr 03 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt0.M70P.1
- built for M70P

* Wed Mar 19 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt0.M70P.1
- built for M70P

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- new version

* Tue Dec 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1.M70P.1
- built for M70P

* Thu Nov 14 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt2
- turn on by default "ConnectAutomatically" during account creation

* Fri Nov 01 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- new version

* Wed Oct 09 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt0.M70P.1
- built for M70P

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt1
- new version

* Mon Jun 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
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

* Mon Apr 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- initial build
