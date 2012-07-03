BuildRequires: desktop-file-utils
Name:		qgmailnotifier
Summary:	QGMailNotifier is a GMail notifier
License:	GPL
Group:		Networking/Mail
Version:	2008.2
Release:	alt1.qa1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
URL:		http://qt-apps.org/content/show.php/QGMailNotifier?content=85979
Source0:	http://www.codef00.com/projects/%name-%version.tgz
Source1:	%name.desktop

# Automatically added by buildreq on Sat Jan 09 2010 (-bi)
BuildRequires: ImageMagick-tools gcc-c++ libqt4-devel

%description
A portable QT4 based GMail notifier, which is
designed to provide all of the functionality
that the official Windows notifier has, and more.

%prep
%setup -n %name

%build
subst s'|/bin/|/usr/bin/|g' %name.pro
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 img/gmail.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 img/gmail.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 img/gmail.png %buildroot%_miconsdir/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Email \
	%buildroot%_desktopdir/qgmailnotifier.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2008.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qgmailnotifier
  * postclean-03-private-rpm-macros for the spec file

* Fri Jan 08 2010 Motsyo Gennadi <drool@altlinux.ru> 2008.2-alt1
- initial build for ALT Linux
