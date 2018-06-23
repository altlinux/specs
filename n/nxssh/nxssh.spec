%def_with kerberos5

Name: nxssh
Version: 7.5
Release: alt7

Summary: Openssh portable (Etersoft edition) for using with NX

License: GPL, MIT/X11 for X11 bits
Group: Networking/Remote access
Url: https://github.com/openssh/openssh-portable

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-git: https://github.com/openssh/openssh-portable.git
Source: %name-%version.tar

Patch1: 0001-fix-openssl-1.1.patch-eterbug-12901.patch

Requires: nx-libs >= 3.5.0.31

# Automatically added by buildreq on Wed Nov 08 2017
# optimized out: gnu-config libcom_err-devel libkrb5-devel nx perl python-base python-modules python3 python3-base zlib-devel
BuildRequires: libjpeg-devel libpam-devel libpng-devel libssl-devel libstdc++-devel nx-libs-devel openssh-clients

%if_with kerberos5
BuildRequires: libkrb5-devel
%endif

%description
Openssh portable (Etersoft edition) for using with NX.

%prep
%setup

# fix build with openssl 1.1
if [ -s %_libdir/libssl.so.1.1 ] ; then
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
%configure --without-zlib-version-check %{subst_with kerberos}
%make_build || %make

echo "checking ssh config path"
grep "/etc${confdir}/ssh_config" nxssh

%install
mkdir -p %buildroot%_bindir/
install -m755 nxssh %buildroot%_bindir/

%files
%_bindir/nxssh

%changelog
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

