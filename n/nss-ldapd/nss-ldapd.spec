%def_disable test
%def_disable debug
%def_enable  systemd

Name: 	 nss-ldapd
Version: 0.9.9
Release: alt1

Summary: An nsswitch module which uses directory servers
License: LGPLv2+
Group:   System/Base
URL: 	 http://arthurdejong.org/nss-pam-ldapd/

Source:  %name-%version.tar
Source1: nslcd.init
Source2: nslcd.sysconfig
Source3: nslcd.tmpconf
Source4: nslcd.service
Patch:   %name-0.8.10-alt-DSO.patch
Patch1:	 %name-nslcd-user-name.patch

Requires: nscd
Requires: su

Conflicts: nss_ldap
Conflicts: pam_ldap
Provides:  nss-pam-ldapd = %version-%release
Provides:  nss-ldap

BuildRequires: libkrb5-devel libldap-devel libsasl2-devel docbook2X libpam0-devel
%if_enabled systemd
BuildRequires: systemd
%endif

%description
The nss-pam-ldapd daemon, nslcd, uses a directory server to look up name
service information (users, groups, etc.) on behalf of a lightweight
nsswitch module.


%prep
%setup
%patch -p2
%patch1 -p2
%autoreconf


%build
%add_optflags -I%_includedir/krb5
# Override man generator name
export DOCBOOK2X_MAN=/usr/bin/db2x_docbook2man
%configure \
	--with-ldap-conf-file=%_sysconfdir/nslcd.conf \
	--with-pam-seclib-dir=/%_lib/security \
%if_enabled debug
	--enable-debugging \
%endif
	--with-ldap-lib=openldap

%make_build SYSLIBDIR=/%_lib
%make check


%install
mkdir -p %buildroot{%_sysconfdir,%_libdir,/%_lib}

# Install the nsswitch module.
%make_install  SYSLIBDIR=/%_lib install \
	DESTDIR=%buildroot \
	INST_UID=`id -un` INST_GID=`id -gn`

