# TODO: need pkgconfig cyrussasl
# TODO: need pkgconfig openldap

# BEGIN SourceDeps(oneline):
BuildRequires: %_bindir/gcov %_bindir/gprof %_bindir/lcov %_bindir/rrdtool libevent-devel libgnutls-devel libldns-devel liblmdb-devel perl(DBD/mysql.pm) perl(DBI.pm) perl(IO/Handle.pm) perl(RRDs.pm) pkgconfig(jansson) pkgconfig(libcurl) pkgconfig(librrd) pkgconfig(tre)
# END SourceDeps(oneline)

%global upname OpenDKIM
%global bigname OPENDKIM

Name: opendkim
Version: 2.10.3
Release: alt4

Summary: A DomainKeys Identified Mail (DKIM) milter to sign and/or verify mail

Group: System/Servers
License: BSD and Sendmail
Url: http://%name.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/%name/%name-%version.tar

Requires: lib%name = %version-%release

# skip libbsd-devel (can be used for bsd/string.h)

BuildRequires: sendmail-devel, libssl-devel, libtool, opendbx-devel
Requires(pre): shadow-utils

BuildRequires: libdb4.7-devel, libmemcached-devel
#, libldap-devel

#Patch: %name.init.patch

%description
%upname allows signing and/or verification of email through an open source
library that implements the DKIM service, plus a milter-based filter
application that can plug in to any milter-aware MTA, including sendmail,
Postfix, or any other MTA that supports the milter protocol.

%package -n lib%name
Summary: An open source DKIM library
Group: System/Libraries

%description -n lib%name
This package contains the library files required for running services built
using libopendkim.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopendkim.

%prep
%setup

%build
# Always use system libtool instead of pacakge-provided one to
# properly handle 32 versus 64 bit detection and settings
%define LIBTOOL LIBTOOL=`which libtool`

%configure --with-odbx --with-db --with-libmemcached --with-openldap --localstatedir=/var

# Remove rpath
%__subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%__subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%install
%makeinstall_std
install -d %buildroot%_sysconfdir/
install -d %buildroot%_sysconfdir/sysconfig/
install -m 0755 contrib/init/redhat/%name-default-keygen %buildroot%_sbindir/%name-default-keygen

install -d -m 0755 %buildroot%_unitdir/
install -m 0644 contrib/systemd/%name.service %buildroot%_unitdir/%name.service

cat > %buildroot%_sysconfdir/%name.conf << 'EOF'
## BASIC %bigname CONFIGURATION FILE
## See %name.conf(5) or %_docdir/%name/%name.conf.sample for more

## BEFORE running %upname you must:

## - make your MTA (Postfix, Sendmail, etc.) aware of %upname
## - generate keys for your domain (if signing)
## - edit your DNS records to publish your public keys (if signing)

## See %_docdir/%name/INSTALL for detailed instructions.

## DEPRECATED CONFIGURATION OPTIONS
##
## The following configuration options are no longer valid.  They should be
## removed from your existing configuration file to prevent potential issues.
## Failure to do so may result in %name being unable to start.
##
## Removed in 2.10.0:
##   AddAllSignatureResults
##   ADSPAction
##   ADSPNoSuchDomain
##   BogusPolicy
##   DisableADSP
##   LDAPSoftStart
##   LocalADSP
##   NoDiscardableMailTo
##   On-PolicyError
##   SendADSPReports
##   UnprotectedPolicy

## CONFIGURATION OPTIONS

##  Specifies the path to the process ID file.
PidFile	%_var/run/%name/%name.pid

##  Selects operating modes. Valid modes are s (sign) and v (verify). Default is v.
##  Must be changed to s (sign only) or sv (sign and verify) in order to sign outgoing
##  messages.
Mode	v

##  Log activity to the system log.
Syslog	yes

##  Log additional entries indicating successful signing or verification of messages.
SyslogSuccess	yes

##  If logging is enabled, include detailed logging about why or why not a message was
##  signed or verified. This causes an increase in the amount of log data generated
##  for each message, so set this to No (or comment it out) if it gets too noisy.
LogWhy	yes

