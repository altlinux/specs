Summary: Comic book viewer
Name: comix
Version: 4.0.4
Release: alt2.1
License: GPLv2+
Group: Graphics
Url: http://comix.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: %name-%version.tar.gz
Patch1: %name.netbsd.patch1
Patch2: %name.netbsd.patch2
Patch3: %name-4.0.3-filechooser.patch
BuildArch: noarch
Requires: python-module-imaging

BuildPreReq: desktop-file-utils shared-mime-info GConf
# Automatically added by buildreq on Thu Apr 03 2008 (-bi)
BuildRequires: GConf libjpeg-utils python-module-imaging python-module-imaging-devel python-module-pygobject unrar python-module-pygtk-devel python-module-pygtk libsqlite3-devel

%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup -q
#patch1 -p0
#patch2 -p0
#patch3 -p0 -b .filechooser

%build
%install
%__install -d %buildroot%prefix
%__python install.py install --dir %buildroot%prefix
#__install -p -m 644 Mime/* %buildroot%_datadir/mime/application/

%__mkdir_p $RPM_BUILD_ROOT%_datadir/mime/packages
%__install -c -p -m644 mime/comix.xml \
	$RPM_BUILD_ROOT%_datadir/mime/packages/%name.xml

%__mkdir_p $RPM_BUILD_ROOT%_sysconfdir/gconf/schemas
%__install -c -p -m644 mime/comicbook.schemas \
	$RPM_BUILD_ROOT%_sysconfdir/gconf/schemas/%name.schemas

%find_lang %name
%pre
[ "$1" -gt 1 ] || exit 0

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
	%_sysconfdir/gconf/schemas/%name.schemas >/dev/null

exit 0

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%_sysconfdir/gconf/schemas/%name.schemas > /dev/null



exit 0

%preun
[ "$1" -eq 0 ] || exit 0

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
	%_sysconfdir/gconf/schemas/%name.schemas > /dev/null

exit 0

%postun

[ $1 -eq 0 ] || exit 0

exit 0


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
