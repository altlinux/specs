%define post_apacheconf		/sbin/service httpd condreload
%define postun_apacheconf	/sbin/service httpd condreload
%define appname	smartsieve
%define appvers	1.0.RC2
%define appdir %_datadir/%name

Name:		%appname
Version:	%appvers
Release:	alt1
Summary:	%appname - a web based graphical user interface for creating and managing Sieve scripts on a Cyrus-imap mail server.
Summary(ru_RU.KOI8-R):	%appname - веб интерфейс управления Sieve скриптами Cyrus-imap сервера.

License:	GNU
Group:		Networking/Mail

URL:		http://smartsieve.sourceforge.net
Source0:	%appname-%version.tar.bz2
Source1:	%appname.apache.conf

BuildRequires: rpm-macros-webserver-common
Requires: webserver-common, php-engine, php5-mcrypt, pear-Log

BuildArch:	noarch

%description
%name - a web based graphical user interface for creating and 
managing Sieve scripts on a Cyrus imap mail server. It provides a 
way for non-technical Cyrus imap users to generate Sieve rules for 
mail filtering and vacation messaging without prior knowledge of the 
Sieve scripting language. SmartSieve is written in PHP and is 
intended to be intuitive to use, and simple to configure.

SmartSieve will be of interest to institutions running Cyrus imapd 
to provide imap based mail access and who require a user-friendly 
way for users to manage mail filtering and vacation messaging. It 
will be of particular interest to those currently deploying Websieve 
for this purpose. SmartSieve is compatible with Websieve in that 
Sieve scripts created using Websieve can be read and modified using 
SmartSieve, and visa-versa.

SmartSieve is not a Sieve script 'parser'. It cannot directly read 
and understand the Sieve language itself. For this reason, the GUI 
will only work for Sieve scripts created by SmartSieve. Other 
non-SmartSieve scripts can be edited in SmartSieve's direct edit 
mode.

%package apache
Summary: %name's apache config file
Group: System/Servers
Requires: %name = %version-%release, apache

%description apache
%name's apache config file

%prep
%setup -q -n %appname

%build

%install

# Any files
install -pd -m0755 %buildroot%appdir

install -m644 *.php %buildroot%appdir/
cp -aRf images include lib scripts %buildroot%appdir/

mkdir -p %buildroot%_sysconfdir/%name
cp -aRf conf/{*,.htaccess} %buildroot%_sysconfdir/%name
ln -s %_sysconfdir/%name %buildroot%appdir/conf

install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%files
%defattr(644, root, %webserver_group,755)

%config(noreplace) %_sysconfdir/%name/*.php
%_sysconfdir/%name/.htaccess
%_sysconfdir/%name/locale/

%attr(755, root, %webserver_group) %appdir/scripts/*.pl

%appdir

%doc README CHANGES ChangeLog INSTALL NOTICE TODO


%files apache
%_sysconfdir/httpd/conf/addon-modules.d/%name.conf


%changelog
* Thu May 07 2009 Timur Batyrshin <erthad@altlinux.org> 1.0.RC2-alt1
- updated to 1.0-RC2

* Mon Dec 05 2005 Aleksey Avdeev <solo@altlinux.ru> 0.5.2.20051129-alt1
- cvs snapshot 20051129 (see CHANGES)

* Thu Nov 24 2005 Aleksey Avdeev <solo@altlinux.ru> 0.5.2.20051116-alt1
- cvs snapshot 20051116 (see CHANGES)
- set requires apache -> apache-common
- resolved PHP Note

* Thu Apr 14 2005 Aleksey Avdeev <solo@altlinux.ru> 0.5.2.20050321-alt1
- first rpm distribution.
- cvs snapshot 20050321.

