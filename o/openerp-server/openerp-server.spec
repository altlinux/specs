%define rel %nil
Name: openerp-server
Version: 5.0.14
Release: alt2.1

Summary: Open ERP server - free ERP and CRM software

License: GPL
Group: Office
Url: http://openerp.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://openerp.com/download/stable/source/%name-%version%rel.tar
Source1: %name.init
Source2: %name.cfg

BuildArch: noarch

%py_requires _imaging pygraphviz

%add_python_req_skip ir netsvc osv report sql_db tools wizard printscreen addons pooler schoolbell

# Automatically added by buildreq on Tue Oct 05 2010
BuildRequires: python-devel python-module-Reportlab python-module-lxml python-module-psycopg2 python-module-pychart python-module-pydot

BuildPreReq: rpm-build-python

Requires: python-module-PyXML

Provides: tinyerp-server = %version-%release
Conflicts: tinyerp-server

%description
Open ERP is a complete ERP and CRM. The main features are accounting
(analytic and financial), stock management, sales and purchases
management, tasks automation, marketing campaigns, help desk, POS,
etc. Technical features include a distributed server, flexible
workflows, an object database, a dynamic GUI, customizable reports,
and SOAP and XML-RPC interfaces.

%prep
%setup -n %name-%version%rel

%build
python -c "import compileall, os; compileall.compile_dir(os.path.join(os.environ['PWD'], 'doc'), force=True)"
python -O -c "import compileall, os; compileall.compile_dir(os.path.join(os.environ['PWD'], 'doc'), force=True)"
%python_build

%install
%python_install

# FIXME: install stage does not run correctly
install -m755 %name %buildroot%_bindir/%name
%__subst 's|%buildroot|/|g' %buildroot%_bindir/%name
#__subst 's|\$@|-c /etc/%name.cfg \$@|g' %buildroot%_bindir/%name

install -pD %SOURCE1 %buildroot%_initdir/openerp-server
install -pD %SOURCE2 %buildroot%_sysconfdir/openerp-server.cfg

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_docdir/%name-%version%rel/
%python_sitelibdir/%name/
%python_sitelibdir/openerp_server*.egg-info
%config(noreplace) %_sysconfdir/openerp-server.cfg
%_initdir/openerp-server
%_man1dir/*
%_man5dir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.14-alt2.1
- Rebuild with Python-2.7

* Tue Feb 22 2011 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt2
- update russian translation for modules
- fix default config path

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt1
- new version 5.0.14
- fix install run script (ALT bug #20460)
- fix requires (ALT bug #20497)

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt3.1
- Rebuilt with python 2.6

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 5.0.0-alt3
- add config and init script files

* Sat Mar 14 2009 Denis Klimov <zver@altlinux.org> 5.0.0-alt2
- new version 5.0.0-3
- remove neeless -q option from setup marcos
- change source url
- add requires to python-module-PyXML
- remove pychart from skip requires
- add sed command for replace needless buildroot item of path in 
  startup script
- add two python command before python_build macros as in 
  rpminstall_sh.txt
- add egg-info file to package

* Sun Jan 04 2009 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- rename package
- new version 5.0.0-rc3

* Thu Feb 21 2008 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt1
- new version 4.2.2 (with rpmrb script)
- build as noarch

* Fri Jan 18 2008 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- new version 4.2.1 (with rpmrb script)

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2
- update buildreq

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt0.1
- new version (3.5.0)

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt0.1
- new version

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt0.1
- initial build for ALT Linux Sisyphus
