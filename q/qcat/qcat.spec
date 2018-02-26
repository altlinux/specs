Name:		qcat
Version:	0.5
Release:	alt5.1
Summary:	A catalog application for various media types
Group:		Databases
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://sourceforge.net/projects/qcat/
Source0:	http://kent.dl.sourceforge.net/sourceforge/qcat/%name-src-%version.tar.gz
Source1:	%name.desktop
Patch0:		%name-0.5-x86_64.diff
Patch1:		%name-0.5-qt4.7.diff
Patch2:		%name-0.5-qt4.7-2.diff

Requires:	libqt4-sql-sqlite

# Automatically added by buildreq on Mon Nov 05 2007 (-bi)
BuildRequires: gcc-c++ ImageMagick libqt4-devel libqt4-sql

%description
A catalog application for various media types - CD, DVD,
NetDrives, USB flash keys, etc. It can import data from
famous WhereIsIt Windows applicaion. In a word this is a
try to make a WhereIsIt-like application for Linux.

%prep
%setup -q -n %name-dist-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
%__install -Dp -m 0755 bin/%name %buildroot%_bindir/%name

# icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 icons/db_icons/catalog_enabled.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 icons/db_icons/catalog_enabled.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icons/db_icons/catalog_enabled.png %buildroot%_miconsdir/%name.png

# menu
%__install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Tue Nov 23 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt5.1
- full fix build for Qt4.7 (thanks to DOOMer for patch)

* Sat Jul 31 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt5
- fix build with Qt4.7

* Wed Feb 18 2009 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt4
- add libqt4-sql-sqlite to requires (#18864)

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3
- delete post/postun scripts (new rpm)

* Sun Dec 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt2
- add Url for Source

* Thu Nov 22 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt1
- fix categories in desktop-file (thanks to Igor Vlasenko for hint)
- fix x86_64 build (thanks to Victor Forsyuk for hint)

* Thu Nov 22 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt1
- fix spec-file (icons)

* Mon Nov 05 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt0
- initial build for ALT Linux
