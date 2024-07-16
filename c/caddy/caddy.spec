%global import_path github.com/caddyserver/caddy
%global _unpackaged_files_terminate_build 1

%define caddy_user _caddy
%define caddy_group _caddy

Name: caddy
Version: 2.8.4
Release: alt2
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

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang rpm-macros-webserver-common rpm-macros-systemd >= 5
BuildRequires: rpm-build-golang golang >= 1.21.0

Provides: webserver

%description
Caddy is the web server with automatic HTTPS.

%prep
# Vendorized go modules
# $ GO111MODULE=on go mod vendor -v
# $ git add -f vendor
# $ git commit -m "update go vendor modules by go mod vendor"

%setup
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/caddyserver/caddy/v2.CustomVersion=v%version"

%golang_prepare
export CGO_ENABLED=0
%golang_build cmd/caddy

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"
export IGNORE_SOURCES=1

%golang_install

# command
#install -D -p -m 0755 caddy %buildroot%_bindir/caddy

# man pages
mkdir -p %buildroot%_man8dir
%buildroot%_bindir/%name manpage --directory %buildroot%_man8dir

# config
install -D -p -m 0640 %SOURCE1 %buildroot%_sysconfdir/%name/Caddyfile
install -d -m 0750 %buildroot%_sysconfdir/%name/Caddyfile.d

# systemd units
install -D -p -m 0644 %SOURCE2 %buildroot%_unitdir/caddy.service
install -D -p -m 0644 %SOURCE3 %buildroot%_unitdir/caddy-api.service

# data directory
install -d -m 0750 %buildroot%_sharedstatedir/%name

# welcome page
install -D -p -m 0644 %SOURCE4 %buildroot%webserver_datadir/%name/index.html

# shell completion
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
# ensure that the version was embedded correctly
[[ "$(%buildroot%_bindir/%name version)" == "v%{version}" ]] || exit 1
 
# run the upstream tests
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
cd $BUILDDIR/src/%import_path
%gotest ./...

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
%_bindir/%name
%_man8dir/caddy*.8*
%_unitdir/*.service
%attr(0750,root,%caddy_group) %dir %_sysconfdir/%name
%attr(0750,root,%caddy_group) %dir %_sysconfdir/%name/Caddyfile.d
%attr(0644,root,%caddy_group) %config(noreplace) %_sysconfdir/%name/Caddyfile
%attr(1770,root,%caddy_group) %dir %_sharedstatedir/%name
%config(noreplace) %webserver_datadir/%name/index.html
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue Jul 16 2024 Alexey Shabalin <shaba@altlinux.org> 2.8.4-alt2
- fix add user

* Fri Jul 05 2024 Alexey Shabalin <shaba@altlinux.org> 2.8.4-alt1
- New version 2.8.4.

* Mon Dec 11 2023 Alexey Shabalin <shaba@altlinux.org> 2.7.6-alt1
- New version 2.7.6.

* Thu Oct 19 2023 Alexey Shabalin <shaba@altlinux.org> 2.7.5-alt1
- New version 2.7.5.

* Fri Aug 18 2023 Alexey Shabalin <shaba@altlinux.org> 2.7.4-alt1
- New version 2.7.4.

* Tue Aug 08 2023 Alexey Shabalin <shaba@altlinux.org> 2.7.3-alt1
- New version 2.7.3.

* Sun Mar 26 2023 Alexey Shabalin <shaba@altlinux.org> 2.6.4-alt2
- fix version info

* Mon Feb 20 2023 Alexey Shabalin <shaba@altlinux.org> 2.6.4-alt1
- new version 2.6.4

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

