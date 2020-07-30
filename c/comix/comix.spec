Summary: Comic book viewer
Name: comix
Version: 4.0.4
Release: alt4
License: GPLv2+
Group: Graphics
Url: http://comix.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: %name-%version.tar.gz

## FC patches
Patch1: FC-4.0.4-archive-directory-removed.patch
Patch2: FC-4.0.4-thumb-imaging_error.patch
Patch3: FC-4.0.4-gettext-usrmove.patch
Patch4: FC-4.0.4-pathname2url-utf8.patch
Patch5: FC-4.0.4-import-PIL-for-Image.patch
Patch6: FC-4.0.4-tobytes.patch
Patch7: FC-4.0.4-PIL6-version-deprecation.patch

## Ubuntu patches

## ALT patches
Patch501: %name.netbsd.patch1
Patch502: %name.netbsd.patch2
Patch503: %name-4.0.3-filechooser.patch
Patch504: %name-fix-install-opts.patch

## done

BuildArch: noarch
##Requires: python-module-imaging

##BuildPreReq: desktop-file-utils shared-mime-info GConf
##BuildRequires: GConf libjpeg-utils python-module-imaging python-module-pygobject unrar python-module-pygtk-devel python-module-pygtk libsqlite3-devel

# Automatically added by buildreq on Sat Mar 09 2019
# optimized out: libdbus-glib libgpg-error python-base python-module-cffi python-module-scandir python-module-six python-modules python-modules-compiler python-modules-ctypes python-modules-logging sh4 shared-mime-info
BuildRequires: GConf python-module-Pillow python-module-pathlib2 python-module-pygobject unrar

%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup
## FC apply patches
%patch1 -p1 -b .missing
%patch2 -p1 -b .debug1
%patch3 -p1 -b .usrmove
%patch4 -p1 -b .p2url
%patch5 -p1 -b .pil
%patch6 -p1 -b .tobytes
%patch7 -p1 -b .version

## Ubuntu apply patches

## ALT apply patches
%patch504 -p2

## Done

# Set correct python2 executable in shebang and scripts
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *) \
        $(find ./ -name '*.py')

%build
## XXX summon buildreq
mkdir BUILD
mv install.py setup.py
%python_build_install --dir=`pwd`/BUILD

%install
mkdir -p %buildroot%prefix
%python_install --dir=%buildroot%prefix

install -D mime/comix.xml %buildroot%_datadir/mime/packages/%name.xml
install -D mime/comicbook.schemas %buildroot%_sysconfdir/gconf/schemas/%name.schemas

%find_lang %name

%files -f %name.lang
%doc ChangeLog COPYING README
%_man1dir/*.1*
%_bindir/*
%_sysconfdir/gconf/schemas/%name.schemas
%_datadir/mime/packages/%name.xml
%_datadir/mime/*
%_datadir/%name/images/*
%_datadir/%name/src/*
%_datadir/applications/comix.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/icons/hicolor/*/mimetypes/*
#_liconsdir/*
%_datadir/icons/hicolor/scalable/apps/comix.svg
#_datadir/pixmaps/*
%exclude %_datadir/mime/XMLnamespaces
%exclude %_datadir/mime/aliases
%exclude %_datadir/mime/application/x-cbr.xml
%exclude %_datadir/mime/application/x-cbt.xml
%exclude %_datadir/mime/application/x-cbz.xml
%exclude %_datadir/mime/generic-icons
%exclude %_datadir/mime/globs
%exclude %_datadir/mime/globs2
%exclude %_datadir/mime/icons
%exclude %_datadir/mime/magic
%exclude %_datadir/mime/mime.cache
%exclude %_datadir/mime/subclasses
%exclude %_datadir/mime/treemagic
%exclude %_datadir/mime/types
%exclude %_datadir/mime/version

%changelog
* Thu Jul 30 2020 Pavel Vasenkov <pav@altlinux.org> 4.0.4-alt4
- NMU: the following fixes applied:
  * version-deprecation
  * correct python2 executable in shebang and scripts
  * correct spec macros and apply install-py opts patch

* Sat Mar 09 2019 Fr. Br. George <george@altlinux.ru> 4.0.4-alt3
- Resurrected from orphaned
- Fedora patches applied

* Tue Nov 18 2014 Andrey Cherepanov <cas@altlinux.org> 4.0.4-alt2.2
- Remove deprecated requirements on python-module-imaging-devel

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.4-alt2.1
- Rebuild with Python-2.7

* Mon Dec 20 2010 Ilya Mashkin <oddity@altlinux.ru> 4.0.4-alt2
- rebuild

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 4.0.4-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for comix
  * desktop-mime-entry for comix
  * shared-mime-info for comix
  * postclean-05-filetriggers for spec file

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.1
- Rebuilt with python 2.6

* Sun Apr 05 2009 Ilya Mashkin <oddity@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Fri Apr 03 2009 Ilya Mashkin <oddity@altlinux.ru> 4.0.3-alt1
- 4.0.3
- apply repocop patch

* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 3.6.5-alt1
- 3.6.5

* Mon Apr 21 2008 Mikhail Pokidko <pma@altlinux.org> 3.6.4-alt3
- netbsd-patches (by php-coder)

* Thu Apr 03 2008 Mikhail Pokidko <pma@altlinux.org> 3.6.4-alt2
- repocop fix

* Fri Mar 21 2008 Mikhail Pokidko <pma@altlinux.org> 3.6.4-alt1
- Version up, fix #15019

* Tue Jul 18 2006 Mikhail Pokidko <pma@altlinux.ru> 3.1.3-alt1
- initial build
