Version:	0.9.4
Name:		qtdbf
Release:	alt1
Summary:	A simple DBF viewer and editor
License: 	GPLv2+
Group: 		Databases
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.va-soft.ru/project_8.html
Source0:	%name-%version.tar.gz
Source1:	%name.desktop

BuildRequires: ImageMagick-tools gcc-c++ libqt4-devel

Provides:	qtDbf
Obsoletes:	qtDbf < 0.9.4

%description
A simple DBF viewer and editor. Can be set as default dbf viewer.
Supports XBase, dDbase III, IV, FoxPro 2.x, Visual Foxpro files with memos.
Memo content can be viewed but can't be edited yet.

%prep
%setup -q

%build
subst 's|share/doc/qtdbf|share/doc/qtdbf-%version|g' qtDbf.pro ./src/dbfeditor.cpp
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" qtDbf.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install
mv %buildroot%_bindir/qtDbf %buildroot%_bindir/qtdbf
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 images/qtdbf.svg %buildroot%_liconsdir/%name.png
convert -resize 32x32 images/qtdbf.svg %buildroot%_niconsdir/%name.png
convert -resize 16x16 images/qtdbf.svg %buildroot%_miconsdir/%name.png

%files
%dir %_docdir/%name-%version
%dir %_datadir/%name
%_bindir/*
%_desktopdir/*
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_docdir/%name-%version
%_datadir/%name

%changelog
* Fri Jul 12 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Wed Jul 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.3-alt2
- fixed MimeTipe in desktop-file

* Wed Jul 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.3-alt1
- initial build for ALT Linux
