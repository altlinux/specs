%define rel %nil

Name: openerp-web
Version: 5.0.14
Release: alt2.1

Summary: Open ERP web - free ERP and CRM software

License: GPL
Group: Office
Url: http://openerp.com

Packager: Denis Klimov <zver@altlinux.org>

Source: http://openerp.com/download/stable/source/%name-%version%rel.tar

%py_requires cherrypy

Requires: python-module-cherrypy >= 3.1.2

BuildArch: noarch
BuildRequires: python-module-PyXML python-module-setuptools

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
%python_build

%install
%python_install
install -pD %buildroot/usr/config/openerp-web.cfg %buildroot%_sysconfdir/openerp-web.cfg
rm -f %buildroot/usr/config/openerp-web.cfg
install -pD %buildroot/usr/scripts/openerp-web %buildroot%_initdir/openerp-web
rm -f %buildroot/usr/scripts/openerp-web
rm -rf %buildroot/usr/doc

%find_lang %name

%files -f %name.lang
%doc doc/ChangeLog doc/LICENSE.txt doc/README.txt
%_bindir/openerp-web
%python_sitelibdir/openerp/
%python_sitelibdir/openerp_web-*
# FIXME: fix installing and using
%python_sitelibdir/locales/*/LC_MESSAGES/messages.mo
%python_sitelibdir/locales/messages.pot
%config(noreplace) %_sysconfdir/openerp-web.cfg
%_initdir/openerp-web


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.14-alt2.1
- Rebuild with Python-2.7

* Mon Apr 11 2011 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt2
- fix cherrypy required version

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt1
- new version (5.0.14) import in git
- fix requires (ALT bug #20497)

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt3.1
- Rebuilt with python 2.6

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 5.0.0-alt3
- set openerp-web.cfg as config(noreplace)

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 5.0.0-alt2
- change place init script and config file

* Sun Mar 29 2009 Denis Klimov <zver@altlinux.org> 5.0.0-alt1
- new version

