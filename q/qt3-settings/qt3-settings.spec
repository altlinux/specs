# Versions
%define rname	qt
%define major	3
%define minor	3
%define bugfix	4
%define rlz alt4

%define qtname %rname%major
%define qtdir %_libdir/%qtname
%define kdename kde3
%define libkdedir %_libdir/%kdename

Name: %qtname-settings
Version: %major.%minor
Release: %rlz

Group: System/Libraries
Summary: Qt%major settings
Url: http://www.trolltech.com/products/qt.html
License: GPL & QPL

Source0: qtrc
Source10: qt3-set-QTDIR-environment-sh
Source11: qt3-set-QTDIR-environment-csh

%package -n lib%name
Summary: Qt%major settings files
Group: System/Libraries
Conflicts: lib%qtname <= 3.3.3-alt5

%description -n lib%name
Qt%major settings files

%description
Qt%major settings files

%prep
%setup -q -T -c
%build
%install

install -d -m 0755 %buildroot/%_sysconfdir/%qtname/settings
install -m 644 %SOURCE0 %buildroot/%_sysconfdir/%qtname/settings

install -d -m 0755 %buildroot/%_sysconfdir/profile.d/
install -m 0755 %SOURCE10 %buildroot/%_sysconfdir/profile.d/qt%{major}dir.sh
install -m 0755 %SOURCE11 %buildroot/%_sysconfdir/profile.d/qt%{major}dir.csh

for f in %buildroot/%_sysconfdir/profile.d/qt* \
	%buildroot/%_sysconfdir/%qtname/settings/*
do
    sed -i "s|@QTDIR@|%qtdir|" "$f"
    sed -i "s|@LIBKDEDIR@|%libkdedir|" "$f"
done

%files -n lib%name
%config(noreplace) %_sysconfdir/profile.d/qt3dir.csh
%config(noreplace) %_sysconfdir/profile.d/qt3dir.sh
%_sysconfdir/%qtname

%changelog
* Wed Jan 25 2006 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt4
- fix QTDIR for x86_64

* Mon Nov 28 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt3
- fix %%prep in specfile

* Mon May 23 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt2
- update color sceme
- set default theme to Plastik

* Thu Nov 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3-alt1
- initial spec
