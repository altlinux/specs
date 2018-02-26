%def_without backport
%define gnome2ver 2.90
%define gnome3ver 3.90

Name: altlinux-freedesktop-menu
Version: 0.51
%if_without backport
%def_with gnome3
%def_without gnome2
Release: alt1
%else
%def_without gnome3
%def_with gnome2
Release: alt0.M60P.1
%endif

Summary: Implementation of the freedesktop.org menu specification
License: BSD or GPL
Group: Graphical desktop/Other

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>

#BuildPreReq: rpm-build-xdg
BuildRequires: intltool glib2-devel
BuildArch: noarch

%description
altlinux freedesktop.org menu

%package common
Summary: common files for altlinux freedesktop menus
Group: Graphical desktop/Other
Requires(pre): %name-icon-theme
Requires: %name-icon-theme
Requires: wm-common-freedesktop

%description common
%summary

%package nested-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires(pre): %name-common
Requires: %name-common
Provides: %name

%description nested-menu
freedesktop.org compliant altlinux menu with nested layout

%package shallow-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires(pre): %name-common
Requires: %name-common
Provides: %name
Provides: %name-gnomish-menu

%description shallow-menu
freedesktop.org compliant altlinux menu with shallow layout

%if_with gnome2
%package gnomish-menu
Summary: altlinux freedesktop menu with shallow layout (GNOME-based)
Group: Graphical desktop/Other
Requires(pre): %name-common
Requires: %name-common > 0.39
Provides: %name
Requires: gnome2-menus-resources

%description gnomish-menu
freedesktop.org compliant altlinux menu with shallow layout
that use GNOME desktop directories and looks like GNOME menu.
%endif

%package xfce
Summary: xfce freedesktop menu
Group: Graphical desktop/XFce
Provides: xfce-freedesktop-menu
Conflicts: libgarcon-freedesktop-menu
Obsoletes: libgarcon-freedesktop-menu
Requires: %name

%description xfce
ALTLinux freedesktop.org menu for XFCE

%package enlightenment
Summary: Enlightenment freedesktop menu
Group: Graphical desktop/Other
Provides: enlightenment-freedesktop-menu
Requires(pre): %name
Requires: %name

%description enlightenment
ALTLinux freedesktop.org menu for Enlightenment DE

%package lxde
Summary: lxde freedesktop menu
Group: Graphical desktop/Other
Provides: lxde-freedesktop-menu
Conflicts: lxde-lxmenu-data
Obsoletes: lxde-lxmenu-data < 0.2
# specifics of lxde menu migration
Requires(pre): %name
Requires: %name

%description lxde
ALTLinux freedesktop.org menu for LXDE

%package mate
Summary: mate freedesktop menu
Group: Graphical desktop/Other
Provides: mate-freedesktop-menu
Conflicts: mate-menus-default
#Requires: mate-menus-resources
Requires: %name

%description mate
ALTLinux freedesktop.org menu for MATE

%package gnome
Summary: gnome freedesktop menu
Group: Graphical desktop/GNOME
Provides: gnome2-freedesktop-menu
Conflicts: gnome-menus-default
Provides: gnome-menus = %gnome2ver.%version
Obsoletes: gnome-menus-default < %gnome2ver.%version
Requires: gnome2-menus-resources
Requires: %name

%description gnome
ALTLinux freedesktop.org menu for GNOME

%package gnome3
Summary: gnome3 freedesktop menu
Group: Graphical desktop/GNOME
Provides: gnome3-freedesktop-menu
Conflicts: gnome-menus-default
Provides: gnome-menus = %gnome3ver.%version
Obsoletes: gnome-menus-default < %gnome3ver.%version
Requires: %name

%description gnome3
ALTLinux freedesktop.org menu for GNOME3

%package kde3
Summary: kde3 freedesktop menu
Group: Graphical desktop/KDE
Provides: kde3-freedesktop-menu
Conflicts: kde3-menu-original
Obsoletes: kde3-menu-original
Requires(pre): %name
Requires: %name
Requires: kde3-menu-common
Conflicts: kdelibs <= 3.5.12-alt8

%description kde3
ALTLinux freedesktop.org menu for KDE3

