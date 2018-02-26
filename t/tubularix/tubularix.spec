Name: tubularix
Summary: Tubularix is a game similar to Tetrix but seen from a tubular perspective
Version: 0.5.1.7
Release: alt1
License: GPL
Group: Games/Arcade
Url: http://tubularix.sourceforge.net/
Source0: http://dl.sourceforge.net/sourceforge/%name/%name-src-%version.tar.gz
Source1: licon.png
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: gcc-c++ libqt4-devel

%description
Tubularix is a game similar to Tetrix but seen from a tubular
perspective. Game's rules and behavior are very similar to
the Tetrix ones. It's written in c++ with the Qt 4 libraries.

%prep
%setup -n %name
cp %SOURCE1 icon.png
%build
# move icon out of pixmaps
sed -i 's@/share/pixmaps/@/../%_iconsdir/hicolor/128x128/apps/@' %name.pro
qmake-qt4
%make_build
sed -i '/Path=/d' icons/%name.desktop

%install
qmake-qt4
%makeinstall INSTALL_ROOT=%buildroot
# legacy icon
install -D icon.png %buildroot%_liconsdir/%name.png
# menu
#suse_update_desktop_file -i %name Game BlocksGame

%files
%doc README LICENSE CHANGELOG COPYING
%exclude %_datadir/doc/packages/*

%_bindir/*
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/applications/%name.desktop

#defattr(664,root,games,775)
%dir %_datadir/games/%name
%_datadir/games/%name/*.qm

%changelog
* Mon Jun 27 2011 Fr. Br. George <george@altlinux.ru> 0.5.1.7-alt1
- Autobuild version bump to 0.5.1.7

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 0.5.1.5-alt1
- Autobuild version bump to 0.5.1.5

* Fri Sep 10 2010 Fr. Br. George <george@altlinux.ru> 0.5.0.1-alt1
- Version up

* Thu Aug 19 2010 Fr. Br. George <george@altlinux.ru> 0.4.1.12-alt1
- Version up

* Thu Apr 29 2010 Fr. Br. George <george@altlinux.ru> 0.4.0.3-alt1
- Version up

* Thu Sep 24 2009 Fr. Br. George <george@altlinux.ru> 0.2.7.0-alt1
- Version up

* Thu Aug 06 2009 Fr. Br. George <george@altlinux.ru> 0.2.0.1-alt2
- Remove 'Path=' from desktop file (closes #20429)

* Wed Jul 29 2009 Fr. Br. George <george@altlinux.ru> 0.2.0.1-alt1
- Version up

* Thu Jun 25 2009 Fr. Br. George <george@altlinux.ru> 0.1.7.1-alt1
- Version up

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 0.1.5.2-alt1
- Version up

* Wed Apr 08 2009 Fr. Br. George <george@altlinux.ru> 0.1.3.3-alt1
- Initial build from PackMan

* Tue Apr 07 2009 Toni Graffy <toni@links2linux.de> - 0.1.3.3-0.pm.1
- update to 0.1.3.3
* Thu Apr 02 2009 Toni Graffy <toni@links2linux.de> - 0.1.3.2-0.pm.1
- update to 0.1.3.2
- using upstreams icon
- switched to %%makeinstall
* Tue Mar 31 2009 Toni Graffy <toni@links2linux.de> - 0.1.3.1-0.pm.1
- update to 0.1.3.1
* Thu Mar 26 2009 Toni Graffy <toni@links2linux.de> - 0.1.2.0-0.pm.1
- initial release 0.1.2.0
