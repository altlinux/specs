%define with_ldap 0

Name: z-push
Version: 2.0
Release: alt1

Summary: ActiveSync over-the-air implementation for mobile syncing
License: AGPLv3 with exceptions
Group: Networking/WWW

Url: http://z-push.sourceforge.net/
Source: http://download.berlios.de/%name/%name-%version.tar
Source1: z-push.conf
Packager: Radik Usupov <radik@altlinux.org>

BuildRequires(pre): rpm-build-apache2
Requires: apache2
Requires: php5-imap

%if %with_ldap
Requires: php5-ldap
%endif

BuildArch: noarch

%description
Z-Push is an implementation of the ActiveSync protocol which is used
'over-the-air' for multi platform ActiveSync devices, including Windows
Mobile, Android, iPhone, Sony Ericsson and Nokia mobile devices. With
Z-Push any groupware can be connected and synced with these devices.

This package is prepared for use with the Zarafa Collaboration Platform
and Open Source Collaboration. For non-Zarafa use cases, please use the
regular Z-Push package.

%prep
%setup -T -c -a 0

# Correct wrong file permissions
chmod 644 %name/include/z_RFC822.php

%build
%install
# Create all needed directories
mkdir -p %buildroot%_sysconfdir/{zarafa/%name,httpd/conf.d}
mkdir -p %buildroot{%_bindir,%_datadir/%name}
mkdir -p %buildroot%_datadir/%name/state/

# Z-Push for Zarafa
pushd %name

# Install all files into destination
cp -af * %buildroot%_datadir/%name/

# Move configuration file to its place
mv -f %buildroot%_datadir/%name/config.php %buildroot%_sysconfdir/zarafa/%name/config.php
ln -sf ../../..%_sysconfdir/zarafa/%name/config.php %buildroot%_datadir/%name/config.php

# Install the apache2 configuration file
	mkdir -p %buildroot%apache2_sites_available
	mkdir -p %buildroot%apache2_sites_enabled
	install -p -m 644 %SOURCE1 %buildroot%apache2_sites_available/%name.conf
	pushd %buildroot%apache2_sites_enabled
	    ln -sf ../sites-available/%name.conf
	popd

# Remove all non-Zarafa related files
rm -f %buildroot%_datadir/%name/backend/{diffbackend,imap,maildir,vcarddir}.php

# Move searchldap configuration to its place
%if %with_ldap
mv -f %buildroot%_datadir/%name/backend/searchldap/config.php %buildroot%_sysconfdir/zarafa/%name/searchldap.php
ln -sf ../../../../..%_sysconfdir/zarafa/%name/searchldap.php %buildroot%_datadir/%name/backend/searchldap/config.php
%else
rm -rf %buildroot%_datadir/%name/backend/{searchbackend.php,searchldap/}
%endif

# Install Zarafa-related command line tool
#install -p -m 755 backend/zarafa/z-push-admin.php %buildroot%_bindir/z-push-admin

popd

# Remove all unwanted files and directories
rm -rf %buildroot%_datadir/%name/{backend/{kolab,zarafa}}/
rm -f %buildroot%_datadir/%name/{INSTALL,LICENSE,{config,debug}.php.{package,zarafa}}

%files
%doc %name/LICENSE
%config(noreplace) %apache2_sites_available/%name.conf
%config(noreplace) %apache2_sites_enabled/%name.conf
%dir %_sysconfdir/zarafa/%name/
%config(noreplace) %_sysconfdir/zarafa/%name/config.php
%if %with_ldap
%config(noreplace) %_sysconfdir/zarafa/%name/searchldap.php
%endif
%_datadir/%name/

%changelog
* Wed Jul 11 2012 Radik Usupov <radik@altlinux.org> 2.0-alt1
- New version (2.0-1346)

* Fri Mar 16 2012 Radik Usupov <radik@altlinux.org> 1.5.7-alt2
- Fixed state path (tnx ainur@)

* Fri Feb 03 2012 Radik Usupov <radik@altlinux.org> 1.5.7-alt1
- New version (1.5.7)

* Tue Jan 31 2012 Radik Usupov <radik@altlinux.org> 1.5.6-alt1
- New version (1.5.6)

* Tue Sep 27 2011 Radik Usupov <radik@altlinux.org> 1.5.5-alt1
- New version (1.5.5)

* Tue May 17 2011 Radik Usupov <radik@altlinux.org> 1.5.3-alt1
- initial build for ALT Linux Sisyphus
