%global import_path github.com/42wim/matterbridge

Name: matterbridge
Version: 1.18.3
Release: alt1

Summary: A simple chat bridge

License: Apache-2.0
Group: Networking/Instant messaging
Url: https://github.com/42wim/matterbridge

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

# repacked https://github.com/42wim/matterbridge/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.watch

%description
Bridges between a growing number of protocols.

Features:

* Support bridging between any protocols
* Support multiple gateways(bridges) for your protocols
* Message edits and deletes
* Preserves threading when possible
* Attachment / files handling
* Username and avatar spoofing
* Private groups
* API

Natively supported:

* Discord
* Gitter
* IRC
* Keybase
* Matrix
* Mattermost
* Microsoft Teams
* Nextcloud Talk
* Rocket.chat
* Slack
* Ssh-chat
* Steam
* Telegram
* Twitch
* WhatsApp
* XMPP
* Zulip

3rd party via matterbridge API:

* Discourse
* Facebook messenger
* Minecraft
* Reddit
* Counter-Strike, half-life and more
* MatterAMXX

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd .gopath/src/%import_path
export VERSION=%version
export BRANCH=altlinux
export CODENAME=montdor
export DATE="$(date '+%%Y-%%m-%%d' ${SOURCE_DATE_EPOCH:+-d$SOURCE_DATE_EPOCH})"
export GOFLAGS="-mod=vendor"
go generate
%gobuild
popd

%install
pushd .gopath/src/%import_path
install -pD matterbridge %buildroot%_bindir/matterbridge
install -pD contrib/matterbridge.service %buildroot%_unitdir/matterbridge.service
install -pm600 -D matterbridge.toml.simple %buildroot%_sysconfdir/matterbridge/bridge.toml
popd

%post
%_sbindir/groupadd -r -f matterbridge ||:
%_sbindir/useradd -r -g matterbridge -d /var/empty -s /dev/null -c 'A simple chat bridge' matterbridge ||:

%files
%doc changelog.md LICENSE README.md
%doc matterbridge.toml.sample
%doc matterbridge.toml.simple
%dir %_sysconfdir/matterbridge
%config(noreplace) %_sysconfdir/matterbridge/bridge.toml
%_bindir/matterbridge
%_unitdir/matterbridge.service

%changelog
* Sun Sep 06 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.3-alt1
- Updated to 1.18.3.

* Fri Aug 28 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.2-alt1
- Updated to 1.18.2.

* Wed Jul 29 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.0-alt1
- Updated to 1.18.0.

* Mon Jun 22 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.17.5-alt1
- Updated to 1.17.5.
- Updated watch file.

* Sun May 03 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.17.4-alt1
- Updated to 1.17.4.

* Fri Dec 20 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.3-alt1
- Updated to 1.16.3.

* Tue Nov 19 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.2-alt1
- Updated to 1.16.2.

* Sun Oct 27 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.1-alt1
- Initial build for ALT Sisyphus.


