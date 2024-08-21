%define _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec
#set capability dropping library.
#Currently supported values are "libcap" and "native".
%define capabilities libcap
%def_enable gcrypt
%def_enable eap_sim_pcsc
%def_disable load_tests
%def_enable nm
%def_enable tpm
%def_enable sqlite
%def_disable static
%def_disable uci
%def_disable unit_tests
# this one requires that libhydra and libcharon be
# underlinked on purpose, contact mike@ for email
# explanation by Tobias Brunner (11 May 2010)
%def_disable integrity_test

%define beta %nil

Name: strongswan
Version: 5.9.14
Release: alt4

Summary: strongSwan IPsec implementation
License: GPLv2+
Group: System/Servers

# git://git.strongswan.org/strongswan.git
Url: http://www.strongswan.org
Source0: %name-%version%beta.tar.gz
Source1: %name.init
Source100: strongswan.watch
Patch10: strongswan-5.6.0-uintptr_t.patch
# https://github.com/strongswan/strongswan/issues/1198
Patch11: strongswan-5.9.7-error-no-format.patch
Patch12: strongswan-disable-bypass-lan.patch
Patch13: strongswan-dont-load-kernel-libipsec-plugin-by-default.patch

Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Jul 02 2012
# optimized out: pkg-config
BuildRequires: flex gperf libcap-devel libcurl-devel libgmp-devel libldap-devel libpam-devel libssl-devel
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libip4tc)
%{?_enable_tpm:BuildRequires: pkgconfig(tss2-sys) pkgconfig(tss2-esys)}
%{?_enable_eap_sim_pcsc:BuildRequires: pkgconfig(libpcsclite)}
%{?_enable_gcrypt:BuildRequires: libgcrypt-devel libgpg-error-devel}
%{?_enable_sqlite:BuildRequires: libsqlite3-devel}
%{?_enable_nm:BuildRequires: pkgconfig(gthread-2.0) pkgconfig(libnm)}
BuildRequires: pkgconfig(systemd)

Provides: libstrongswan = %version-%release
Obsoletes: libstrongswan < 4.3

%define pkgdocdir %_docdir/%name-%version

%description
strongSwan is a free implementation of IPsec & IKE for Linux. IPsec is the
Internet Protocol Security and uses strong cryptography to provide both
authentication and encryption services. These services allow you to build
secure tunnels through untrusted networks. Everything passing through the
untrusted net is encrypted by the ipsec gateway machine and decrypted by the
gateway at the other end of the tunnel. The resulting tunnel is a virtual
private network or VPN.

This package contains the service and userland tools for setting up strongSwan
on a freeswan enabled kernel.

%package testing
Summary: %name testing
Group: Documentation
Requires: %name = %version
BuildArch: noarch

%description testing
This package contains testing scripts and configuration snippets
of strongSwan documentation

%package charon-nm
Summary: NetworkManager plugin for Strongswan
Group: System/Servers

%description charon-nm
NetworkManager plugin integrates a subset of Strongswan capabilities
to NetworkManager.

%package sqlite
Summary: SQLite support for strongSwan
Group: System/Servers
Requires: %name = %EVR

%description sqlite
The sqlite plugin adds an SQLite database backend to strongSwan.
 
%package tnc-imcvs
Summary: Trusted network connect (TNC)'s IMC/IMV functionality
Group: System/Servers
Requires: %name = %EVR
Requires: %name-sqlite = %EVR

%description tnc-imcvs
This package provides Trusted Network Connect's (TNC) architecture support.
It includes support for TNC client and server (IF-TNCCS), IMC and IMV message
exchange (IF-M), interface between IMC/IMV and TNC client/server (IF-IMC
and IF-IMV). It also includes PTS based IMC/IMV for TPM based remote
attestation, SWID IMC/IMV, and OS IMC/IMV. It's IMC/IMV dynamic libraries
modules can be used by any third party TNC Client/Server implementation
possessing a standard IF-IMC/IMV interface. In addition, it implements
PT-TLS to support TNC over TLS.

