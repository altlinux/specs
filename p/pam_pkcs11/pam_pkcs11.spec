# vim: set ft=spec: -*- rpm -spec -*-

%define _unpackaged_files_terminate_build 1

Name: pam_pkcs11
Version: 0.6.12.1
Release: alt2

Summary: PKCS #11 PAM Module and Login Tools
Group: System/Base
License: LGPL
Url: https://github.com/OpenSC/pam_pkcs11

Source: %name-%version.tar
Patch0: %name-%version-alt-cumulative.patch
#Patch1: pam_pkcs11-0.6.9-build-with-LibreSSL.patch

%add_findreq_skiplist %_sysconfdir/pam.d/*
Requires: pam-config PAM(pam_mkhomedir.so) PAM(pam_pkcs11.so) PAM(pam_succeed_if.so)
Requires: pcsc-lite pcsc-lite-ccid

BuildRequires: docbook-style-xsl flex libldap-devel libpam-devel libpcsclite-devel libssl-devel xsltproc
BuildRequires: doxygen
BuildRequires: docbook-dtds

BuildRequires: libopensc-devel

BuildPreReq: gcc-c++
# SCARD_READERSTATE_A will change to SCARD_READERSTATE afterwards:
BuildPreReq: libpcsclite-devel >= 1.7.4

BuildRequires: libpasswdqc-devel

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

%package isbc
Summary: ISBC (ESMART) low-level modules for pam_pkcs11
Group: System/Base
Requires: %name = %version-%release

%description isbc
This package contains ISBC (ESMART) low-level modules for pam_pkcs11

%prep
%setup
%patch0 -p1
#patch1 -p1

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
    --with-passwdqc \
	#
%make_build docdir=%_datadir/doc/%name-%version
cd doc
./generate-api.sh

%install
%makeinstall_std docdir=%_datadir/doc/%name-%version unitdir=%_unitdir

mkdir -p %buildroot%_sysconfdir/security/%name/{cacerts,crls}

# Install the example configs in /etc
install -D -m0644 \
        %buildroot%_datadir/doc/%name-%version/pam_pkcs11.conf.example \
        %buildroot%_sysconfdir/security/%name/pam_pkcs11.conf
install -D -m0644 \
        %buildroot%_datadir/doc/%name-%version/pkcs11_eventmgr.conf.example \
        %buildroot%_sysconfdir/security/%name/pkcs11_eventmgr.conf
install -D -m0644 \
        %buildroot%_datadir/doc/%name-%version/card_eventmgr.conf.example \
        %buildroot%_sysconfdir/security/%name/card_eventmgr.conf

install -D -m0644 \
        %buildroot%_datadir/doc/%name-%version/digest_mapping.example \
        %buildroot%_sysconfdir/security/%name/digest_mapping
install -D -m0644 \
        %buildroot%_datadir/doc/%name-%version/mail_mapping.example \
        %buildroot%_sysconfdir/security/%name/mail_mapping
install -D -m0644 \
        %buildroot%_datadir/doc/%name-%version/subject_mapping.example \
        %buildroot%_sysconfdir/security/%name/subject_mapping

install -D -m0644 \
        %buildroot%_datadir/doc/%name-%version/pam.d_ignore_no_card.example \
        %buildroot%_sysconfdir/pam.d/system-auth-pkcs11_strict

# Make additional "use_first_pass" config (needed by control system-auth):
sed -e 's/pam_pkcs11\.so/pam_pkcs11.so use_first_pass/g' \
    -e '/^account/ d' \
    -e '/^session/ d' \
    %buildroot%_sysconfdir/pam.d/system-auth-pkcs11_strict \
    >%buildroot%_sysconfdir/pam.d/system-auth-use_first_pass-pkcs11_strict

# Cleanup .la files
rm %buildroot/%_lib/*/*.la

%find_lang %name

%post
[ ! -e %_sysconfdir/security/%name/openssl.cnf ] || \
    mv -v %_sysconfdir/security/%name/openssl.cnf \
          %_sysconfdir/security/%name/openssl.cnf.rpmold

