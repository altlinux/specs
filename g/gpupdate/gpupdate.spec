%define _unpackaged_files_terminate_build 1

Name: gpupdate
Version: 0.9.9.1
Release: alt1

Summary: GPT applier
License: GPLv3+
Group: Other
Url: https://github.com/altlinux/gpupdate
BuildArch: noarch

Requires: control

BuildRequires: rpm-build-python3
BuildRequires: gettext-tools
Requires: python3-module-rpm
Requires: python3-module-dbus
Requires: oddjob-%name >= 0.2.0
Requires: libnss-role >= 0.5.0
Requires: local-policy >= 0.4.9
Requires: pam-config >= 1.9.0
Requires: autofs
# This is needed by shortcuts_applier
Requires: desktop-file-utils
# This is needed for smb file cache support
Requires: python3-module-smbc >= 1.0.23-alt3

Source0: %name-%version.tar

%description
gpupdate is the facility to apply various GPO/GPT settings retrieved
from Active Directory domain in UNIX environment.

%prep
%setup -q

%install
mkdir -p \
	%buildroot%python3_sitelibdir/
cp -r gpoa \
	%buildroot%python3_sitelibdir/

# Generate translations
msgfmt \
	-o %buildroot%python3_sitelibdir/gpoa/locale/ru_RU/LC_MESSAGES/gpoa.mo \
	%buildroot%python3_sitelibdir/gpoa/locale/ru_RU/LC_MESSAGES/gpoa.po

mkdir -p \
	%buildroot%_bindir/ \
	%buildroot%_sbindir/ \
	%buildroot%_cachedir/%name/ \
	%buildroot%_cachedir/%{name}_file_cache/ \
	%buildroot%_cachedir/%name/creds

ln -s %python3_sitelibdir/gpoa/gpoa \
	%buildroot%_sbindir/gpoa
ln -s %python3_sitelibdir/gpoa/gpupdate \
	%buildroot%_bindir/gpupdate
ln -s %python3_sitelibdir/gpoa/gpupdate-setup \
	%buildroot%_sbindir/gpupdate-setup

mkdir -p \
	%buildroot%_prefix/libexec/%name

ln -s %python3_sitelibdir/gpoa/pkcon_runner \
	%buildroot%_prefix/libexec/%name/pkcon_runner

mkdir -p %buildroot%_datadir/%name
mv %buildroot%python3_sitelibdir/gpoa/templates \
	%buildroot%_datadir/%name/

mkdir -p %buildroot%_sysconfdir/%name
touch %buildroot%_sysconfdir/%name/environment

install -Dm0644 dist/%name.service %buildroot%_unitdir/%name.service
install -Dm0644 dist/%name-user.service %buildroot/usr/lib/systemd/user/%name-user.service
install -Dm0644 dist/system-policy-%name %buildroot%_sysconfdir/pam.d/system-policy-%name
install -Dm0644 dist/%name-remote-policy %buildroot%_sysconfdir/pam.d/%name-remote-policy
install -Dm0644 dist/%name.ini %buildroot%_sysconfdir/%name/%name.ini
install -Dm0644 doc/gpoa.1 %buildroot/%_man1dir/gpoa.1
install -Dm0644 doc/gpupdate.1 %buildroot/%_man1dir/gpupdate.1

for i in gpupdate-localusers \
	 gpupdate-group-users \
	 gpupdate-system-uids
do
	install -pD -m755 "dist/$i" \
		"%buildroot%_sysconfdir/control.d/facilities/$i"
done

%preun
%preun_service gpupdate

%post
%post_service gpupdate

# Remove storage in case we've lost compatibility between versions.
# The storage will be regenerated on GPOA start.
%define active_policy %_sysconfdir/local-policy/active
%triggerpostun -- %name < 0.9.6
rm -f %_cachedir/%name/registry.sqlite
if test -L %active_policy; then
	sed -i "s|^\s*local-policy\s*=.*|local-policy = $(readlink -f %active_policy)|" \
		%_sysconfdir/%name/%name.ini
