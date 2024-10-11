%define _unpackaged_files_terminate_build 1
#add_python3_self_prov_path %buildroot%python3_sitelibdir/gpoa

%add_python3_req_skip backend
%add_python3_req_skip frontend.frontend_manager
%add_python3_req_skip gpt.envvars
%add_python3_req_skip gpt.folders
%add_python3_req_skip gpt.gpt
%add_python3_req_skip gpt.printers
%add_python3_req_skip gpt.shortcuts
%add_python3_req_skip gpt.gpo_dconf_mapping
%add_python3_req_skip gpt.dynamic_attributes
%add_python3_req_skip messages
%add_python3_req_skip plugin
%add_python3_req_skip storage
%add_python3_req_skip storage.fs_file_cache
%add_python3_req_skip storage.dconf_registry
%add_python3_req_skip util
%add_python3_req_skip util.arguments
%add_python3_req_skip util.config
%add_python3_req_skip util.dbus
%add_python3_req_skip util.exceptions
%add_python3_req_skip util.kerberos
%add_python3_req_skip util.logging
%add_python3_req_skip util.paths
%add_python3_req_skip util.preg
%add_python3_req_skip util.roles
%add_python3_req_skip util.rpm
%add_python3_req_skip util.sid
%add_python3_req_skip util.signals
%add_python3_req_skip util.system
%add_python3_req_skip util.users
%add_python3_req_skip util.util
%add_python3_req_skip util.windows
%add_python3_req_skip util.xml
%add_python3_req_skip util.gpoa_ini_parsing

Name: gpupdate
Version: 0.11.4
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
Requires: python3-module-configobj
Requires: oddjob-%name >= 0.2.3
Requires: libnss-role >= 0.5.0
Requires: local-policy >= 0.4.9
Requires: pam-config >= 1.9.0
Requires: autofs
Requires: dconf-profile
Requires: libgvdb-gir
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
ln -s %python3_sitelibdir/gpoa/scripts_runner \
	%buildroot%_prefix/libexec/%name/scripts_runner

mkdir -p %buildroot%_datadir/%name
mv %buildroot%python3_sitelibdir/gpoa/templates \
	%buildroot%_datadir/%name/

mkdir -p %buildroot%_sysconfdir/%name
touch %buildroot%_sysconfdir/%name/environment

install -Dm0644 dist/%name.service %buildroot%_unitdir/%name.service
install -Dm0644 dist/%name.timer %buildroot%_unitdir/%name.timer
install -Dm0644 dist/%name-scripts-run.service %buildroot%_unitdir/%name-scripts-run.service
install -Dm0644 dist/%name-user.service %buildroot/usr/lib/systemd/user/%name-user.service
install -Dm0644 dist/%name-scripts-run-user.service %buildroot/usr/lib/systemd/user/%name-scripts-run-user.service
install -Dm0644 dist/%name-user.timer %buildroot/usr/lib/systemd/user/%name-user.timer
install -Dm0644 dist/system-policy-%name %buildroot%_sysconfdir/pam.d/system-policy-%name
install -Dm0644 dist/%name-remote-policy %buildroot%_sysconfdir/pam.d/%name-remote-policy
install -Dm0644 dist/%name.ini %buildroot%_sysconfdir/%name/%name.ini
install -Dm0644 doc/gpoa.1 %buildroot/%_man1dir/gpoa.1
install -Dm0644 doc/gpupdate.1 %buildroot/%_man1dir/gpupdate.1
install -Dm0644 completions/gpoa %buildroot/%_datadir/bash-completion/completions/gpoa
install -Dm0644 completions/gpupdate %buildroot/%_datadir/bash-completion/completions/gpupdate
install -Dm0644 completions/gpupdate-setup %buildroot/%_datadir/bash-completion/completions/gpupdate-setup

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
if [ -x "/bin/systemctl" ]; then
    gpupdate-setup update
fi

# Remove storage in case we've lost compatibility between versions.
# The storage will be regenerated on GPOA start.
%define active_policy %_sysconfdir/local-policy/active
%triggerpostun -- %name < 0.9.13.6
rm -f %_cachedir/%name/registry.sqlite
if test -L %active_policy; then
	sed -i "s|^\s*local-policy\s*=.*|local-policy = $(readlink -f %active_policy)|" \
		%_sysconfdir/%name/%name.ini
fi

