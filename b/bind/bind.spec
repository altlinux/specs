%define _unpackaged_files_terminate_build 1

# build rules
%def_with docs
%def_with openssl
%def_with libjson
%def_without python
%def_with check
%def_without system_tests

# common directory for documentation
%define docdir %_docdir/bind-%version
# root directory for chrooted environment
%define _chrootdir %_localstatedir/bind
%define run_dir /run/named
%define log_dir %_logdir/named
%define restart_flag /run/named/named.restart

%define named_user named
%define named_group named

%ifndef timestamp
%define timestamp %(TZ=UTC LC_TIME=C date +%%Y%%m%%d)
%endif

Name: bind
Version: 9.16.35
%define src_version 9.16.35
Release: alt1

Summary: ISC BIND - DNS server
License: MPL-2.0
Group: System/Servers
Url: https://www.isc.org/bind/
VCS: https://gitlab.isc.org/isc-projects/bind9.git

# ftp://ftp.isc.org/isc/bind9/%src_version/bind-%src_version.tar.xz
Source0: %name-%version.tar
Source3: README.bind-devel
Source4: README.ALT

Source11: bind.init

Source21: rndc.conf
Source22: rndc.key

Source31: bind.named.conf
Source32: bind.options.conf
Source33: bind.rndc.conf
Source34: bind.local.conf
Source35: bind.rfc1912.conf
Source36: bind.rfc1918.conf
Source37: bind.sysconfig

Source41: bind.localhost
Source42: bind.localdomain
Source43: bind.127.in-addr.arpa
Source44: bind.empty

Source50: bind.service
Source51: bind.tmpfiles.conf

# NB: there must be at least one patch :)
Patch0001: 0001-ALT-defaults-Reintroduce-chrooted-named-by-default.patch
Patch0002: 0002-ALT-Minimize-linux-capabilities.patch
Patch0003: 0003-ALT-Make-it-possible-to-retain-Linux-capabilities-of.patch
Patch0004: 0004-ALT-named-Allow-non-writable-working-directory.patch
Patch0005: 0005-ALT-tests-Unchroot-named-for-tests.patch
Patch0006: 0006-ALT-tests-Add-tests-for-signing-with-custom-OpenSSL.patch
Patch0007: 0007-ALT-tests-Raise-expected-delta-time-for-cds.patch
Patch0008: 0008-ALT-tests-Wait-up-to-30sec-for-the-server-start.patch

%if_with docs
BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)
%endif

%if_with check
%if_with system_tests
BuildRequires: python3(dns)
BuildRequires: python3(hypothesis)
# requires only for pkcs11 tests
BuildRequires: softhsm
BuildRequires: libp11
BuildRequires: opensc
%else
BuildRequires: rpm-build-vm
BuildRequires: /sbin/runuser
BuildRequires: /dev/kvm
%endif

BuildRequires: iproute2
BuildRequires: perl-Net-DNS
BuildRequires: perl-File-Fetch
BuildRequires: perl-Digest-HMAC
BuildRequires: python3(pytest)
%endif

Provides: bind-chroot(%_chrootdir)
Obsoletes: bind-chroot, bind-debug, bind-slave, caching-nameserver
# Because of /etc/syslog.d/ feature.
Conflicts: syslogd < 1.4.1-alt11
Requires(pre): bind-control >= 1.3

# due to %_chrootdir/dev/log
BuildPreReq: coreutils

# due to broken configure script
BuildPreReq: gcc-c++

# for better --enable-linux-caps experience
BuildPreReq: libcap-devel

%{?_with_openssl:BuildPreReq: libssl-devel}
%{?_with_libjson:BuildPreReq: libjson-c-devel}
BuildPreReq: libkrb5-devel
BuildRequires: libuv-devel
BuildRequires: libidn2-devel

%package utils
Summary: Utilities provided by ISC BIND
Group: Networking/Other
Requires: libbind = %EVR

%package -n libbind
Summary: Shared library used by ISC BIND
Group: System/Libraries
Provides: libdns = %EVR
Provides: libisc = %EVR
Provides: libisccc = %EVR
Provides: libisccfg = %EVR
Obsoletes: libdns8, libdns9, libdns10, libdns11, libdns16
Obsoletes: libisc4, libisc7, libisccc0, libisccfg0

%package devel
Summary: ISC BIND development libraries and headers
Group: Development/C
Requires: libbind = %EVR
Provides: libisc-export-devel = %EVR
Obsoletes: libisc-export-devel < %version

%if_with docs
%package doc
Summary: Documentation for ISC BIND
Group: Development/Other
BuildArch: noarch
Prefix: %prefix
%endif

%description
The Berkeley Internet Name Domain (BIND) implements an Internet domain
name server.  BIND is the most widely-used name server software on the
Internet, and is supported by the Internet Software Consortium (ISC).

This package provides the %src_version server and related
configuration files.

%description utils
This package contains various utilities related to DNS that are derived
from the BIND %src_version source tree, including dig, host,
nslookup and nsupdate.

