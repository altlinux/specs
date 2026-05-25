%define _unpackaged_files_terminate_build 1
%global import_path github.com/oauth2-proxy/oauth2-proxy

Name: oauth2-proxy
Version: 7.15.2
Release: alt1

Group: Security/Networking
Summary: OAuth2 Proxy for authentication
License: MIT
Url: https://oauth2-proxy.github.io/oauth2-proxy
Vcs: https://%import_path.git
Source0: %name-%version.tar
Source1: vendor-%version.tar
Source2: README.ALT

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.9

%description
A reverse proxy and static file server that provides authentication using Providers (Google,
Keycloak, GitHub and others) to validate accounts by email, domain or group.

%prep
%setup -a 1
cp -a %SOURCE2 .
sed -i 's|^WorkingDirectory=.*|WorkingDirectory=/var/lib/oauth2-proxy|g' contrib/oauth2-proxy.service.example

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-X github.com/oauth2-proxy/oauth2-proxy/v7/pkg/version.VERSION=%version"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot{%_datadir/bash-completion/completions,%_unitdir,{%_sysconfdir,%_localstatedir}/%name}

install -m0644 contrib/%name.service.example %buildroot%_unitdir/%name.service
install -m0644 contrib/%name.cfg.example %buildroot%_sysconfdir/%name/%name.cfg
install -m0644 contrib/%{name}_autocomplete.sh %buildroot%_datadir/bash-completion/completions/%name

%check
export LDFLAGS="-X github.com/oauth2-proxy/oauth2-proxy/v7/pkg/version.VERSION=%version"
%gotest

%pre
groupadd -r -f %name > /dev/null 2>&1 ||:
useradd -r -g %name -d %_localstatedir/%name -M -s /dev/null -c "oauth2-proxy service" %name > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name
%files
%doc *.md LICENSE README.ALT
%_bindir/*
%_datadir/bash-completion/completions/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/%name/*
%dir %attr(750, root, %name) %_localstatedir/%name

%changelog
* Fri May 22 2026 Artyom Sinyugin <writers@altlinux.org> 7.15.2-alt1
- New version 7.15.2.
- Added support for trusted reverse proxy IPs via --trusted-proxy-ip.
- Added --config-test option for configuration validation.
- Added OIDC JWT signing algorithm allow-list, CSRF SameSite option and Unix socket mode support.
- Tighten /var/lib/oauth2-proxy directory permissions from 755 to 750.

* Fri Jan 23 2026 Artyom Sinyugin <writers@altlinux.org> 7.14.2-alt1
- New version 7.14.2.

* Thu Sep 11 2025 Artyom Sinyugin <writers@altlinux.org> 7.12.0-alt2
- oauth2-proxy service was added (ALT#54460).
- autocomplete file was added.

* Thu Aug 28 2025 Artyom Sinyugin <writers@altlinux.org> 7.12.0-alt1
- New version 7.12.0.

* Thu Jan 20 2024 Artyom Sinyugin <writers@altlinux.org> 7.8.1-alt1
- Initial build.
