%define _spampd_user     _spampd
%define _spampd_group    _spampd
%define _spampd_home     %_localstatedir/spampd

Name: spampd
Version: 2.30
Release: alt1.1

Summary: spamassassin based SMTP/LMTP proxy daemon
License: GPLv2+
Group: System/Servers

Url: http://www.worlddesign.com/index.cfm/rd/mta/spampd.htm
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar

# Automatically added by buildreq on Mon Aug 18 2008 (-bi)
BuildRequires: perl-Mail-SpamAssassin perl-Net-Server
BuildRequires: perl-podlators

%description
spampd is an SMTP/LMTP server designed to be hooked into the
MTA processing chain (e.g. as a content filter). It is
written in Perl and uses the Net::Server framework. It is
intended to provide spam filtering at the system level (i.e.
ususally for all users). If you rely on per-user configuration
or per-user Bayes databases, spampd is not for you.
.
The major advantage of spampd over plain SpamAssassin (both
directly and through spamd) is that it doesn't need to load
all needed perl modules on every invocation or spawn
a C programme for every mail it receives. Compared to using
spamc/spamd, spampd can usually provide a 25%% performance
increase with local-only tests.
.
The advantage of spampd over amavisd-new is that it uses the
original SpamAssassin header tags, which are more verbose than
the tags which amavisd-new provides. This allows easier
filtering in the mail client and easier tuning of SpamAssassin.

%prep
%setup

%build

%install
# pid dir
install -dm1775 %buildroot%_var/run/%name

# home dir
install -dm1770 %buildroot%_localstatedir/%name

# binary
install -pDm755 %name %buildroot%_sbindir/%name

# initscript
install -pDm755 spampd.init %buildroot%_initdir/%name
install -pDm644 spampd.sysconfig %buildroot%_sysconfdir/sysconfig/%name

# generate manpage
install -d %buildroot%_man8dir
pod2man --section=8 --center="Spam Proxy Daemon" spampd > %buildroot%_man8dir/spampd.8

%pre
/usr/sbin/groupadd -r -f %_spampd_group ||:
/usr/sbin/useradd -g %_spampd_group -c 'The spampd  daemon' \
	-d %_spampd_home -s /dev/null -r %_spampd_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/*
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_man8dir/*
%dir %attr(1775,root,%_spampd_group) %_var/run/%name
%dir %attr(1770,root,%_spampd_group) %_localstatedir/%name
%doc changelog.txt spampd.html

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 2.30-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Aug 18 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.30-alt1
- Initial build for ALT Linux
