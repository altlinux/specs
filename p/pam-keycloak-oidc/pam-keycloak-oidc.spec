%global import_path github.com/zhaow-de/pam-keycloak-oidc
Name:    pam-keycloak-oidc
Version: 1.1.5
Release: alt1

Summary: PAM module connecting to Keycloak for user authentication using OpenID Connect/OAuth2, with MFA/2FA/TOTP support
License: MIT
Group:   Other
Url:     https://github.com/zhaow-de/pam-keycloak-oidc

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar
Source2: pam-keycloak-oidc.tml
Patch0: alt-config-path.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
PAM module connecting to Keycloak for user authentication using OpenID Connect
protocol, MFA (Multi-Factor Authentication) or TOTP (Time-based One-time
Password) is supported.

%prep
%setup
%patch0 -p1
tar xf %SOURCE1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dpm 0640 %SOURCE2 %buildroot%_sysconfdir/security/pam-keycloak-oidc.tml

%files
%doc README.md
%config(noreplace) %_sysconfdir/security/pam-keycloak-oidc.tml
%_bindir/*

%changelog
* Tue Jun 25 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus
