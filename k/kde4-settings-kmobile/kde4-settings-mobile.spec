
%define theme kmobile
%define Theme KMobile
%define kdeconfdir %_K4sysconfdir/kde4
%define thisconfdir %kdeconfdir/%theme

%define major 0
%define minor 2
%define bugfix 13
Name: kde4-settings-%theme
Version: %major.%minor.%bugfix
Release: alt11

Group: Graphical desktop/KDE
Summary: %Theme - specific KDE settings
License: GPL
Url: http://www.altlinux.ru/

BuildArch: noarch

PreReq(post,preun): alternatives >= 0.2
Requires: kde-common >= 4

Source: plasma-contour-config-%version.tar
Source1: kmobile-settings-%version.tar

BuildRequires: kde-common-devel qmergeinifiles rpm-macros-alternatives

%description
%Theme - specific KDE settings


%prep
%setup -qn plasma-contour-config-%version -a1
mv kmobile-settings-* kmobile-settings

%build

%install
mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name <<__EOF__
%kdeconfdir/current	%thisconfdir 50
__EOF__

#
mkdir -p %buildroot/%thisconfdir/share/config/
install -m 0644 *rc %buildroot/%thisconfdir/share/config
install -m 0644 emaildefaults %buildroot/%thisconfdir/share/config
install -m 0644 kdeglobals %buildroot/%thisconfdir/share/config

#install -m 0644 default-apps %buildroot/%thisconfdir/share/config

#
#mkdir -p %buildroot/%kdeconfdir/xdg/menus/applications-merged/
#install -m 0644 %theme.menu %buildroot/%kdeconfdir/xdg/menus/applications-merged/

# addon configs
pushd kmobile-settings
ls -1 *rc kdeglobals | \
while read f; do
    qmergeinifiles %buildroot/%thisconfdir/share/config/$f $f
done
popd

# autostart
mkdir -p %buildroot/%thisconfdir/share/autostart/
for f in kmobile-settings/*.desktop
do
    install -m 0644 $f %buildroot/%thisconfdir/share/autostart/
done

# startkde
install -m 0755 kmobile-settings/startkde %buildroot/%thisconfdir/

%files
%config %_altdir/%name
%config %thisconfdir

%changelog
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