%description -n libbind
This package contains shared libraries used by BIND's %src_version
daemons and clients.

%description devel
This package contains development libraries, header files, and API man
pages for libdns, libisc, libisccc, libisccfg. These are
only needed if you want to compile packages that need more BIND
%src_version nameserver API than the resolver code provided by
glibc.

%if_with docs
%description doc
This package provides various documents that are useful for maintaining
a working BIND %src_version installation.
%endif

%prep
%setup

# NB: there must be at least one patch :)
%autopatch -p2

mkdir addon
install -pm644 \
    %_sourcedir/bind.init \
    %_sourcedir/bind.named.conf \
    %_sourcedir/bind.options.conf \
    %_sourcedir/bind.rndc.conf \
    %_sourcedir/bind.local.conf \
    %_sourcedir/bind.rfc1912.conf \
    %_sourcedir/bind.rfc1918.conf \
    %_sourcedir/bind.localhost \
    %_sourcedir/bind.localdomain \
    %_sourcedir/bind.127.in-addr.arpa \
    %_sourcedir/bind.empty \
    %_sourcedir/bind.sysconfig \
    %_sourcedir/bind.service \
    %_sourcedir/bind.tmpfiles.conf \
    %_sourcedir/rndc.conf \
    %_sourcedir/rndc.key \
    addon/

find -type f -print0 |
	xargs -r0 grep -lZ '@[A-Z_]\+@' -- |
	xargs -r0 sed -i \
'
s,@ROOT@,%_chrootdir,g;
s,@DISTRO_OPTIONS@,-u %named_user,g;
s,@RUN_DIR@,%run_dir,g;
s,@NAMED_USER@,%named_user,g;
s,@LOG_DIR@,%log_dir,g;
' --

%build
%if_with docs
# see HTMLTARGET in configure.ac and doc/arm/Makefile.in
export SPHINX_BUILD=/usr/bin/sphinx-build-3
%endif

%autoreconf
%configure \
	--localstatedir=/var \
	--with-libidn2 \
	--enable-linux-caps \
	--enable-fixed-rrset \
	 %{subst_with openssl} \
%if_with libjson
	--with-json-c=yes \
%endif
	 %{subst_with python} \
	--disable-static \
	--includedir=%{_includedir}/bind9 \
	--with-libtool \
	--with-gssapi=yes \
	#

%make_build

%if_with docs
%make doc
%endif

%install
%makeinstall_std

# Install additional headers.
install -pm644 lib/isc/unix/errno2result.h %buildroot%_includedir/bind9/isc/

# Install startup scripts.
install -pD -m755 addon/bind.init %buildroot%_initdir/bind

# Install systemd service
install -pD -m644 addon/bind.service %buildroot%_unitdir/bind.service
install -pD -m644 addon/bind.tmpfiles.conf %buildroot%_tmpfilesdir/bind.conf

# Install configurations files
install -pm640 addon/rndc.conf %buildroot%_sysconfdir/
install -pD -m644 addon/bind.sysconfig %buildroot%_sysconfdir/sysconfig/bind

mkdir -p %buildroot%run_dir
mkdir -p %buildroot%log_dir

# Create a chrooted environment...
mkdir -p %buildroot%_chrootdir/{dev,%_sysconfdir,var/run,session,zone/slave}
for n in named options rndc local rfc1912 rfc1918; do
	install -pm640 "addon/bind.$n.conf" \
		"%buildroot%_chrootdir%_sysconfdir/$n.conf"
done
for n in localhost localdomain 127.in-addr.arpa empty; do
	install -pm640 "addon/bind.$n" \
		"%buildroot%_chrootdir/zone/$n"
	sed -i s/YYYYMMDDNN/%{timestamp}00/ \
		"%buildroot%_chrootdir/zone/$n"
done

install -pm640 addon/rndc.key bind.keys %buildroot%_chrootdir%_sysconfdir/
ln -snfr %buildroot%_sysconfdir/bind/{named.conf,bind.keys} \
	%buildroot%_sysconfdir/

# Create symlinks for unchrooted bind.
ln -snf . %buildroot%_chrootdir%_sysconfdir/bind
ln -snf ../zone %buildroot%_chrootdir%_sysconfdir/zone
ln -snfr %buildroot%_chrootdir%_sysconfdir %buildroot%_sysconfdir/bind

# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
/usr/bin/mksock %buildroot%_chrootdir/dev/log
mkdir %buildroot%_sysconfdir/syslog.d
ln -s %_chrootdir/dev/log %buildroot%_sysconfdir/syslog.d/bind
#... end of the chroot configuration.

# ALT docs
mkdir -p %buildroot%docdir
cp -a README %SOURCE3 %SOURCE4 CHANGES %buildroot%docdir/

%if_with docs
mkdir -p %buildroot%docdir/arm
cp -a doc/arm/_build/html %buildroot%docdir/arm/
%endif

# legacy path for plugins (for example, bind-dyndb-ldap)
mkdir -p %buildroot%_libdir/bind