##  Attempt to become the specified user before starting operations.
UserID	%name:%name

##  Create a socket through which your MTA can communicate.
Socket	inet:8891@localhost

##  Required to use local socket with MTAs that access the socket as a non-
##  privileged user (e.g. Postfix)
Umask	002

##  This specifies a text file in which to store DKIM transaction statistics.
##  %upname must be manually compiled with --enable-stats to enable this feature.
# Statistics	%_var/spool/%name/stats.dat

##  Specifies whether or not the filter should generate report mail back
##  to senders when verification fails and an address for such a purpose
##  is provided. See opendkim.conf(5) for details.
SendReports	yes

##  Specifies the sending address to be used on From: headers of outgoing
##  failure reports.  By default, the e-mail address of the user executing
##  the filter is used (executing_user@hostname).
# ReportAddress	"Example.com Postmaster" <postmaster@example.com>

##  Add a DKIM-Filter header field to messages passing through this filter
##  to identify messages it has processed.
SoftwareHeader	yes

## SIGNING OPTIONS

##  Selects the canonicalization method(s) to be used when signing messages.
Canonicalization	relaxed/relaxed

##  Domain(s) whose mail should be signed by this filter. Mail from other domains will
##  be verified rather than being signed. Uncomment and use your domain name.
##  This parameter is not required if a SigningTable is in use.
# Domain	example.com

##  Defines the name of the selector to be used when signing messages.
Selector	default

##  Specifies the minimum number of key bits for acceptable keys and signatures.
MinimumKeyBits	1024

##  Gives the location of a private key to be used for signing ALL messages. This
##  directive is ignored if KeyTable is enabled.
KeyFile	%_sysconfdir/%name/keys/default.private

##  Gives the location of a file mapping key names to signing keys. In simple terms,
##  this tells %upname where to find your keys. If present, overrides any KeyFile
##  directive in the configuration file. Requires SigningTable be enabled.
# KeyTable	%_sysconfdir/%name/KeyTable

##  Defines a table used to select one or more signatures to apply to a message based
##  on the address found in the From: header field. In simple terms, this tells
##  %upname how to use your keys. Requires KeyTable be enabled.
# SigningTable	refile:%_sysconfdir/%name/SigningTable

##  Identifies a set of "external" hosts that may send mail through the server as one
##  of the signing domains without credentials as such.
# ExternalIgnoreList	refile:%_sysconfdir/%name/TrustedHosts

##  Identifies a set "internal" hosts whose mail should be signed rather than verified.
# InternalHosts	refile:%_sysconfdir/%name/TrustedHosts

##  Contains a list of IP addresses, CIDR blocks, hostnames or domain names
##  whose mail should be neither signed nor verified by this filter.  See man
##  page for file format.
# PeerList	X.X.X.X

##  Always oversign From (sign using actual From and a null From to prevent
##  malicious signatures header fields (From and/or others) between the signer
##  and the verifier.  From is oversigned by default in the Fedora package
##  because it is often the identity key used by reputation systems and thus
##  somewhat security sensitive.
OversignHeaders	From
EOF

cat > %buildroot%_sysconfdir/sysconfig/%name << 'EOF'
# Set the necessary startup options
OPTIONS="-x %_sysconfdir/%name.conf -P %_var/run/%name/%name.pid"

# Set the default DKIM selector
DKIM_SELECTOR=default

# Set the default DKIM key location
DKIM_KEYDIR=%_sysconfdir/%name/keys
EOF

mkdir -p %buildroot%_sysconfdir/%name
cat > %buildroot%_sysconfdir/%name/SigningTable << 'EOF'
# %bigname SIGNING TABLE
# This table controls how to apply one or more signatures to outgoing messages based
# on the address found in the From: header field. In simple terms, this tells
# %upname "how" to apply your keys.

# To use this file, uncomment the SigningTable option in %_sysconfdir/%name.conf,
# then uncomment one of the usage examples below and replace example.com with your
# domain name, then restart %upname.

