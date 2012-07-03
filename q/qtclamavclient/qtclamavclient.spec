Name:		qtclamavclient
Version:	0.02
Release:	alt4
Summary:	QT3 ClamAv client
License:	GPLv2
Group:		Security/Antivirus
Url:		http://www.xystumnet.com/qtclamavclient.html
Source0:	http://www.xystumnet.com/qtclamavclient/%name-%version.tar.gz
Source1:	%name.desktop
Source2:	%name-qt4.desktop
Patch0:		%name-0.02-qt3toqt4.diff
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Requires:	%name-icons

# Automatically added by buildreq on Sun Oct 07 2007 (-bi)
BuildRequires: ImageMagick gcc-c++ libXext-devel libqt3-devel libqt4-devel

%description
This is a small Qt client for ClamAV that uses the STREAM
socket connection to a a clamd server machine where the
daemon is listening to locally scan files.
Compiled with QT3
===================================================
To run this package:
qtclamavclient <server> <port>
by default <server> is localhost and <port> is 3310
qtclamavclient 192.168.0.1 3310

%package -n %name-qt4
Summary:	QT4 ClamAv client
Group:		Security/Antivirus
Requires:	%name-icons
Provides:	%name

%description -n %name-qt4
This is a small Qt client for ClamAV that uses the STREAM
socket connection to a a clamd server machine where the
daemon is listening to locally scan files.
Compiled with QT4
===================================================
To run this package:
qtclamavclient-qt4 <server> <port>
by default <server> is localhost and <port> is 3310
qtclamavclient-qt4 192.168.0.1 3310

%package -n %name-doc
Summary:	Howtos for QT3/4 ClamAv client
Group:		Books/Howtos
BuildArch:	noarch

%description -n %name-doc
Documentation for QT3/4 ClamAv client

%package -n %name-icons
Summary:	Icons for QT3/4 ClamAv client
Group:		Security/Antivirus
BuildArch:	noarch

%description -n %name-icons
Shared icons for QT3/4 ClamAv client

%prep
%setup -q

%build
# with qt3
export OLDPATH=$PATH
export PATH=$PATH:$QTDIR/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build
mv ./%name ./%name-qt3

# with qt4
export PATH=$OLDPATH:%_qt4dir/bin
qt3to4 -alwaysOverwrite %name.pro
make clean
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
%__install -Dp -m 0755 %name-qt3 %buildroot%_bindir/%name
%__install -Dp -m 0755 %name %buildroot%_bindir/%name-qt4

# icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 clamav.xpm %buildroot%_liconsdir/%name.png
convert -resize 32x32 clamav.xpm %buildroot%_niconsdir/%name.png
convert -resize 16x16 clamav.xpm %buildroot%_miconsdir/%name.png

# menus
%__install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
%__install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name-qt4.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop

%files -n %name-qt4
%_bindir/%name-qt4
%_desktopdir/%name-qt4.desktop

%files -n %name-doc
%doc AUTHORS INSTALL README COPYING

%files -n %name-icons
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.02-alt4
- delete post/postun scripts (new rpm)

* Sun Sep 07 2008 Motsyo Gennadi <drool@altlinux.ru> 0.02-alt3
- set 'noarch' for %name-icons and %name-doc packages (new rpm supported)

* Sat Jun 07 2008 Motsyo Gennadi <drool@altlinux.ru> 0.02-alt2
- fix repocop warning for pixmaps in non-standard locations
  + generated and separated icons to additional package

* Sat Oct 06 2007 Motsyo Gennadi <drool@altlinux.ru> 0.02-alt1
- build for Sisyphus
- add icons & menus

* Sun Jul 01 2007 Motsyo Gennadi <drool@altlinux.ru> 0.02-alt0.M40.1
- build for M40
- run buildreq -bi

* Thu Mar 29 2007 Motsyo Gennadi <drool@altlinux.ru> 0.02-alt0.M24.1
- initial build for ALT Linux (ALM-2.4)
