%define _unpackaged_files_terminate_build 1

Name:      trac
Version:   1.3.3
Release:   alt1

Group:     Development/Other
Summary:   Integrated scm, wiki, issue tracker and project environment
Url:       http://trac.edgewall.org/
License:   BSD
BuildArch: noarch

Source:    %name-%version.tar

Source1:   trac-0.9-alt-apache2.conf
Source2:   trac-0.9.4-alt-nginx.cgi.conf
Source3:   trac-0.9.4-alt-nginx.fcgi.conf
Source4:   trac-0.9.4-alt-cherokee.cgi.conf
Source5:   trac-0.9.4-alt-cherokee.fcgi.conf
Source6:   trac-passwd
Source7:   trac.init
Source8:   trac.sysconfig
Source9:   trac-restrict-env
Source10:  Alt-linux-team-bar-small.png
Source11:  trac.service

BuildRequires(pre): rpm-macros-apache2
BuildRequires:      python-devel
BuildRequires:      python-module-setuptools
BuildRequires:      python-module-jinja2

Requires: python-module-genshi >= 0.6
Requires: python-modules-sqlite3
Requires: python-module-clearsilver


%description
Trac is a minimalistic web-based software project management and bug/issue
tracking system. It provides an interface to the Subversion revision control
systems, an integrated wiki, flexible issue tracking and convenient report
facilities.

%package contrib
Summary: Trac contribs
Group: Development/Other
Requires: %name = %version

%description contrib
This package contains trac contribs

%package mod_python
Summary: Trac mod_python web frontend
Group: Development/Other
Requires: %name = %version
Requires: apache2

%description mod_python
This package contains trac mod_python web frontend

%package -n python-module-trac-fcgi
Summary: Trac FastCGI web frontend
Group: Development/Other
Requires: %name = %version
Requires: trac-spawn-fcgi

%description -n python-module-trac-fcgi
This package contains trac FastCGI web frontend

%prep
%setup

cp %SOURCE2 nginx-A.trac.cgi.conf
cp %SOURCE3 nginx-A.trac.fcgi.conf
cp %SOURCE4 cherokee-A.trac.cgi.conf
cp %SOURCE5 cherokee-A.trac.fcgi.conf

%__subst "s|site/your_project_logo.png|common/Alt-linux-team-bar-small.png|g" trac/web/chrome.py

%build
%python_build

%install
%python_install

mkdir -p %buildroot%apache2_addonconfdir
sed -e 's,@DATADIR@,%_datadir,g' \
    -e 's,@AHTDOCSDIR@,%apache2_htdocsdir,g' \
    -e 's,@ACONFDIR@,%apache2_confdir,g' \
    -e 's,@LOCALSTATEDIR@,%_localstatedir,g' \
    %SOURCE1 > %buildroot%apache2_addonconfdir/A.%name.conf
install -d %buildroot%_localstatedir/%name %buildroot%_sysconfdir/%name
touch %buildroot%_sysconfdir/%name/passwd
mkdir -p %buildroot/%_bindir
install -m 755 %SOURCE6 %buildroot/%_bindir
install -m 755 %SOURCE9 %buildroot/%_bindir

install -pD -m 755 %SOURCE7 %buildroot/%_initdir/%name
install -pD -m 644 %SOURCE11 %buildroot%_unitdir/%name.service

mkdir -p %buildroot/%_sysconfdir/sysconfig
install -m 644 %SOURCE8 %buildroot/%_sysconfdir/sysconfig/%name

install -m 644 %SOURCE10 %buildroot%python_sitelibdir/%name/htdocs/Alt-linux-team-bar-small.png

rm -rf %buildroot%python_sitelibdir/{admin,db,mimeview,prefs,search,tests,ticket,timeline,util,web,wiki}

%pre
%_sbindir/groupadd -r -f tracadmin ||:
%_sbindir/useradd -r -g tracadmin -d /var/lib/trac -s /dev/null trac \
    2> /dev/null > /dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%post -n python-module-trac-fcgi
%post_service trac-spawn-fcgi

%preun -n python-module-trac-fcgi
%preun_service trac-spawn-fcgi