# filetrigger: delayed restart of named if named or its plugins were
# installed/upgraded
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/%name-restart.filetrigger <<'EOF'
#!/bin/sh -u
# delayed restart of named if its plugins were installed/upgraded

grep -qsE -- '^%_libdir/(named|bind)/' && [ -f '%restart_flag' ] || exit 0
rm -f '%restart_flag'

service bind start
exit 0
EOF
chmod 0755 %buildroot%_rpmlibdir/%name-restart.filetrigger

%check
%if_with system_tests
# setup and teardown require root
perl bin/tests/system/testsock.pl || sudo sh -x bin/tests/system/ifconfig.sh up

# setup softhsm
export SOFTHSM_MODULE_PATH=%_libdir/softhsm/libsofthsm2.so
export SOFTHSM2_CONF=/tmp/softhsm2/softhsm2.conf
export OPENSSL_CONF=/tmp/softhsm2/openssl.cnf
export PKCS11_ENGINE=pkcs11
export SLOT=$(sh -eu bin/tests/prepare-softhsm2.sh)

# tests are run as current user
# see .gitlab-ci.yml
pushd bin/tests/system
# named must be unchrooted for upstream tests
export ALT_NAMED_OPTIONS=' -t / '
SYSTEMTEST_NO_CLEAN=1 %make_build -k test V=1

# depends on PKCS11_TEST, which is only defined if named is built with native
# PKCS11
SYSTEMTEST_NO_CLEAN=1 sh run.sh pkcs11

# teardown
popd
sudo sh bin/tests/system/ifconfig.sh down

%else
# today's (2021) vm-run (underlying KVM) is relatively slow.
# The complete tests suite takes ~1h on x86_64 and results are not stable atm.
# I tried to filter out some expected heavy tests by roughly the number of
# named instances they use (<=2). The expected acceptable tests time is ~10min
# on x86_64.

cat > run_smoke.sh <<'_EOF'
# setup
runas="$1"
perl bin/tests/system/testsock.pl || sh -x bin/tests/system/ifconfig.sh up
ip a

# tests
# named must be unchrooted for upstream tests
export ALT_NAMED_OPTIONS=' -t / '

pushd bin/tests/system
source ./conf.sh
for testdir in $SUBDIRS; do
    subns=$(find "$testdir" -maxdepth 1 -type d -name "ns[0-9]" | wc -l)
    if [ $subns -lt 2 ]; then
        runuser -u "$runas" -- sh run.sh "$testdir"
    fi
done

# teardown
popd
sh bin/tests/system/ifconfig.sh down
_EOF
time vm-run --kvm=cond --sbin -- /bin/bash --norc --noprofile -eu run_smoke.sh "$(id -un)"
%endif

%pre
/usr/sbin/groupadd -r -f %named_group
/usr/sbin/useradd -r -g %named_group -d %_chrootdir -s /dev/null -n \
    -c "Domain Name Server" %named_user >/dev/null 2>&1 ||:
[ -f %_initdir/named -a ! -L %_initdir/named ] && /sbin/chkconfig --del named ||:

# save running status and use it in post-transaction
rm -f '%restart_flag'

if [ "$1" -gt 1 ]; then
    SYSTEMCTL=systemctl
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" is-active bind.service >/dev/null 2>&1 &&
        "$SYSTEMCTL" stop bind.service 2>/dev/null &&
        mkdir -p "$(dirname '%restart_flag')" &&
        touch '%restart_flag' 2>/dev/null ||:
    else
        %_initdir/bind status >/dev/null 2>&1 &&
        %_initdir/bind stop 2>/dev/null &&
        mkdir -p "$(dirname '%restart_flag')" &&
        touch '%restart_flag' 2>/dev/null ||:
    fi
fi

%pre_control bind-chroot bind-debug bind-slave bind-caps

%preun
%preun_service bind

%post
SYSLOGD_SCRIPT=/etc/init.d/syslogd
SYSLOGD_CONFIG=/etc/sysconfig/syslogd
if grep -qs '^SYSLOGD_OPTIONS=.*-a %_chrootdir/dev/log' "$SYSLOGD_CONFIG"; then
	# Remove artefacts of pre-syslog.d epoch.
	sed -i 's|^\(SYSLOGD_OPTIONS=.*\) \?-a %_chrootdir/dev/log|\1|' "$SYSLOGD_CONFIG"
	if [ -x "$SYSLOGD_SCRIPT" ]; then
		"$SYSLOGD_SCRIPT" condreload ||:
	fi
fi

%post_control -s enabled bind-chroot
%post_control -s disabled bind-debug bind-slave bind-caps

# next section is the copy of post_service, but
# it doesn't restart named since this is responsibility of filetrigger
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
    "$SYSTEMCTL" daemon-reload
    if [ "$1" -eq 1 ]; then
        "$SYSTEMCTL" -q preset bind
    fi
else
    if [ "$1" -eq 1 ]; then
        chkconfig --add bind
    else
        chkconfig bind resetpriorities
    fi
