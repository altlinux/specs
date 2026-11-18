%global import_path github.com/smallstep/certificates

Name: step-ca
Version: 0.30.2
Release: alt1

Summary: Online certificate authority for secure automated certificate management
License: Apache-2.0
Group: Networking/Other

Url: https://smallstep.com/docs/step-ca
Vcs: https://github.com/smallstep/certificates

Source0: %name-%version.tar
Source1: vendor.tar
Source2: step-ca.sysusers
Source3: step-ca.tmpfiles
Source4: README.ALT
Source5: step-ca-init
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: libpcsclite-devel
Requires: /usr/bin/step-cli

ExclusiveArch: %go_arches
ExcludeArch: %ix86

%description
step-ca is an online certificate authority for secure, automated certificate
management. It supports X.509 and SSH certificates as well as the ACME, SCEP
and OIDC provisioning protocols.

%prep
%setup -a 1
%autopatch -p1
cp -p %SOURCE4 README.ALT

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -X main.Version=%version"
%golang_prepare
%golang_build cmd/step-ca

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IGNORE_SOURCES=1
%golang_install

install -Dm644 systemd/%name.service %buildroot%_unitdir/%name.service
install -Dm644 %SOURCE2 %buildroot%_sysusersdir/%name.conf
install -Dm644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf
install -Dm750 %SOURCE5 %buildroot%_sbindir/%name-init

mkdir -p %buildroot%_sysconfdir/%name/config
mkdir -p %buildroot%_localstatedir/%name/db

%pre
%sysusers_create_package %name %SOURCE2

%post
%tmpfiles_create_package %name %SOURCE3
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%attr(0750,root,step) %_sbindir/%name-init
%attr(0750, step, step) %dir %_sysconfdir/%name
%attr(0750, step, step) %dir %_sysconfdir/%name/config
%attr(0750, step, step) %dir %_localstatedir/%name
%attr(0700, step, step) %dir %_localstatedir/%name/db
%_unitdir/%name.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%doc README.md README.ALT LICENSE

%changelog
* Mon Oct 12 2026 Vladislav Tatjanin <l27001@altlinux.org> 0.30.2-alt1
- Initial build (ALT #60521).
