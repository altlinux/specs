%global _unpackaged_files_terminate_build 1
%global import_path github.com/AdguardTeam/AdGuardHome

Name: adguardhome
Version: 0.107.50
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
# git add vendor -f && git commit -m "Updated go vendor modules."
# npm --prefix client ci
# git add client/node_modules -f && git commit -m "Updated node modules."
%setup -a 1 -a 2

%build
export GO111MODULE=on
export GOTOOLCHAIN=local
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export NODE_OPTIONS=--openssl-legacy-provider

# build web
cp %SOURCE3 $PWD
npm --prefix client run build-prod

# build bin
%golang_prepare
cd .gopath/src/%import_path
go build --ldflags "-w \
         -X %import_path/internal/version.version=%version \
         -X %import_path/internal/version.channel=release" \
         --race=0 --tags= --trimpath -o=%name -v=0 -x=0

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_sysconfdir \
         %buildroot%_localstatedir/%name
install -m 0755 .gopath/src/%import_path/%name %buildroot%_bindir/%name
install -m 0644 %SOURCE4 %buildroot%_unitdir/%name.service
touch %buildroot%_sysconfdir/%name.yaml

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_localstatedir/%name
%_unitdir/%name.service
%ghost %config(noreplace) %_sysconfdir/%name.yaml

%changelog
* Wed May 29 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.107.50-alt1
- Updated to version 0.107.50.

* Thu May 23 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.107.49-alt1
- Updated to version 0.107.49.

* Fri May 17 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.107.48-alt1
- Updated to version 0.107.48.

* Wed Mar 06 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.45-alt1
- Updated to version 0.107.45.

* Wed Feb 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.44-alt1
- Updated to version 0.107.44.
- Fixed version show.

* Sun Feb 04 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.107.43-alt1
- Initial build for ALT.