fi

%triggerun -- bind < 9.11.19-alt3
F=/etc/sysconfig/bind
if [ $2 -gt 0 -a -f $F ]; then
	grep -q '^#\?CHROOT=' $F || echo '#CHROOT="-t /"' >> $F
	grep -q '^#\?RETAIN_CAPS=' $F || echo '#RETAIN_CAPS="-r"' >> $F
fi

%files -n libbind
%_libdir/libbind9-%version.so
%_libdir/libdns-%version.so
%_libdir/libirs-%version.so
%_libdir/libisc-%version.so
%_libdir/libisccc-%version.so
%_libdir/libisccfg-%version.so
%_libdir/libns-%version.so

%files devel
%dir %docdir
%docdir/README.bind-devel
%_libdir/libbind9.so
%_libdir/libdns.so
%_libdir/libirs.so
%_libdir/libisc.so
%_libdir/libisccc.so
%_libdir/libisccfg.so
%_libdir/libns.so
%_includedir/bind9

%files
%dir %docdir
%docdir/CHANGES
%docdir/README
%docdir/README.ALT
# plugins
%dir %_libdir/named
%_libdir/named/filter-aaaa.so
# legacy path for plugins (for example, bind-dyndb-ldap)
%dir %_libdir/bind

%_bindir/arpaname
%_bindir/named-rrchecker
%_sbindir/*
%_sysconfdir/bind
%_sysconfdir/bind.keys
%_sysconfdir/named.conf
%config %_initdir/bind
%config(noreplace) %_sysconfdir/sysconfig/bind
%config(noreplace) %attr(640,root,%named_group) %_sysconfdir/rndc.conf
%dir %attr(770,root,%named_group) %run_dir
%dir %attr(770,root,%named_group) %log_dir
%_unitdir/bind.service
%_tmpfilesdir/bind.conf

%_rpmlibdir/%name-restart.filetrigger

%_man1dir/named-rrchecker.1*
%_man5dir/*
%_man8dir/*
%_man1dir/arpaname*

#chroot
%_sysconfdir/syslog.d/*
%defattr(640,root,%named_group,710)
%dir %_chrootdir
%dir %_chrootdir/dev
%dir %_chrootdir%_sysconfdir
%dir %attr(1770,root,%named_group) %_chrootdir/zone
%dir %attr(700,root,%named_group) %verify(not mode) %_chrootdir/zone/slave
%dir %attr(700,root,%named_group) %verify(not mode) %_chrootdir/var
%dir %attr(1770,root,%named_group) %_chrootdir/var/run
%dir %attr(700,root,%named_group) %_chrootdir/session
%config(noreplace) %_chrootdir%_sysconfdir/*.conf
%config(noreplace) %verify(not md5 mtime size) %_chrootdir%_sysconfdir/rndc.key
%_chrootdir%_sysconfdir/bind.keys
%attr(-,root,root) %_chrootdir%_sysconfdir/bind
%attr(-,root,root) %_chrootdir%_sysconfdir/zone
%config %_chrootdir/zone/localhost
%config %_chrootdir/zone/localdomain
%config %_chrootdir/zone/127.in-addr.arpa
%config %_chrootdir/zone/empty

%ghost %attr(666,root,root) %_chrootdir/dev/*

%files utils
%_bindir/delv
%_bindir/dig
%_bindir/mdig
%_bindir/host
%_bindir/nslookup
%_bindir/nsupdate
%_man1dir/delv.*
%_man1dir/dig.*
%_man1dir/mdig.*
%_man1dir/host.*
%_man1dir/nslookup.*
%_man1dir/nsupdate.*

%if_with docs
%files doc
%dir %docdir
%docdir/arm
%endif

%changelog
* Wed Nov 16 2022 Stanislav Levin <slev@altlinux.org> 9.16.35-alt1
- 9.16.34 -> 9.16.35.

* Tue Oct 25 2022 Stanislav Levin <slev@altlinux.org> 9.16.34-alt1
- 9.11.37 -> 9.16.34 (closes: #40170).
- Built with libidn2 (closes: #24573).
- Fixed Url (closes: #43556).

* Thu Mar 17 2022 Stanislav Levin <slev@altlinux.org> 9.11.37-alt1
- 9.11.36 -> 9.11.37 (fixes: CVE-2021-25220).

* Thu Oct 28 2021 Stanislav Levin <slev@altlinux.org> 9.11.36-alt1
- 9.11.32 -> 9.11.36 (fixes: CVE-2021-25219).

* Mon May 24 2021 Stanislav Levin <slev@altlinux.org> 9.11.32-alt1
- 9.11.31 -> 9.11.32.

* Thu Apr 29 2021 Stanislav Levin <slev@altlinux.org> 9.11.31-alt1
- 9.11.28 -> 9.11.31 (fixes: CVE-2021-25214, CVE-2021-25215, CVE-2021-25216).

* Thu Feb 18 2021 Stanislav Levin <slev@altlinux.org> 9.11.28-alt1
- 9.11.25 -> 9.11.28 (fixes: CVE-2020-8625).

* Mon Nov 30 2020 Stanislav Levin <slev@altlinux.org> 9.11.25-alt2
- Backported fix for man pages (closes: #39350).

* Fri Nov 27 2020 Stanislav Levin <slev@altlinux.org> 9.11.25-alt1
- 9.11.22 -> 9.11.25.

* Fri Aug 21 2020 Stanislav Levin <slev@altlinux.org> 9.11.22-alt1
- 9.11.20 -> 9.11.22 (fixes: CVE-2020-8622, CVE-2020-8623, CVE-2020-8624).

* Mon Jun 29 2020 Stanislav Levin <slev@altlinux.org> 9.11.20-alt1
- 9.11.19 -> 9.11.20 (fixes: CVE-2020-8619).

* Fri May 29 2020 Stanislav Levin <slev@altlinux.org> 9.11.19-alt3
- Placed Linux capabilities dropping under control(1).

* Fri May 29 2020 Stanislav Levin <slev@altlinux.org> 9.11.19-alt2
- Re-applied the lost patch.

* Tue May 19 2020 Stanislav Levin <slev@altlinux.org> 9.11.19-alt1
- 9.11.18 -> 9.11.19 (fixes: CVE-2020-8616, CVE-2020-8617).

* Fri Apr 17 2020 Stanislav Levin <slev@altlinux.org> 9.11.18-alt1
- 9.11.13 -> 9.11.18.

* Thu Nov 21 2019 Stanislav Levin <slev@altlinux.org> 9.11.13-alt1
- 9.11.12 -> 9.11.13 (fixes: CVE-2019-6477).

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 9.11.12-alt1
- 9.11.10 -> 9.11.12.

* Wed Sep 18 2019 Stanislav Levin <slev@altlinux.org> 9.11.10-alt2
- Fixed integration with ipa-dnskeysync.

* Tue Aug 27 2019 Stanislav Levin <slev@altlinux.org> 9.11.10-alt1
- 9.11.9 -> 9.11.10.

* Thu Aug 01 2019 Stanislav Levin <slev@altlinux.org> 9.11.9-alt1
- 9.11.8 -> 9.11.9.

* Thu Jun 20 2019 Stanislav Levin <slev@altlinux.org> 9.11.8-alt1
- 9.11.7 -> 9.11.8 (fixes: CVE-2019-6471).

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 9.11.7-alt1
- 9.11.6.P1 -> 9.11.7.

* Thu Apr 25 2019 Stanislav Levin <slev@altlinux.org> 9.11.6.P1-alt1
- 9.11.6 -> 9.11.6.P1 (fixes: CVE-2018-5743).

* Wed Mar 27 2019 Stanislav Levin <slev@altlinux.org> 9.11.6-alt2
- Fixed support for GSSAPI (closes: #36429).

* Fri Mar 01 2019 Stanislav Levin <slev@altlinux.org> 9.11.6-alt1
- 9.11.5.P4 -> 9.11.6.

* Fri Feb 22 2019 Stanislav Levin <slev@altlinux.org> 9.11.5.P4-alt1
- 9.11.5 -> 9.11.5.P4 (fixes: CVE-2018-5744, CVE-2018-5745, CVE-2019-6465).

* Fri Nov 23 2018 Stanislav Levin <slev@altlinux.org> 9.11.5-alt1
- 9.11.4.P2 -> 9.11.5.

* Thu Sep 20 2018 Stanislav Levin <slev@altlinux.org> 9.11.4.P2-alt1
- 9.11.4.P1 -> 9.11.4.P2.

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 9.11.4.P1-alt2
- Build with new openssl1.1.

* Mon Aug 13 2018 Stanislav Levin <slev@altlinux.org> 9.11.4.P1-alt1
- 9.11.3 -> 9.11.4.P1 (fixes: CVE-2018-5738, CVE-2018-5740).

* Wed Apr 04 2018 Stanislav Levin <slev@altlinux.org> 9.11.3-alt1
- 9.11.2.P1 -> 9.11.3

* Wed Feb 28 2018 Stanislav Levin <slev@altlinux.org> 9.11.2.P1-alt2
- Build with libjson support (statistics channels)

* Wed Jan 17 2018 Stanislav Levin <slev@altlinux.org> 9.11.2.P1-alt1
- 9.11.2 -> 9.11.2-P1 (fixes: CVE-2017-3145).

* Thu Dec 07 2017 Stanislav Levin <slev@altlinux.org> 9.11.2-alt2
- Fix lack of rndc.key in non-chrooted bind (closes: #34292).

* Fri Nov 03 2017 Stanislav Levin <slev@altlinux.org> 9.11.2-alt1
- 9.10.6 -> 9.11.2.

* Fri Jul 28 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.6-alt1
- 9.10.5-P3 -> 9.10.6.

* Tue Jul 11 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.5.P3-alt1
- 9.10.4-P8 -> 9.10.5-P3
  (fixes: CVE-2017-3140, CVE-2017-3141, CVE-2017-3142, CVE-2017-3143).

* Wed Apr 12 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.4.P8-alt1
- 9.10.4-P6 -> 9.10.4-P8 (fixes: CVE-2017-3136, CVE-2017-3137, CVE-2017-3138).
- bind.service: pass $CHROOT to named-checkconf (closes: #33239).
- bind.init: check named configuration on startup.

* Wed Feb 08 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.4-alt2
- 9.10.4-P5 -> 9.10.4-P6 (fixes CVE-2017-3135).

* Thu Jan 12 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.4-alt1
- 9.9.9-P5 -> 9.10.4-P5 (closes: #30124, #32590).
- Enabled multiprocessing support.
- bind: bind.service: fixed EnvironmentFile.
- bind: options.conf: fixed typo in comment (closes: #31359).
- bind: enabled "fixed" ordering support in rrset-order statement.
- bind: packaged named-rrchecker.
- bind: imported "dynamic-db" statement support from Fedora
  (by Sergey Bolshakov).
- bind: placed chrooted mode under control(1) (by Sergey Bolshakov).
- bind-devel: packaged bind9-config.
- bind-utils: packaged delv.

* Sat Jan 07 2017 Dmitry V. Levin <ldv@altlinux.org> 9.9.9-alt1
- 9.9.8-P4 -> 9.9.9-P5.
- Implemented early drop of linux capabilities.

* Wed Nov 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.9.8-alt5
- Applied upstream fix for CVE-2016-8864.

* Tue Sep 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.9.8-alt4
- Applied upstream fix for CVE-2016-2776.

* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 9.9.8-alt3
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P4.tar.gz
- Build with --enable-fetchlimit (Closes: #31701)

* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 9.9.8-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P3.tar.gz

* Thu Dec 17 2015 Fr. Br. George <george@altlinux.ru> 9.9.8-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P2.tar.gz

* Thu Sep 03 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt3
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P3/bind-9.9.7-P3.tar.gz

* Wed Jul 29 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P2/bind-9.9.7-P2.tar.gz

* Tue Jul 28 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P1/bind-9.9.7-P1.tar.gz
- CVE-2015-5477 fix

* Thu Dec 11 2014 Fr. Br. George <george@altlinux.ru> 9.9.6-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.6-P1/bind-9.9.6-P1.tar.gz

* Tue Nov 18 2014 Fr. Br. George <george@altlinux.ru> 9.9.6-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.6/bind-9.9.6.tar.gz
- Fix old style autoheader AC_DEFINE
- Enable ratelimits (Closes: #30398)
- Provide initial rndc_keygen (Closes: #28034)

* Mon Oct 06 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt3
- Build with GSSAPI

* Tue Jun 17 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt2
- Updated to ftp://ftp.isc.org/isc/bind9/9.9.5-P1/bind-9.9.5-P1.tar.gz

* Mon Feb 03 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.5/bind-9.9.5.tar.gz
- Don't package bind9-config (in favour of lib*-export)

* Thu Nov 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.4-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.4-P1/bind-9.9.4-P1.tar.gz
- (CVE-2013-6230 is fixed in this version)

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 9.9.4-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.4/bind-9.9.4.tar.gz

* Sun Jul 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt3
- Update to ftp://ftp.isc.org/isc/bind/9.9.3-P2/bind-9.9.3-P2.tar.gz

* Tue Jun 11 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.3-P1/bind-9.9.3-P1.tar.gz

* Thu Jun 06 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.3/bind-9.9.3.tar.gz
- Drop alt-isc-config.patch

* Thu Mar 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.2-alt5
- Update to ftp://ftp.isc.org/isc/bind9/9.9.2-P2/bind-9.9.2-P2.tar.gz
- Turn regex support off

* Fri Dec 28 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt4
- Service file fixup

* Tue Dec 11 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt3
- Update to 9.9.2-P1 (CVE-2012-5688 and bugfixes)
- Add systemd service file (from FC)

* Wed Nov 07 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt2
- Fix pidfile recreation try on reload
- Replace index IDs in patches to dummy ones

* Wed Oct 17 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt1
- Version up to 9.9.2 (CVE 5166 included)

* Mon Oct 15 2012 Fr. Br. George <george@altlinux.ru> 9.9.1-alt1
- Version up to 9.9.1-P3 (6 middle versions jump!)
- Drop outdated patches (including CVE 5166, this is insecure build)
- Adapt actual patches

* Wed Oct 10 2012 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt8
- Imported fixes for several vulnerabilities from RH bind-9.3.6-20.P1.5
  (CVE-2012-{1033,1667,4244,5166}).

* Fri Dec 16 2011 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt7
- Imported fixes for several DNSSEC vulnerabilities from RH bind
  (CVE-2009-4022, CVE-2010-0097, CVE-2010-3762, CVE-2011-4313);
  note that DNSSEC is not enabled by default.
- Enabled IPv6 support.
- Fixed RPATH issue.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt6
- Rebuilt with libcrypto.so.10.

* Tue Jul 28 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt5
- Backported upstream fix for a remote DoS bug (CVE-2009-0696).

* Thu Apr 30 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt4
- Removed resolver(5) manual page (closes: #19784).

* Fri Mar 06 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt3
- options.conf:
  + Removed root-delegation-only directive.
  + Added interface-interval directive example.
- Made "max open files" limit by default as large as default "max sockets" limit.

* Wed Jan 07 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt2
- Updated to 9.3.6-P1 release.

* Mon Nov 24 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt1
- Updated to 9.3.6 release.

* Sun Aug 10 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt4
- Implemented automatic fdsets expansion to overcome FD_SETSIZE limit.

* Thu Aug 07 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt3
- Updated to 9.3.5-P2 release.

* Fri Jun 06 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt2
- Updated to 9.3.5-P1 release (fixes VU#800113/CVE-2008-1447).

* Wed Apr 16 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt1
- Updated to 9.3.5 release.

* Mon Nov 05 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt5
- options.conf: Added recursing-file directive.
- Updated L.ROOT-SERVERS.NET: 198.32.64.12 -> 199.7.83.42.

* Tue Jul 24 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt4
- Updated to 9.3.4-P1 release (fixes CVE-2007-2926).

* Fri Apr 06 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt3
- rndc-confgen: Revert previous change.
- Changed startup script to use /dev/urandom as a source
  of randomness during rndc key generation.

* Wed Apr 04 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt2
- rndc-confgen: Restore default key size (#11321).

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt1
- Updated to 9.3.4 release.

* Fri Dec 29 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt2
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt1
- Updated to 9.3.3 release.

* Fri Nov 03 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.2
- Updated to 9.3.3 RC3.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.1
- Updated to 9.3.3 RC2.

* Wed Sep 06 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt2
- Updated to 9.3.2 P1.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt1
- Updated to 9.3.2 release.

* Tue Sep 27 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt2
- Fixed /etc/syslog.d/bind bug introduced in previous release:
  /etc/syslog.d/* must be absolute symlinks.

* Wed Sep 21 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt1
- Updated to 9.3.1 release.
- Synced with Owl's bind-9.3.1-owl1 package.
- Applied few fixes from RH and SuSE bind packages.
- Merged all shared libraries into single package, libbind.
- Replaced -debug and -slave subpackages with control facilities.
- Converted absolute symlinks into relative.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt2
- Fixed build of queryperf utility on x86_64 platform (closes #6083).

* Fri Sep 24 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt1
- Updated to 9.2.4 release (== 9.2.4rc8).

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc8-alt1
- Updated to 9.2.4rc8.
- Renamed subpackage according to soname change:
  libdns11 -> libdns16.
- Updated startup script to make use of new "status --lockfile" option.

* Wed Jun 30 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc5-alt1
- Updated to 9.2.4rc5.
- Updated patches.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 9.2.3.rel-alt2.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 10 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt2
- Updated build dependencies.
- Do not build static library by default.

* Mon Nov 24 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt1
- Updated to 9.2.3 release.
- Rediffed patches.
- Do not package .la files.
- named.8: fixed reference to the BIND 9 Administrator Reference Manual.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc4-alt1
- Updated to 9.2.3rc4.
- Renamed subpackage according to soname change:
  libdns10 -> libdns11.
- Replaced "delegation-only" defaults implemented in previous release
  with new option, root-delegation-only, and enabled it by default.

* Thu Sep 18 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc2-alt1
- Updated to 9.2.3rc2.
- Renamed subpackage according to soname change:
  libdns9 -> libdns10.
- Marked all known gTLDs and ccTLDs as delegation-only by default.

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt2
- Merged patches from OpenBSD, thanks to Jarno Huuskonen:
  + write pidfile before chroot (#2866);
  + use chroot jailing by default, no -u/-t options are necessary;
- Make named-checkconf use chroot jail by default (Jarno Huuskonen).
- options.conf: added few samples (#2968).

* Tue Aug 26 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt1
- Updated to 9.2.3rc1.
- Removed alt-lib_dns_rootns patch (merged upstream).
- Explicitly disable use of linux capabilities.
- Renamed subpackages according to soname changes:
  libdns8 -> libdns9, libisc4 -> libisc7.

* Tue Jul 29 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt2
- Fixed message from 'service bind reload' (#0002411).
- Moved 'include "/etc/rfc1912.conf";' directive
  from bind.conf to local.conf (#0002791).
- Rewritten start/stop script to new rc scheme.

* Tue Mar 04 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt1
- Updated to 9.2.2 release.

* Wed Feb 12 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt2
- Relocated initial rndc key generation from %%post to startup script.
- Added some information about ALT specific to named(8) and rndc(8).
- Added README.ALT.

* Thu Feb 06 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt1
- Migrated to 9.2.2rc1.
- Build --with-libtool --with-openssl --disable-ipv6 --disable-threads.
- Do not package contrib.
- Package queryperf utility.
- Package each shared library separately:
  libdns8 libisc4 libisccc0 libisccfg0 liblwres1.
- Package lwresd separately (chrooted to /var/resolv).
- Moved %_chrootdir/zone/slave to separate subpackage, %name-slave.
- Moved %_chrootdir/var/run to separate subpackage, %name-debug.
- Added nslookup(1) and resolver(5) manpages from bind8.
- Minor manpage corrections.
- isc-config.sh: fixed --cflags.
- libdns: updated root_ns list to 2002110501.
- rndc-confgen: added "-A" option support.
- Implemented default rndc settings.
- named: patched to get correct chroot jailing support.
- Updated chroot jail and relocated it to /var/lib/bind:
  default CE is now readonly.
- Renamed %_initdir/named to %_initdir/bind.
- Merged caching-nameserver into bind package.
- Split named.conf into several configurations files.
- Added more rfc1912 zones by default.
- Added rfc1918 zones (not enabled by default).

* Wed Nov 13 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt2
- Security fixes from ISC:
  + 1469. buffer length calculation for PX was wrong.
  + 1468. ns_name_ntol() could overwite a zero length buffer.
  + 1467. off by one bug in ns_makecannon().
  + 1466. large ENDS UDP buffer size could trigger a assertion.
  + 1465. possible NULL pointer dereference in db_sec.c
  + 1464. the buffer used to construct the -ve record was not
    	  big enough for all possible SOA records.  use pointer
    	  arithmetic to calculate the remaining size in this
    	  buffer.
  + 1463. use serial space arithmetic to determine if a SIG is
    	  too old, in the future or has internally constistant
    	  times.
  + 1462. write buffer overflow in make_rr().
- Changed named.init:
  + added condreload();
  + fixed argument for "-c" option.
- Changed bind chroot jail:
  + removed /var/lib;
  + removed /etc/{host,nsswitch}.conf;
  + added /etc/{protocols,services}.
- Use subst instead of perl in %%post script.
- Dont't calc perl dependencies for -contrib.

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt1
- Updated code to 8.3.3 release.
- Explicitly use mksock from fileutils.
- Fixed build when glibc-core-archopt is installed.
- Updated packager information.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 8.3.1-alt1
- Updated code to 8.3.1 release.
- Fixed bind to use /dev/null from core system.
- Make use of syslogd-1.4.1-alt9 /etc/syslog.d/ feature.
- Renamed /etc/chroot.d/named.* to /etc/chroot.d/bind.*
- Relaxed dependencies (conflicts instead of requires).

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.5-alt1
- 8.2.5

* Tue Sep 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt3
- Corrected manpages according to chrooted scheme.
- More manpages moved to man-pages package.

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt2
- Moved chroot from /var/named to %_localstatedir/named (according to FHS).
- Merged bind-chroot into main package.
- Updated scripts to handle new syslogd.
- Removed restart support from named.

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt1
- 8.2.4

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.3-ipl4mdk
- Updated PreReqs.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl3mdk
- Fixed %%devel subpackage.

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl2mdk
- Pacthed db_defs.h to ease finding errors.
- Added %%triggerpostun.
- Added call for chrooted environment adjustment before server start.

* Sun Jan 28 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl1mdk
- 8.2.3
- Ported to new chrooted scheme.

* Thu Nov 16 2000 Dmitry V. Levin <ldv@fandra.org> 8.2.2_P7-ipl1mdk
- 8.2.2_P7
- Moved chrooted environment to separate subpackage.
- Removed few manpages, obsoleted by new man-pages package.

* Sat May 13 2000 Dmitry V. Levin <ldv@fandra.org>
- xfer tmpdir patch
- chrooted environment fix

* Fri Mar 10 2000 Dmitry V. Levin <ldv@fandra.org>
- fixed startup script to exit with error if no configuration available
- updated to rpm-3.0.4

* Thu Nov 11 1999 Dmitry V. Levin <ldv@fandra.org>
- 8.2.2-P3

* Sun Oct 31 1999 Dmitry V. Levin <ldv@fandra.org>
- chrooted environment
- doc and contrib packages
- optimal manpage compression
- Fandra adaptions

* Sat Oct 09 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Add lame server patch

* Fri Jul 16 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 8.2.1

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Mar 31 1999 Bill Nottingham <notting@redhat.com>
- add ISC patch
- add quick hack to make host not crash
- add more docs

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add probing information in the init file to keep linuxconf happy
- dont strip libbind

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- removed 'done' output at named shutdown.

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.2

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to use the __FDS_BITS macro
- build for glibc 2.1

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- change named.restart to /usr/sbin/ndc restart

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- install man pages correctly.
- change K10named to K45named.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- don't start if /etc/named.conf doesn't exist.

* Sat Aug  8 1998 Jeff Johnson <jbj@redhat.com>
- autmagically create /etc/named.conf from /etc/named.boot in %post
- remove echo in %post

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in 5.1 mods

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>
