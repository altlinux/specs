%global import_path github.com/caddyserver/caddy
%global _unpackaged_files_terminate_build 1

%define caddy_user _caddy
%define caddy_group _caddy

Name: caddy
Version: 2.6.2
Release: alt1
Summary: Web server with automatic HTTPS
License: Apache-2.0
Url: https://caddyserver.com
Group: System/Servers

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Use official resources for config, unit file, and welcome page.
# https://github.com/caddyserver/dist
Source1: https://raw.githubusercontent.com/caddyserver/dist/master/config/Caddyfile
Source2: https://raw.githubusercontent.com/caddyserver/dist/master/init/caddy.service
Source3: https://raw.githubusercontent.com/caddyserver/dist/master/init/caddy-api.service
Source4: https://raw.githubusercontent.com/caddyserver/dist/master/welcome/index.html
Source5: https://raw.githubusercontent.com/caddyserver/dist/master/scripts/completions/bash-completion
Source6: https://raw.githubusercontent.com/caddyserver/dist/master/scripts/completions/_caddy

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang rpm-macros-webserver-common
BuildRequires(pre): rpm-macros-systemd >= 5

Requires: webserver-common
Provides: webserver
Conflicts: apache2-html

%description
Caddy is the web server with automatic HTTPS.

%prep
# Vendorized go modules
# $ GO111MODULE=on go mod vendor -v
# $ git add -f vendor
# $ git commit -m "update go vendor modules by go mod vendor"

%setup
%patch -p1
sed -e '/mod.Version/ s/unknown/%{version}-%{release}/' -i caddy.go

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
export CGO_ENABLED=0
%golang_build cmd/caddy

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install
# cleanup
rm -rf -- %buildroot%_datadir

# command
#install -D -p -m 0755 caddy %buildroot%_bindir/caddy

# config
install -D -p -m 0640 %SOURCE1 %buildroot%_sysconfdir/caddy/Caddyfile
install -d -m 0750 %buildroot%_sysconfdir/caddy/Caddyfile.d

# systemd units
install -D -p -m 0644 %SOURCE2 %buildroot%_unitdir/caddy.service
install -D -p -m 0644 %SOURCE3 %buildroot%_unitdir/caddy-api.service

# data directory
install -d -m 0750 %buildroot%_sharedstatedir/caddy

# welcome page
install -D -p -m 0644 %SOURCE4 %buildroot%webserver_htdocsdir/index.html

# shell completion
install -D -p -m 0644 %SOURCE5 %buildroot%_datadir/bash-completion/completions/caddy
install -D -p -m 0644 %SOURCE6 %buildroot%_datadir/zsh/site-functions/_caddy

%pre
groupadd -r -f %caddy_group 2>/dev/null ||:
useradd -r -N -g %caddy_group -G %webserver_group -c 'Caddy web server' \
        -s /sbin/nologin -M -d %_sharedstatedir/%name %caddy_user 2>/dev/null ||:

%post
%post_systemd_postponed %name

%preun
%preun_systemd %name

%files
%doc AUTHORS LICENSE README.md
%_bindir/caddy
%_unitdir/caddy.service
%_unitdir/caddy-api.service
%attr(0750,root,%caddy_group) %dir %_sysconfdir/caddy
%attr(0750,root,%caddy_group) %dir %_sysconfdir/caddy/Caddyfile.d
%attr(0644,root,%caddy_group) %config(noreplace) %_sysconfdir/caddy/Caddyfile
%attr(1770,root,%caddy_group) %dir %_sharedstatedir/caddy
%webserver_htdocsdir/index.html
%_datadir/bash-completion/completions/caddy
%_datadir/zsh/site-functions/_caddy

%changelog
* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 2.6.2-alt1
- new version 2.6.2

* Thu May 12 2022 Alexey Shabalin <shaba@altlinux.org> 2.5.1-alt1
- new version 2.5.1

* Thu Nov 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.6-alt1
- new version 2.4.6

* Mon Oct 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.5-alt2
- Rebuild with updated systemd macros.

* Sun Sep 05 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.5-alt1
- new version 2.4.5

* Wed Feb 17 2021 Alexey Shabalin <shaba@altlinux.org> 2.3.0-alt1
- Initial Caddy v2 package

