Name: pflogsumm
Version: 1.1.0
Release: alt4

Summary: Postfix Log Entry Summarizer
License: GPL
Group: Monitoring

Url: http://jimsun.linxnet.com/postfix_contrib.html
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar
Source1: pflogsumm-daily
# http://www.nmedia.net/~chris/mail/mail-cgi.txt
Source2: pflogsumm.mail-cgi.txt
Source3: pflogsumm.htaccess
Patch0: pflogsumm-1.1.0-alt-mail.cgi.patch
Patch1: pflogsumm-1.1.0-conn-delays-dsn.patch

# Automatically added by buildreq on Sun Apr 27 2008 (-bi)
BuildRequires: perl-Date-Calc

%package cgi
Summary: CGI script that interfaces to %name
Group: Monitoring
Requires: %name = %version-%release

%description
Pflogsumm is a log analyzer/summarizer for the Postfix MTA.  It is
designed to provide an over-view of Postfix activity, with just enough
detail to give the administrator a "heads up" for potential trouble
spots.
Pflogsumm generates summaries and, in some cases, detailed reports of
mail server traffic volumes, rejected and bounced email, and server
warnings, errors and panics.

%description cgi
CGI script that interfaces to %name

%prep
%setup
cp -a %SOURCE2 .
%patch0 -p1
%patch1 -p0

%install
install -pD -m0755 pflogsumm.pl %buildroot/%_sbindir/%name
install -pD -m0644 pflogsumm.1 %buildroot/%_man1dir/%name.1
install -pD -m0755 %SOURCE1 %buildroot/%_sysconfdir/cron.daily/010%name

install -pD -m0755 pflogsumm.mail-cgi.txt %buildroot%_var/www/cgi-bin/%name/index.cgi
install -pD -m0644 %SOURCE3 %buildroot%_var/www/cgi-bin/%name/.htaccess

%files
%_sbindir/%name
%_man1dir/%name.*
%config(noreplace) %_sysconfdir/cron.daily/010%name
%doc ChangeLog pflogsumm-faq.txt README ToDo rem_smtpd_stats_supp.pl

%files cgi
%_var/www/cgi-bin/%name/index.cgi
%_var/www/cgi-bin/%name/.htaccess

%changelog
* Sun Apr 27 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1.0-alt4
- Rename default cron job (Closes: #15444)

* Thu Nov 16 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1.0-alt3
- Added pflogsumm-1.1.0-conn-delays-dsn.patch from postfix source tree. This
  patch adds support for logfiles with conn_use, delays, and dsn
  attributes.

* Wed Jun 14 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1.0-alt2
- Packaged cgi-script that interfaces to pflogsumm
- Minor spec cleanup

* Mon Sep 20 2004 Leonid Shalupov <shalupov@altlinux.ru> 1.1.0-alt1
- Rebuilt for Sisyphus

* Fri Jul 23 2004 Leonid Shalupov <shalupov@ucvt.ru> 1.1.0-ls1
- Repackaged for ALT Linux
- cron.daily script

* Sun Dec 14 2003 Luca Berra <bluca@vodka.it> 1.1.0-1mdk
- 1.1.0
- bzipped source

* Fri Oct 24 2003 Luca Berra <bluca@vodka.it> 1.0.15-1mdk
- Initial contrib
