%global _unpackaged_files_terminate_build 1
%global import_path github.com/AdguardTeam/AdGuardHome
%define normalized_name adguardhome
%define original_name AdGuardHome

Name: %normalized_name
Version: 0.107.43
Release: alt1
Summary: Network-wide ads & trackers blocking DNS server
License: GPL-3.0
Group: System/Servers
Url: https://github.com/AdguardTeam/AdGuardHome
Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: .twosky.json
Source4: %name.service

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: npm
BuildRequires: node-cross-env
BuildRequires: node-cross-spawn

%description
Free and open source, powerful network-wide ads & trackers blocking DNS server.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Added go vendor modules."
# npm --prefix client ci
# git add client/node_modules -f && git commit -m "Added node modules."
%setup -a 1 -a 2

%build
export GO111MODULE=on
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export VERSION=%version
export NODE_OPTIONS=--openssl-legacy-provider

# build web
cp %SOURCE3 $PWD
npm --prefix client run build-prod

# build bin
%golang_prepare
cd .gopath/src/%import_path
%golang_build .

%install
export BUILDDIR=$PWD/.gopath
export IGNORE_SOURCES=1
%golang_install
ln -sv %original_name %buildroot%_bindir/%name
mkdir -p %buildroot%_unitdir \
         %buildroot%_sysconfdir \
         %buildroot%_localstatedir/%name
install -m 0644 %SOURCE4 %buildroot%_unitdir/%name.service
touch %buildroot%_sysconfdir/%name.yaml

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_bindir/%original_name
%_localstatedir/%name
%_unitdir/%name.service
%ghost %config(noreplace) %_sysconfdir/%name.yaml

%changelog
* Sun Feb 04 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.43-alt1
- Initial build for ALT.

