# useful defaults
%define name sqlgrey
%define ver  1.6.8
%define rel  alt1
%define sqlgrey_admin mailadm
%define sqlgrey_owner sqlgrey
%define ROOT %_localstatedir/%name

Summary: SQLgrey is a postfix grey-listing policy service
Name: 	 %name
Version: %ver
Release: %rel
License: GPL
Url: http://sqlgrey.sourceforge.net
Group: System/Servers
Source0: %name-%ver.tar.bz2
Source1: %name-alt-init
Patch: %name-alt-conf.patch

BuildArch: noarch

# Automatically added by buildreq on Sat Jun 25 2005 (-ba)
BuildRequires: less perl-DBI perl-Date-Calc perl-Net-Server perldoc

Requires: perl-DBD-SQLite 

%description
SQLgrey is a Postfix grey-listing policy service with auto-white-listing
written in Perl with SQL database as storage backend.
Greylisting stops 50 to 90 % junk mails (spam and virus) before they
reach your Postfix server (saves BW, user time and CPU time).

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall ROOTDIR=$RPM_BUILD_ROOT
%__install -p -m755 -D %SOURCE1 $RPM_BUILD_ROOT%_initdir/%name
%__mkdir_p %buildroot%ROOT

for i in $RPM_BUILD_ROOT%_sysconfdir/%name/clients_*; do
	>"$RPM_BUILD_ROOT%_sysconfdir/%name/`basename $i`.local";
done

%pre
/usr/sbin/groupadd -r -f %sqlgrey_owner
/usr/sbin/groupadd -r -f %sqlgrey_admin

/usr/sbin/useradd -r -n -g %name -d %ROOT -s /dev/null -c %name %name >/dev/null 2>&1 ||:

%post
if [ $1 = 1 ]; then
	/sbin/chkconfig --add %name
fi

if [ $1 -ge 2 ]; then
	%_initdir/%name condrestart
fi

%preun
if [ $1 = 0 ]; then
	%_initdir/%name condstop
	/sbin/chkconfig --del %name
	%__rm -f %ROOT/*
fi

%files
%_initrddir/sqlgrey
%_sbindir/sqlgrey
%_sbindir/update_sqlgrey_config
%_bindir/sqlgrey-logstats.pl
%_man1dir/*
%doc README* HOWTO Changelog FAQ TODO
%attr(750,%name,%sqlgrey_admin) %_sysconfdir/%name
%attr(640,%name,%sqlgrey_admin) %config(noreplace) %_sysconfdir/%name/%name.conf
%attr(750,%name,%name) %ROOT

%changelog
* Fri Nov 06 2009 Afanasov Dmitry <ender@altlinux.org> 1.6.8-alt1
- New upstream.

* Sat Oct 29 2005 LAKostis <lakostis at altlinux.ru> 1.6.7-alt1
- New upstream.

* Sat Aug 06 2005 LAKostis <lakostis at altlinux.ru> 1.6.5-alt1
- New upstream.

* Sat Jun 25 2005 LAKostis <lakostis at altlinux.ru> 1.6.1-alt1
- New upstream.
- Some init script tweaks.
- Update BuildRequires.
- Add upgrade handling.

* Sun Mar 06 2005 LAKostis <lakostis at altlinux.ru> 1.4.8-alt1
- New upstream.

* Wed Feb 16 2005 LAKostis <lakostis at altlinux.ru> 1.4.3-alt1
- initial build for Sisyphus.

