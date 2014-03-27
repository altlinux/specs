%define  unmangled_version 7.0-20140326-002928
%define  addonsdir %python_sitelibdir/openerp/addons

Name: 	 openerp
Version: 7.0
Release: alt1.20140326

Summary: Business Applications Server

	 # See LICENSING-BREAKDOWN
License: AGPLv3 and GPLv3 and BSD and Beerware
Group:   System/Servers
URL:     http://www.openerp.com/

Source0: http://nightly.openerp.com/7.0/nightly/src/openerp-%{unmangled_version}.tar.gz
Source1: openerp.service
Source2: openerp-gen-cert
Source3: README.ALT
Source4: LICENSING-BREAKDOWN
         # https://bugs.launchpad.net/openobject-server/+bug/1167034
Source5: fonts-access.conf
	 # For SysV init 
Source6: openerp.init

# Additional components
Source10: google_api-7.0.1.0.zip
Source11: smsclient-7.0.1.0.zip
Source12: oerp_project_git-7.0.1.0.0.zip 
Source13: risk_management-7.0.2.0.zip
Source14: gap_analysis-7.0.1.0.zip
Source15: gap_analysis_project-7.0.1.0.zip
Source16: gap_analysis_project_long_term-7.0.1.0.zip
Source17: openeducat_erp-7.0.1.3.zip 
Source18: planning_management_capacity_planning-7.0.1.0.zip
Source19: planning_management_shared_calendar-7.0.1.0.zip

Patch0: openerp-7.0-setup.patch
        # Patch is not usable upstream.
Patch1: openerp-unbundle-pyftpdlib.patch
        # Patch is not usable upstream.
Patch2: openerp-server.conf.patch
        # https://bugs.launchpad.net/openerp-web/+bug/1177027
Patch3: openerp-unbundle-fonts.patch


BuildArch: noarch

#%%py_requires _imaging pygraphviz feedparser gdata pychart vatnumber vobject _xmlplus xlwt ZSI json

#%%add_python_req_skip ir netsvc osv report sql_db tools wizard printscreen pooler schoolbell
# TODO remove unmets from code
%add_python_req_skip com netsvc osv pooler pythonloader SendtoServer tools uno unohelper xlrd xlutils

# Mageia requires
#Requires: python-pillow

# Fedora requires
# https://fedorahosted.org/fpc/ticket/171
# Requires:  python-trml2pdf
# See BZ 817268
# Requires:   python-faces
          # https://bugzilla.redhat.com/show_bug.cgi?id=956127
#Requires: entypo-fonts
#Requires: ghostscript
          # https://bugzilla.redhat.com/show_bug.cgi?id=956134
#Requires: mnmlicons-fonts

BuildPreReq:   rpm-build-python 
BuildPreReq:   unzip 
BuildRequires: python-devel 
BuildRequires: postgresql9.1-python
BuildRequires: python-module-babel 
BuildRequires: python-module-cli
BuildRequires: python-module-dateutil 
BuildRequires: python-module-distribute 
BuildRequires: python-module-docutils 
BuildRequires: python-module-feedparser 
BuildRequires: python-module-gdata 
BuildRequires: python-module-imaging 
BuildRequires: python-module-jinja2
BuildRequires: python-module-ldap 
BuildRequires: python-module-libxslt
BuildRequires: python-module-lxml 
BuildRequires: python-module-mako
BuildRequires: python-module-mock
BuildRequires: python-module-openid 
BuildRequires: python-module-psycopg2 
BuildRequires: python-module-pychart 
BuildRequires: python-module-pydot 
BuildRequires: python-module-pyftpdlib
BuildRequires: python-module-pygtk-devel
BuildRequires: python-module-pyparsing
BuildRequires: python-module-pytz 
BuildRequires: python-module-pywebdav 
BuildRequires: python-module-Reportlab 
BuildRequires: python-module-simplejson
BuildRequires: python-module-unittest2
BuildRequires: python-module-vatnumber 
BuildRequires: python-module-vobject 
BuildRequires: python-module-werkzeug
BuildRequires: python-module-xlwt 
BuildRequires: python-module-yaml 
BuildRequires: python-module-ZSI 
 
