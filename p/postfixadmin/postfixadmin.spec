Name: postfixadmin
Version: 2.3.2
Release: alt4

Summary: web based interface used to manage mailboxes, virtual domains and aliases
License: GPLv2+
Group: System/Servers

Url: http://postfixadmin.sourceforge.net
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-apache rpm-macros-apache2
BuildRequires: rpm-macros-webserver-common perl-DBI perl-MIME-EncWords perl-Email-Valid perl-Mail-Sender perl-Log-Log4perl

Requires: php-engine php5-mysql php5-mbstring php5-imap

%package apache
Summary: %name's apache config file
Group: System/Servers
Requires: %name = %version-%release, apache

%description apache
%name's apache config file

%package apache2
Summary: %name's apache2 config file
Group: System/Servers
Requires: %name = %version-%release, apache2

%description apache2
%name's apache2 config file

%package vacation
Summary: %name's vacation script
Group: System/Servers
Requires: %name = %version-%release, postfix

%description vacation
%name's Virtual Vacation script

%description
Postfix Admin is a Web Based Management tool created for Postfix.
It is a PHP based application that handles Postfix Style Virtual
Domains and Users that are stored in MySQL.

Postfix Admin supports:
- Virtual Mailboxes / Virtual Aliases / Forwarders.
- Domain to Domain forwarding / Catch-All.
- Vacation (auto-response) for Virtual Mailboxes.
- Quota / Alias & Mailbox limits per domain.
- Backup MX.
- Packaged with over 25 languages.

%prep
%setup

%install
# webapp main part
install -d %buildroot%_datadir/%name
cp -rp *.php *.txt admin css images languages model templates users %buildroot%_datadir/%name

# webapp's config
rm -f %buildroot%_datadir/%name/config.inc.php
install -pDm0640 config.inc.php %buildroot%_sysconfdir/%name/config.inc.php
ln -sf %_sysconfdir/%name/config.inc.php %buildroot%_datadir/%name/

# apache2 config
install -pD -m640 altlinux/apache2.conf %buildroot%apache2_confdir/addon.d/A.%name.conf

# apache config
install -pD -m640 altlinux/apache.conf %buildroot%apache_modconfdir/%name.conf

# vocation script
install -pD -m750 VIRTUAL_VACATION/vacation.pl %buildroot%_datadir/%name/VACATION/vacation.pl
install -pD -m644 VIRTUAL_VACATION/INSTALL.TXT %buildroot%_datadir/%name/VACATION/INSTALL.TXT

cat > %buildroot%_sysconfdir/%name/vacation.conf << __END__ 
# ========== begin configuration ==========

# IMPORTANT: If you put passwords into this script, then remember
# to restrict access to the script, so that only the vacation user
# can read it.

# db_type - uncomment one of these
our $db_type = 'Pg';
#our $db_type = 'mysql';

# leave empty for connection via UNIX socket
our $db_host = '';

# connection details
our $db_username = 'user';
our $db_password = 'password';
our $db_name     = 'postfix';

our $vacation_domain = 'autoreply.example.org';

# smtp server used to send vacation e-mails
our $smtp_server = 'localhost';
our $smtp_server_port = 25;

# SMTP authentication protocol used for sending.
# Can be 'PLAIN', 'LOGIN', 'CRAM-MD5' or 'NTLM'
# Leave it blank if you don't use authentification
our $smtp_auth = undef;
# username used to login to the server
our $smtp_authid = 'someuser';
# password used to login to the server
our $smtp_authpwd = 'somepass';

# Set to 1 to enable logging to syslog.
our $syslog = 0;

# path to logfile, when empty logging is supressed
# change to e.g. /dev/null if you want nothing logged.
# if we can't write to this, and $log_to_file is 1 (below) the script will abort.
our $logfile='/var/log/vacation.log';
# 2 = debug + info, 1 = info only, 0 = error only
our $log_level = 2;
# Whether to log to file or not, 0 = do not write to a log file
our $log_to_file = 0; 

# notification interval, in seconds
# set to 0 to notify only once
# e.g. 1 day ...
#my $interval = 60*60*24;
# disabled by default
our $interval = 0;

__END__ 


%files
%dir %attr(0755,root,root) %_sysconfdir/%name/
%config(noreplace) %attr(0640,root,%webserver_group) %_sysconfdir/%name/config.inc.php
%_datadir/%name
%doc INSTALL.TXT CHANGELOG.TXT DOCUMENTS ADDITIONS VIRTUAL_VACATION altlinux/README*

%exclude %_datadir/%name/VACATION*

%files apache
%config(noreplace) %apache_modconfdir/%name.conf

%files apache2
%config(noreplace) %apache2_confdir/addon.d/A.%name.conf

%files vacation
%dir %_datadir/%name/VACATION
%_datadir/%name/VACATION/INSTALL.TXT
%config(noreplace) %attr(0750,root,mail) %_datadir/%name/VACATION/vacation.pl
%config(noreplace) %attr(0640,root,mail) %_sysconfdir/%name/vacation.conf

%changelog
* Wed Jun 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt4
- Fix (ALT #25760)

* Mon Feb 28 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt3
- Add config for vacation script
- Change group for vacation.pl

* Thu Feb 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt2
- Fix copying model files
- Add %name-vacation subpackage

* Mon Dec 20 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt1
- New release
- Add %name-apache2 subpackage

* Thu Apr 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3-alt1.svn.792
- Post 2.3-release svn snapshot.
- Fix default apache config.
- Add README.ALT with examle configurations.

* Mon Apr 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3-alt1.rc3
- Initial build for Sisyphus.