%files -f %name.lang
%dir %_sysconfdir/security/%name
%dir %_sysconfdir/security/%name/cacerts
%dir %_sysconfdir/security/%name/crls
%config(noreplace) %_sysconfdir/security/%name/pam_pkcs11.conf
%config(noreplace) %_sysconfdir/security/%name/pkcs11_eventmgr.conf
%config(noreplace) %_sysconfdir/security/%name/*_mapping
%_bindir/*
%exclude %_bindir/card_eventmgr
%dir /%_lib/%name
/%_lib/%name/openssh_mapper.so
/%_lib/%name/opensc_mapper.so
%_pam_modules_dir/pam_pkcs11.so
%_man1dir/*.1*
%_man8dir/*.8*
%config(noreplace) %_sysconfdir/pam.d/*
%_unitdir/*
%_datadir/doc/%name-%version/*.example

%files pcsc
%config(noreplace) %_sysconfdir/security/%name/card_eventmgr.conf
%_bindir/card_eventmgr
%_mandir/man1/card_eventmgr.1*

%files ldap
/%_lib/%name/ldap_mapper.so

%files isbc
/%_lib/%name/ll_isbc.so

%changelog
* Mon Jul 15 2024 Paul Wolneykien <manowar@altlinux.org> 0.6.12.1-alt2
- Fixed build: Pass unitdir to make.

* Thu Apr 07 2022 Paul Wolneykien <manowar@altlinux.org> 0.6.12.1-alt1
- Updated version: upstream commit 4efa29f with fixed LGTM.com errors
  and spelling in configuration files and docs.
- Bring back the pkcs11_make_hash_link tool with improved filename
  handling (thx krolikov) (closes: 42324).

* Fri Aug 27 2021 Paul Wolneykien <manowar@altlinux.org> 0.6.12-alt1
- Fresh up to v0.6.12.
- Fixed segfault in CRL check (thx Komarov Egor).
- Fixed libpasswdqc initialization (closes: 39790).
- Fixed memory corruption in mapper modules (closes: 40814).

* Thu Mar 18 2021 Paul Wolneykien <manowar@altlinux.org> 0.6.11-alt4
- Build with libpasswdqc (closes: 39790)
- Warn about undefined symbols when linking the module.

* Thu Sep 03 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.11-alt3
- Fixed OpenSSL-related compilation warnings.

* Thu Sep 03 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.11-alt2
- Added support for GOST-2012.

* Mon Aug 31 2020 Paul Wolneykien <manowar@altlinux.org> 0.6.11-alt1
- Fresh up to v0.6.11.
- Refactor the patches.
- Transform the 'ask_pin' option into 'ask_pin_later'.

* Tue Mar 12 2019 Oleg Solovyov <mcpain@altlinux.org> 0.6.10-alt6
- rebuild with openssl 1.1

* Fri Jan 11 2019 Paul Wolneykien <manowar@altlinux.org> 0.6.10-alt5
- Fix/improve: Write a message when the token authentication is
  cancelled.

* Wed Nov 28 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.10-alt4
- Fix: Put the examples into the package docdir.
- Install the default mapping configs.

* Tue Nov 20 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.10-alt3
- Improve: Add option "use_waitevent" utilizing C_WaitForSlotEvent().
- Introduce the "pin_len_min" and "pin_len_max" configuration
  options that control the allowed PIN-code length.

* Mon Nov 19 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.10-alt2
- Fix: Don\'t force PIN change from the screensaver session.
- State the token label and serial in the syslog messages.
- Round the "PIN changed" event timestamp and the system time prior
  to compare them.
- Fix/improve: Take a journal record with the minimal index when
  looking for the last event of particular type.

* Thu Sep 13 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.10-alt1
- New version 0.6.10.
- Cleanup passwords with `cleanse()` in the new code too.
- README.md: removed license section (thx Frank Morgner).
- Update README.md (thx Frank Morgner).
- fixed wiping secrets with OpenSSL_cleanse() (thx Frank Morgner).
- fixed buffer overflow with long home directory (thx Frank Morgner).
- verify using a nonce from the system, not the card (thx Frank Morgner).
- Fixed segfault and fetch problems when checking CRLs (thx Gil Kloepfer).

* Mon Aug 13 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt34
- Distinguish between entering a wrong user PIN and SO PIN during
  the PIN change / initialization procedure.

* Mon Aug 06 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt33
- Fixed: Distinguish between expired PIN and other cases to change it.

* Fri Jun 15 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt32
- Build with a new LibreSSL version (2.7.3).

* Thu Jun 07 2018 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt31
- Fixed SIGSEGV on empty password.
- Simplify the password cleanup in the PIN change procedure.
- Implement the "check_pin_early" option.

* Fri Nov 24 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt30
- Move the control scripts and base profiles to the "pkcs11-profiles"
  package.

* Thu Nov 16 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt29
- Don\'t show a welcome message when is asked by a screensaver.

* Tue Nov 14 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt28
- 'isbc': Set debug level on ititialization.
- Call 'pin_status()' of a low-level module to check if PIN has
  expired.
- Add some Cryptoki API to pkcs11_lib module.
- Split the lowlevel API onto public and private parts.
- Implement 'pin_status()' for the 'isbc' low-level module.
- Fixed 'force_pin_change' configuration option.
- Fixed ISBC journal timestamp.
- Fixed cleanup of the old password.

* Mon Nov 13 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt27
- Fix: Report password quality check error only when the return
  code is less than zero.

* Fri Nov 10 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt26
- Output the modified info message for a user PIN change session
  when the card is locked.

* Thu Nov 09 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt25
- Check and warn about PIN attempts in PIN change mode.
- Reset the PIN only if card is locked, by default.

* Wed Nov 08 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt24
- Use libpwquality to check the PIN (optional, configurable).
- Add option to automatically set PIN init mode for `pam_chauthtok`
  if there were incorrect login attempts (false by default).
- Implement ISBC (ESMART) APDUs to query the number of rest PIN attempts.
- Fixed `init_pin` flag.

* Tue Oct 31 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt23
- Added "pam_pkcs11_query_config" helper tool.
- Fresh/Fix the GOST support patch.

* Tue Oct 24 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt22
- Support "PAM_RESET_AUTHTOK" PAM env. var. known to be set by
  LightDM.
- Fix: Answer with INFO message and PAM_IGNORE code from
  "pam_sm_chauthtok()" when no card present and we are not restricted
  to card-only login.
- Added info messages for user PIN change and reset.
- Fixed double free() in refresh_slots().

* Mon Oct 23 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt21
- Automatically enable InitPIN mode for pam_sm_chauthtok() when
  user PIN is locked.

* Mon Oct 23 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt20
- Remove the redudant "pam-pkcs11-gost" control.
- Build with LibreSSL.

* Mon Oct 23 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt19
- Distinguish between welcome and welcome PIN locked.
- Distinguish between wrong PIN and wrong PIN locked.
- Fix: Exit quietly only if "card_only" is false.
- Fix: Do not return error when there are no slots.
- Return ignore or error when PKCS#11 module loading fails based
  on config.
- Use "default_username" configuration parameter to set the username
  in PAM stack when it is unset.
- Reorganize the sources: use cumulative patch.
- Fail if no token found only when it is strictly required.
- Fix/improve: Don\'t require the user to be loged-in to change the PIN.
- Allow to configure the prompts on the per-service basis. Parse prompts
  from the root conf, then "prompts default {}", then "prompts <service> {}".
- Use C_InitPIN() to setup PIN in SO login mode.
- Support PAM_CHANGE_EXPIRED_AUTHTOK flag in pam_sm_chauthtok().
- Implement forced PIN change after login when it is expired.
- Clean the password values more accurate.
- Configurable messages for PIN checks, warnings and wrong PIN
  attempts.
- Add plural / singular pin low messages.
- Fixed unloading of low-level modules and the PAM handle in
  report_pkcs11_lib_error().
- Add "pin_count_low" configuration option.
- User PIN checks (low, final, locked).
- Implement a describer returning an OID (optionally mapped).
- Fix: Welcome the user only once.
- Add support for user descriptions to the mapper interface and
  the manager.
- Skip empty prompts. Output a user welcome prompt with a description
  (as returned by a mapper).
- Make the 'quiet' config parameter affect syslog ouput only.
- Output only the last certificate verification error.
- Add support for \-escapes in the config file including \n\r\t\".
- Fix: Return PAM_AUTH_ERR for login error.
- Introduce new "verbose" config parameter.
- Get rid of duplicate "no token" error.
- Output "no token" errors only when wait-for-card mode is off.
- Fix: Make wait-for-card work when the user is not logged in.
- Add the default prompt message profile.
- Off the debug mode by default.
- Fix: Read the configuration before output any prompts.

* Tue Oct 03 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt18
- Add 'pam-pkcs11-messages' control.
- Make PAM prompts configurable.

* Wed Sep 06 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt17
- Skip soft slots by default. Also mask slots by manufacturer
  and description.

* Mon Sep 04 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt16
- Fix: Pass the OpenSSL config name directly.

* Fri Sep 01 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt15
- Use local openssl.cnf if it exists.
- Copy the system-wide openssl.cnf after the package is installed.
- Add OpenSSL GOST engine control (for local openssl.cnf).
- Add 'mapfile' entries to SNILS profiles (commented out).
- Add 'subject', 'mail' and 'cert' mapping profiles and use 'cert'
  by default.

* Thu Aug 24 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt14
- Fix/improve: Return PAM_IGNORE if the token isn\'t present and
  card_only isn\'t set.
- Fix: Return PAM_IGNORE on PIN change request if the current login
  is not related to a token.

* Thu Aug 24 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt13
- Add password (PIN) management steps to the PAM stack.
- Implement "pam_sm_chauthtok" (the "password" part of PAM).

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt12
- Explicitly require pcsc-lite (for pcscd).
- Also require pcsc-lite-ccid (as related to the default OpenSC
  profile).

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 0.6.9-alt11
- Drop versioned dependency of alterator-service-functions (chroot
  usage is rare).
- Add 'mate-screensaver' to the screen saver list.

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

