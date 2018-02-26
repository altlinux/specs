Name: pam-config
Version: 1.5.3
Release: alt1

Summary: Systemwide PAM config files
License: GPLv2+
Group: System/Base
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-deps.sh

Source2: pam_mktemp.control
Source3: system-auth.control

%define _pamdir %_sysconfdir/pam.d

# All pam dependencies now provided/required by subpackages.
AutoReqProv: nopam

PreReq: %name-control = %version-%release
Requires: libpasswdqc >= 0:1.1.0-alt0.2
Requires: glibc-crypt_blowfish >= 1.2
Provides: %_pamdir, /etc/security
Provides: pam-common = %version-%release
Obsoletes: pam-common

# due to %_pamdir/other
Conflicts: pam < 0:0.75-alt21
# due to pam_mktemp.so
Conflicts: openssh-server < 0:4.6p1

BuildPreReq: rpm-build >= 0:4.0.4-alt98.15

%package control
Summary: Control rules for the systemwide PAM config files
Group: System/Base

%package -n pam0-config
Summary: Systemwide PAM config files for Linux-PAM
Group: System/Base
PreReq: %name = %version-%release
# This is quite low-level code; synced with rpm-build-4.0.4-alt98.15.
Requires: %([ -x "%SOURCE1" ] && RPM_LIB=%_lib RPM_LIBDIR=%_libdir PAM_SO_SUFFIX= PAM_NAME_SUFFIX=0 RPM_BUILD_ROOT=%buildroot %SOURCE1 %SOURCE0 req || echo unknown)
Provides: %([ -x "%SOURCE1" ] && PAM_SO_SUFFIX= PAM_NAME_SUFFIX=0 RPM_BUILD_ROOT=%buildroot %SOURCE1 %SOURCE0 prov || echo unknown)
# Compatibility.
Provides: pam(system-auth), pam(system-auth-use_first_pass), pam(other)

%package -n pam2-config
Summary: Systemwide PAM config files for OpenPAM
Group: System/Base
PreReq: %name = %version-%release
# This is quite low-level code; synced with rpm-build-4.0.4-alt98.15.
Requires: %([ -x "%SOURCE1" ] && RPM_LIB=%_lib RPM_LIBDIR=%_libdir PAM_SO_SUFFIX=.2 PAM_NAME_SUFFIX=2 RPM_BUILD_ROOT=%buildroot %SOURCE1 %SOURCE0 req || echo unknown)
Provides: %([ -x "%SOURCE1" ] && PAM_SO_SUFFIX=.2 PAM_NAME_SUFFIX=2 RPM_BUILD_ROOT=%buildroot %SOURCE1 %SOURCE0 prov || echo unknown)

%description
PAM (Pluggable Authentication Modules) is a system security tool
which allows system administrators to set authentication policy
without having to recompile programs which do authentication.

This package contains systemwide PAM config files.
This package also contains common files and directories
shared by various PAM implementations.

%description control
This package contains control rules for systemwide PAM config files.
See control(8) for details.

%description -n pam0-config
PAM (Pluggable Authentication Modules) is a system security tool
which allows system administrators to set authentication policy
without having to recompile programs which do authentication.

This package contains systemwide config files for Linux-PAM.

%description -n pam2-config
PAM (Pluggable Authentication Modules) is a system security tool
which allows system administrators to set authentication policy
without having to recompile programs which do authentication.

This package contains systemwide config files for OpenPAM.

%prep
%setup

%install
mkdir -p %buildroot{%_pamdir,%_controldir,/etc/security}

cp -a * %buildroot%_pamdir/
chmod 644 %buildroot%_pamdir/*

for f in pam_mktemp system-auth; do
	install -pm755 %_sourcedir/$f.control %buildroot%_controldir/$f
done

%pre
%pre_control pam_mktemp
for f in %_pamdir/system-auth %_pamdir/system-auth-use_first_pass; do
	if [ -f "$f" -a ! -L "$f" ]; then
		mv -f "$f" "$f-local" &&
		ln -f "$f-local" "$f-local.rpmsave" &&
		touch "/var/run/${f##*/}-local.update" &&
		ln -s "${f##*/}-local" "$f" ||:
	fi
done
%pre_control system-auth

%post
cd %_pamdir
for f in system-auth system-auth-use_first_pass; do
	if [ -f "/var/run/$f-local.update" -a -f "$f-local.rpmsave" ]; then
		[ -f "$f-local.rpmnew" ] ||
			ln -f "$f-local" "$f-local.rpmnew" ||:
		mv -f "$f-local.rpmsave" "$f-local" &&
			rm -f "/var/run/$f-local.update" ||:
		cmp -s "$f-local" "$f-local.rpmnew" &&
			rm -f "$f-local.rpmnew" ||:
	fi
