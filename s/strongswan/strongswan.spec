%def_disable static
%def_enable curl
%def_enable ldap
#set capability dropping library.
#Currently supported values are "libcap" and "native".
%define capabilities libcap
%def_disable mysql
%def_disable sqlite
%def_enable stroke
%def_disable medsrv
%def_enable medcli
%def_enable smp
%def_enable sql
%def_enable smartcard
%def_enable pkcs11
%def_enable cisco_quirks
%def_disable unit_tests
%def_disable load_tests
%def_enable eap_radius
%def_enable eap_identity
%def_enable eap_mschapv2
%def_enable eap_tls
%def_enable eap_ttls
%def_enable eap_tnc
%def_enable eap_sim
%def_enable eap_sim-file
%def_enable eap_md5
%def_enable eap_gtc
%def_enable eap_aka
%def_enable kernel_netlink
%def_enable kernel_pfkey
%def_enable kernel_klips
%def_enable nat_transport
%def_disable dumm
%def_disable manager
%def_enable mediation
%def_enable self_test
%def_enable dhcp
%def_enable farp
%def_enable ha
%def_enable openssl
%def_enable agent
%def_enable ctr
%def_enable ccm
%def_enable gcm
%def_enable addrblock
%def_disable uci
%def_disable nm
# this one requires that libhydra and libcharon be
# underlinked on purpose, contact mike@ for email
# explanation by Tobias Brunner (11 May 2010)
%def_disable integrity-test

%ifarch %ix86
%def_enable padlock
%else
%def_disable padlock
%endif

%define beta %nil

Name: strongswan
Version: 5.0.0
Release: alt1

Summary: StrongSWAN IPSEC implementation
License: GPLv2+
Group: System/Servers

# git://git.strongswan.org/strongswan.git
Url: http://www.strongswan.org
Source0: %name-%version%beta.tar.gz
Source1: ipsec.init
Patch0: strongswan-4.4.0-alt-tmpfile.patch
Patch1: strongswan-4.4.1-alt-makefile.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Jul 02 2012
# optimized out: pkg-config
BuildRequires: flex gperf libcap-devel libcurl-devel libgmp-devel libldap-devel libpam-devel libssl-devel libxml2-devel

Provides: libstrongswan = %version-%release
Obsoletes: libstrongswan < 4.3

%define pkgdocdir %_docdir/%name-%version
%add_verify_elf_skiplist %_libdir/%name/ipsec/plugins/*

%description
StrongSWAN is a free implementation of IPSEC & IKE for Linux.  IPSEC is
the Internet Protocol Security and uses strong cryptography to provide
both authentication and encryption services.  These services allow you
to build secure tunnels through untrusted networks.  Everything passing
through the untrusted net is encrypted by the ipsec gateway machine and
decrypted by the gateway at the other end of the tunnel.  The resulting
tunnel is a virtual private network or VPN.

This package contains the service and userland tools for setting up
StrongSWAN on a freeswan enabled kernel.

%package testing
Summary: %name testing
Group: Documentation
Requires: %name = %version
BuildArch: noarch

%description testing
This package contains testing scripts and configuration snippets
of StrongSWAN documentation

%prep
%setup -n %name-%version%beta
#patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure \
	--sysconfdir=%_sysconfdir/%name \
	--libexecdir=%_libdir/%name \
	%{subst_enable static} \
	%{subst_enable curl} \
	%{subst_enable ldap} \
	%{subst_enable mysql} \
	%{subst_enable sqlite} \
	%{subst_enable stroke} \
	%{subst_enable medsrv} \
	%{subst_enable medcli} \
	%{subst_enable smp} \
	%{subst_enable sql} \
	%{subst_enable smartcard} \
	%{subst_enable pkcs11} \
	--with-default-pkcs11=%_libdir/pkcs11/opensc-pkcs11.so \
	%{?_enable_cisco_quirks: --enable-cisco-quirks} \
	%{?_enable_unit_tests: --enable-unit-tests} \
	%{?_enable_load_tests: --enable-load-tests} \
	%{?_enable_eap_radius: --enable-eap-radius} \
	%{?_enable_eap_identity: --enable-eap-identity} \
	%{?_enable_eap_mschapv2: --enable-eap-mschapv2} \
	%{?_enable_eap_tls: --enable-eap-tls} \
	%{?_enable_eap_ttls: --enable-eap-ttls} \
	%{?_enable_eap_tnc: --enable-eap-tnc} \
	%{?_enable_eap_sim: --enable-eap-sim} \
	%{?_enable_eap_sim_file: --enable-eap-sim-file} \
	%{?_enable_eap_md5: --enable-eap-md5} \
	%{?_enable_eap_gtc: --enable-eap-gtc} \
	%{?_enable_eap_aka: --enable-eap-aka} \
	%{?_enable_kernel_netlink: --enable-kernel-netlink} \
	%{?_enable_kernel_pfkey: --enable-kernel-pfkey} \
	%{?_enable_kernel_klips: --enable-kernel-klips} \
	%{?_enable_nat_transport: --enable-nat-transport} \
	%{subst_enable dumm} \
	%{subst_enable manager} \
	%{subst_enable mediation} \
	%{?_enable_integrity_test: --enable-integrity-test} \
	%{?_enable_self_test: --enable-self-test} \
	%{subst_enable padlock} \
	%{subst_enable dhcp} \
	%{subst_enable farp} \
	%{subst_enable ha} \
	%{subst_enable openssl} \
	%{subst_enable agent} \
	%{subst_enable ctr} \
	%{subst_enable ccm} \
	%{subst_enable gcm} \
	%{subst_enable addrblock} \
	%{subst_enable uci} \
	%{subst_enable nm} \
	--with-capabilities=%capabilities

#
%make_build

%install
%makeinstall_std
install -pDm755 %SOURCE1 %buildroot%_initdir/ipsec
rm -f %buildroot%_libdir/lib%name.{a,so}

mkdir -p %buildroot%pkgdocdir
install -pm644 ChangeLog NEWS README TODO %buildroot%pkgdocdir/
rm -f testing/do-tests* testing/Makefile.*
cp -a testing/ %buildroot%pkgdocdir/

%files
%dir %pkgdocdir
%pkgdocdir/[A-Z]*
%attr(700,root,root) %dir %_sysconfdir/%name
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/acerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/aacerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/ocspcerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/certs
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/cacerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/crls
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/private
%config(noreplace) %_sysconfdir/%name/ipsec.conf
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_initdir/ipsec
%_libdir/%name/
%_libdir/ipsec/
%_sbindir/*
%_mandir/*/*

