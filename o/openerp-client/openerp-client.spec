%define  rev 2102
%define  branch stable

Name:    openerp-client
Version: 7.0
Release: alt1.r%rev
Summary: Python-based desktop client, based on the Gnome Toolkit, giving you fast access to any OpenERP Server

License: GPL
Group:   Office
Url:     https://launchpad.net/openobject-client

Packager: Andrey Cherepanov <cas@altlinux.ru>

Source:   %name-%version.tar
Source1:  %name.desktop

Patch1:   %name-build-translations.patch

BuildArch: noarch

%py_requires libglade
%py_requires pytz

#add_python_req_skip common modules options printer rpc service tools widget observator screen signal_event widget_search
%add_python_req_skip win32con win32ui

BuildRequires: python-module-egenix-mx-base python-module-paste python-module-peak python-module-pygobject-devel python-module-pygtk-libglade python-modules-encodings
BuildRequires: python-module-pytz

BuildPreReq: rpm-build-python

Provides:  tinyerp-client = %version
Obsoletes: tinyerp-client

%description
OpenERP is an open source suite of business applications. OpenERP GTK
Client (openobject-client) is the Python-based desktop client, based on
the Gnome Toolkit, giving you fast access to any OpenERP Server.

%prep
%setup
%patch1 -p2
subst "s/^version.*$/version = '%version'/g" bin/release.py


# disable library checking due gtk issues
#__subst "s/^check_modules//" ./setup.py
subst "s|\('path.share':\).*|\1 '%_datadir/%name',|g" bin/options.py
subst "s|\('path.pixmaps':\).*|\1 '%_pixmapsdir/%name',|g" bin/options.py
subst "s|'lib'|'%_lib'|g" bin/options.py
subst 's|self.install_libbase|"%python_sitelibdir"|g' mydistutils.py


%build
%python_build
# Build translations
make -f Makefile.translation translate_set

%install
%python_install

# BUG: is not installed (due DISPLAY?)
install %name %buildroot%_bindir/

#mkdir -p %buildroot%_datadir/%name/themes/
#cp -a bin/themes/* %buildroot%_datadir/%name/themes/

ln -s openerp-client/openerp-icon.png %buildroot%_pixmapsdir/openerp-icon.png
install -D -m 0644 %SOURCE1 %buildroot/%_desktopdir/openerp-client.desktop

%find_lang %name

%files -f %name.lang
%_bindir/%name
%doc %_docdir/%name-%version/
%_datadir/%name/
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info
%_desktopdir/*
%_pixmapsdir/*
%doc %_man1dir/*

%changelog
* Tue May 14 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1.r2102
- New version 7.0 (revision 2102)
- Translate desktop file into Russian, fix category and icon

* Wed Jan 16 2013 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt1
- New version 6.1.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.14-alt2.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt2
- update buildreqs

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt1
- new version 5.0.14

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1.1
- Rebuilt with python 2.6

* Sun Jan 04 2009 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- rename package
- new version 5.0.0-rc3

* Thu Feb 21 2008 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt1
- new version 4.2.2 (with rpmrb script)
- build as noarch

* Fri Jan 18 2008 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- new version 4.2.1 (with rpmrb script)
- add glade requires

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2
- reenable check_modules, update buildreq

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt0.1
- new version 3.5.0 (fix bug #9892)
- remove old bug fixes from spec

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt0.1
- initial build for ALT Linux Sisyphus
