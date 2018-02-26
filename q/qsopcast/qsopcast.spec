%define oname qsopcast_vlc_mplayer
Name: qsopcast
Version: 0.4.16
Release: alt1

Summary: A QT GUI front-end for the executive of P2P TV sopcast

Group: Video
License: GPL
Url: http://code.google.com/p/qsopcast/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://qsopcast.googlecode.com/files/%oname-%version.tar
Source4: sopcast.xpm
Patch: %name-channel.patch
Patch4: %name-0.3.1-trayicon.patch
Patch5: %name-arg.patch
Patch6: %name-gcc43.patch

# Automatically added by buildreq on Wed Sep 07 2011
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ glibc-devel-static libvlc-devel phonon-devel

BuildRequires: desktop-file-utils

#Requires: sp-sc >= 1.1.1

%description
qsopcast is a QT GUI front-end for the Linux command line executive of P2P TV sopcast.
If required sp-sc package is missed in your repository,
you can download sp-sc package from ftp://updates.etersoft.ru/pub/Etersoft/BuildFarm/sp-sc

%prep
%setup -n %oname-%version
#%patch
# use arg as url
#%patch5
#%patch6

%build
export PATH=%_qt4dir/bin:$PATH
pushd src
qmake
lrelease qsopcast.pro
%make_build
popd

%install
mkdir -p %buildroot%_bindir
install -m 755 src/qsopcast %buildroot%_bindir/qsopcast
#install -D -m 644 src/language/language_zh.qm %buildroot%_datadir/locale/zh_CN/LC_MESSAGES/language_zh_CN.qm
mkdir -p %buildroot%_pixmapsdir
install -m 644 %SOURCE4 %buildroot%_pixmapsdir/qsopcast.xpm

mkdir -p %buildroot%_desktopdir
cat >%buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Name=%name
Comment=%summary
Exec=qsopcast
Icon=%name.xpm
Terminal=0
Type=Application
Categories=Application;Multimedia;
EOF
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Multimedia \
	--remove-category=Application \
	--add-category=AudioVideo \
	--add-category=Video \
	--add-category=TV \
	%buildroot%_desktopdir/%name.desktop

%files
%doc README
%_bindir/%name
%_pixmapsdir/*
%_desktopdir/%name.desktop

%changelog
* Tue Sep 06 2011 Vitaly Lipatov <lav@altlinux.ru> 0.4.16-alt1
- new version (0.4.16) with rpmgs script
- build with Qt4

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.5-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qsopcast

* Wed Sep 30 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt5
- remove sp-sc requires due missed on x86_64

* Sat Jan 10 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt4
- fix sp-sc requires
- cleanup spec

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt3
- add comment about sp-sc download page
- add strict requires to sp-sc package
- fix build with gcc 4.3

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for qsopcast

* Sun Mar 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt1
- new version 0.3.5 (with rpmrb script)

* Sun Mar 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus

* Tue Nov 28 2006 Liu Di <liudidi@gmail.com> - 0.2.4-4mgc
- update sp-sc to 1.0.1

* Mon Oct 23 2006 Liu Di <liudidi@gmail.com> - 0.2.4-1mgc
- initial RPM
