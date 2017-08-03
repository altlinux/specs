# vim: set ft=spec: -*- rpm -spec -*-

Name: pam_pkcs11
Version: 0.6.9
Release: alt10

Summary: PKCS #11 PAM Module and Login Tools
Group: System/Base
License: LGPL
Url: https://github.com/OpenSC/pam_pkcs11

Source: %name-%version.tar
Patch: %name-%version-alt-build.patch
Patch1: %name-%version-docs.patch
Patch2: %name-%version-option-global_ca.patch
Patch3: %name-%version-ru.po.patch
Patch4: %name-%version-buffer.patch
Patch5: %name-%version-ask-pin-later.patch
Patch6: %name-%version-option-ask_pin.patch
Patch7: pam_pkcs11-0.6.9-eventmgr-init-from-token.patch
Patch8: pam_pkcs11-0.6.9-ignore-no-card.patch
Patch9: pam_pkcs11-0.6.9-config-control.patch
Patch10: pam_pkcs11-0.6.9-systemd.patch
Patch11: pam_pkcs11-0.6.9-gost-support.patch
Patch12: pam_pkcs11-0.6.9-oid-mapper.patch
Patch13: pam_pkcs11-0.6.9-oid-mapper-profiles.patch

%add_findreq_skiplist %_sysconfdir/pam.d/*
Requires: pam-config PAM(pam_mkhomedir.so) PAM(pam_pkcs11.so) PAM(pam_succeed_if.so)
Requires: alterator-service-functions >= 2.0.4

BuildRequires: docbook-style-xsl flex libldap-devel libpam-devel libpcsclite-devel libssl-devel xsltproc
BuildRequires: doxygen
BuildRequires: docbook-dtds

BuildPreReq: gcc-c++
# SCARD_READERSTATE_A will change to SCARD_READERSTATE afterwards:
BuildPreReq: libpcsclite-devel >= 1.7.4

%description
This Linux-PAM login module allows a X.509 certificate based user login.
The certificate and its dedicated private key are thereby accessed by
means of an appropriate PKCS #11 module. For the verification of the
user certificates, locally stored CA certificates as well as either
online or locally accessible CRLs are used.

Adittional included pam_pkcs11 related tools:

 - pkcs11_eventmgr: Generate actions on card insert/removal/timeout
   events
 - pklogin_finder: Get the loginname that maps to a certificate
 - pkcs11_inspect: Inspect the contents of a certificate

%package pcsc
Summary: PCSC-Lite extra tools for pam_pkcs11
Group: System/Base
Requires: %name = %version-%release

%description pcsc
This package contains pam_pkcs11 tools that relies on PCSC-Lite library:

 - card_eventmgr: Generate card insert/removal events.

%package ldap
Summary: LDAP Cert-to-Login mapper for pam_pkcs11
Group: System/Base
Requires: %name = %version-%release

%description ldap
This package contains a Certificate-To-Login mapper based on queries
to a LDAP server. As it depends on extra libraries, is distributed
as a separate package.

- ldap_mapper.so: LDAP-based mapper module.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

# fixup configs
sed -i -e '
	s,/usr/lib/pam_pkcs11/,/%_lib/%name/,g;
	s,/usr/lib/,%_libdir/,g;
	s,/etc/pam_pkcs11/,%_sysconfdir/security/%name/,g;
	' etc/*.example doc/*.in doc/*.xml

%build
%autoreconf
#	--disable-rpath \
%configure \
	--libdir=/%_lib \
	--disable-static \
	--enable-shared \
	--enable-debug \
	--with-ldap \
	--with-confdir=%_sysconfdir/security/%name \
	#
%make_build
cd doc
./generate-api.sh

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/security/%name/{cacerts,crls}
for f in pam_pkcs11.conf card_eventmgr.conf pkcs11_eventmgr.conf; do
  install -pm644 "etc/$f.example" -T "%buildroot%_sysconfdir/security/%name/$f"
done

# Cleanup .la files
rm %buildroot/%_lib/*/*.la

%find_lang %name