%files
%doc README.* COPYING AUTHORS THANKS
%_bindir/trac-admin
%_bindir/tracd
%_bindir/trac-passwd
%_bindir/trac-restrict-env
%attr(0750,root,tracadmin) %dir %_sysconfdir/%name
%attr(0660,root,tracadmin) %config(noreplace) %_sysconfdir/%name/passwd
%attr(2770,root,tracadmin) %dir %_localstatedir/%name
%python_sitelibdir/*
%_initdir/%name
%_unitdir/%name.service
%_sysconfdir/sysconfig/%name

%exclude %python_sitelibdir/%name/web/modpython_frontend.*
%exclude %python_sitelibdir/%name/web/fcgi_frontend.*
%exclude %python_sitelibdir/%name/web/_fcgi.*

%files contrib
%doc contrib

%files mod_python
%python_sitelibdir/%name/web/modpython_frontend.*
%config(noreplace) %apache2_addonconfdir/A.%name.conf

%files -n python-module-trac-fcgi
%python_sitelibdir/%name/web/fcgi_frontend.*
%python_sitelibdir/%name/web/_fcgi.*
%doc nginx-A.trac.cgi.conf nginx-A.trac.fcgi.conf
%doc cherokee-A.trac.cgi.conf cherokee-A.trac.fcgi.conf


%changelog
* Thu Feb 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.3-alt1
- version updated to 1.3.3

* Wed Sep 03 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0-alt4
- #30277
- Fixed rpm-filesystem-conflict-file-file
- Fixed init-lsb
- Fixed init-but-no-native-systemd
- Fixed altlinux-policy-obsolete-httpd2-reload

* Wed Apr 17 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0-alt3
- 1.0 Fixed attachments folder permissions

* Wed Apr 17 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0-alt2
- 1.0 New version

* Tue Sep 11 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- 1.0

* Sun Mar 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.3-alt1
- 0.12.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1-alt3.1
- Rebuild with Python-2.7

* Fri Dec 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.1-alt3
- Build localization

* Thu Nov 18 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.1-alt2
- Fix (ALT #24591)

* Fri Nov 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.1-alt1
- 0.12.1
- Drop 40_timeline_author_filter.dpatch.patch

* Tue Apr 20 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11.7-alt1
- 0.11.7
- (ALT #22842)
- Add post_service and preun_service
- Add trac-0.11.7-trac-admin-initenv-fixp-group-privileges.patch for make 0775 permission
- Add patches from Debian
- Add ALT logo :)

* Wed Jan 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11.6-alt1
- 0.11.6
- update trac-0.11.6-tracd-drop-privileges.patch

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt3.1
- Rebuilt with python 2.6

* Mon May 25 2009 Eugene Prokopiev <enp@altlinux.ru> 0.11.2-alt3
- rename subpackage trac-fcgi to python-module-trac-fcgi

* Sat Jan 10 2009 Eugene Prokopiev <enp@altlinux.ru> 0.11.2-alt2
- move nginx/cherokee configuration examples to fcgi subpackage
- add trac-passwd tool and empty /etc/trac/passwd file
- apply trac-drop-privileges.patch for tracd (see upstream #7958)
- add initscript and sysconfig file for tracd
- add trac-restrict-env tool

* Sun Nov 16 2008 Ivan Fedorov <ns@altlinux.org> 0.11.2-alt1
- 0.11.2
- spec cleanup

* Sun Nov 16 2008 Ivan Fedorov <ns@altlinux.org> 0.10.5-alt2
- fix build with new apache

* Wed Jul 30 2008 Ivan Fedorov <ns@altlinux.org> 0.10.5-alt1
- 0.10.5 (bug&security fix release).

* Sun Apr 22 2007 Ivan Fedorov <ns@altlinux.ru> 0.10.4-alt1
- 0.10.4 (bug&security fix release).

* Thu Dec 14 2006 Grigory Batalov <bga@altlinux.ru> 0.10.3-alt1
- 0.10.3 (bug fix release).

* Tue Nov 14 2006 Grigory Batalov <bga@altlinux.ru> 0.10.2-alt1
- 0.10.2 (security fix release).

* Tue Oct 03 2006 Grigory Batalov <bga@altlinux.ru> 0.10-alt1
- 0.10

* Fri Sep 08 2006 Ivan Fedorov <ns@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Sat Apr 22 2006 Ivan Fedorov <ns@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Sat Apr 15 2006 Ivan Fedorov <ns@altlinux.ru> 0.9.4-alt1
- build for ALT Linux Sisyphus

* Tue Mar 14 2006 Grigory Batalov <bga@altlinux.ru> 0.9.4-alt0.M24.1
- 0.9.4
- apache2 config and reload calls
- fcgi.py updated
- pass on fcgi exit
- htdocs: syntax support
- backport to Master 2.4

* Sun Jan 29 2006 Ivan Fedorov <ns@altlinux.ru> 0.9.3-alt2
- splitted out contrib and mod_python subpackages

* Sun Jan 08 2006 Ivan Fedorov <ns@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Sun Jan 08 2006 Ivan Fedorov <ns@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Sat Nov 12 2005 Ivan Fedorov <ns@altlinux.ru> 0.9-alt1
- 0.9

* Sun Oct 09 2005 Ivan Fedorov <ns@altlinux.ru> 0.9.0-alt0.svn2338
- svn trunk

* Thu Oct 06 2005 Ivan Fedorov <ns@altlinux.ru> 0.9.0-alt0.svn2328
- svn trunk

* Sun Jun 26 2005 Ivan Fedorov <ns@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sat Jun 18 2005 Ivan Fedorov <ns@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Wed Jun 08 2005 Ivan Fedorov <ns@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Apr 28 2005 Ivan Fedorov <ns@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Dec 21 2004 Ivan Fedorov <ns@altlinux.ru> 0.8-alt1
- 0.8

* Sat Oct 16 2004 Ivan Fedorov <ns@altlinux.ru> 0.7.1-alt1
- Initial build
