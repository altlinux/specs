Name: appliance-trac
Version: 0.1
Release: %branch_release alt8.3.1

Summary: Appliance for Trac quick start
License: %gpl3plus
Group: Networking/WWW
URL: http://git.altlinux.org/people/enp/packages/%name.git/
Packager: Eugene Prokopiev <enp@altlinux.ru>
Buildarch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-branch
BuildRequires: rpm-macros-apache2
Requires: apache2-base apache2-mod_wsgi trac

%description
Appliance for Trac quick start

%package scm-git
Summary: Git support for Trac appliance
Group: Networking/WWW
BuildRequires: git-core
Requires: %name = %version python-module-trac-gitplugin subversion-python git-core

%description scm-git
Git support for Trac appliance

%package scm-svn
Summary: Subversion support for Trac appliance
Group: Networking/WWW
Requires: %name = %version subversion subversion-server-dav subversion-python

%description scm-svn
Subversion support for Trac appliance

%prep
%setup

%install
mkdir -p %buildroot
cp -a * %buildroot
mkdir -p %buildroot/%webserver_datadir/%name/env
mkdir -p %buildroot/%webserver_datadir/%name/egg
mkdir -p %buildroot/%webserver_datadir/%name/scm/git
mkdir -p %buildroot/%webserver_datadir/%name/scm/git-template
touch %buildroot/%webserver_datadir/%name/scm/git.lock
mkdir -p %buildroot/%webserver_datadir/%name/scm/svn
mkdir -p %buildroot/%webserver_datadir/%name/scm/svn-template
touch %buildroot/%webserver_datadir/%name/passwd
touch %buildroot/%webserver_datadir/%name/group
mkdir -p %buildroot/%apache2_extra_enabled
touch %buildroot/%apache2_extra_enabled/appliance-trac-env.conf
touch %buildroot/%apache2_extra_enabled/appliance-trac-scm-git.conf
touch %buildroot/%apache2_extra_enabled/appliance-trac-scm-svn.conf

%files
%_bindir/*
%_datadir/*
%exclude %_datadir/%name/scm/*
%config(noreplace) %webserver_datadir/%name/passwd
%config(noreplace) %webserver_datadir/%name/group
%webserver_datadir/*
%exclude %webserver_datadir/%name/scm/*
%config(noreplace) %apache2_extra_available/appliance-trac-env.conf
%config(noreplace) %apache2_extra_start/101-appliance-trac-env.conf
%config(noreplace) %apache2_mods_start/101-appliance-trac-env.conf
%ghost %apache2_extra_enabled/appliance-trac-env.conf

%files scm-git
%_datadir/%name/scm/git
%webserver_datadir/%name/scm/git
%webserver_datadir/%name/scm/git-template
%attr(0660,root,apache2) %webserver_datadir/%name/scm/git.lock
%config(noreplace) %apache2_extra_available/appliance-trac-scm-git.conf
%config(noreplace) %apache2_extra_start/101-appliance-trac-scm-git.conf
%config(noreplace) %apache2_mods_start/101-appliance-trac-scm-git.conf
%ghost %apache2_extra_enabled/appliance-trac-scm-git.conf

%files scm-svn
%_datadir/%name/scm/svn
%webserver_datadir/%name/scm/svn
%webserver_datadir/%name/scm/svn-template
%config(noreplace) %apache2_extra_available/appliance-trac-scm-svn.conf
%config(noreplace) %apache2_extra_start/101-appliance-trac-scm-svn.conf
%config(noreplace) %apache2_mods_start/101-appliance-trac-scm-svn.conf
%ghost %apache2_extra_enabled/appliance-trac-scm-svn.conf

%post
%_sbindir/a2chkconfig > /dev/null
%post_apache2conf

%post scm-svn
%_datadir/%name/scm/svn init-template
%_sbindir/a2chkconfig > /dev/null
%post_apache2conf

%post scm-git
%_datadir/%name/scm/git init-template
%_sbindir/a2chkconfig > /dev/null
%post_apache2conf

%postun
%_sbindir/a2chkconfig > /dev/null
%postun_apache2conf

%postun scm-svn
%_sbindir/a2chkconfig > /dev/null
%postun_apache2conf

%postun scm-git
%_sbindir/a2chkconfig > /dev/null
%postun_apache2conf

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt8.3.1
- Rebuild with Python-2.7

* Wed Dec 30 2009 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt8.3
- NMU
- Fix use %%webserver_datadir/%%name/{passwd,group} and apache2 configs
  (Closes: #22532)

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt8.1
- Rebuilt with python 2.6

* Tue Mar 24 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt8
- update requires

* Thu Jan 29 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt7
- scm templates postinstall creation

* Thu Jan 29 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt6
- git integrated auth support

* Wed Jan 28 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt5
- svn integrated auth support

* Wed Jan 28 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt4
- refactoring

* Wed Jan 28 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt3
- initial svn repo support

* Wed Jan 28 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt2
- initial git repo support

* Tue Jan 27 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- first build for Sisyphus