%files
%_sbindir/gpoa
%_sbindir/gpupdate-setup
%_bindir/gpupdate
%_prefix/libexec/%name/scripts_runner
%_prefix/libexec/%name/pkcon_runner
%attr(755,root,root) %python3_sitelibdir/gpoa/gpoa
%attr(755,root,root) %python3_sitelibdir/gpoa/gpupdate
%attr(755,root,root) %python3_sitelibdir/gpoa/gpupdate-setup
%attr(755,root,root) %python3_sitelibdir/gpoa/scripts_runner
%attr(755,root,root) %python3_sitelibdir/gpoa/pkcon_runner
%python3_sitelibdir/gpoa
%_datadir/%name
%_unitdir/%name.service
%_unitdir/%name-scripts-run.service
%_unitdir/%name.timer
%_man1dir/gpoa.1.*
%_man1dir/gpupdate.1.*
%_datadir/bash-completion/completions/gpoa
%_datadir/bash-completion/completions/gpupdate
%_datadir/bash-completion/completions/gpupdate-setup
%_user_unitdir/%name-user.service
%_user_unitdir/%name-user.timer
%_user_unitdir/%name-scripts-run-user.service
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
* Fri Oct 11 2024 Valery Sinelnikov <greh@altlinux.org> 0.11.4-alt1
- Added skip plugin (closes: 51631)
- Fixed getting the network path (closes:51606)
- The _appliers sequence has been changed,
  package_applier has been moved to the end

* Fri Sep 06 2024 Valery Sinelnikov <greh@altlinux.org> 0.11.3-alt1
- Optimized string cleaning using str.translate()

* Wed Sep 04 2024 Valery Sinelnikov <greh@altlinux.org> 0.11.2-alt1
- Fixed data type handling in kde_applier
- Removing legacy unused code
- Added saving policy data without polfile
- Added escaping of special characters in data (closes: 51201)

* Tue Aug 27 2024 Valery Sinelnikov <greh@altlinux.org> 0.11.1-alt1
- Fixed setting links in shortcuts (closes: 51275)

* Fri Aug 09 2024 Valery Sinelnikov <greh@altlinux.org> 0.11.0-alt1
- Added saving preferences in dconf
- Added versioning support for gpt
- Added the ability to force gpt download
- Added completions for --force
- Added new exceptions for Chromium 126
- Added information to the man pages
- Fixed handling of incorrect valuename

* Mon Jul 08 2024 Valery Sinelnikov <greh@altlinux.org> 0.10.6-alt1
- Fixed firefox_applier errors

* Fri Jun 28 2024 Valery Sinelnikov <greh@altlinux.org> 0.10.5-alt1
- Correction of missing entries with a upper case
- Fixed string processing in date (closes: 50782)
- Fixed getting correct data for the user for pkcon_runner

* Thu Jun 27 2024 Valery Sinelnikov <greh@altlinux.org> 0.10.4-alt1
- Fixed the definition of the module activation check (closes: 50755)
- Fixed sorting of scripts (closes: 50756)
- Fixed reading key values from dconf
- Changed the method for getting the list of packages for pkcon_runner

* Wed Jun 19 2024 Valery Sinelnikov <greh@altlinux.org> 0.10.3-alt1
- Added autocompletion for gpoa, gpupdate, gpupdate-setup
- Added correct work with json data in keys for the Firefox browser
- Polkit_appliers changed to non-experimental
- Fixed bug of not clearing kde applier settings (closes: 50336)
- Fixed registry key reading (closes: 50553)
- Added waiting for data generation for scripts (closes: 50667)

* Fri Jun 07 2024 Valery Sinelnikov <greh@altlinux.org> 0.10.2-alt1
- Added some fixes to dconf_registry and scripts
- Fixed windows registry key reading for loopback

* Tue Jun 04 2024 Valery Sinelnikov <greh@altlinux.org> 0.10.1-alt1
- Added handling of unexpected data types when writing to dconf

* Mon May 13 2024 Valery Sinelnikov <greh@altlinux.org> 0.10.0-alt1
- A method for storing registry keys obtained from GPOs (Group Policy Objects)
  has undergone significant repairs. We have switched from using SQLite
  to using Dconf to improve data storage efficiency

* Wed Mar 13 2024 Valery Sinelnikov <greh@altlinux.org> 0.9.13.9-alt1
- Fixed premature removal of double slash

* Thu Feb 22 2024 Valery Sinelnikov <greh@altlinux.org> 0.9.13.8-alt1
- Added search for dc on the site
- Added compatibility support for the oldest versions of SQLAlchemy

* Mon Feb 05 2024 Valery Sinelnikov <greh@altlinux.org> 0.9.13.7-alt1
- Editing the cache size in the Yandex browser has returned (closes: 44621)
- Removed unnecessary calls to subprocess

* Wed Jan 31 2024 Valery Sinelnikov <greh@altlinux.org> 0.9.13.6-alt1
- Added support for hidden attribute for folders (closes: 48964)
- Added support for Cyrillic and spaces for mounting disks (closes: 49229)

