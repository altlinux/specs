###############################################################################
#
# General
#
###############################################################################

%define upstreamname webapp
%define svnrevision	35292
%define appprefix	%_datadir/%name

Name: zarafa-%upstreamname
Version: 7.0.8
Release: alt1
License: AGPLv3
Group: Networking/Mail
Summary: New and improved WebApp for the Zarafa Collaboration Platform
Packager: Radik Usupov <radik@altlinux.org>
Url: http://www.zarafa.com/

Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-apache2 rpm-build-php5
BuildRequires:	ant php5-devel php5-mapi java-1.6.0-sun-devel
BuildArch:	noarch

%description
Provides a web-client written in PHP that makes use of Jason and ExtJS
to allow users to make full use of the Zarafa Collaboration Platform
through a modern web browser.

###############################################################################
#
# Build
#
###############################################################################

%prep
%setup

%build
export JAVA_HOME=/usr/lib/jvm/java-1.6.0
ant deploy

###############################################################################
#
# Install
#
###############################################################################

%install

# install webapp
install -d -m 755 %buildroot/%_datadir/%name
cp -ar deploy/* %buildroot/%_datadir/%name

install -d -m 755 %buildroot/%_localstatedir/%name/tmp
mv plugins %buildroot/%_localstatedir/%name/
ln -sf %_localstatedir/%name/plugins %buildroot/%_datadir/%name/plugins

install -d -m 755 %buildroot/%_sysconfdir/zarafa/%upstreamname
mv config.php.dist %buildroot/%_sysconfdir/zarafa/%upstreamname/config.php
%__ln_s -f %_sysconfdir/zarafa/%upstreamname/config.php %buildroot/%_datadir/%name/config.php

install -d -m 755 %buildroot/{%apache2_sites_available,%apache2_sites_enabled}
mv %name.conf %buildroot/%apache2_sites_available/
pushd %buildroot%apache2_sites_enabled
        %__ln_s -f ../sites-available/%name.conf
popd


###############################################################################
#
# File list
#
###############################################################################

%files
%dir %appprefix/
%dir %_sysconfdir/zarafa/
# add writeable temp dir
%attr(3775,root,apache2) %dir %_localstatedir/%name/tmp
%_localstatedir/%name
%_datadir/%name
%config %dir %_sysconfdir/zarafa/%upstreamname
%config(noreplace) %_sysconfdir/zarafa/%upstreamname/config.php
%config(noreplace) %apache2_sites_available/%name.conf
%config(noreplace) %apache2_sites_enabled/%name.conf

%changelog
* Thu Jun 21 2012 Radik Usupov <radik@altlinux.org> 7.0.8-alt1
- New version (1.1.svn35292)

* Wed May 23 2012 Radik Usupov <radik@altlinux.org> 7.0.7-alt1
- New version (svn34755)

* Tue Apr 24 2012 Radik Usupov <radik@altlinux.org> 7.0.6-alt4
- New version (svn33885)
- Updated Russian translation

* Fri Apr 13 2012 Radik Usupov <radik@altlinux.org> 7.0.6-alt3
- New version (svn33663)

* Wed Mar 28 2012 Radik Usupov <radik@altlinux.org> 7.0.6-alt2
- New version (svn33196)

* Thu Mar 01 2012 Radik Usupov <radik@altlinux.org> 7.0.6-alt1
- New version (svn32793)

* Fri Feb 17 2012 Radik Usupov <radik@altlinux.org> 7.0.5-alt1
- New version (svn31834)

* Fri Dec 09 2011 Radik Usupov <radik@altlinux.org> 7.0.4-alt1
- Initial build (thanks viy@ and snejok@)
