%def_with kerberos5

Name: nxssh
Version: 7.5
Release: alt11

Summary: Openssh portable (Etersoft edition) for using with NX in RX@Etersoft

License: GPL, MIT/X11 for X11 bits
Group: Networking/Remote access
Url: https://github.com/openssh/openssh-portable

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-git: https://github.com/openssh/openssh-portable.git
Source: %name-%version.tar

Patch1: 0001-fix-openssl-1.1.patch-eterbug-12901.patch

Requires: nx-libs >= 3.5.0.31

BuildRequires: libpam-devel libssl-devel nx-libs-devel openssh-clients

%if_with kerberos5
BuildRequires: libkrb5-devel
%endif

%description
Openssh portable (Etersoft edition) for using with NX in RX@Etersoft.

%prep
%setup

# fix build with openssl 1.1
if [ -s %_libdir/libssl.so.1.1 ] || [ -s /%_lib/libssl.so.1.1 ] ; then
%patch1 -p1
fi

%build
# detect config placement
confdir=""
[ -r "/etc/openssh/ssh_config" ] && confdir="/openssh"
[ -r "/etc/ssh/ssh_config" ] && confdir="/ssh"
[ -r "/etc/ssh_config" ] && confdir="/"
%__subst "s|-DSSHDIR=\\\\\"\$(sysconfdir)\\\\\"|-DSSHDIR=\\\\\"\$(sysconfdir)${confdir}\\\\\"|g" Makefile.in

%autoreconf
%configure --without-zlib-version-check %{subst_with kerberos5}
%make_build || %make

echo "checking ssh config path"
grep -a "/etc${confdir}/ssh_config" nxssh

%install
mkdir -p %buildroot%_bindir/
install -m755 nxssh %buildroot%_bindir/

%files
%_bindir/nxssh

%changelog
* Wed Aug 29 2018 Pavel Vainerman <pv@altlinux.ru> 7.5-alt11
- fix openssl 1.1 detection, use grep -a for check text in binary

* Wed Aug 08 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt10
- (CI): added build for c7
- revert "(CI): added build for c7"

* Fri Jul 06 2018 Vitaly Lipatov <lav@altlinux.ru> 7.5-alt9
- fix bug with kerberos build missing
- drop gcc-c++ and other image libs buildrequires
- use optflags from rpm (drop hardcoded CFLAGS)

* Thu Jun 28 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt8
- (CI): added test build

* Sat Jun 23 2018 Vitaly Lipatov <lav@altlinux.ru> 7.5-alt7
- cleanup spec, pack only nxssh

* Wed Jun 06 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt6
- added path validation for ssh config (eterbug #12807)

* Wed May 23 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt5
- restore fix-openssl-1.1.patch

* Thu Apr 12 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt4
- update build requires: use nx-libs

* Fri Mar 30 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt3
- update build requires

* Fri Mar 30 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt2
- fixed openssh confdir (eterbug #12796)

* Tue Mar 20 2018 Etersoft Builder <builder@etersoft.ru> 7.5-alt1
- added gitlab-ci.yml
- (gitlab-ci): fixed spec name
- (gitlab-ci): fixed spec path

* Wed Nov 08 2017 Pavel Vainerman <pv@altlinux.ru> 7.5-alt0.5
- update requires

* Wed Nov 08 2017 Pavel Vainerman <pv@altlinux.ru> 7.5-alt0.4
- fixed bug for SSL session

* Wed Nov 01 2017 Pavel Vainerman <pv@altlinux.ru> 7.5-alt0.3
- fixed bug in spec file (--enable-kerberos5 --> --with-kerberos5)

* Mon Oct 30 2017 Pavel Vainerman <pv@altlinux.ru> 7.5-alt0.2
- build with kerberos5 

* Wed Oct 18 2017 Pavel Vainerman <pv@altlinux.ru> 7.5-alt0.1
- initial commit

