Name: lightlang
Version: 0.8.6.s
Release: alt1

Summary: Dictionary Shell on Qt4
Summary(ru_RU.UTF-8): Словарь на основе Qt4

License: GPL
Group: Office
Url: http://code.google.com/p/lightlang/
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://lightlang.googlecode.com/files/lightlang-0.8.6-20110413.tar.bz2
Source: http://lightlang.googlecode.com/files/lightlang-%version.tar

# Automatically added by buildreq on Sun Jun 03 2012
# optimized out: fontconfig libgst-plugins libqt4-clucene libqt4-core libqt4-dbus libqt4-declarative libqt4-designer libqt4-gui libqt4-help libqt4-multimedia libqt4-network libqt4-opengl libqt4-script libqt4-scripttools libqt4-sql libqt4-svg libqt4-test libqt4-webkit libqt4-xml libqt4-xmlpatterns pkg-config python-base python-module-distribute python-module-peak python-module-sip python-module-zope python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json
BuildRequires: python-module-PyQt4 python-module-mwlib python-module-paste python-module-xlib sox-base

%description
LightLang is a small and powerfull dictionary shell, writed on qt4 and has a many dictionary (ru-en and en-ru).

%description -l ru_RU.UTF-8
LightLang это маленькая и быстрая словарная оболочка на Qt4, которая содержит в комплекте множество словарей (ru-en и en-ru).

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

# do not use yet
rm -rf %buildroot%_pkgconfigdir/*.pc

# move /usrshare/sl to /var/lib/lightlang
mkdir -p %buildroot/var/lib
mv -v %buildroot%_datadir/sl/ %buildroot/var/lib/%name
ln -s ../../var/lib/%name %buildroot%_datadir/sl

%files
%_bindir/lightlang
%_bindir/llrepo
%_bindir/sl
%_bindir/xsl
%_libdir/xsl/
%_libdir/llrepo/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/sl/
%dir /var/lib/%name/
%attr(1777,root,root) /var/lib/%name/dicts/
%attr(1777,root,root) /var/lib/%name/sounds/
%_datadir/xsl/
%_man1dir/*
%_mandir/ru/man1/*
%_docdir/lightlang/
#%_pkgconfigdir/*.pc

%changelog
* Sun Jun 03 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.6.s-alt1
- new version (0.8.6-20110413) with rpmgs script

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.6.rev927-alt1.qa1.1
- Rebuild with Python-2.7

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.6.rev927-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for lightlang
  * postclean-05-filetriggers for spec file

* Fri Jan 29 2010 Vitaly Lipatov <lav@altlinux.ru> 0.8.6.rev927-alt1
- new version (0.8.6 svn rev 927) import in git
- move shared dict dir to /var/lib/%name
- set 1777 perm on shared dirs with dicts and sounds

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1
- initial build for ALT Linux Sisyphus

* Sat May 30 2009 Alexander Kazancev <kazancas@mandriv.ru>
- build for SVN538

* Thu Apr 23 2009 root <root@mandriva.com> 0.8.6-2mdk
- rebuild

* Sun Mar 22 2009 Alexandr Kazancev <kazancas@mandriva.ru> - 0.8.6
- New release 0.8.6-rc2

* Sun Oct 26 2008 Alexandr Kazancev <kazancas@mandriva.ru> - 0.8.5
- Build for 2009.0

* Sat Jan 27 2008 Alexandr Kazancev <kazancas@mail.ru> - 0.8.5
- First release