# WILDCARD EXAMPLE
# Enables signing for any address on the listed domain(s), but will work only if
# "refile:%_sysconfdir/%name/SigningTable" is included in %_sysconfdir/%name.conf.
# Create additional lines for additional domains.

#*@example.com default._domainkey.example.com

# NON-WILDCARD EXAMPLE
# If "file:" (instead of "refile:") is specified in %_sysconfdir/%name.conf, then
# wildcards will not work. Instead, full user@host is checked first, then simply host,
# then user@.domain (with all superdomains checked in sequence, so "foo.example.com"
# would first check "user@foo.example.com", then "user@.example.com", then "user@.com"),
# then .domain, then user@*, and finally *. See the %name.conf(5) man page under
# "SigningTable" for more details.

#example.com default._domainkey.example.com
EOF

cat > %buildroot%_sysconfdir/%name/KeyTable << 'EOF'
# %bigname KEY TABLE
# To use this file, uncomment the #KeyTable option in %_sysconfdir/%name.conf,
# then uncomment the following line and replace example.com with your domain
# name, then restart %upname. Additional keys may be added on separate lines.

#default._domainkey.example.com example.com:default:%_sysconfdir/%name/keys/default.private
EOF

cat > %buildroot%_sysconfdir/%name/TrustedHosts << 'EOF'
# %bigname TRUSTED HOSTS
# To use this file, uncomment the #ExternalIgnoreList and/or the #InternalHosts
# option in %_sysconfdir/%name.conf then restart %upname. Additional hosts
# may be added on separate lines (IP addresses, hostnames, or CIDR ranges).
# The localhost IP (127.0.0.1) should always be the first entry in this file.
127.0.0.1
::1
#host.example.com
#192.168.1.0/24
EOF

cat > README.fedora << 'EOF'
#####################################
#FEDORA-SPECIFIC README FOR %bigname#
#####################################
Last updated: Apr 30, 2015 by Steve Jenkins (steve@stevejenkins.com)

Generating keys for %upname
============================
After installing the %name package, you MUST generate a pair of keys (public and private) before
attempting to start the %name service.

A valid private key must exist in the location expected by %_sysconfdir/%name.conf before the service will start.

A matching public key must be included in your domain's DNS records before remote systems can validate
your outgoing mail's DKIM signature.

Generating Keys Automatically
=============================
To automatically create a pair of default keys for the local domain, do:

% sudo %_sbindir/%name-default-keygen

The default keygen script will attempt to fetch the local domain name, generate a private and public key for
the domain, then save them in %_sysconfdir/%name/keys as default.private and default.txt with the proper
ownership and permissions.

NOTE: The default key generation script MUST be run by a privileged user (or root). Otherwise, the resulting
private key ownership and permissions will not be correct.

Generating Keys Manually
========================
A privileged user (or root) can manually generate a set of keys by doing the following:

1) Create a directory to store the new keys:

% sudo mkdir %_sysconfdir/%name/keys/example.com

2) Generate keys in that directory for a specific domain name and selector:

% sudo %_sbindir/%name-genkey -D %_sysconfdir/%name/keys/example.com/ -d example.com -s default

3) Set the proper ownership for the directory and private key:

% sudo chown -R root:%name %_sysconfdir/%name/keys/example.com

4) Set secure permissions for the private key:

% sudo chmod 640 %_sysconfdir/%name/keys/example.com/default.private

5) Set standard permissions for the public key:

% sudo chmod 644 %_sysconfdir/%name/keys/example.com/default.txt

Updating Key Location(s) in Configuration Files
===============================================
If you run the %name-default-keygen script, the default keys will be saved in %_sysconfdir/%name/keys as
default.private and default.txt, which is the location expected by the default %_sysconfdir/%name.conf file.

If you manually generate your own keys, you must update the key location and name in %_sysconfdir/%name.conf
before attempting to start the %name service.

Using %upname with SQL Datasets
================================
%upname on RedHat-based systems relies on OpenDBX for database access. Depending on which database you use,
you may have to manually install one of the following OpenDBX subpackages (all of which are available via yum):

