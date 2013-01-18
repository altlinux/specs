%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir

%define theme kmobile
%define Theme KMobile
%define kdeconfdir %_K4sysconfdir/kde4
%define thisconfdir %kdeconfdir/%theme

%define major 0
%define minor 3
%define bugfix 0
Name: kde4-settings-%theme
Version: %major.%minor.%bugfix
Release: alt6

Group: Graphical desktop/KDE
Summary: %Theme - specific KDE settings
License: GPL
Url: http://www.altlinux.ru/

BuildArch: noarch

PreReq(post,preun): alternatives >= 0.2
Requires: kde-common >= 4

Source: plasma-contour-config-%version.tar
Source1: kmobile-settings-%version.tar

BuildRequires: cmake gcc-c++ kde-common-devel qmergeinifiles rpm-macros-alternatives

%description
%Theme - specific KDE settings


%prep
%setup -qn plasma-contour-config-%version -a1
mv kmobile-settings-* kmobile-settings

%build
# addon configs
ls -1 skel/dotkde/share/config/* kmobile-settings/appconfig/* | \
while read f; do
    conffile=`basename "$f"`
    qmergeinifiles appconfig/$conffile $f
done

# autostart
mkdir -p autostart
for f in skel/dotconfig/autostart/*.desktop kmobile-settings/autostart/*.desktop
do
    install -m 0644 $f autostart/
done

# prifile.d
rm -rf profile.d/*
install -m 0755 kmobile-settings/profile.d/startkde profile.d/
%ifarch x86_64
echo -e "\n" >> profile.d/startkde
%endif


%install
mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name <<__EOF__
%kdeconfdir/current	%thisconfdir 50
__EOF__

# configs
mkdir -p %buildroot/%thisconfdir/share/config/
install -m 0644 appconfig/* %buildroot/%thisconfdir/share/config/


#
#mkdir -p %buildroot/%kdeconfdir/xdg/menus/applications-merged/
#install -m 0644 %theme.menu %buildroot/%kdeconfdir/xdg/menus/applications-merged/

# autostart
mkdir -p %buildroot/%thisconfdir/share/autostart/
install -m 0644 autostart/* %buildroot/%thisconfdir/share/autostart/

# startkde
install -m 0755 profile.d/startkde %buildroot/%thisconfdir/

#install -m 0644 default-apps %buildroot/%thisconfdir/share/config

%files
%config %_altdir/%name
%config %thisconfdir

%changelog
* Fri Jan 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt6
- don't use gconf

* Tue Nov 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt5
- don't package arch-dependent files

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt4
- fix deleting script contents

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt3
- clean requires

* Fri Nov 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt2
- start proper kwin on arm

* Wed Oct 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Wed Apr 18 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt10.M60P.1
- build for M60P

* Wed Mar 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt11
- increase default font size
- don't autostart klipper

* Thu Mar 01 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt10
- start nepomuk by default

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt9
- don't lock screensaver by default

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt8
- don't autostart krunner

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt7
- set default ksplash theme

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt6
- set qt graphics system to raster by default

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt5
- turn off nepomuk by default

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt4
- add plasmarc

* Mon Feb 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt3
- add startkde include

* Wed Feb 15 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt2
- package kdeglobals

* Tue Feb 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.13-alt1
- initial build
