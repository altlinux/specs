%global _unpackaged_files_terminate_build 1
%global import_path github.com/rcourtman/pulse-go-rewrite

Name: pulse
Version: 4.14.0
Release: alt1
Summary: A responsive monitoring application for Proxmox VE
License: MIT
Group: Monitoring
Url: https://github.com/rcourtman/Pulse

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: %name.service
Source4: %name.sysconfig

# native rollup js bundler is needed to build
ExclusiveArch: x86_64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: npm

%description
Real-time monitoring for Proxmox VE and PBS with alerts and webhooks.
Monitor your entire Proxmox infrastructure from a single dashboard.
Get instant alerts when nodes go down, backups fail, or storage
fills up. Supports email, Discord, Slack, Telegram, and more.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
# npm --prefix frontend-modern install
# git add frontend-modern/node_modules -f && git commit -m "Updated node modules."
%setup -a 1 -a 2

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
npm --prefix frontend-modern run build
cp -r frontend-modern internal/api
%golang_prepare
go build --ldflags "-X main.Version=v%version" -o %name ./cmd/pulse

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_sysconfdir/%name \
         %buildroot%_sysconfdir/sysconfig
install -m 0755 pulse %buildroot%_bindir/%name
install -m 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%name

%pre
%_sbindir/groupadd -r -f _%name
%_sbindir/useradd -r -g _%name -s /sbin/nologin _%name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(0770, root, _%name) %_sysconfdir/%name
%doc LICENSE

%changelog
* Wed Sep 24 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.14.0-alt1
- Initial build for ALT.