%files -f %name.lang
%doc AUTHORS README
%doc doc/pam_pkcs11.html
%doc doc/mappers_api.html
%doc doc/README.autologin
%doc doc/README.mappers
%dir %_sysconfdir/security/%name
%dir %_sysconfdir/security/%name/cacerts
%dir %_sysconfdir/security/%name/crls
%config(noreplace) %_sysconfdir/security/%name/pam_pkcs11.conf
%config(noreplace) %_sysconfdir/security/%name/pkcs11_eventmgr.conf
%_bindir/pkcs11_eventmgr
%_bindir/pklogin_finder
%_bindir/pkcs11_inspect
%_bindir/pkcs11_listcerts
%_bindir/pkcs11_setup
%_bindir/pkcs11_make_hash_link
%dir /%_lib/%name
/%_lib/%name/openssh_mapper.so
/%_lib/%name/opensc_mapper.so
%_pam_modules_dir/pam_pkcs11.so
%_man1dir/pkcs11_eventmgr.1*
%_man1dir/pkcs11_inspect.1*
%_man1dir/pkcs11_listcerts.1*
%_man1dir/pkcs11_setup.1*
%_man1dir/pklogin_finder.1*
%_man1dir/pkcs11_make_hash_link.1*
%_man8dir/pam_pkcs11.8*
%dir %_datadir/%name
%_datadir/%name/pam_pkcs11.conf.example
%_datadir/%name/pam.d_login.example
%_datadir/%name/subject_mapping.example
%_datadir/%name/mail_mapping.example
%_datadir/%name/digest_mapping.example
%_datadir/%name/pkcs11_eventmgr.conf.example
%dir %_sysconfdir/security/%name/profiles
%config(noreplace) %_sysconfdir/security/%name/profiles/*
%dir %_sysconfdir/security/%name/modules.avail
%config(noreplace) %_sysconfdir/security/%name/modules.avail/*
%dir %_sysconfdir/security/%name/mapping.profiles
%config(noreplace) %_sysconfdir/security/%name/mapping.profiles/*
%_controldir/pam-*
%_controldir/*event*
%config(noreplace) %_sysconfdir/pam.d/*
%_unitdir/*

%files pcsc
%doc doc/README.eventmgr
%config(noreplace) %_sysconfdir/security/%name/card_eventmgr.conf
%_bindir/card_eventmgr
%_mandir/man1/card_eventmgr.1*
%_datadir/%name/card_eventmgr.conf.example

%files ldap
%doc doc/README.ldap_mapper
/%_lib/%name/ldap_mapper.so

%changelog
* Thu Aug 03 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt10
- Use alterator-service-functions (need >= 2.0.4) to control the
  service in a chroot.

* Fri Jul 21 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt9
- Don\'t include 'debug' settings in the profiles.
- Support nested module configuration in 'pam-pkcs11-profile' control
  profiles.
- Independently select the cert mapping scheme using 'pam-pkcs11-mapping'
  control.
- Add SNILS (OID 1.2.643.100.3) mapping profiles.

* Fri Jul 07 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt8
- Added post-processing options to the generic mapper (prefix,
  postfix, scrambling).
- The generic mapper is now able to search for OID values both
  in the the main subject and subject extensions.

* Tue Jun 27 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt7
- Add support for GOST certificates (thx cas@ and Max Kosmach).
- Complete Russian translation of pam_pkcs11 (thx cas@ and Max Kosmach).

* Thu Jun 22 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt6
- Allow to pass to the next module if the auth isn\'t restricted to
  card only.

* Fri Jun 09 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt5
- Fix: Initialize the event manager state value from token (closes: 33534).
- Add configuration control scripts: support "profiles" and "modules.avail"
  configuration directories.
- Add pkcs11_strict system-auth PAM configuration.
- Fix: Don\'t stuck if wait_for_card=false.
- Fix: Ignore the token not found error when the auth isn\'t restricted to
  card only login.
- Add systemd service unit for pkcs11_eventmgr.

* Wed Jun 07 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt4
- Fix: Initialize the event manager state value from token (closes: 33534).

* Mon Nov 21 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.9-alt3
- ask_pin (by default: true) option added (thx cas@);
  the corresponding PAM options are: ask_pin, dont_ask_pin.

* Sun Nov 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.9-alt2
- Restored ALT-specific features (from p7's 0.6.4-alt2, originally by raorn@):
  1. The example configs are placed in %_datadir/%name/.
  2. The use of OpenSSL's c_hash instead of pkcs11_make_hash_links
     is advised in the documentation; more options in example configs.
  3. global_ca configuration option for the system-wide cert storage.
  4. Russian translations updated
     (and shortened "smart card" into "token" in some places).
  5. Larger buffers (to hold localized strings) and safer operations
     with them (no unjustified sprintf).
  6. Check if there are any valid certificates before asking for PIN.

* Mon Oct 31 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.9-alt1
- New version 0.6.9
- Fix project homepage

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.8-alt1.git20140828
- Version 0.6.8

* Mon Jul 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.4-alt2
- fix build

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Jun 28 2010 Alexey I. Froloff <raorn@altlinux.org> 0.6.4-alt1
- [0.6.4]

* Tue Oct 06 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.1-alt5
- Ask PIN only if there are any certificates that can be mapped to user

* Sat Sep 05 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.1-alt4
- Fix buffer overflow in non-POSIX locales

* Sun Aug 23 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.1-alt3
- Russian translations updated

* Fri Jul 31 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.1-alt2
- Document moar pam_pkcs11 options in default config
- cert_policy: global_ca - use system-wide cert storage when verifying
  certificates
- Fix paths in manpages and documentation
- Dropped make_hash_links.sh in favor of c_rehash (openssl)

* Tue Jul 21 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.1-alt1
- Built for Sisyphus

