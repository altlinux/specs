Name: firefox-legacy-profile
Version: 0.1
Release: alt1

Summary: Make Firefox use existing ("legacy") profile
License: MPL-2.0
Group: Networking/WWW

Url: http://github.com/NixOS/nixpkgs/pull/119849
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
AutoProv: no
AutoReq: no

%description
%summary
instead of creating a new profile for new version.

%prep

%build
cat > firefox-esr.sh <<EOF
# don't force a new blank profile after version change
# NB: do NOT use SNAP_NAME=firefox (heavy side effects)

[ -z "$MOZ_NO_LEGACY_PROFILES" ] || exit 0
export MOZ_LEGACY_PROFILES=1 MOZ_ALLOW_DOWNGRADE=1
EOF

cat > firefox-esr.csh <<EOF
# don't force a new blank profile after version change
# NB: do NOT use SNAP_NAME=firefox (heavy side effects)

if (! $?MOZ_NO_LEGACY_PROFILES) then
	setenv MOZ_LEGACY_PROFILES 1
	setenv MOZ_ALLOW_DOWNGRADE 1
endif
EOF

%install
# provide environment variables
for i in sh csh; do
	install -pDm755 firefox-esr.$i \
		%buildroot%_sysconfdir/profile.d/firefox-esr.$i
done

%files
%dir %_sysconfdir/profile.d
%config(noreplace) %_sysconfdir/profile.d/firefox-esr.sh
%config(noreplace) %_sysconfdir/profile.d/firefox-esr.csh

%changelog
* Thu Oct 29 2026 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (cf. firefox-esr 140.7.0-alt3)
