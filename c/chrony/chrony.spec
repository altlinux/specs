%define vendorzone ru.

Name: chrony
Version: 4.6
Release: alt1

Summary: Chrony clock synchronization program
License: GPLv2
Group: System/Configuration/Other

Url: https://chrony-project.org/
VCS: https://gitlab.com/chrony/chrony
Source0: %name-%version.tar

Source1: clknetsim-chrony-%version.tar
Patch0: %name-%version-alt.patch
Source2: chronyd.init
Source3: chrony.sh

BuildRequires: libcap-devel libncurses-devel libedit-devel
BuildRequires: libnss-devel asciidoctor lynx libseccomp-devel
BuildRequires: libgnutls-devel
BuildRequires: libnettle-devel
BuildRequires: makeinfo control
BuildRequires: pps-tools-devel
# for tests
BuildRequires: /proc gcc-c++ /dev/kvm rpm-build-vm

Provides: ntp-server

Conflicts: ntpd openntpd

%define _localstatedir %_var

%description
A pair of programs for keeping computer clocks accurate. chronyd is a daemon
program and chronyc is a command-line interface to it. Time reference sources
for chronyd can be RFC1305 NTP servers, human (via keyboard and chronyc), and
the computer's real-time clock at boot time. chronyd can determine the rate at
which the computer gains or loses time and compensate for it whilst no external
reference is present. chronyd's use of NTP servers can be switched on and off
(through chronyc) to support computers with dial-up/intermittent access to the
Internet. chronyd can also act as an RFC1305-compatible NTP server.

%prep
%setup -a 1
%patch0 -p1
mv clknetsim-chrony-* test/simulation/clknetsim
# prepare git sources (make_release)
# version in version.txt file
echo %version > version.txt

# regenerate the file from getdate.y
rm -f getdate.c

# use our vendor zone
sed -e 's|\([0-3]\.\)\(pool.ntp.org\)|\1%{vendorzone}\2|' \
        < examples/chrony.conf.example2 > chrony.conf

echo '# Keys used by chronyd for command and NTP authentication' > chrony.keys

echo '# Pass extra arguments to chronyd' > chronyd.sysconfig
echo '#CHRONYD_ARGS=' >> chronyd.sysconfig

sed -i -e 's/OPTIONS/CHRONYD_ARGS/' examples/chronyd.service examples/chronyd-restricted.service
sed -i -e 's/User=chrony/User=_chrony/' examples/chronyd-restricted.service

%build
%configure \
	--with-user=_chrony \
	--with-hwclockfile=%_sysconfdir/adjtime \
	--chronyrundir=/run/chrony \
	--with-pidfile=/run/chrony/chronyd.pid \
	--enable-ntp-signd \
	--enable-scfilter \
	--with-ntp-era=$(date -d '1970-01-01 00:00:00+00:00' +'%%s') \
	--with-sendmail=%_sbindir/sendmail

%make_build all docs 
make -C doc txt

%check
export CLKNETSIM_RANDOM_SEED=34653
%make_build -C test/simulation/clknetsim
%make check

# chronyc dump + scfilter always falls when working in virtual environment under fakeroot, but in 
# real system it works fine. need to investigate
rm -f test/system/099-scfilter

# system tests must be run in kvm with fakeroot for permissions override
pushd test/system
vm-run fakeroot ./run
popd

%install
%makeinstall_std
install -pD -m755 %SOURCE2 %buildroot%_initrddir/chronyd
install -pD -m644 chrony.conf %buildroot%_sysconfdir/chrony.conf
install -pD -m644 chrony.keys %buildroot%_sysconfdir/chrony.keys
install -pD -m755 examples/chrony.nm-dispatcher.dhcp %buildroot%_sysconfdir/NetworkManager/dispatcher.d/20-chrony-dhcp
install -pD -m755 examples/chrony.nm-dispatcher.onoffline %buildroot%_sysconfdir/NetworkManager/dispatcher.d/21-chrony-onoffline
install -pD -m644 examples/chrony.logrotate %buildroot%_sysconfdir/logrotate.d/chrony
install -pD -m644 chronyd.sysconfig %buildroot%_sysconfdir/sysconfig/chronyd
install -pD -m644 examples/chronyd.service %buildroot%_unitdir/chronyd.service
install -pD -m644 examples/chronyd-restricted.service %buildroot%_unitdir/chronyd-restricted.service
install -pD -m644 examples/chrony-wait.service %buildroot%_unitdir/chrony-wait.service
install -pD -m755 %SOURCE3 %buildroot%_sysconfdir/control.d/facilities/chrony
ln -s chronyd.service %buildroot%_unitdir/chrony.service

install -d %buildroot/lib/systemd/ntp-units.d

echo 'chronyd.service' > \
        %buildroot/lib/systemd/ntp-units.d/50-chronyd.list

rm -rf %buildroot/usr/doc
install -d %buildroot%_localstatedir/{lib,log}/%name
touch %buildroot%_localstatedir/lib/%name/{drift,rtc}

mkdir -p  %buildroot%_tmpfilesdir
echo 'd /run/chrony 0750 _chrony _chrony' >> %buildroot%_tmpfilesdir/chronyd.conf

%pre
%_sbindir/groupadd -r -f _chrony 2> /dev/null ||:
%_sbindir/useradd -r -g _chrony -d %_localstatedir/lib/%name -s /dev/null -c "Chrony User" _chrony 2> /dev/null ||:

%post
# Move old configs to /etc
[ -e %_sysconfdir/%name/chrony.conf ] && mv %_sysconfdir/%name/chrony.conf %_sysconfdir/chrony.conf >/dev/null 2>&1 || :
[ -e %_sysconfdir/%name/chrony.keys ] && mv %_sysconfdir/%name/chrony.keys %_sysconfdir/chrony.keys >/dev/null 2>&1 || :

