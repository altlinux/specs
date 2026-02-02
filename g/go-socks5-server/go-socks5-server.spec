%define _unpackaged_files_terminate_build 1

Name: go-socks5-server
Version: 1.2.1
Release: alt1

Summary: Primitive but modern SOCKS5 proxy server
License: GPL-3.0
Group: System/Servers
Url: https://github.com/foi/go-socks5-server
Vcs: https://github.com/foi/go-socks5-server.git

# Source-url: https://github.com/foi/go-socks5-server/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: /proc

%description
A primitive but modern SOCKS5 proxy server written in Go.
Authorization uses a JSON configuration file rather than Linux PAM.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="github.com/foi/go-socks5-server"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="github.com/foi/go-socks5-server"
export IGNORE_SOURCES=1
%golang_install

install -Dpm644 %name.service %buildroot%_unitdir/%name.service
install -Dpm644 %name.config.json.example %buildroot%_sysconfdir/%name.config.json
install -Dpm644 sysusers.conf %buildroot%_sysusersdir/%name.conf

%pre
%sysusers_create_package %name sysusers.conf

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE CHANGES
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%config(noreplace) %_sysconfdir/%name.config.json

%changelog
* Mon Feb 02 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Sisyphus