mv %buildroot%_libdir/* %buildroot/%_lib/
install -pD -m755 %SOURCE1 %buildroot%_initdir/nslcd
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/nslcd
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/tmpfiles.d/nslcd.conf
%if_enabled systemd
install -pD -m644 %SOURCE4 %buildroot/lib/systemd/system/nslcd.service
%endif
chmod 755 %buildroot/%_lib/*.so*

chmod 600 %buildroot%_sysconfdir/nslcd.conf
# Disable SSL cert check
subst 's/^#tls_reqcert/tls_reqcert/' %buildroot%_sysconfdir/nslcd.conf

mkdir -pm711 %buildroot/var/run/nslcd
mksock %buildroot/var/run/nslcd/socket


%pre
getent group _nslcd > /dev/null || /usr/sbin/groupadd -r _nslcd
getent passwd _nslcd > /dev/null || \
%_sbindir/useradd -M -r -g _nslcd -c 'NSS-LDAP Daemon' \
     -d / -s /sbin/nologin _nslcd 2> /dev/null ||:


%preun
[ "$1" -eq "0" ] && %preun_service nslcd
exit 0


%post
# Import important non-default settings from nss_ldap or pam_ldap configuration
# files, but only the first time this package is installed.
comment="This comment prevents repeated auto-migration of settings."
if test -s /etc/nss-ldapd.conf ; then
        source=/etc/nss-ldapd.conf
elif test -s /etc/nss_ldap.conf ; then
        source=/etc/nss_ldap.conf
elif test -s /etc/pam_ldap.conf ; then
        source=/etc/pam_ldap.conf
else
        source=/etc/ldap.conf
fi
target=/etc/nslcd.conf
if test "$1" -eq "1" && ! grep -q -F "# $comment" $target 2> /dev/null ; then
        # Try to make sure we only do this the first time.
        echo "# $comment" >> $target
        if grep -E -q '^uri[[:blank:]]' $source 2> /dev/null ; then
                # Comment out the packaged default host/uri and replace it...
                sed -i -r -e 's,^((host|uri)[[:blank:]].*),# \1,g' $target
                # ... with the uri.
                grep -E '^uri[[:blank:]]' $source >> $target
        elif grep -E -q '^host[[:blank:]]' $source 2> /dev/null ; then
                # Comment out the packaged default host/uri and replace it...
                sed -i -r -e 's,^((host|uri)[[:blank:]].*),# \1,g' $target
                # ... with the "host" reformatted as a URI.
                scheme=ldap
                # check for 'ssl on', which means we want to use ldaps://
                if grep -E -q '^ssl[[:blank:]]+on$' $source 2> /dev/null ; then
                        scheme=ldaps
                fi
                grep -E '^host[[:blank:]]' $source |\
                sed -r -e "s,^host[[:blank:]](.*),uri ${scheme}://\1/,g" >> $target
        fi
        # Base doesn't require any special logic.
        if grep -E -q '^base[[:blank:]]' $source 2> /dev/null ; then
                # Comment out the packaged default base and replace it.
                sed -i -r -e 's,^(base[[:blank:]].*),# \1,g' $target
                grep -E '^base[[:blank:]]' $source >> $target
        fi
        # Pull in these settings, if they're set, directly.
        grep -E '^(binddn|bindpw|port|scope|ssl|pagesize)[[:blank:]]' $source 2> /dev/null >> $target
        grep -E '^(tls_)' $source 2> /dev/null >> $target
        grep -E '^(timelimit|bind_timelimit|idle_timelimit)[[:blank:]]' $source 2> /dev/null >> $target
fi
# If this is the first time we're being installed, and the system is already
# configured to use LDAP as a naming service, enable the daemon, but don't
# start it since we can never know if that's a safe thing to do.  If this
# is an upgrade, leave the user's runlevel selections alone.
%post_service nslcd
if [ "$1" -eq "1" ]; then
	if grep -qs '^passwd:.*ldap' /etc/nsswitch.conf; then
        /sbin/chkconfig nslcd on
        service nslcd start
	fi
fi
exit 0


%files
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%doc %_man5dir/*
%doc %_man8dir/*
%_sbindir/nslcd
/%_lib/*.so*
/%_lib/security/pam_ldap.so
%attr(0755,root,root) %_initdir/nslcd
%config(noreplace) %_sysconfdir/sysconfig/nslcd
%attr(600,_nslcd,_nslcd) %config(noreplace) %verify(not md5 size mtime) %_sysconfdir/nslcd.conf
%attr(711,_nslcd,root) %dir /var/run/nslcd
%attr(666,_nslcd,_nslcd) %ghost /var/run/nslcd/socket
%attr(644,root,root) %config(noreplace) %_sysconfdir/tmpfiles.d/nslcd.conf
%if_enabled systemd
%config(noreplace) /lib/systemd/system/*
%endif

%changelog
* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.9-alt1
- New version.

* Mon Jun 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version

* Thu Dec 29 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.7-alt2
- Remove executable flag from service file

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.7-alt1
- new version 0.9.7

* Mon Jun 06 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version

* Wed May 14 2014 Andrey Cherepanov <cas@altlinux.org> 0.8.14-alt1
- New version
- Implement an -n switch to not daemonise

* Thu Jan 30 2014 Andrey Cherepanov <cas@altlinux.org> 0.8.13-alt1
- New version
- Log EPIPE only on debug level
- When the NSS modules closes the connection and skips any remaining
  result data, wait for up to 500 msec to read any available data (see
  https://bugzilla.redhat.com/show_bug.cgi?id=1003011 )

* Mon Nov 26 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.12-alt1
- New verison 0.8.12 (see http://arthurdejong.org/nss-pam-ldapd/release-0-8-12)
- Fix nslcd user and group name in configuration file

* Thu Nov 08 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.11-alt1
- New version 0.8.11
- Add real systemd support

* Thu Oct 04 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.10-alt4
- Provide nss-ldap for adapted alterator-auth
- Change obsolete of pam_ldap to conflict

* Tue Oct 02 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.10-alt3
- Strict check of LDAP use in NSS
- Auto enable and run daemon

* Tue Oct 02 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.10-alt2
- Import setting from nss-ldap
- Obsoletes for pam_ldap
- Remove double su in daemon
- Disable SSL cert check

* Fri Sep 07 2012 Mikhail Pluzhnikov <amike@altlinux.ru> 0.8.10-alt1
- New version: 0.8.10

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.8-alt1.2
- Fixed build

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 0.6.8-alt1.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Mon Apr 20 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.8-alt1
- 0.6.8
- build fixed

* Wed Jul 09 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.4.1-alt3
- Fixed initscript start message (Closes: #16306)
- Added missed dependency on su(1) (Closes: #16307)
- Implemented sysconfig-file support (Closes: #16308)

* Thu Jan 24 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt2
- added Conflicts: nss_ldap (#14147)

* Thu Dec 27 2007 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- rebuilt for Sisyphus
- fixed Url:, Source:, Summary: and %%description
- truncated %%changelog

* Sat Nov 03 2007 Nick S. Grechukh <gns@altlinux.org> 0.4.1-alt0.1
- nss-ldapd / based on nss_ldap sisyphus package