%files testing
%pkgdocdir/testing/

# TODO:
# - libstrongswan{,-devel} subpackages
# - review configurables (see also fedora-proposed spec)

%changelog
* Mon Jul 02 2012 Michael Shigorin <mike@altlinux.org> 5.0.0-alt1
- 5.0.0
- buildreq

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 5.0.0-alt0.1
- 5.0.0rc1
  + pluto is there no more, see also
    http://www.strongswan.org/blog/2012/06/20/bye-bye-pluto.html

* Fri Jun 01 2012 Michael Shigorin <mike@altlinux.org> 4.6.4-alt1
- 4.6.4
  + CVE-2012-2388 is fixed (an attacker presenting a forged
    signature and/or certificate can authenticate as any
    legitimate user provided that "gmp" plugin is in use
    and a connection definition using RSA auth exists)

* Thu May 03 2012 Michael Shigorin <mike@altlinux.org> 4.6.3-alt1
- 4.6.3
  + patch2 unneeded (included upstream)

* Tue Feb 21 2012 Michael Shigorin <mike@altlinux.org> 4.6.2-alt1
- 4.6.2
- added upstream patch to fix trivial FTBFS

* Thu Dec 29 2011 Alexey Shabalin <shaba@altlinux.ru> 4.5.3-alt3
- add configure options: pkcs11,eap-*,dhcp,farp,ha,ctr,ccm,gcm,addrblock
- fix subst_enable for options with "-"
- build with libcap

* Mon Oct 03 2011 Michael Shigorin <mike@altlinux.org> 4.5.3-alt2
- drop testing/do-tests as it's not targeted at deployments
  but rather used for regression testing by upstream
  (maybe the whole subpackage should be purged)
- include all plugin-related files
- buildreq

* Fri Aug 05 2011 Michael Shigorin <mike@altlinux.org> 4.5.3-alt1
- 4.5.3
  + NB: libstrongswan and plugins moved into a private directory

* Wed May 25 2011 Michael Shigorin <mike@altlinux.org> 4.5.2-alt1
- 4.5.2

* Sun Mar 20 2011 Michael Shigorin <mike@altlinux.org> 4.5.1-alt2
- fix buildrequires

* Sat Feb 12 2011 Michael Shigorin <mike@altlinux.org> 4.5.1-alt1
- 4.5.1
  + NB: strongswan.conf parser changes:
    - 'include' statements implemented
    - configuration syntax for the attr plugin has changed

