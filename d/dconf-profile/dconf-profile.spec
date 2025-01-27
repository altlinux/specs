%define _unpackaged_files_terminate_build 1

Name: dconf-profile
Version: 0.2
Release: alt1

Summary: Dconf-profile configuration
License: GPLv3+
Group: System/Configuration/Other
BuildArch: noarch

Source0: %name-%version.tar

%description
Dconf-profile ALT configuration with group policies support. Two main
profiles are available: system and user. System profile added for
applications in read-only mode. The profile stack includes three base
layers: policy, local and default. The user profile is similar to the
system profile, but allows user to override the values of not locked
keys for writing.

A mandatory user profile template is prepared for a user profile with
user policies in a separate database. The mandatory profile stack
includes four base layers: policy, policy{UID}, local and default.
The mandatory user profile file is dynamically generated at login time
in the /run/dconf/user/UID file.

%prep
%setup -q

%install
mkdir -p %buildroot%_sysconfdir/dconf/{profile,db/{default,local,policy,distr}.d/locks}

install -Dm0644 dconf_mandatory_dir.conf \
	--target-directory %buildroot%_tmpfilesdir
install -Dm0644 user system \
	--target-directory %buildroot%_sysconfdir/dconf/profile/
install -Dm0644 user system user_mandatory.template \
		user_original.template user_old_policy.template service.template \
	--target-directory %buildroot%_datadir/%name/default/

%triggerpostun -- %name < 0:0.2
if cmp -s "%_datadir/%name/default/user_original.template" "%_sysconfdir/dconf/profile/user" ||
	cmp -s "%_datadir/%name/default/user_old_policy.template" "%_sysconfdir/dconf/profile/user"; then
	cp -f %_datadir/%name/default/user %_sysconfdir/dconf/profile/user
fi

%files
%_tmpfilesdir/dconf_mandatory_dir.conf
%config(noreplace) %_sysconfdir/dconf/profile/user
%config(noreplace) %_sysconfdir/dconf/profile/system
%dir %_sysconfdir/dconf
%dir %_sysconfdir/dconf/db
%dir %_sysconfdir/dconf/db/*.d
%dir %_sysconfdir/dconf/db/*.d/locks
%dir %_sysconfdir/dconf/profile
%dir %_datadir/%name
%dir %_datadir/%name/default
%_datadir/%name/default/

%changelog
* Fri Jan 24 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2-alt1
- Add support distr profile layer
- Add service specific system profile template
- Update obsoletes default user profile during upgrade

* Wed Jul 26 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1-alt1
- Initial release
