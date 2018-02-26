Name: kniga
Version: 0.1.11
Release: alt4.qa1

Summary: Kniga is Qt-based advanced text viewer for Linux
License: GPL
Group: Office

Url: http://kniga.linux.kiev.ua
Source: %name-%version.tar.bz2
Source1: %name.menu
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed May 14 2008
BuildRequires: gcc-c++ libqt3-devel ImageMagick

%description
Kniga is Qt-based advanced text viewer for Linux

%prep
%setup -n %name
subst "s,/opt/kniga/doc,/usr/share/doc/kniga,g" kniga.pro src/config.h
subst "s,/opt/kniga/bin,/usr/bin,g" kniga.pro
subst "s,/opt/kniga,/usr/share/kniga,g" kniga.pro src/config.h
subst "s,/kniga/icons,/icons,g" kniga.pro
subst "s,i18n,translations,g" kniga.pro src/config.h
subst "s,icon.png,kniga_icon.png,g" kniga.pro src/kniga.cpp
mv pic/icon.png pic/kniga_icon.png
mv i18n translations

%build
unset QTDIR || : ; . /etc/profile.d/qt3dir.sh ; PATH=$PATH:$QTDIR/bin
lrelease kniga.pro
qmake
subst "s,../../../../,/usr/,g" Makefile
%make

%install
%make_install INSTALL_ROOT=%buildroot install

mkdir -p %buildroot%_liconsdir
convert -size 48x48 %buildroot%_iconsdir/kniga_icon.png %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Kniga
GenericName=Text Viewer
Comment=Kniga is Qt-based advanced text viewer for Linux
Icon=%name
Exec=%name %%f
Terminal=false
Categories=Office;Viewer;
MimeType=text/plain;text/english;
EOF

%files
%_bindir/*
%doc %_docdir/%name
%_datadir/%name
%_desktopdir/%{name}.desktop
%_iconsdir/*.png
%_liconsdir/%name.png

%changelog
* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.11-alt4.qa1
- NMU: converted menu to desktop file

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.1.11-alt4
- applied repocop patch

* Wed May 14 2008 Michael Shigorin <mike@altlinux.org> 0.1.11-alt3
- fixed x86_64 build
- more spec cleanups
- updated Packager:

* Tue May 13 2008 Michael Shigorin <mike@altlinux.org> 0.1.11-alt2
- picked up an orphan
- spec macro abuse cleanup
- buildreq

* Wed Jun 15 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.1.11-alt1
- First Sisyphus build