Provides:  tinyerp-server = %version-%release 
Obsoletes: tinyerp-server <= %version-%release 
Provides:  openerp-server <= %version-%release 
Obsoletes: openerp-server <= %version-%release 
Provides:  openerp-web <= %version-%release 
Obsoletes: openerp-web <= %version-%release 

%description
Server package for OpenERP, the version 7 branch.

OpenERP is a free Enterprise Resource Planning and Customer Relationship
Management software. It is mainly developed to meet changing needs.

The main functional features are: CRM & SRM, analytic and financial
accounting, double-entry stock management, sales and purchases
management, tasks automation, help desk, marketing campaign, ... and
vertical modules for very specific businesses.

Technical features include a distributed server, flexible work-flows, an
object database, dynamic GUIs, custom reports, NET-RPC and XML-RPC
interfaces, ...

For more information, please visit: http://www.openerp.com

This server package contains the core (server) of OpenERP system and all
additions of the official distribution. You may need the GTK client to
connect to this server, or the web-client which serves to HTML browsers.
You can also find more additions (aka. modules) for this ERP system in:
http://www.openerp.com/ or  http://apps.openerp.com/

%package -n openerp-google-api
Summary: OpenERP solution for synchronizing crm_meeting with google calendar
License: AGPLv3+
Group:   Other
URL:     http://www.solutions2use.com/google-calendar 
Requires: openerp
#Requires: python-google-api-python-client

%description -n openerp-google-api 
OpenERP solution for synchronizing crm_meeting with google calendar

%package -n openerp-openeducat
Summary: OpenEduCat is a fully open source ERP system for educational institute
License: AGPLv3+
Group:   Other
URL:     http://www.openeducat.org/
Requires: openerp

%description -n openerp-openeducat
OpenEduCat is a fully open source ERP system for educational
institute, for efficient management of students, faculties, courses
and classes keeping a collaborative platform.

Based on best of class enterprise level architecture make OpenEduCat
ready to use in environments like local infrastructure or a highly
scalable cloud environment.

%package -n openerp-git
Summary: OpenERP project, task connector with Git OpenERP Project management & Git Integration 
License: AGPLv3+
Group:   Other
Requires: openerp
#Requires: python-gitpython >= 0.3.1

%description -n openerp-git
OpenERP project, task connector with Git OpenERP Project management &
Git Integration Features: Allows to configure git report at level of
project. Multiple branches support. Diff view for each
commit. Automatic commit association with task depending upon the
tracking number mention in git commit message.

%package -n openerp-gap-analysis
Summary: This module provides the necessary tools to create and manage your gap-analysis
License: AGPLv3+
Group:   Other
Requires: openerp
#Requires: python-xlwt
#Requires: python-xlutils

%description -n openerp-gap-analysis
This module provides the necessary tools to create and manage your
gap-analysis.  Once the Gap Analysis set as Done, you can generate a
new project with all the task from the Gap Analysis.

%package -n openerp-risk-management
Summary: Business Continuity Management and Risk Management for your projects
License: AGPLv3+
Group:   Other
Requires: openerp

%description -n openerp-risk-management
Manage the risks to your projects in line with your Project Management
Approach. Business Continuity Planning as it should be - for small and
large organisations. Avoid the 'Buried Word Document Syndrome' manage
your actions to deal with your risks within OpenERP Project Tasks.

%package -n openerp-extras
Summary: Extra addons to OpenERP
License: AGPLv3+
Group:   Other
Requires: openerp

%description -n openerp-extras
Extra addons to OpenERP

%package httpd-fonts-access
Summary: Apache2 configuration to allow fonts access
Group:   System/Servers
Requires: apache2-base

%description  httpd-fonts-access
Allow web application to access the /usr/share/fonts directory tree.

%package  full
Summary:  OpenERP with all additional modules
Group:    System/Servers
Requires: openerp = %version-%release
Requires: openerp-google-api = %version-%release
Requires: openerp-openeducat = %version-%release
Requires: openerp-git = %version-%release
Requires: openerp-gap-analysis = %version-%release
Requires: openerp-risk-management = %version-%release
Requires: openerp-extras = %version-%release

%description  full
OpenERP with all additional modules.

%prep
%setup -q -n openerp-%{unmangled_version}
%patch -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

