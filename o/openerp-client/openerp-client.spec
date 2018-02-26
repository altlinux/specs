%define rel %nil
%define branch stable
Name: openerp-client
Version: 5.0.14
Release: alt2.1

Summary: Open ERP client - free ERP and CRM software

License: GPL
Group: Office
Url: http://openerp.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://openerp.com/download/%branch/source/%name-%version%rel.tar

BuildArch: noarch

%py_requires libglade

#add_python_req_skip common modules options printer rpc service tools widget observator screen signal_event widget_search
%add_python_req_skip win32con win32ui

# manually removed: eric
# Automatically added by buildreq on Sun Oct 24 2010
BuildRequires: python-module-egenix-mx-base python-module-paste python-module-peak python-module-pygobject-devel python-module-pygtk-libglade python-modules-encodings


BuildPreReq: rpm-build-python

Provides: tinyerp-client = %version
Obsoletes: tinyerp-client

%description
Open ERP is a complete ERP and CRM. The main features are accounting
(analytic and financial), stock management, sales and purchases
management, tasks automation, marketing campaigns, help desk, POS,
etc. Technical features include a distributed server, flexible
workflows, an object database, a dynamic GUI, customizable reports,
and SOAP and XML-RPC interfaces.

%prep
%setup -n %name-%version%rel
# disable library checking due gtk issues
#__subst "s/^check_modules//" ./setup.py
%__subst "s|\('path.share':\).*|\1 '%_datadir/%name',|g" bin/options.py
%__subst "s|\('path.pixmaps':\).*|\1 '%_pixmapsdir/%name',|g" bin/options.py
%__subst "s|'lib'|'%_lib'|g" bin/options.py
%__subst 's|self.install_libbase|"%python_sitelibdir"|g' mydistutils.py


%build
%python_build

%install
%python_install

# BUG: is not installed (due DISPLAY?)
install %name %buildroot%_bindir/

#mkdir -p %buildroot%_datadir/%name/themes/
#cp -a bin/themes/* %buildroot%_datadir/%name/themes/

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_docdir/%name-%version%rel/
%_datadir/%name/
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info
#%_desktopdir/*
%_pixmapsdir/*
%_man1dir/*

%changelog
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
