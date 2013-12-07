Name: rancid
Version: 2.3.8
Release: alt2
Summary: Really Awesome New Cisco confIg Differ

Group: System/Configuration/Networking
License: BSD with advertising
Url: http://www.shrubbery.net/rancid/
Source0: %name-%version.tar.gz
Source1: %name.cron
Source2: %name.logrotate
Source3: csbrancid
Source4: csblogin
Patch0: rancid-2.3.2-Makefile.patch
Patch1: rancid-2.3.8-alt-conf.patch
Patch2: rancid-2.3.8-ping.patch
Patch3: rancid-2.3.8-csb.patch

BuildRequires: expect >= 5.40
BuildRequires: iputils
BuildRequires: perl-CGI perl-LockFile-Simple perl-MailTools

PreReq: shadow-utils
AutoReq: no
Requires: expect >= 5.40
Requires: MTA
Requires: cvs, perl-base, telnet, openssh-clients, iputils

%description
RANCID monitors a router's (or more generally a device's) configuration,
including software and hardware (cards, serial numbers, etc) and uses CVS
(Concurrent Version System) or Subversion to maintain history of changes.

%prep
%setup -n %name-%version
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
%configure --sysconfdir=%_sysconfdir/%name --bindir=%_libexecdir/%name --enable-conf-install
make

%install
%makeinstall_std
install -d -m 0755 %buildroot/%_localstatedir/%name
install -d -m 0755 %buildroot/%_logdir/%name
install -d -m 0755 %buildroot/%_logdir/%name/old
install -d -m 0755 %buildroot/%_sysconfdir/cron.d
install -d -m 0755 %buildroot/%_bindir/

#symlink some bins from %%{_libexecdir}/%%{name} to %%{_bindir}
for base in \
 %name %name-cvs %name-fe %name-run
 do
 ln -sf %_libexecdir/%name/${base} \
  %buildroot/%_bindir/${base}
done

install -D -p -m 0755 %SOURCE1 %buildroot/%_sysconfdir/cron.d/%name

#Patch cron file to point to correct installation directory
sed -i 's|RANCIDBINDIR|%_libexecdir/%name|g' %buildroot/%_sysconfdir/cron.d/%name

install -D -p -m 0644 %SOURCE2 %buildroot/%_sysconfdir/logrotate.d/%name

# Cisco small business support:
install -D -p -m 755 %SOURCE3 %buildroot/%_libexecdir/%name/csbrancid
install -D -p -m 755 %SOURCE4 %buildroot/%_libexecdir/%name/csblogin

mkdir docs
mv %buildroot%_datadir/%name/* docs

%pre
/usr/sbin/groupadd -r -f rancid
/usr/sbin/useradd -r -g rancid -d %_localstatedir/%name/ -s /bin/sh -m -c "RANCID" rancid >/dev/null 2>&1 ||:

%files
#%%{_sysconfdir}-files
%attr(750,%name,%name) %dir %_sysconfdir/%name
%attr(640,%name,%name) %config(noreplace) %_sysconfdir/%name/*
%attr(644,root,root) %config(noreplace) %_sysconfdir/cron.d/%name
%attr(644,root,root) %config(noreplace) %_sysconfdir/logrotate.d/%name

#%%{_libexecdir}/%%{name}-files
%dir %_libexecdir/%name/
%_libexecdir/%name/*

#%%{_bindir}-files
%_bindir/*

#%%{_mandir}-files
%_mandir/*/*

#%%{_localstatedir}-directories
%attr(750,%name,%name) %dir %_logdir/%name
%attr(750,%name,%name) %dir %_logdir/%name/old
%attr(750,%name,%name) %dir %_localstatedir/%name/

%doc docs/*

%changelog
* Sun Dec  8 2013 Terechkov Evgenii <evg@altlinux.org> 2.3.8-alt2
- Crontab entry fixed
- Cisco small business support from https://github.com/chrpinedo/rancid-cisco-sb

* Tue Dec  3 2013 Terechkov Evgenii <evg@altlinux.org> 2.3.8-alt1
- Initial build for ALT Linux Sisyphus
