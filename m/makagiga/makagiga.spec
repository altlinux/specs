Name: makagiga
Version: 3.4
Release: alt1

Summary: To-do List, Feed Reader, Notepad, Image Viewer/Editor

License: Apache
Url: http://makagiga.sourceforge.net
Group: Office

BuildArch: noarch

BuildRequires: ant java-devel-default

Requires: java

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-source-%version.tar.bz2

%description
Makagiga is a free, easy-to-use, cross-platform application for doing
a variety of tasks, such as text editing, todo listing, feed reading,
and simple image viewing/editing. Plugins are used to implement its various
capabilities. It can perform file import/export,
backing up files into a zip file, Internet searching (Google, Wikipedia),
and more. The interface features custom colors, a tabbed view,
and labels and comments for each file or folder.

%prep
%setup -q -n makagiga-source-%version
chmod a+x tools/*.sh
#mkdir -p src/resources/tips && touch src/resources/tips/dummy.xml
%__subst "s|@@INSTALL_PREFIX@@|%prefix|g" tools/%name tools/%name.desktop

%build
%make_build dist

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_desktopdir/
mkdir -p %buildroot%_niconsdir/
mkdir -p %buildroot%_datadir/%name/

cp dist/boot.jar %buildroot%_datadir/%name/
# FIXME: it is glossitope, can be external?
cp lib/desklet.jar %buildroot%_datadir/%name/
cp dist/i18n.jar %buildroot%_datadir/%name/
cp dist/images.jar %buildroot%_datadir/%name/
cp dist/makagiga.jar %buildroot%_datadir/%name/
cp tools/%name %buildroot%_bindir/
cp tools/%name.desktop %buildroot%_desktopdir
cp makagiga.png %buildroot%_niconsdir/
cp splash.png %buildroot%_datadir/%name/

%files
%doc LICENSE.txt README.html
%_bindir/makagiga
%_desktopdir/*.desktop
%_niconsdir/*.png
%dir %_datadir/%name/
%_datadir/%name/splash.png
%_datadir/%name/boot.jar
%_datadir/%name/desklet.jar
%_datadir/%name/i18n.jar
%_datadir/%name/images.jar
%_datadir/%name/makagiga.jar

%changelog
* Mon May 25 2009 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4 (with rpmrb script) (fix bug #18780)

* Mon Jan 14 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- new version 2.0

* Sat Jul 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus

* Mon Apr 3 2006 Konrad Twardowski
- Updated description and summary

* Tue Jan 31 2006 Konrad Twardowski
- Removed "packages" directory

* Thu Oct 20 2005 Konrad Twardowski
- Added "mousegestures"
- Fixed incompatibility with .deb packages

* Thu Sep 1 2005 Konrad Twardowski
- Changed summary and description

* Mon Aug 1 2005 Konrad Twardowski
- Removed email address
- Updated description
- README.txt -> README.html

* Tue Jul 5 2005 Konrad Twardowski
- Makagiga 0.9 Beta