fi

%files
%_sbindir/gpoa
%_sbindir/gpupdate-setup
%_bindir/gpupdate
%_prefix/libexec/%name/pkcon_runner
%attr(755,root,root) %python3_sitelibdir/gpoa/gpoa
%attr(755,root,root) %python3_sitelibdir/gpoa/gpupdate
%attr(755,root,root) %python3_sitelibdir/gpoa/gpupdate-setup
%attr(755,root,root) %python3_sitelibdir/gpoa/pkcon_runner
%python3_sitelibdir/gpoa
%_datadir/%name
%_unitdir/%name.service
%_man1dir/gpoa.1.*
%_man1dir/gpupdate.1.*
/usr/lib/systemd/user/%name-user.service
%dir %_sysconfdir/%name
%_sysconfdir/control.d/facilities/*
%config(noreplace) %_sysconfdir/%name/environment
%config(noreplace) %_sysconfdir/%name/%name.ini
%config(noreplace) %_sysconfdir/pam.d/system-policy-%name
%config(noreplace) %_sysconfdir/pam.d/%name-remote-policy
%dir %attr(0700, root, root) %_cachedir/%name
%dir %attr(0755, root, root) %_cachedir/%{name}_file_cache
%dir %attr(0700, root, root) %_cachedir/%name/creds
%exclude %python3_sitelibdir/gpoa/.pylintrc
%exclude %python3_sitelibdir/gpoa/.prospector.yaml
%exclude %python3_sitelibdir/gpoa/Makefile
%exclude %python3_sitelibdir/gpoa/test

%changelog
* Thu Mar 03 2022 Valery Sinelnikov <greh@altlinux.org> 0.9.9.1-alt1
- Fixed method call (Closes: 41994)
- Removed unnecessary replace
- Fixed declaration of variable

* Fri Feb 18 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.9.9-alt1
- Add gpupdate-remote-policy PAM substack (for pam_mount support)
- Added lookup for possible dc if first found is unreadable
- Correct folder applier (still experimental)
- Update logging and translations
- Fix error when control facilites not exists
- Add check for the presence of Gsettings schema and keys exists
- Add support of package applier via pkcon (still experimental)

* Mon Oct 25 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.8-alt1
- Added exception for org.gnome.Vino authentication-methods
- Fixed bug for alternative-port in org.gnome.Vino

* Wed Sep 29 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.7-alt1
- Fix regression with kestroy for user credential cache
- Update system-policy-gpupdate PAM-rules to ignore applying group policies
  for local users and system users with uid less than 500
- Add control facilities to rule system-policy-gpupdate rules:
  + gpupdate-group-users
  + gpupdate-localusers
  + gpupdate-system-uids

* Mon Sep 20 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.6-alt1
- Add support changed GPO List Processing for '**DelVals.' value name

* Tue Sep 14 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.5-alt1
- Refix local policy path detection
- gpupdate-setup: revert settings to default when disabled

* Tue Sep 14 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.4-alt1
- Add improvement with new local-policy system-policy control
- Fix gpupdate-setup and user service installation regressions
- Set empty local policy and local backend by default
- Fix local policy path detection

* Mon Sep 06 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.3-alt1
- Use NetBIOS name for Kerberos authentification
- Add support actions (create, update, delete, replace) for Shortcuts
- Add support GSettings with locks feature
- Add support file cache for special GSettings policy:
  Software\BaseALT\Policies\GSettings\org.mate.background.picture-filename
  (requires python smbc module with use_kerberos option support)

* Wed Jul 28 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.2-alt1
- Fix Shortcuts applier double running in user context
- Add LogonUser variable to expand_windows_var() function
- Add support of path variable expansion to Shortcuts applier

* Sun Jul 18 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.1-alt1
- Fix GSettings applier user part support
- Add support additional firefox appliers
- Add new windows policies mapping capability feature ruled by:
  Software\BaseALT\Policies\GPUpdate\WindowsPoliciesMapping
- Improve drop privileges mechanism with fork and dbus session

* Fri Jun 25 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.0-alt1
- Change policies.json location for Firefox
- Set GSettings, Chromium and Firefox appliers
  not experimental and enabled by default

* Tue Dec 22 2020 Igor Chudov <nir@altlinux.org> 0.8.2-alt1
- Increased D-Bus timeouts on calls
- Minor logging fixes

* Wed Oct 07 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.8.1-alt3
- Fixed compatibility upgrade trigger condition

* Wed Oct 07 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.8.1-alt2
- Fixed compatibility upgrade trigger from 0.7 releases for update
  active local-policy in new gpupdate.ini configuartion file

* Fri Sep 11 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.8.1-alt1
- Workaround for control names with special symbols
- Improved logging on Kerberos errors

* Fri Sep 04 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.8.0-alt1
- Improve gpo applier logging
- Add new configuration file /etc/gpupdate/gpupdate.ini
- Fix folders applier regression
- kinit move to samba backend
- Replace gpupdate-setup utility with new implementation

* Wed Jul 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.7.0-alt1
- Add multiple appliers, part of which marks as experimental yet

* Wed May 20 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.6.0-alt2
- Update system-policy PAM-rules (clean system-auth-common, add pam_env support)
- Add dependency to pam-config later than 1.9.0 release

* Fri May 15 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.6.0-alt1
- Add drives policy for shared folders with cifs applier using autofs
- Update shortcuts policy with xdg-users-dir support for DESKTOP

* Wed Apr 22 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.5.0-alt1
- Update samba format: local.xml -> Machine/Registry.pol.xml
- Add support of ad-domain-controller local policy profile
- Set properly URL of project

* Mon Apr 20 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.5-alt1
- Add support for control system-policy and requires to new pam-config

* Sun Apr 19 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.4-alt1
- Add gpupdate-setup initialization script supported local-policy profiles

* Fri Mar 06 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.3-alt1
- Fix polfile merging
- Add support controls with strings values
- Initial SIGINT signal handling

* Wed Feb 19 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.2-alt1
- Change service type to 'simple' because gpoa is not systemd-aware
- Shortcuts fixes and improvements

* Wed Feb 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.1-alt1
- Update license to GPLv3+
- Run gpudate as root without user argument for Computer target only
- Fix chromium applier

* Thu Jan 30 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.0-alt1
- Update release with first pack of stabilization fixes

* Thu Jan 16 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.3.0-alt1
- Add user appliers support and machine gsettings apllier
- Add require to oddjob-gpupdate

* Fri Dec 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.2.1-alt2
- Add support system-policy for PAM settings

* Thu Dec 19 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.2.1-alt1
- Next part of refactoring
- Add simple support adp

* Fri Dec 06 2019 Igor Chudov <nir@altlinux.org> 0.2.0-alt1
- Code refactored to work with storage facility
- Retrieval of HKCU preferences implemented
- Numerous backend and frontend stability improvements
- Chromium and Firefox appliers implemented

* Thu Nov 28 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Change license to GPLv2+
- Refactor and separate code to backend and frontend

* Sun Nov 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.0.3-alt1
- Clean code, fix functionality (Initialize cache if missing, retrieve SIDs)
- Run GPO applier as /usr/sbin/gpoa

* Fri Nov 15 2019 Igor Chudov <nir@altlinux.org> 0.0.2-alt1
- Removed hreg dependency
- Introduced caches for SIDs and Registry.pol file paths
- gpupdate transformed into simple gpoa starter
- gpoa learned to work with username
- Introduced TDB manager in order to work with samba-regedit registry
- DC domain detection now uses native python-samba functions to query LDAP

* Thu Nov 14 2019 Igor Chudov <nir@altlinux.org> 0.0.1-alt1
- Initial release

