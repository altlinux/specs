%define rname	qt
%define major	4
%define minor	5
%define bugfix	3
%define rlz alt2

%define qtname %rname%major
%define qtdir %_libdir/%qtname
%define kdename kde4
%define libkdedir %_libdir/%kdename

Name: %rname%major-settings
Version: %major.%minor
Release: %rlz

Group: System/Libraries
Summary: Qt%major settings
Url: http://www.trolltech.com/products/qt.html
License: GPL & QPL

Requires: %rname%major-common

Source0: Trolltech.conf
Source10: qt4-set-QTDIR-environment-sh
Source11: qt4-set-QTDIR-environment-csh

%description
Qt%major settings files

%prep
%setup -q -T -c
%build
%install

install -d -m 0755 %buildroot/%_sysconfdir/%rname%major
install -d -m 0755 %buildroot/%_sysconfdir/xdg
install -d -m 0755 %buildroot/%_sysconfdir/xdg/Trolltech

install -m 644 %SOURCE0 %buildroot/%_sysconfdir/xdg/
ln -s ../..%_sysconfdir/xdg/Trolltech.conf %buildroot/%_sysconfdir/%rname%major/

install -d -m 0755 %buildroot/%_sysconfdir/profile.d/
install -m 0755 %SOURCE10 %buildroot/%_sysconfdir/profile.d/qt%{major}dir.sh
install -m 0755 %SOURCE11 %buildroot/%_sysconfdir/profile.d/qt%{major}dir.csh

for f in %buildroot/%_sysconfdir/profile.d/qt* \
	%buildroot/%_sysconfdir/xdg/* %buildroot/%_sysconfdir/xdg/Trolltech/*
do
    [ -f "$f" ] || continue
    sed -i "s|@QTDIR@|%qtdir|" "$f"
    sed -i "s|@LIBKDEDIR@|%libkdedir|" "$f"
done

%files
#%config(noreplace) %_sysconfdir/profile.d/qt%{major}dir.sh
#%config(noreplace) %_sysconfdir/profile.d/qt%{major}dir.csh
#%dir %_sysconfdir/xdg/Trolltech
#%config(noreplace) %_sysconfdir/xdg/Trolltech.conf
#%dir %_sysconfdir/%rname%major
#%config %_sysconfdir/%rname%major/Trolltech.conf

%changelog
* Wed Oct 28 2009 Sergey V Turchin <zerg@altlinux.org> 4.5-alt2
- remove all default settings

* Tue Mar 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.5-alt1
- new version

* Wed May 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.4-alt1
- new version

* Fri Jun 01 2007 Sergey V Turchin <zerg at altlinux dot org> 4.3-alt1
- new version

* Tue Oct 03 2006 Sergey V Turchin <zerg at altlinux dot org> 4.2-alt1
- new version
- don't package compatibility symlinks from /etc/qt4

* Sun Feb 26 2006 Sergey V Turchin <zerg at altlinux dot org> 4.1-alt2
- moved to /etc/xdg
- make architecture depended

* Thu Dec 22 2005 Sergey V Turchin <zerg at altlinux dot org> 4.1-alt1
- new version

* Fri Oct 28 2005 Sergey V Turchin <zerg at altlinux dot org> 4.0-alt3
- fix specfile

* Thu Oct 27 2005 Sergey V Turchin <zerg at altlinux dot org> 4.0-alt2
- fix specfile

* Tue Oct 25 2005 Sergey V Turchin <zerg at altlinux dot org> 4.0-alt1
- new Qt4

* Mon May 23 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt2
- update color sceme
- set default theme to Plastik

* Thu Nov 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt1
- initial spec
