%global _unpackaged_files_terminate_build 1
%global import_path github.com/MizuchiLabs/mantrae

Name: mantrae
Version: 0.8.8
Release: alt1
Summary: Web UI for managing Traefik
License: MIT
Group: System/Servers
Url: https://mantrae.pages.dev
VCS: https://github.com/MizuchiLabs/mantrae

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: mantrae.sysconfig
Source4: mantrae.service

ExclusiveArch: x86_64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# temporary build with bundled esbuild
# BuildRequires: esbuild
BuildRequires: rollup-native
BuildRequires: npm

%description
A web-based configuration manager for Traefik's dynamic configuration file.
It provides a clean, intuitive interface to manage your routers, middleware,
and services without editing YAML or TOML files manually.

%prep
%setup -a 1 -a 2
ln -svf %_bindir/rollup web/ui/node_modules/.bin/rollup
# ln -sv %_bindir/esbuild web/ui

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export LDFLAGS='-X main.Version=%version'
# export ESBUILD_BINARY_PATH=$PWD/web/ui/esbuild

npm --prefix web/ui run build

%golang_prepare
%golang_build .

%install
install -Dm 0755 .gopath/bin/mantrae %buildroot%_bindir/mantrae
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/mantrae
install -Dm 0644 %SOURCE4 %buildroot%_unitdir/mantrae.service
mkdir -p %buildroot%_sharedstatedir/mantrae

%pre
%_sbindir/groupadd -r -f _mantrae
%_sbindir/useradd -r -g _mantrae -s /sbin/nologin \
                  -d %_sharedstatedir/mantrae _mantrae 2>/dev/null ||:

%post
%post_service mantrae

%preun
%preun_service mantrae

%files
%_bindir/mantrae
%_unitdir/mantrae.service
%config(noreplace) %_sysconfdir/sysconfig/mantrae
%dir %attr(750, _mantrae, _mantrae) %_sharedstatedir/mantrae
%doc LICENSE

%changelog
* Sun Mar 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.8-alt1
- Initial build for ALT.