* Fri Jan 12 2024 Valery Sinelnikov <greh@altlinux.org> 0.9.13.5-alt1
- Fixed blocking check for machine policies with multiple sections (closes: 48971)
- Extension of the valuename_typeint list for the admx-chromium 120.0
- Extension of the valuename_typeint list for the admx-yandex 118.0
- Changed PAM logic to prevent re-call (closes: 48973)
- Changed timer option OnStartupSec to prevent re-call

* Mon Dec 18 2023 Valery Sinelnikov <greh@altlinux.org> 0.9.13.4-alt1
- Fixed regular expression to search for wallpaper management section (closes: 48828)

* Wed Dec 13 2023 Valery Sinelnikov <greh@altlinux.org> 0.9.13.3-alt1
- Fixed bug handling of invalid username
  when requesting cache (closes: 48310)

* Tue Nov 28 2023 Valery Sinelnikov <greh@altlinux.org> 0.9.13.2-alt1
- Fixed kde_applier bug (closes: 47995)

* Wed Oct 18 2023 Valery Sinelnikov <greh@altlinux.org> 0.9.13.1-alt1
- Fixed kde_applier bug (closes: 47995)
- Fixed kde_applier bug (closes: 47996)
- Fixed kde_applier bug (closes: 47998)
- Fixed kde_applier bug (closes: 47820)
- Fixed shortcut_applier bug (closes: 47638)
- Fixed shortcut_applier bug (closes: 47641)
- Fixed systemd_applier bug (closes: 47652)

* Tue Sep 19 2023 Valery Sinelnikov <greh@altlinux.org> 0.9.13.0-alt1
- Added KDE applier
- Fixed loopback policy processing
- Fixed appliers exception for some chromium policies
- Fixed ntp error
- cifs_appliers, polkit_appliers changed to non-experimental

* Wed Jun 14 2023 Valery Sinelnikov <greh@altlinux.org> 0.9.12.6-alt1
- Added support for dictionaries as policy values for
  yandex_browser_applier and chromium_applier
- Extended functionality of ConfigObj to save comments ';'
- Added support for SQLAlchemy2 in storage
- Added 'cifsacl' option to mount templates

* Fri May 26 2023 Valery Sinelnikov <greh@altlinux.org> 0.9.12.5-alt1
- Fixed editing cache volume (DiskCacheSize) in Yandex browser (closes: 44621)
- The access to caching files has been fixed

* Sun Mar 19 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.9.12.4-alt1
- Fixed an implementation of replace action in folder applier
- Improve file cache store() with copy in temporary file before saving
- Added implementation of using executable bit in file copy applier
- Fixed debug messages typos in file copy applier

* Tue Feb 28 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.9.12.3-alt1
- Add support of set copyied files to be executed by paths and suffixes (extensions).
- Add support of saving comments in ini files.
- Add support samba-4.17 python interface for gp.gpclass instead of gpclass.

* Thu Dec 29 2022 Valery Sinelnikov <greh@altlinux.org> 0.9.12.2-alt2
- Fixed a typo in cifs_applier.py

* Thu Dec 29 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.9.12.2-alt1
- Add support of create and delete symlinks in user home directory for mapped
  network drives in cifs applier
- Fix file copy applier support of delete files with substitution

* Tue Dec 13 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.9.12.1-alt1
- Update file copy applier with substitution support
- Update translations for several logs

* Mon Dec 12 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.9.12-alt2
- Update release with forgotten changes

* Sun Dec 11 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.9.12-alt1
- Fixed mapped drive maps for user and add support for machine
 + Added label option support
 + Fixed letters collisions and assigning as Windows
- Replaced cifs applier mountpoints into shown gvfs directories:
 + /media/gpupdate/Drive - for system shares
 + /media/gpupdate/.Drive - for system hidden shares
 + /run/media/USERNAME/DriveUser - for user shares
 + /run/media/USERNAME/.DriveUser - for user hidden shares
- Added network shares support for user
- Fixed bug (closes: 44026) for chromium applier
- Added keylist handling when generating firefox settings (closes: 44209)
- Added a check of the need to scroll DC (scrolling DCs disabled by default!)
- Added the ability to generate rules for all polkit actions
- Added applier for Yandex.Browser

* Fri Sep 30 2022 Valery Sinelnikov <greh@altlinux.org> 0.9.11.2-alt1
- Fixed formation of the correct path for creating a user directory

* Tue Sep 27 2022 Valery Sinelnikov <greh@altlinux.org> 0.9.11.1-alt1
- Fixed merge for nodomain_backend
- Added support for complex types in chromium_applier

* Wed Sep 14 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.9.11-alt1
- Add Chromium applier
- Update Firefox applier

* Fri Aug 26 2022 Valery Sinelnikov <greh@altlinux.org> 0.9.10-alt1
- INI-files preferences implementation
- Files preferences implementation
- Scripts (logon logoff startup shutdown) implementation
- UserPolicyMode set accordingly
- Folder bugs fixed
- Firefox app full release

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