done
if [ ! -f system-auth ]; then
	if [ -f system-auth.rpmsave ]; then
		cp -af system-auth.rpmsave system-auth
	elif [ -f system-auth.rpmnew ]; then
		cp -af system-auth.rpmnew system-auth
	fi
fi
%post_control -s enabled pam_mktemp
%post_control -s local system-auth

%triggerpostun -- pam <= 0:0.75-alt8
[ $2 -gt 0 ] || exit 0
cd %_pamdir
if [ ! -f system-auth ]; then
	if [ -f system-auth.rpmsave ]; then
		cp -pf system-auth.rpmsave system-auth
	elif [ -f system-auth.rpmnew ]; then
		cp -pf system-auth.rpmnew system-auth
	fi
fi

%files
%dir %_pamdir
%config %_pamdir/other
%config(noreplace) %_pamdir/*-local
%config(noreplace) %_pamdir/*-ldap
%config(noreplace) %_pamdir/*-krb5
%config(noreplace) %_pamdir/*-multi
%config(noreplace) %_pamdir/*-pkcs11
%config(noreplace) %_pamdir/common-login*
%_pamdir/system-auth
%_pamdir/system-auth-use_first_pass
/etc/security

%files control
%config %_controldir/*

%files -n pam0-config

%changelog
* Fri Aug 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1.5.3-alt1
- system-auth-*: changed to use the "$2y$" hash encoding prefix.

* Sat May 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.5.2-alt1
- common-login: added optional pam_systemd.so (closes: #25606).

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.1-alt1
- Moved /lib*/security to filesystem package.
- Packaged as noarch.

* Tue Jun 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.5.1-alt1
- Added common-login and common-login-use_first_pass.

* Fri Aug 07 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.0.2-alt1
- NMU:
  + added PKCS#11 authentication support (closes: #20946)

* Tue Jun 30 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.1-alt1
- Fixed system-auth*-multi introduced in previous release.

* Fri Jun 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- Reindented pam config files to use tabs instead of spaces.
- system-auth-*: Rewritten "sufficient" controls with conditional jumps.
- Added experimental pam configs:
  system-auth-multi, system-auth-use_first_pass-multi.

* Sun Apr 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.5.1-alt1
- system-auth-krb5: Added pam_mkhomedir.so to the session stack (closes: #19540).

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt1
- system-auth-ldap: Added pam_mkhomedir.so to the session stack (closes: #19540).

* Thu Mar 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.4.1-alt1
- pam_mktemp.control: added system config autodetection

* Fri Oct 10 2008 Ivan A. Melnikov <iv@altlinux.org> 1.4.4-alt1
- system-auth.control: added authentication method autodetection
- added kerberos 5 authentication support

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.1-alt1
- system-auth-use_first_pass-ldap: Fixed typo.

* Fri Jun 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- system-auth-{local,ldap}: Replaced pam_passwdqc.so parameters
  with reference to /etc/passwdqc.conf file.

* Tue Jun 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- Fixed system-auth upgrade.

* Sat Jun 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt1
- Added ldap authentication support (inger).

* Mon May 28 2007 Stanislav Ievlev <inger@altlinux.org> 1.4.0-alt1.1
- add support for ldap authentication

* Thu Apr 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt1
- system-auth: Moved pam_mktemp.so from "account" to "session".
- Added pam_mktemp control, based on script from raorn@.

* Mon Jan 16 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- Do not suppress all autogenerated dependencies (#8849).

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- Updated for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Fri Aug 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Added "nullok" option to password management entry (#7606).

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- system-auth: Added "account required pam_mktemp.so" (#6814).
- Added multilib support (mouse, closes #6098).

* Sat Oct 04 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.7-alt1
- pam-config: merged pam-common into this package.

* Wed Jul 09 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt1
- Keep all configuration files in the main package, pam-config.
- Kepp all pam dependencies in pam-specific subpackages.

* Wed Jul 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt1
- Added -flavour subpackage and moved dependencies there.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- PAM configuration policy enforcement.

* Thu Apr 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- Added prefix= and count= parameters for auth tcb methods.
  This is required to activate timing attack protection
  implemented in pam_tcb-0.9.8.4-alt1.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.1.2-alt1
- Added password entry for system-auth-use_first_pass.

* Thu Dec 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.1.1-alt1
- Changed password quality enforcement policy:
  enforce=everyone --> enforce=users.

* Mon Dec 17 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.1-alt1
- Switched to tcb.

* Mon Dec 17 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.1-alt1
- Added new config for userpass support: system-auth-use_first_pass.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0-alt1
- Initial revision.
- Updated system-auth from pam package now lives here.