* Sun Oct 31 2010 Michael Shigorin <mike@altlinux.org> 4.5.0-alt1
- 4.5.0
  + see http://download.strongswan.org/CHANGES4.txt
  + IMPORTANT: IKEv2 becomes the default key exchange mode
- disabled patch0 (deals with non-issue, actually)

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 4.4.1-alt1.1
- rebuilt against openssl-1.0.0a

* Wed Sep 22 2010 Michael Shigorin <mike@altlinux.org> 4.4.1-alt1
- 4.4.1
- added patch following earlier explanation by Tobias Brunner
  to force proper linking of libcharon and libhydra against
  libstrongswan (this breaks optional integrity tests though)

* Tue Aug 03 2010 Michael Shigorin <mike@altlinux.org> 4.3.7-alt1
- 4.3.7: major security fix for snprintf() misuse
  introduced in 4.3.3

* Mon May 10 2010 Michael Shigorin <mike@altlinux.org> 4.4.0-alt1
- 4.4.0
  + see http://download.strongswan.org/CHANGES4.txt
- updated patch
- buildreq

* Mon Feb 22 2010 Michael Shigorin <mike@altlinux.org> 4.3.6-alt1
- 4.3.6
  + NB: 4.3.5 has seen some plugin shuffling,
    check upstream changelog in case of doubt
- buildreq (including gperf)

* Tue Sep 15 2009 Michael Shigorin <mike@altlinux.org> 4.3.4-alt1
- 4.3.4

* Sun Jul 26 2009 Michael Shigorin <mike@altlinux.org> 4.3.3-alt3
- fixed incomplete patch (forgot to actually use prepared variable)

* Fri Jul 24 2009 Michael Shigorin <mike@altlinux.org> 4.3.3-alt2
- moved testing docs into a noarch subpackage (thanks repocop)
- patched testing script to avoid 100%% predictable /tmp paths

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 4.3.3-alt1
- 4.3.3 (closes: #20849)
  + the RDN parser vulnerability discovered by Orange Labs research team
    was not completely fixed in version 4.3.2. Some more modifications
    had to be applied to the asn1_length() function to make it robust.
  + thanks crux@ for prompt notification

* Wed Jul 08 2009 Michael Shigorin <mike@altlinux.org> 4.3.2-alt1
- 4.3.2
  + disabled patch0 (applied upstream)
  + dropped patch1 (irrelevant with 4.3.x)
- finally got around to merging strongswan.git by ildar@
  (also closes: #18260)
  + including library subpackage removal
  + initscript status fix
- disabled VIA Padlock support on non-x86_32 (fails to build)
- spec cleanup
- buildreq

* Tue Jun 23 2009 Michael Shigorin <mike@altlinux.org> 4.2.16-alt1
- 4.2.16 fixes DoS vulnerability in the ASN.1 parser;
  thanks crux@ for notification (closes: #20527)

* Thu May 28 2009 Michael Shigorin <mike@altlinux.org> 4.2.15-alt1
- 4.2.15 fixes two DoS issues with charon
  + sending a malformed IKE_SA_INIT request leaved an incomplete state
    which caused a null pointer dereference if a subsequent
    CREATE_CHILD_SA request was sent
  + sending an IKE_AUTH request with either a missing TSi or TSr payload
    caused a null pointer derefence because the checks for TSi and TSr
    were interchanged
  + patch2 unneeded (included upstream)
- thanks crux@ for heads-up (closes: #20206)

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 4.2.14-alt1
- 4.2.14 fixes CVE-2009-0790: DoS against dead peer detection code
- fixed FTBFS with glibc-2.9
- appled vendor patch fixing invalid IKE state issue

* Sat Jan 10 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt3
- added a patch to avoid superfluous file dependencies

* Thu Jan 08 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt2
- fixed ntpd comments in initscript ;-)

* Thu Jan 08 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt1
- 4.2.10
- removed patches (builds as is)
- spec cleanup

* Sat Dec 20 2008 Ildar Mulyukov <ildar@altlinux.ru> 4.2.9-alt1
- new version
- many new features
- spec refactoring

* Wed Oct 10 2007 Grigory Milev <week@altlinux.ru> 4.1.6-alt2
- Rebuild for x86_64
- cleanup spec
- move libraries to separate package

* Mon Sep 03 2007 $inister <sinister@altlinux.ru> 4.1.6-alt1
- new version

* Tue Aug 28 2007 $inister <sinister@altlinux.ru> 4.1.5-alt1
- initial packaging
