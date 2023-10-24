Name: gjots2
Version: 3.2.1
Release: alt1

Summary: A note jotter. Organise your ideas, notes, facts in a hierarchy

License: GPLv2
Group: Text tools
Url: http://bhepple.freeshell.org/gjots

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://downloads.sourceforge.net/project/gjots2/gjots2/%version/gjots2-%version.tgz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: desktop-file-utils
BuildRequires: python3-module-setuptools

# missed on p10
BuildRequires: python3-module-wheel

# see %_libdir/girepository-1.0
Requires: libgtk+3-gir libgtksourceview3-gir

AutoProv: no

# FIXME: fix broken autoreq
%add_python3_req_skip common file find general gui prefs printDialog sortDialog version

%description
gjots2 ("gee-jots" or, if you prefer, "gyachts"!) is a way to marshall
and organise your text notes in a convenient, hierachical way. I use
it for all my notes on Unix, my personal bits and pieces, recipes and
even PINs and passwords (encrypted with ccrypt(1)).

You can also use it to "mind-map" your compositions - write down all
your thoughts and then start to organise them into a tree. By
manipulating the tree you can easily reorder your thoughts and
structure them appropriately.

This is a Python/GTK-2 version of the original gjots program by the same author.

%prep
%setup
subst 's|/usr/bin/bash|/bin/bash|' bin/*
#sed -i "s|lib/gjots2|%python_sitelibdir/%name|g" setup.py
#sed -i "s|prefix + '/lib/gjots2|'%python_sitelibdir/%name|g" setup.py bin/%name

%build
%pyproject_build

%install
%pyproject_install

# fix strict python
#sed -i "s,/usr/bin/python,/usr/bin/env python," %name

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=TextTools \
	%buildroot%_desktopdir/gjots2.desktop

%files -f %name.lang
%_docdir/%name-%version/
%_bindir/%name
%_bindir/docbook2gjots
%_bindir/gjots2docbook
%_bindir/gjots2html
%_bindir/gjots2lpr
/usr/bin/gjots2emacs
/usr/bin/gjots2html.py
/usr/bin/gjots2org
/usr/bin/org2gjots
/usr/share/glib-2.0/schemas/org.gtk.gjots2.gschema.xml
/usr/share/metainfo/gjots2.metainfo.xml
%python3_sitelibdir/%name/
%python3_sitelibdir/gjots2-%version.dist-info
%_desktopdir/*
%_pixmapsdir/*
%_datadir/%name/
%_man1dir/*

%changelog
* Sun Oct 22 2023 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- new version 3.2.1 (with rpmrb script)
- switch to pyproject_build, disable AutoProv

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.9-alt1
- new version (3.1.9) with rpmgs script
- switch to python3

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 2.3.15-alt1
- new version 2.3.15 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.8-alt1.1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.3.8-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gjots2
  * postclean-03-private-rpm-macros for the spec file

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt1.1
- Rebuilt with python 2.6

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 2.3.8-alt1
- new version 2.3.8 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.7-alt1
- new version 2.3.7 (with rpmrb script)

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt0.1
- new version 2.3.4
- use desktop/pixmaps dir macroses
- add python libglade requires

* Wed Jan 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt0.1
- initial build for ALT Linux Sisyphus
- disable translations for time
