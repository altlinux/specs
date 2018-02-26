Name: gjots2
Version: 2.3.8
Release: alt1.1.qa1.1

Summary: A note jotter. Organise your ideas, notes, facts in a hierarchy

License: GPL
Group: Text tools
Url: http://bhepple.freeshell.org/gjots

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://bhepple.freeshell.org/gjots/%name-%version.tar.bz2

BuildArch: noarch
Requires: python%__python_version(libglade) python%__python_version(bonobo)

# manually removed: eric
# Automatically added by buildreq on Wed Jan 25 2006
BuildRequires: python-devel python-modules-compiler python-modules-encodings

BuildPreReq: rpm-build-compat >= 1.2
BuildRequires: desktop-file-utils

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
%setup -q
sed -i "s|lib/gjots2|%python_sitelibdir/%name|g" setup.py
sed -i "s|prefix + '/lib/gjots2|'%python_sitelibdir/%name|g" setup.py bin/%name

%build
%python_build

%install

%python_install

# fix strict python
#sed -i "s,/usr/bin/python,/usr/bin/env python," %name

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=TextTools \
	%buildroot%_desktopdir/gjots2.desktop

%files
# it is still broken
# -f %name.lang
%_docdir/%name-%version/
%_bindir/%name
%python_sitelibdir/%name/
%_desktopdir/*
%_pixmapsdir/*
%_datadir/%name/
%_man1dir/*

%changelog
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