- opendbx-firebird
- opendbx-mssql
- opendbx-mysql
- opendbx-postgresql
- opendbx-sqlite
- opendbx-sqlite2
- opendbx-sybase

If you have %upname configured to use SQL datasets on a systemd-based server, it might also be necessary to start
the %name service after the database servers by referencing your database unit file(s) in the "After" section of
the %upname unit file.

For example, if using both MariaDB and PostgreSQL, in %_unitdir/%name.service change:

After=network.target nss-lookup.target syslog.target

to:

After=network.target nss-lookup.target syslog.target mariadb.service postgresql.service

Additional Configuration Help
=============================
For help configuring your MTA (Postfix, Sendmail, etc.) with %upname, setting up DNS records with your
public DKIM key, as well as instructions on configuring %upname to sign outgoing mail for multiple
domains, follow the how-to at:

http://wp.me/p1iGgP-ou

Official documentation for %upname is available at http://%name.org/

%upname mailing lists are available at http://lists.%name.org/

###
EOF

install -p -d %buildroot%_tmpfilesdir
cat > %buildroot%_tmpfilesdir/%name.conf <<'EOF'
D %_var/run/%name 0700 %name %name -
EOF

rm -r %buildroot%_docdir/%name
rm %buildroot%_libdir/*.a
rm %buildroot%_libdir/*.la

mkdir -p %buildroot%_var/spool/%name
mkdir -p %buildroot%_var/run/%name
mkdir -p %buildroot%_sysconfdir/%name
mkdir %buildroot%_sysconfdir/%name/keys

install -m 0755 stats/%name-reportstats %buildroot%prefix/sbin/%name-reportstats
%__subst 's|^%{bigname}STATSDIR="/var/db/%name"|%{bigname}STATSDIR="%_var/spool/%name"|g' %buildroot%prefix/sbin/%name-reportstats
%__subst 's|^%{bigname}DATOWNER="mailnull:mailnull"|%{bigname}DATOWNER="%name:%name"|g' %buildroot%prefix/sbin/%name-reportstats

chmod 0644 contrib/convert/convert_keylist.sh

%pre
getent group %name >/dev/null || groupadd -r %name
getent passwd %name >/dev/null || \
	useradd -r -g %name -G mail -d %_var/run/%name -s /sbin/nologin \
	-c "%upname Milter" %name
exit 0

%files
%doc LICENSE LICENSE.Sendmail
%doc FEATURES KNOWNBUGS RELEASE_NOTES RELEASE_NOTES.Sendmail INSTALL
%doc contrib/convert/convert_keylist.sh %name/*.sample
%doc %name/%name.conf.simple-verify %name/%name.conf.simple
%doc %name/README contrib/lua/*.lua
%doc README.fedora
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_tmpfilesdir/%name.conf
%config(noreplace) %attr(0640,%name,%name) %_sysconfdir/%name/SigningTable
%config(noreplace) %attr(0640,%name,%name) %_sysconfdir/%name/KeyTable
%config(noreplace) %attr(0640,%name,%name) %_sysconfdir/%name/TrustedHosts
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sbindir/*
%_mandir/*/*
%dir %attr(-,%name,%name) %_var/spool/%name
%dir %attr(0775,%name,%name) %_var/run/%name
%dir %attr(-,root,%name) %_sysconfdir/%name
%dir %attr(0750,%name,%name) %_sysconfdir/%name/keys
%attr(0755,root,root) %_sbindir/%name-default-keygen

%attr(0644,root,root) %_unitdir/%name.service

%files -n libopendkim
%doc LICENSE LICENSE.Sendmail
%doc README
%_libdir/lib%name.so.*

%files -n libopendkim-devel
%doc LICENSE LICENSE.Sendmail
%doc lib%name/docs/*.html
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Aug 14 2016 Vitaly Lipatov <lav@altlinux.ru> 2.10.3-alt4
- build without libbsd-devel
- fix configure localstatedir

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.10.3-alt3
- initial manual build for ALT Linux Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt2_4
- update to new release by fcimport

* Fri Dec 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.10.3-alt2_2
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt1_2
- update to new release by fcimport

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt1_2
- new version

