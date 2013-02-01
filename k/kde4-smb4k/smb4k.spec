
%define _kde_alternate_placement 1
%define sover 4
%define libsmb4kcore libsmb4kcore%sover

%define rname smb4k
Name: kde4-%rname
Version: 1.0.5
Release: alt1

Group: Networking/Other
Summary: A KDE SMB/CIFS share browser
License: GPLv2+
Url: http://smb4k.sourceforge.net/

Requires: samba-client cifs-utils
Requires: %libsmb4kcore = %version-%release

Source: %rname-%version.tar
# FC
Patch1: smb4k-0.10.9-sudo.patch

# Automatically added by buildreq on Fri Apr 30 2010 (-bi)
#BuildRequires: gcc-c++ glib2-devel glibc-devel-static kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel qt4-assistant qt4-designer rpm-build-ruby
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ glib2-devel glibc-devel kde4libs-devel

%description
Smb4K is an SMB/CIFS share browser for KDE. It uses the Samba software suite to
access the SMB/CIFS shares of the local network neighborhood. Its purpose is to
provide a program that's easy to use and has as many features as possible.


%package -n %libsmb4kcore
Summary: %name core library
Group: System/Libraries
Requires: kde4libs >= %{get_version kde4libs}
%description -n %libsmb4kcore
%name core library

%package devel
Summary: Developemnt files for %name
Group: Development/KDE and QT
%description devel
Developemnt files for %name


%prep
%setup -q -n %rname-%version
#%patch1 -p1


%build
%K4build


%install
%K4install
%K4find_lang --with-kde %rname


%files -f %rname.lang
%_kde4_bindir/*
%_K4exec/mounthelper
%_K4conf_update/*
%_K4lib/*.so
%_K4libdir/libsmb4ktooltips.so
%_kde4_xdg_apps/smb4k.desktop
%_K4apps/smb4k
%_K4cfg/smb4k.kcfg
%_kde4_iconsdir/hicolor/*/*/*.*
%_K4iconsdir/oxygen/*/apps/*.*
%_K4dbus_system/de.berlios.smb4k.mounthelper.conf
%_K4dbus_sys_services/de.berlios.smb4k.mounthelper.service
%_datadir/polkit-1/actions/de.berlios.smb4k.mounthelper.policy

%files -n %libsmb4kcore
%_K4libdir/libsmb4kcore.so.%sover
%_K4libdir/libsmb4kcore.so.%sover.*


%changelog
* Fri Feb 01 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 0.10.9-alt2
- fix build requires

* Fri Sep 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.10.9-alt0.M51.1
- built for M51

* Fri Sep 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.10.9-alt1
- new version

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 0.10.7-alt0.M51.1
- build for M51

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 0.10.7-alt1
- inittial built (ALT#20974)