%prep
%setup -n %name-%version%beta
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--with-ipsec-script=%name \
	--sysconfdir=%_sysconfdir/%name \
	--with-ipsecdir=%_libexecdir/%name \
	--bindir=%_libexecdir/%name \
	--with-ipseclibdir=%_libdir/%name \
	--with-piddir=/run \
	--with-nm-ca-dir=%_sysconfdir/%name/ipsec.d/cacerts/ \
	--enable-acert \
	--enable-addrblock \
	--enable-af-alg \
	--enable-agent \
	--enable-bypass-lan \
	--enable-ccm \
	--enable-certexpire \
	--enable-chapoly \
	--enable-connmark \
	--enable-cmd \
	--enable-ctr \
	--enable-curl \
	--enable-dhcp \
	--enable-duplicheck \
	--enable-eap-aka \
	--enable-eap-aka-3gpp \
	--enable-eap-aka-3gpp2 \
	--enable-eap-dynamic \
	--enable-eap-gtc \
	--enable-eap-identity \
	--enable-eap-md5 \
	--enable-eap-mschapv2 \
	--enable-eap-peap \
	--enable-eap-radius \
	--enable-eap-sim \
	--enable-eap-sim-file \
	%{?_enable_eap_sim_pcsc: --enable-eap-sim-pcsc} \
	--enable-eap-tls \
	--enable-eap-tnc \
	--enable-eap-ttls \
	--enable-ext-auth \
	--enable-error-notify \
	--enable-farp \
	--enable-forecast \
	--enable-gcm \
	%{subst_enable gcrypt} \
	--enable-ha \
	--enable-ipseckey \
	--enable-ldap \
	--enable-led \
	--enable-lookip \
	--enable-md4 \
	--enable-newhope \
	--enable-ntru \
	--enable-openssl \
	--enable-pkcs11 \
	--enable-smp \
	--enable-sql \
	--enable-sqlite \
	--enable-stroke \
	--enable-swanctl \
	--enable-unity \
	%{subst_enable tpm} \
	--enable-tss-tss2 \
	%{subst_enable uci} \
	%{subst_enable nm} \
	--enable-systemd \
	--with-systemdsystemunitdir=%_unitdir \
	--with-capabilities=%capabilities \
	%{?_enable_unit_tests: --enable-unit-tests} \
	%{?_enable_load_tests: --enable-load-tests} \
	--enable-xauth-eap \
	--enable-xauth-pam \
	--enable-xauth-noauth \
	--enable-tnc-ifmap \
	--enable-tnc-pdp \
	--enable-tnc-imc \
	--enable-tnc-imv \
	--enable-tnccs-20 \
	--enable-tnccs-11 \
	--enable-tnccs-dynamic \
	--enable-imc-test \
	--enable-imv-test \
	--enable-imc-scanner \
	--enable-imv-scanner  \
	--enable-imc-attestation \
	--enable-imv-attestation \
	--enable-imv-os \
	--enable-imc-os \
	--enable-imc-swima \
	--enable-imv-swima \
	--enable-imc-hcd \
	--enable-imv-hcd \
	--enable-vici \
	%{?_enable_kernel_netlink: --enable-kernel-netlink} \
	%{?_enable_kernel_pfkey: --enable-kernel-pfkey} \
	%{?_enable_integrity_test: --enable-integrity-test} \
	%ifarch x86_64 %{ix86}
	--enable-aesni \
	--enable-rdrand \
	%endif
	--enable-kernel-libipsec \
	--disable-fast \
	CPPFLAGS="-DSTARTER_ALLOW_NON_ROOT" \
	%nil

#

# ensure manual page is regenerated with local configuration
rm -f src/ipsec/_ipsec.8

%make_build

%install
%makeinstall_std

install -pDm755 %SOURCE1 %buildroot%_initdir/%name
rm -f testing/do-tests* testing/Makefile.*

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

