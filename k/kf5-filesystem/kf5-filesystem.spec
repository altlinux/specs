
%define major 5
%define minor 0
%define bugfix 0

Name: kf5-filesystem
Version: %major.%minor.%bugfix
Release: alt0.1
%K5init altplace

Summary: The basic directory layout for KF5
License: Public Domain
Group: System/Base

Requires: filesystem qt5-base-common

BuildRequires(pre): rpm-build-kf5

%description
The %name package is one of the basic KF5 packages that is installed on
a %distribution system; %name contains the basic directory layout
for the KDE 5, including the correct permissions for the directories.

%install
mkdir -p %buildroot/%_libdir

mkdir -p %buildroot/%_kf5_bin
mkdir -p %buildroot/%_kf5_sbin

mkdir -p %buildroot/%_kf5_icon
mkdir -p %buildroot/%_K5mod
mkdir -p %buildroot/%_K5exec
mkdir -p %buildroot/%_K5start
mkdir -p %buildroot/%_K5app
mkdir -p %buildroot/%_K5emo
mkdir -p %buildroot/%_K5snd
mkdir -p %buildroot/%_K5tmpl
mkdir -p %buildroot/%_K5wall
mkdir -p %buildroot/%_K5srv
mkdir -p %buildroot/%_K5srvtyp
mkdir -p %buildroot/%_K5doc
mkdir -p %buildroot/%_K5l10n
mkdir -p %buildroot/%_K5conf
mkdir -p %buildroot/%_K5cfg

mkdir -p %buildroot/%_kf5_xdgapp
mkdir -p %buildroot/%_desktopdir/kf5
mkdir -p %buildroot/%_K5xdgdir
mkdir -p %buildroot/%_K5xdgmime

mkdir -p %buildroot/%_K5inc
mkdir -p %buildroot/%_K5link
mkdir -p %buildroot/%_K5plug/kf5


ln -s `relative %_kf5_bin %_K5prefix/bin` %buildroot/%_K5prefix/bin
ln -s `relative %_libdir %_K5prefix/lib` %buildroot/%_K5prefix/lib

%files
%_K5prefix/
%dir %_kf5_bin
%dir %_kf5_sbin
%dir %_K5exec
%dir %_K5inc
%dir %_K5link
%dir %_K5plug/kf5
%dir %_desktopdir/kf5

%changelog
* Thu Feb 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.1
- initial build