%package kde4
Summary: kde4 freedesktop menu
Group: Graphical desktop/KDE
Provides: kde4-freedesktop-menu = %version
Conflicts: kde4-menu-original
Obsoletes: kde4-menu-original
Requires(pre): %name
Requires: %name
Requires(pre): %name-generic
Requires: %name-generic
#Requires: kde4-menu-common
Conflicts: altlinux-menus
Conflicts: kde4libs <= 4.6.2-alt6
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%description kde4
ALTLinux freedesktop.org menu for KDE4

%package generic
Summary: generic freedesktop menu
Group: Graphical desktop/Other
Provides: generic-freedesktop-menu
Requires(pre): %name
Requires: %name
Conflicts: altlinux-menus
Conflicts: kde4libs <= 4.6.2-alt6
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%description generic
ALTLinux freedesktop.org menu for a generic freedesktop-compliant DE

%prep
%setup

%build
touch AUTHORS ChangeLog NEWS README
intltoolize
%autoreconf 
%configure 
%make_build

%check
cat > ignore.list <<EOF
altlinux-audiovideo-audiovideoediting.directory
altlinux-audiovideo-midi.directory
altlinux-audiovideo-player.directory
altlinux-audiovideo-recorder.directory
altlinux-audiovideo-tuner.directory
altlinux-audiovideo-tv.directory
altlinux-education-construction.directory
altlinux-education-medicalsoftware.directory
altlinux-enlightenment.directory
altlinux-game-roleplaying.directory
altlinux-graphics-rastergraphics.directory
altlinux-java.directory
altlinux-lxde.directory
altlinux-network-instantmessaging.directory
altlinux-network-p2p.directory
altlinux-network-telephony.directory
altlinux-network-videoconference.directory
altlinux-office-flowchart.directory
altlinux-science-medicalsoftware.directory
altlinux-settings-java.directory
altlinux-settings-lxde.directory
altlinux-settings-xfce.directory
altlinux-xfce.directory
EOF

