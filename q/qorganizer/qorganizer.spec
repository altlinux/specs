%define		src qOrganizer
Version:	3.1
Name:		qorganizer
Release:	alt4
Summary:	qOrganizer is a personal organizer
License: 	GPLv2
Group: 		Office
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		https://sourceforge.net/projects/qorganizer
Source0:	http://kent.dl.sourceforge.net/sourceforge/qorganizer/%src-%version.tar.gz
Source1:	%name.desktop
Patch0:		%src-qt-4.5.0.patch

# Automatically added by buildreq on Mon Apr 06 2009 (-bi)
BuildRequires: ImageMagick-tools gcc-c++ libqt4-devel

%description
qOrganizer is a general organizer that includes calendar with
jurnal and schedule for every day in which you can choose to
be reminded of events, a general to-do list for your tasks and
also includes features useful for students like timetable and
a booklet with marks and absences.

%prep
%setup -q -n %src
%patch0 -p1

%build
cd src
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %src.pro
%make_build

%install
cd src
%__install -Dp -m 0755 %src %buildroot%_bindir/%name
%__install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 images/logo.png %buildroot%_miconsdir/%name.png
convert -resize 32x32 images/logo.png %buildroot%_niconsdir/%name.png
convert -resize 48x48 images/logo.png %buildroot%_liconsdir/%name.png

%files
%doc CHANGELOG.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Apr 06 2009 Motsyo Gennadi <drool@altlinux.ru> 3.1-alt4
- fix build with qt4.5 (thanks to E.Ostapets for help)
- refresh BuildReq (run buildreq -bi)
- exclude COPYING from docs

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 3.1-alt3
- delete post/postun scripts (new rpm)

* Sun Dec 09 2007 Motsyo Gennadi <drool@altlinux.ru> 3.1-alt2
- add Url for Source

* Sat Oct 27 2007 Motsyo Gennadi <drool@altlinux.ru> 3.1-alt1
- initial build