%post_service chronyd
%post_service chronyd-restricted

%preun
%preun_service chronyd
%preun_service chronyd-restricted

%files
%doc COPYING NEWS README doc/*.txt
%_initrddir/chronyd
%_unitdir/*.service
/lib/systemd/ntp-units.d/50-chronyd.list
%config(noreplace) %_sysconfdir/sysconfig/chronyd
%config(noreplace) %_sysconfdir/chrony.conf
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,_chrony) %_sysconfdir/chrony.keys
%config(noreplace) %_sysconfdir/logrotate.d/chrony
%config(noreplace) %_sysconfdir/control.d/facilities/chrony
%_tmpfilesdir/chronyd.conf
%_sysconfdir/NetworkManager/dispatcher.d/20-chrony-dhcp
%_sysconfdir/NetworkManager/dispatcher.d/21-chrony-onoffline
%_bindir/*
%_sbindir/*
%dir %attr(-,_chrony,_chrony) %_localstatedir/lib/%name
%ghost %attr(-,_chrony,_chrony) %_localstatedir/lib/%name/drift
%ghost %attr(-,_chrony,_chrony) %_localstatedir/lib/%name/rtc
%dir %attr(1775,root,_chrony) %_localstatedir/log/%name
%_man1dir/*
%_man5dir/*
%_man8dir/*

%changelog
* Tue Oct 08 2024 Anton Farygin <rider@altlinux.ru> 4.6-alt1
- 4.5 -> 4.6

* Mon Mar 25 2024 Alexey Shabalin <shaba@altlinux.org> 4.5-alt2
- package chronyd-restricted.service
- add alias chrony.service -> chronyd.service

* Thu Dec 28 2023 Anton Farygin <rider@altlinux.ru> 4.5-alt1
- 4.4 -> 4.5

* Tue Sep 05 2023 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- 4.3 -> 4.4

* Thu Sep 01 2022 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- 4.2 -> 4.3

* Sat May 21 2022 Anton Farygin <rider@altlinux.ru> 4.2-alt2
- use %%_tmpfilesdir

* Thu Dec 23 2021 Anton Farygin <rider@altlinux.ru> 4.2-alt1
- 4.1 -> 4.2
- enable system tests via run-vm
- added tmpfiles config

* Mon May 17 2021 Anton Farygin <rider@altlinux.ru> 4.1-alt1
- 4.1

* Wed Mar 10 2021 Anton Farygin <rider@altlinux.org> 4.0-alt2
- build with PPS support (closes: #39773)

* Wed Oct 28 2020 Anton Farygin <rider@altlinux.ru> 4.0-alt1
- 4.0
- built with gnutls and nettle to enable NTS support
- built with libedit instead of libreadline

* Wed Aug 26 2020 Anton Farygin <rider@altlinux.ru> 3.5.1-alt1
- 3.5.1 (fixes: CVE-2020-14367)

* Wed Apr 01 2020 Anton Farygin <rider@altlinux.ru> 3.5-alt3
- set ntp era (fixed FTBFS, thanks to glebfm for the investigation)

* Wed Oct 16 2019 Anton Farygin <rider@altlinux.ru> 3.5-alt2
- fixed help in chrony control script (closes: #37340)

* Tue May 21 2019 Anton Farygin <rider@altlinux.ru> 3.5-alt1
- 3.5

* Mon Oct 01 2018 Anton Farygin <rider@altlinux.ru> 3.4-alt1
- 3.4
- enabled tests

* Wed Aug 15 2018 Anton Farygin <rider@altlinux.ru> 3.3-alt2
- enabled seccomp filter and signd features

* Tue Apr 10 2018 Anton Farygin <rider@altlinux.ru> 3.3-alt1
- 3.3

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 3.2-alt1
- new version 

* Tue Aug 01 2017 Anton Farygin <rider@altlinux.ru> 3.1-alt1
- new version

* Sun Mar 12 2017 Evgeny Sinelnikov <sin@altlinux.ru> 2.2-alt2
- Build with universal build tag

* Fri Dec 23 2016 Denis Medvedev <nbr@altlinux.org> 2.2-alt2
- Provides ntp-server, needed for alterator-datetime.
Added chrony control.

* Sat Dec 19 2015 Terechkov Evgenii <evg@altlinux.org> 2.2-alt1.1
- change ownership/mode of logdir according to SPP (ALT #31640)

* Thu Dec 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2

* Wed Sep 17 2014 Alexey Shabalin <shaba@altlinux.ru> 1.31-alt1
- 1.31

* Thu Jul 10 2014 Alexey Shabalin <shaba@altlinux.ru> 1.30-alt1
- 1.30
- moved configs to /etc

* Fri Mar 07 2014 Alexey Shabalin <shaba@altlinux.ru> 1.29.1-alt1
- 1.29.1
- drop root priveleges to user _chrony for chronyd daemon
- add /etc/sysconfig/chronyd
- add systemd support
- update chronyd config
- update chronyd logrotate

* Mon Jul 18 2011 Victor Forsiuk <force@altlinux.org> 1.26-alt1
- 1.26

* Sat Jun 11 2011 Victor Forsiuk <force@altlinux.org> 1.25-alt1
- 1.25

* Mon Feb 08 2010 Victor Forsiuk <force@altlinux.org> 1.24-alt1
- 1.24. Contains security fixes for CVE-2010-0292, CVE-2010-0293, CVE-2010-0294.

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 1.23-alt2
- Project homepage moved, so fix Url.

* Mon Feb 25 2008 Victor Forsyuk <force@altlinux.org> 1.23-alt1
- Initial build.
