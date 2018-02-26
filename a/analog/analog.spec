Name: analog
Version: 6.0
Release: alt1
License: GPL
Summary: WWW server logfile analysis program
Group: Monitoring
URL: http://www.analog.cx/
Packager: Mikhail Pokidko <pma@altlinux.org>
Source0: http://www.analog.cx/%name-%%version.tar.bz2
Source1: localhost.cfg
Patch0: %name-%version-patch

# Automatically added by buildreq on Mon Jul 17 2006 (-bi)
BuildRequires: perl-CGI apache-devel

#BuildRequires: apache-devel

%define apache_htdocsdir /var/www/html
%description
WWW server logfile analysis program with lots of features.

%prep
%setup -q
%patch0 -p1
%build
%make_build DEFS='%optflags -DLANGDIR=\"%_datadir/%name/lang/\" \
	-DCONFIGDIR=\"%_sysconfdir/%name/\" \
	-DLOGSDIR=\"%_logdir/%name/\" \
	-DOUTDIR=\"%apache_htdocsdir/%name/\" '

%install
mkdir -p %buildroot%_bindir \
	%buildroot%_sysconfdir/%name \
	%buildroot%apache_htdocsdir/%name/images \
	%buildroot%apache_htdocsdir/%name \
	%buildroot%_datadir/%name/lang \
	%buildroot%_datadir/%name/images \
	%buildroot/var/www/cgi-bin
%__install -s analog %buildroot%_bindir/%name
%__install -d %buildroot%_datadir/%name
%__install -d %buildroot%_datadir/%name/lang
%__install -m 644 analog.cfg %buildroot%_sysconfdir/%name
%__install -m 555 anlgform.pl %buildroot/var/www/cgi-bin
%__install -m 644 anlgform.html %buildroot%apache_htdocsdir/%name
%__install -m644 %SOURCE1 %buildroot%_sysconfdir/%name

mkdir -p %buildroot%_man1dir
cp images/* %buildroot%apache_htdocsdir/%name/images
cp lang/* %buildroot%_datadir/%name/lang
cp analog.man %buildroot%_man1dir

%files
%doc Licence.txt README.txt docs/ examples/ analog-data.dtd
%config(noreplace) %_sysconfdir/%name/*.cfg
%_man1dir/%name.man.gz
%_bindir/%name
/var/www/cgi-bin/anlgform.pl
%apache_htdocsdir/%name/*
#attr (0755,-,webmaster) %apache_htdocsdir/%name/anlgform.html
#apache_htdocsdir/%name/images/
#attr (0755,-,webmaster) %apache_htdocsdir/%name/
#_datadir/%name/lang/
%attr (0755,-,webmaster) %_datadir/%name

%changelog
* Wed Jul 14 2006 Mikhail Pokidko <pma@altlinux.org> 6.0-alt1
- Initial build