ok=1
for i in desktop-directories/*.directory; do
    j=`basename $i`
    if ! grep $j ignore.list >/dev/null && ! grep 'Name\[ru\]=' $i >/dev/null; then
        echo "$j is not translated - please, update po files"
	ok=0
    fi
done
rm ignore.list
[ $ok -gt 0 ] || exit 1

%install
%makeinstall_std
#find_lang %name

%if_with backport
sed -i s/xfce4-run.desktop/xfrun4.desktop/ %buildroot%_sysconfdir/xdg/menus/xfce-applications.menu
%endif

mkdir -p %buildroot%_sysconfdir/xdg/menus/{,enlightenment-,gnome-,gnome3-,kde3-,lxde-,mate-,xfce-}applications-merged
mkdir -p %buildroot%_sysconfdir/xdg/menus/{,mate-}settings-merged

install -D -m644 layout/kde4-merged.menu %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/50-kde4-merged.menu

# alternatives
mkdir -p %buildroot%_altdir
cat <<EOF >>%buildroot%_altdir/%name-nested-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-nested.menu	1000
EOF
cat <<EOF >>%buildroot%_altdir/%name-shallow-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-shallow.menu	100
EOF
cat <<EOF >>%buildroot%_altdir/%name-gnomish-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-shallow-gnomish.menu	80
EOF

%post lxde
# hack around lxde
touch /etc/xdg/menus/lxde-applications.menu

#files 
#-f %name.lang
#doc AUTHORS ChangeLog NEWS README

%files common
%dir %_sysconfdir/xdg/menus/applications-merged
%_datadir/desktop-directories/altlinux-*.directory
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/altlinux-*.menu

%files nested-menu
%_altdir/%name-nested-menu

%files shallow-menu
%_altdir/%name-shallow-menu

%if_with gnome2
%files gnomish-menu
%_altdir/%name-gnomish-menu
%endif

%files xfce
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/xfce-applications.menu
%dir %_sysconfdir/xdg/menus/xfce-applications-merged

%files lxde
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/lxde-applications.menu
%dir %_sysconfdir/xdg/menus/lxde-applications-merged

%if_with gnome2
%files gnome
%config %_sysconfdir/xdg/menus/gnome-applications.menu
%dir %_sysconfdir/xdg/menus/gnome-applications-merged
%config %_sysconfdir/xdg/menus/settings.menu
%dir %_sysconfdir/xdg/menus/settings-merged
%endif

%if_with gnome3
%files gnome3
%config %_sysconfdir/xdg/menus/gnome3-applications.menu
%dir %_sysconfdir/xdg/menus/gnome3-applications-merged
%endif

%files mate
%config %_sysconfdir/xdg/menus/mate-applications.menu
%dir %_sysconfdir/xdg/menus/mate-applications-merged
%config %_sysconfdir/xdg/menus/mate-settings.menu
%dir %_sysconfdir/xdg/menus/mate-settings-merged


%files kde3
%config %_sysconfdir/xdg/menus/kde3-applications.menu
%dir %_sysconfdir/xdg/menus/kde3-applications-merged

%files generic
%config %_sysconfdir/xdg/menus/applications.menu

%files enlightenment
%config %_sysconfdir/xdg/menus/enlightenment-applications.menu
%dir %_sysconfdir/xdg/menus/enlightenment-applications-merged

%files kde4
%config %_sysconfdir/kde4/xdg/menus/applications-merged/50-kde4-merged.menu
%dir %_sysconfdir/kde4/xdg/menus/applications-merged
%_datadir/kde4/desktop-directories/altlinux-*.directory

%changelog
* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- added menu for MATE (Gnome 2)

* Sun Apr 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- layout/xfce-applications.menu - removed xfhelp4 (#27276)
- note: from now on, backports for p6 should use 0.49 as base

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- added versioned provides for kde4-freedesktop-menu

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- bumped release to allow proper version in p6 branch

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- added tatarian translation

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- support for xfce4-run.desktop (closes: 26801)

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt0.M60P.1
- backport

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- explicitly load /usr/share/gdm desktop files in LXDE menu

* Sun Aug 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.44-alt0.M60P.1
- backport

* Sun Aug 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- killed comments (against KDE4 bugs)

* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt0.M60P.1
- backport

* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- added translation check

* Mon Jul 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.42-alt0.M60P.1
- backport

* Mon Jul 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- simplified Settings > KDE (#25875)

* Mon May 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- build without gnome2, to be included in gnome3 transaction

* Tue May 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- use native gnome2 resources instead of private copy

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- independent gnome3 menu; p6 compatible

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- full conditional support for gnome 3; still p6 compatible

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- aded Net > Blogs, Net > Security; stil p6 compatible

* Sun May 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- submenu adjustments; p6 compatible (use gnome2)

* Thu May 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- conditional support for gnome 3

* Thu May 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- removed references to private kde applications (PATH)

* Wed May 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- added private kde4 desktop-directories

* Tue May 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- removed mergeDir from kde4 menu

* Sat May 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- added more PreReq:'s to help smooth upgrade

* Thu May 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- merge sequence is set according to the menu policy draft

* Tue May 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- enabled KDE4 menu

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- Enlightenment freedesktop menu: does not support MergeDir yet

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- added Enlightenment freedesktop menu

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added generic freedesktop menu (used by Enlightenment)

* Sun May 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- added KDE4 menu (disabled)

* Sat Apr 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- more pixmaps in layouts

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- more pixmaps in layouts

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- nested menu: added Dev>Tools, misc layout improvements 

* Tue Apr 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- added KDE3 menu

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- nested menu: added documentation, preparations for KDE

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- added DE-private merge directories
- updated categories

* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- added shallow gnomish menu (thanks to shrek@)
  based on native GNOME desktop directories.

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- GNOME menu: temporarily removed Obsoletes: gnome-menus-default

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added GNOME menu

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- use System Tools for Gnome and System for the rest

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- use System Tools in shallow menu too (thanks to aris@)

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- use System Tools for applications-system (thanks to aris@)

* Thu Mar 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added shortcut .directory files

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- support for GNOME menu

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- Network menu internally uses Internet for RH/Gnome compatibility

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added native LXDE menu.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- optimizations for LXDE and XFCE settings; ShallowSettings.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- sisyphus release

* Fri Mar 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- shallow layout fixes (thanks to sem@)

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- shallow layout fixes (thanks to gns@)

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- Initial build
