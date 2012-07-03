Name: ocsinventory-server
Version: 1.02.1
Release: alt4

Summary: Hardware and software inventory tool (Communication Server)
Group: System/Servers
License: GPL
Url: http://www.ocsinventory-ng.org/

Packager: Pavel Zilke <zidex at altlinux dot org>

BuildArch: noarch

# We need modulezzzz!!!
Requires(post,postun): apache2-mod_perl
Requires: perl-Apache-DBI perl-Apache2-SOAP perl-DBD-mysql perl-Net-IP perl-XML-Simple perl-XML-Entities

Source: %name-%version.tar
Patch: %name-%version-%release.patch


BuildRequires(pre): rpm-macros-apache2
# Automatically added by buildreq on Mon Apr 07 2008 (-bi)
BuildRequires: apache2-devel perl-Apache-DBI perl-Apache2-SOAP perl-DBD-mysql perl-Net-IP perl-XML-Simple perl-XML-Entities

%description
Open Computer and Software Inventory Next Generation is an application
designed to help a network or system administrator keep track of the
computers configuration and software that are installed on the network.

Information about Hardware and Operating System are collected.
OCS Inventory is also able to detect all active devices on your network,
such as switch, router, network printer and unattended devices.
It also allows deploying softwares, commands or files on client computers.

This package contains the 'Communication Server' part.

%package -n ocsinventory-reports
Summary: Hardware and software inventory tool (Administration Console)
Group: System/Servers
# We need modulezzzz!!!
Requires(post,postun): apache2-mod_php5
Requires: bind-utils nmap php5-mysql php5-gd2 php5-openssl php5-zip samba-client

%description -n ocsinventory-reports
Open Computer and Software Inventory Next Generation is an application
designed to help a network or system administrator keep track of the
computers configuration and software that are installed on the network.

Information about Hardware and Operating System are collected.
OCS Inventory is also able to detect all active devices on your network,
such as switch, router, network printer and unattended devices.
It also allows deploying softwares, commands or files on client computers.

This package contains the 'Administration Console' part.

%prep
%setup
%patch -p1

%build
pushd Apache
%perl_vendor_build
popd

%install
pushd Apache
%perl_vendor_install
popd
mkdir -p %buildroot{%_sysconfdir/{ocsinventory,logrotate.d},%_datadir/%name,%_localstatedir/%name/{ipd,download},%_var/log/%name}
mkdir -p %buildroot{%apache2_extra_available,%apache2_mods_start}
mkdir -p %buildroot%_bindir
cp -av ocsreports %buildroot%_datadir/%name
cp -afv languages %buildroot%_datadir/%name/ocsreports
install -p -m755 Apache/binutils/ocsinventory-injector.pl %buildroot%_bindir/ocsinventory-injector.pl
install -p -m755 Apache/binutils/ipdiscover-util.pl %buildroot%_datadir/%name/ocsreports
install -p -m644 Apache/etc/ocsinventory/ocsinventory-server.conf %buildroot%apache2_extra_available/ocsinventory.conf
install -p -m644 conf/ocsreports.conf %buildroot%apache2_extra_available/ocsreports.conf


cat <<EOF >%buildroot%_sysconfdir/logrotate.d/%name
%_var/log/%name/*.log {
	daily
	rotate 7
	compress
	notifempty
	missingok
}
EOF

cat <<EOF >%buildroot%apache2_mods_start/500-ocsinventory-server.conf
perl=yes
EOF
cat <<EOF >%buildroot%apache2_mods_start/500-ocsinventory-reports.conf
# mod_php still uses addon.d...
#php5=yes
alias=yes
auth_basic=yes
authn_file=yes
authz_user=yes
EOF

cat <<EOF >%buildroot%_sysconfdir/ocsinventory/htpasswd.setup
admin:*
EOF

cat <<EOF >%buildroot%_sysconfdir/ocsinventory/dbconfig.inc.php
<?php 
\$_SESSION["SERVEUR_SQL"]="localhost";
\$_SESSION["COMPTE_BASE"]="ocs";
\$_SESSION["PSWD_BASE"]="ocs";
?>
EOF

%post
a2chkconfig
service httpd2 condreload >/dev/null 2>&1 ||:

%postun
if [ $1 -eq 0 ]; then
    a2chkconfig
    service httpd2 condreload >/dev/null 2>&1 ||:
fi

%post -n ocsinventory-reports
a2chkconfig
service httpd2 condreload >/dev/null 2>&1 ||:

%postun -n ocsinventory-reports
if [ $1 -eq 0 ]; then
    a2chkconfig
    service httpd2 condreload >/dev/null 2>&1 ||:
fi

%files
%doc README.ALT 
%doc ChangeLog 
%doc README 
%doc LICENSE.txt
%config %_sysconfdir/logrotate.d/%name
%attr(640,root,apache2) %config(noreplace) %apache2_extra_available/ocsinventory.conf
%config(noreplace) %apache2_mods_start/500-ocsinventory-server.conf
%_bindir/ocsinventory-injector.pl
%perl_vendor_privlib/Apache/Ocsinventory*
%attr(3775,root,apache2) %dir %_var/log/%name

%files -n ocsinventory-reports
%attr(640,root,apache2) %config(noreplace) %apache2_extra_available/ocsreports.conf
%config(noreplace) %apache2_mods_start/500-ocsinventory-reports.conf
%attr(640,root,apache2) %config(noreplace) %_sysconfdir/ocsinventory/htpasswd.setup
%attr(660,root,apache2) %config(noreplace) %_sysconfdir/ocsinventory/dbconfig.inc.php
%_datadir/%name
%dir %_localstatedir/%name
%attr(3775,root,apache2) %dir %_localstatedir/%name/ipd
%attr(3775,root,apache2) %dir %_localstatedir/%name/download

%changelog
* Tue Dec 15 2009 Pavel Zilke <zidex at altlinux dot org> 1.02.1-alt4
- Fixed #22388, #22389

* Fri Nov 27 2009 Pavel Zilke <zidex at altlinux dot org> 1.02.1-alt3
- Security fix

* Tue Nov 24 2009 Pavel Zilke <zidex at altlinux dot org> 1.02.1-alt2
- Fixed #22316

* Wed Jun 10 2009 Pavel Zilke <zidex@altlinux.org> 1.02.1-alt1
- New version 1.02.1
- Linvinus UTF-8 patch

* Sun Jan 11 2009 Sir Raorn <raorn@altlinux.ru> 1.01-alt4
- Rebuilt with new apache2-devel

* Mon Apr 28 2008 Sir Raorn <raorn@altlinux.ru> 1.01-alt3
- UTF-8 support (barabashka@, based on info from
  http://www.opennet.ru/openforum/vsluhforumID3/14092.html )

* Mon Apr 14 2008 Sir Raorn <raorn@altlinux.ru> 1.01-alt2
- Allow access to ocsreports
- More translations (barabashka@)
- README.ALT

* Sat Apr 12 2008 Sir Raorn <raorn@altlinux.ru> 1.01-alt1
- Built for Sisyphus

