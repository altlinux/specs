Name: dconf-profile
Version: 0.1
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
mkdir -p %buildroot%_sysconfdir/dconf/{profile,db/{default,local,policy}.d/locks}

install -Dm0644 dconf_mandatory_dir.conf \
	--target-directory %buildroot%_tmpfilesdir
install -Dm0644 user system \
	--target-directory %buildroot%_sysconfdir/dconf/profile/
install -Dm0644 user system user_mandatory.template \
	--target-directory %buildroot%_datadir/%name/default/

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
* Wed Jul 26 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1-alt1
- Initial release