# Unpack addition components
unzip %SOURCE10 -d openerp/addons
unzip %SOURCE11 -d openerp/addons
unzip %SOURCE12 -d openerp/addons
unzip %SOURCE13 -d openerp/addons
unzip %SOURCE14 -d openerp/addons
unzip %SOURCE15 -d openerp/addons
unzip %SOURCE16 -d openerp/addons
unzip %SOURCE17 -d openerp/addons
unzip %SOURCE18 -d openerp/addons
unzip %SOURCE19 -d openerp/addons

#  permissions tracker bug: https://bugs.launchpad.net/bugs/993414
chmod 644 openerp/addons/l10n_vn/*.xml
sed -i -e '1i#!/usr/bin/env python' \
    openerp/addons/base_report_designer/openerp_sxw2rml/openerp_sxw2rml.py

# Remove and don't use at all.
# https://bugs.launchpad.net/openerp-web/+bug/1177027
rm -f openerp/addons/auth_oauth/static/lib/zocial/css/zocial-regular-webfont*

# Remove bundled fonts packaged as dependencies, see patch3.
rm -f openerp/addons/web/static/src/font/entypo-webfont*
rm -f openerp/addons/web/static/src/font/mnmliconsv21-webfont*

# Empty and of no use.
rm openerp/addons/base_report_designer/openerp_sxw2rml/office.dtd

# Foreign packaging.
rm -rf win32 debian setup.nsi

# Prebuilt .xpi and .jar files, not usable.
rm -r openerp/addons/plugin_thunderbird

# Version control files:
rm -rf $(find . -name .hg_\* -o -name .bzrignore)

%build
#python -c "import compileall, os; compileall.compile_dir(os.path.join(os.environ['PWD'], 'doc'), force=True)"
#python -O -c "import compileall, os; compileall.compile_dir(os.path.join(os.environ['PWD'], 'doc'), force=True)"
NO_INSTALL_REQS=1 %python_build

%install
python ./setup.py --quiet install --root=%{buildroot}

subst 's|%buildroot|/|g' %buildroot%_bindir/openerp-server

rm %buildroot/usr/openerp/.apidoc

# Move all content from /usr/openerp to python sutelibdir
rm -r %buildroot%python_sitelibdir/openerp
mv %buildroot/usr/openerp %buildroot%python_sitelibdir

install -m 644 -D install/openerp-server.conf  \
    %buildroot%_sysconfdir/openerp/openerp-server.conf
install -d %buildroot%_sysconfdir/openerp/start.d
install -d %buildroot%_sysconfdir/openerp/stop.d

install -D -m 644 %SOURCE1 %buildroot%_unitdir/openerp.service
install -D -m 755 %SOURCE6 %buildroot%_initdir/openerp

install -D -m 755 %SOURCE2 %buildroot%_sbindir/openerp-gen-cert
install -m 644 %SOURCE3 %SOURCE4 .

install -d %buildroot%_datadir/openerp/pixmaps
install -m 644 -D install/*.png  %buildroot%_datadir/openerp/pixmaps

install -D -m 644 install/openerp-server.1   %buildroot%_man1dir/openerp-server.1
install -D -m 644 install/openerp_serverrc.5 %buildroot%_man5dir/openerp-serverrc.5
# https://bugs.launchpad.net/openobject-server/+bug/1167336
ln -s %_man5dir/openerp-serverrc.5 %buildroot%_man5dir/openerp-server.conf.5

install -d %buildroot%_logdir/openerp
install -d %buildroot%_spooldir/openerp
install -d %buildroot%_runtimedir/openerp

install -m 644 -pD %SOURCE5 %buildroot/%_sysconfdir/httpd2/conf.d/fonts-access.conf

install -m 644 openerp/import_xml.rng %buildroot%python_sitelibdir/openerp
install -d %buildroot%python_sitelibdir/openerp/addons/base/security
install -m 644 openerp/addons/base/security/* \
    %buildroot%python_sitelibdir/openerp/addons/base/security

install -d %{buildroot}/%{_datadir}/openerp/pixmaps
install -m 644 -D install/*.png  %{buildroot}/%{_datadir}/openerp/pixmaps

# Fix title in OpenEduCat
sed -i -e "s!<title>OpenEduCat</title>!!" \
   %buildroot%addonsdir/openeducat_erp/controllers/main.py

# Move additional component documentation to _docdir
install -Dm0644 openerp/addons/gap_analysis/gap_analysis_how_to.pdf %buildroot%_datadir/openerp/gap_analysis_how_to.pdf

# Set modules list
echo "google_api" > %buildroot%_datadir/openerp/google-api.modules
echo "openeducat_erp" > %buildroot%_datadir/openerp/openeducat.modules
echo "oerp_project_git" > %buildroot%_datadir/openerp/git.modules
echo "gap_analysis,gap_analysis_project,gap_analysis_project_long_term" > %buildroot%_datadir/openerp/gap-analysis.modules
echo "risk_management" > %buildroot%_datadir/openerp/risk-management.modules
echo "smsclient,planning_management_capacity_planning,planning_management_shared_calendar" > %buildroot%_datadir/openerp/extras.modules

# Clean pixmaps
rm -f %buildroot%_datadir/openerp/pixmaps/*.png

%find_lang %name

%pre
getent group openerp > /dev/null || /usr/sbin/groupadd -r openerp
getent passwd openerp > /dev/null || \
%_sbindir/useradd -M -r -g openerp -c 'OpenERP Server' \
     -d / -s /sbin/nologin openerp 2> /dev/null ||:

%post
%post_service openerp

%preun
%preun_service openerp

# TODO
#%%postun
#%%systemd_postun_with_restart openerp.service

%files -f %name.lang
%doc LICENSE README README.ALT LICENSING-BREAKDOWN
%doc openerp/addons/web_graph/static/lib/flotr2/lib/jasmine/MIT.LICENSE
%doc openerp/addons/web/tests/qunitsuite/grunt/license
%doc openerp/addons/web_calendar/static/lib/dhtmlxScheduler/license.txt
%_bindir/openerp-server
%_sbindir/openerp-gen-cert
%_unitdir/openerp.service
%_initdir/openerp
%python_sitelibdir/openerp
%python_sitelibdir/openerp-*.egg-info
%_spooldir/openerp
%attr(0755,openerp,openerp) %_logdir/openerp
%attr(0755,openerp,openerp) %_runtimedir/openerp
%attr(0755,root,openerp) %dir %_sysconfdir/openerp
%dir %_sysconfdir/openerp/start.d
%dir %_sysconfdir/openerp/stop.d
%attr(0660,root,openerp)  %config(noreplace) %_sysconfdir/openerp/openerp-server.conf
#%%attr(-,openerp,openerp) %ghost %_logdir/openerp/openerp-server.log
%exclude %addonsdir/google_api
%exclude %addonsdir/openeducat_erp
%exclude %addonsdir/oerp_project_git
%exclude %addonsdir/gap_analysis
%exclude %addonsdir/gap_analysis_project
%exclude %addonsdir/gap_analysis_project_long_term
%exclude %addonsdir/risk_management
%exclude %addonsdir/smsclient
%exclude %addonsdir/planning_management_capacity_planning
%exclude %addonsdir/planning_management_shared_calendar
%doc %_man1dir/openerp-server.1*
%doc %_man5dir/openerp-*.5*

%files -n openerp-google-api
%doc %_datadir/openerp/google-api.modules
%addonsdir/google_api

%files -n openerp-openeducat
%doc %_datadir/openerp/openeducat.modules
%addonsdir/openeducat_erp

%files -n openerp-git
%doc %_datadir/openerp/git.modules
%addonsdir/oerp_project_git

%files -n openerp-gap-analysis
%doc %_datadir/openerp/gap_analysis_how_to.pdf
%doc %_datadir/openerp/gap-analysis.modules
%addonsdir/gap_analysis
%addonsdir/gap_analysis_project
%addonsdir/gap_analysis_project_long_term

%files -n openerp-risk-management
%doc %_datadir/openerp/risk-management.modules
%addonsdir/risk_management

%files -n openerp-extras
%doc %_datadir/openerp/extras.modules
%addonsdir/smsclient
%addonsdir/planning_management_capacity_planning
%addonsdir/planning_management_shared_calendar

%files httpd-fonts-access
%_sysconfdir/httpd2/conf.d/fonts-access.conf

%files full

%changelog
* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1.20140326
- New version 7.0 (ALT #27570) syncronized with Mageia and Fedora
- Rename package and service to openerp
- Package some additional components (thanks Mageia) in openerp-full

* Tue Jan 22 2013 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt1
- New version 6.1
- Obsoletes openerp-web
- Run daemon under user _openerp privileges
- Add daemon script to run levels

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
