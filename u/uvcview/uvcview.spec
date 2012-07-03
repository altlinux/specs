Name: uvcview
Version: 20071108
Release: alt1.1.qa1

%define LANG                    ru

Summary:  UVCView is a simple USB Video Camera viewer.

Group: Video

License: GPL2

Url: http://freshmeat.net/projects/uvcview/

Source: %url/%name-%version.tar.gz
Source1: uncview.po.tar.bz2
Source2: uvcviev.png

Patch2: uvcview-20070907-stop.patch

BuildPreReq: libgtk+2-devel


%description
UVCView
 UVCView is a simple USB Video Camera viewer. 
 This program is very simple, because it is part of another software
%prep
%setup -a1
%patch2 -p1

%build
%__autoreconf
export FLAGS="%optflags -DNDEBUG -DNO_DEBUG -D_GNU_SOURCE " \
%configure
%make_build
pushd po
make ru.mo
popd
make distdir



%install
%makeinstall
%find_lang %name

install -d -m 755 %buildroot%_desktopdir

cat > %buildroot%_desktopdir/uvcview.desktop << EOF
[Desktop Entry]
Name=uvcview
GenericName[ru]=просмотр камеры uvcview 
Comment=UVCView is a simple USB Video Camera viewer
Icon=uvcview.png
Categories=AudioVideo;Video;TV;
TryExec=/usr/bin/uvcview
Exec=/usr/bin/uvcview
Terminal=true
Type=Application
EOF


install -d -m 755 %buildroot%_datadir/locale/%LANG/LC_MESSAGES

install -m 644 po/ru.mo %buildroot%_datadir/locale/%LANG/LC_MESSAGES/uvcview.mo

install -D -m 644 %SOURCE2 %buildroot%_niconsdir/uvcview.png

			  
%files -f %name.lang
%_bindir/%name
%doc ChangeLog AUTHORS
%_datadir/locale/%LANG/LC_MESSAGES/uvcview.mo
%_desktopdir/uvcview.desktop
%_niconsdir/uvcview.png

%changelog
* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 20071108-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for uvcview
  * pixmap-in-deprecated-location for uvcview
  * postclean-05-filetriggers for spec file

* Fri Feb 29 2008 Hihin Ruslan <ruslandh@altlinux.ru> 20071108-alt1.1
- correct %%*_menus

* Mon Feb 25 2008 Hihin Ruslan <ruslandh@altlinux.ru> 20071108-alt1.0
- new version

* Mon Oct 29 2007 Hihin Ruslan <ruslandh@altlinux.ru> 20070907-alt1.0
- new version

* Fri Aug 31 2007 Hihin Ruslan <ruslandh@altlinux.ru> 20070607-alt1.0
- First build for ALT Linux.