# prefix man pages
for i in %buildroot%_mandir/*/*; do
    if echo "$i" | grep -vq '/strongswan[^\/]*$'; then
        mv "$i" "`echo "$i" | sed -re 's|/([^/]+)$|/strongswan_\1|'`"
    fi
done
find %buildroot -type f -name '*.la' -delete
# delete unwanted library files - no consumers, so no -devel package
rm -f %buildroot%_libdir/%name/*.so


%post
if sd_booted; then
    %post_service_posttrans_restart strongswan.service
    %post_service_posttrans_restart strongswan-starter.service
else
    %post_service_posttrans_restart strongswan
fi

%preun
if sd_booted; then
    %preun_service strongswan.service
    %preun_service strongswan-starter.service
else
    %preun_service strongswan
fi

# since 5.9.14 we have 'strongswan' chkconfig entry instead of 'ipsec' one
%triggerun -- %name < 5.9.14
if [ $2 -gt 0 ]; then
# This is strongswan upgrade.
        chkconfig ipsec >/dev/null 2>&1 && ipsec_enabled=1 || ipsec_enabled=0
        chkconfig --del ipsec
        chkconfig --add strongswan
        if [ $ipsec_enabled -eq 1 ] ; then
            chkconfig strongswan on
        fi
fi

%files
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_initdir/strongswan
%_unitdir/strongswan.service
%_unitdir/strongswan-starter.service
%_datadir/%name
%_libexecdir/%name
%_libdir/%name
%_sbindir/charon-cmd
%_sbindir/charon-systemd
%_sbindir/%name
%_sbindir/swanctl
%_man1dir/*
%_man5dir/*
%_man8dir/*

%if_enabled nm
%exclude %_libexecdir/%name/charon-nm
%endif
%if_enabled sqlite
%exclude %_libdir/%name/plugins/libstrongswan-sqlite.so
%endif
%exclude %_libdir/%name/imcvs
%exclude %_libdir/strongswan/libimcv.so.*
%exclude %_libdir/strongswan/libtnccs.so.*
%exclude %_libdir/%name/plugins/libstrongswan-*tnc*.so
%exclude %_libexecdir/strongswan/attest
%exclude %_libexecdir/strongswan/pt-tls-client
%exclude %_datadir/strongswan/swidtag

%files testing
%doc testing

%if_enabled nm
%files charon-nm
%_datadir/dbus-1/system.d/nm-strongswan-service.conf
%_libexecdir/%name/charon-nm
%endif

%if_enabled sqlite
%files sqlite
%_libdir/%name/plugins/libstrongswan-sqlite.so
%endif

%files tnc-imcvs
%_sbindir/sw-collector
%_sbindir/sec-updater
%_libdir/strongswan/imcvs
%_libdir/strongswan/libimcv.so.*
%_libdir/strongswan/libtnccs.so.*
%_libdir/strongswan/plugins/libstrongswan-*tnc*.so
%_libexecdir/strongswan/attest
%_libexecdir/strongswan/pt-tls-client
%_datadir/strongswan/swidtag

# TODO:
# - libstrongswan{,-devel} subpackages
# - review configurables (see also fedora-proposed spec)

%changelog
* Wed Aug 21 2024 Alexey Shabalin <shaba@altlinux.org> 5.9.14-alt4
- enable build md4 for eap-mschapv2

* Wed Aug 21 2024 Alexey Shabalin <shaba@altlinux.org> 5.9.14-alt3
- disable bypass-lan plugin in config
- disable kernel-libipsec plugin (ALT #50684) in config
- enable build af-alg (AF_ALG crypto interface to Linux Crypto API)
- enable build rdrand (Intel RDRAND random generator plugin) for x86
- enable build connmark, forecast, lookip plugins

* Tue Jun 18 2024 Alexey Shabalin <shaba@altlinux.org> 5.9.14-alt2
- fixed %%post and %%preun scripts

* Mon Jun 17 2024 Alexey Shabalin <shaba@altlinux.org> 5.9.14-alt1
- new version 5.9.14
- define _libexecdir as /usr/libexec
- update configure options (add build with tpm, eap-peap and other)
- add sqlite and tnc-imcvs subpackages
- rename sbin script and service to strongswan
- add %%post and %%preun sections

* Fri Dec 01 2023 Michael Shigorin <mike@altlinux.org> 5.9.13-alt1
- new version (watch file uupdate)

* Tue Nov 21 2023 Michael Shigorin <mike@altlinux.org> 5.9.12-alt1
- new version (watch file uupdate)

* Mon Jun 12 2023 Michael Shigorin <mike@altlinux.org> 5.9.11-alt1
- new version (watch file uupdate)

* Sat Mar 04 2023 Michael Shigorin <mike@altlinux.org> 5.9.10-alt1
- new version (watch file uupdate)

* Thu Jan 05 2023 Michael Shigorin <mike@altlinux.org> 5.9.9-alt1
- new version (watch file uupdate)

* Tue Oct 04 2022 Michael Shigorin <mike@altlinux.org> 5.9.8-alt1
- new version (watch file uupdate)

* Fri Jul 29 2022 Michael Shigorin <mike@altlinux.org> 5.9.7-alt1
- new version (watch file uupdate)

* Fri Apr 29 2022 Michael Shigorin <mike@altlinux.org> 5.9.6-alt1
- new version (watch file uupdate)

* Wed Jan 26 2022 Michael Shigorin <mike@altlinux.org> 5.9.5-alt1
- new version (watch file uupdate)

* Thu Oct 21 2021 Michael Shigorin <mike@altlinux.org> 5.9.4-alt1
- new version (watch file uupdate)

* Tue Jul 06 2021 Michael Shigorin <mike@altlinux.org> 5.9.3-alt1
- new version (watch file uupdate)

* Sat Feb 27 2021 Michael Shigorin <mike@altlinux.org> 5.9.2-alt1
- new version (watch file uupdate)

* Wed Nov 11 2020 Michael Shigorin <mike@altlinux.org> 5.9.1-alt1
- new version (watch file uupdate)

* Thu Jul 30 2020 Michael Shigorin <mike@altlinux.org> 5.9.0-alt1
- new version (watch file uupdate)

* Thu Jul 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt5
- don't package pki manpages

* Thu Jul 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt4
- fix conflict with pki-tools (Closes: 32705)
- package strongswan-starter unit

* Tue Jul 07 2020 Vitaly Lipatov <lav@altlinux.ru> 5.8.4-alt3
- build charon-nm subpackage with NetworkManager support

* Tue Jul 07 2020 Vitaly Lipatov <lav@altlinux.ru> 5.8.4-alt2
- enable charon-cmd build
- fix elf skiplist for plugins

* Sun Mar 29 2020 Michael Shigorin <mike@altlinux.org> 5.8.4-alt1
- new version (watch file uupdate)

* Wed Mar 25 2020 Michael Shigorin <mike@altlinux.org> 5.8.3-alt1
- new version (watch file uupdate)

* Wed Dec 18 2019 Michael Shigorin <mike@altlinux.org> 5.8.2-alt1
- new version (watch file uupdate)

* Wed Sep 04 2019 Michael Shigorin <mike@altlinux.org> 5.8.1-alt1
- new version (watch file uupdate)

* Tue May 21 2019 Michael Shigorin <mike@altlinux.org> 5.8.0-alt1
- new version (watch file uupdate)

* Thu Dec 27 2018 Michael Shigorin <mike@altlinux.org> 5.7.2-alt1
- new version (watch file uupdate)

* Fri Oct 05 2018 Michael Shigorin <mike@altlinux.org> 5.7.1-alt1
- new version (watch file uupdate)

* Mon Sep 24 2018 Michael Shigorin <mike@altlinux.org> 5.7.0-alt1
- new version (watch file uupdate)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 5.6.3-alt1.qa1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 5.6.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for strongswan-testing

* Mon May 28 2018 Michael Shigorin <mike@altlinux.org> 5.6.3-alt1
- new version (watch file uupdate)

* Mon Feb 19 2018 Michael Shigorin <mike@altlinux.org> 5.6.2-alt1
- new version (watch file uupdate)

* Sun Nov 19 2017 Michael Shigorin <mike@altlinux.org> 5.6.1-alt1
- new version (watch file uupdate)

* Mon Aug 14 2017 Michael Shigorin <mike@altlinux.org> 5.6.0-alt1
- new version (watch file uupdate)

* Wed May 31 2017 Michael Shigorin <mike@altlinux.org> 5.5.3-alt1
- new version (watch file uupdate)

* Tue Mar 28 2017 Michael Shigorin <mike@altlinux.org> 5.5.2-alt1
- new version (watch file uupdate)

* Fri Oct 21 2016 Michael Shigorin <mike@altlinux.org> 5.5.1-alt1
- new version (watch file uupdate)

* Tue Jul 26 2016 Michael Shigorin <mike@altlinux.org> 5.5.0-alt1
- new version (watch file uupdate)

* Wed Mar 23 2016 Michael Shigorin <mike@altlinux.org> 5.4.0-alt1
- new version (watch file uupdate)

* Fri Nov 27 2015 Michael Shigorin <mike@altlinux.org> 5.3.5-alt1
- new version (watch file uupdate)
  + fixups upon 5.3.4

* Mon Nov 16 2015 Michael Shigorin <mike@altlinux.org> 5.3.4-alt1
- new version (watch file uupdate)
  + fixes CVE-2015-8023: authentication bypass in eap-mschapv2, see
    https://www.strongswan.org/blog/2015/11/16/

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 5.3.3-alt1
- new version (watch file uupdate)

* Tue Jun 09 2015 Michael Shigorin <mike@altlinux.org> 5.3.2-alt1
- new version (watch file uupdate)
  + fixes CVE-2015-4171: client info disclosure, see
    https://www.strongswan.org/blog/2015/06/08/

* Tue Jun 02 2015 Michael Shigorin <mike@altlinux.org> 5.3.1-alt1
- new version (watch file uupdate)
  + fixes CVE-2015-3991: DoS with potential code execution, see
    https://www.strongswan.org/blog/2015/06/01/

* Wed Apr 08 2015 Michael Shigorin <mike@altlinux.org> 5.3.0-alt2
- built for Sisyphus (thx Vadim)

* Wed Apr 08 2015 Vadim Illarionov <gbIMoBou@gmail.com> 5.3.0-alt1.1
- added systemd service
- compiled with swanctl

* Mon Mar 30 2015 Michael Shigorin <mike@altlinux.org> 5.3.0-alt1
- new version (watch file uupdate)

* Mon Jan 05 2015 Michael Shigorin <mike@altlinux.org> 5.2.2-alt1
- new version (watch file uupdate)
- fixes CVE-2014-9221 (DoS)

* Sun Oct 19 2014 Michael Shigorin <mike@altlinux.org> 5.2.1-alt1
- new version (watch file uupdate)

* Wed Jul 09 2014 Michael Shigorin <mike@altlinux.org> 5.2.0-alt1
- new version (watch file uupdate)

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 5.1.3-alt1
- new version (watch file uupdate)
- fixes CVE-2014-2338 (authentication bypass via rekeying)

* Sun Mar 09 2014 Michael Shigorin <mike@altlinux.org> 5.1.2-alt2
- added watch file

* Mon Mar 03 2014 Michael Shigorin <mike@altlinux.org> 5.1.2-alt1
- 5.1.2: http://wiki.strongswan.org/versions/50
  + new default configuration file layout is introduced
  + NTRUEncrypt support
- dropped patches (done upstream in a slightly different way)

* Wed Aug 07 2013 Michael Shigorin <mike@altlinux.org> 5.1.0-alt1
- 5.1.0: CVE-2013-5018 fix (charon DoS, see also
  http://www.strongswan.org/blog/2013/08/01/)

* Tue Apr 30 2013 Michael Shigorin <mike@altlinux.org> 5.0.4-alt1
- 5.0.4: CVE-2013-2944 fix (ECDSA signature vulnerability
  if openssl backend is loaded)

* Sat Apr 06 2013 Michael Shigorin <mike@altlinux.org> 5.0.3-alt1
- 5.0.3

* Thu Oct 04 2012 Michael Shigorin <mike@altlinux.org> 5.0.1-alt1
- 5.0.1

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
