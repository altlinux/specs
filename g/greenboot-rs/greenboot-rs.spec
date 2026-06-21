%define _unpackaged_files_terminate_build 1
%define pkgname greenboot
%define _libexecdir %_usr/libexec

Name:    greenboot-rs
Version: 0.16.3
Release: alt1

Summary: Generic Health Check Framework for systemd
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/fedora-iot/greenboot-rs

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
%summary.

%package -n %pkgname
Summary:	%summary
Group:      Other
Requires:	systemd >= 240
Requires:	pam >= 1.4.0

%description -n %pkgname
%summary.

	
%package -n %pkgname-default-health-checks
Summary:	Series of optional and curated health checks
Group:      Other
License:	BSD-3-Clause
Requires:	%pkgname = %{version}-%{release}
Requires:	util-linux
Requires:	jq
 
%description -n %pkgname-default-health-checks
%summary.
 
This package adds some default healthchecks for greenboot.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
%rust_build

%install
mkdir -p %buildroot%_libexecdir
mkdir -p %buildroot%_libexecdir/%pkgname
install -Dpm0755 target/release/greenboot %buildroot%_libexecdir/%pkgname/%pkgname
install -Dpm0644 -t %buildroot%_unitdir usr/lib/systemd/system/*.service
install -Dpm0644 -t %buildroot%_unitdir usr/lib/systemd/system/*.target
mkdir -p %buildroot%_exec_prefix/lib/motd.d/
mkdir -p %buildroot%_libexecdir/%pkgname
install -Dpm0644 -t %buildroot%_sysconfdir/%pkgname etc/greenboot/greenboot.conf
install -D -t %buildroot%_prefix/lib/bootupd/grub2-static/configs.d grub2/08_greenboot.cfg
mkdir -p %buildroot%_sysconfdir/%pkgname/check/required.d
mkdir    %buildroot%_sysconfdir/%pkgname/check/wanted.d
mkdir    %buildroot%_sysconfdir/%pkgname/green.d
mkdir    %buildroot%_sysconfdir/%pkgname/red.d
mkdir -p %buildroot%_prefix/lib/%pkgname/check/required.d
mkdir    %buildroot%_prefix/lib/%pkgname/check/wanted.d
mkdir    %buildroot%_prefix/lib/%pkgname/green.d
mkdir    %buildroot%_prefix/lib/%pkgname/red.d
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_tmpfilesdir
install -DpZm 0755 usr/lib/greenboot/check/required.d/* %buildroot%_prefix/lib/%pkgname/check/required.d
install -DpZm 0755 usr/lib/greenboot/check/wanted.d/* %buildroot%_prefix/lib/%pkgname/check/wanted.d
install -DpZm 0644 usr/lib/systemd/system/greenboot-healthcheck.service.d/10-network-online.conf %buildroot%_unitdir/greenboot-healthcheck.service.d/10-network-online.conf
	
%post -n %pkgname
%post_systemd greenboot-healthcheck.service
%post_systemd greenboot-set-rollback-trigger.service
%post_systemd greenboot-success.target
 
%preun -n %pkgname
%preun_systemd greenboot-healthcheck.service
%preun_systemd greenboot-set-rollback-trigger.service
%preun_systemd greenboot-success.target

%files -n %pkgname
%doc LICENSE README.md
%dir %_libexecdir/%pkgname
%_libexecdir/%pkgname/%pkgname
%_unitdir/greenboot-healthcheck.service
%_unitdir/greenboot-set-rollback-trigger.service
%_unitdir/greenboot-success.target
%config(noreplace) %_sysconfdir/%pkgname/greenboot.conf
%_prefix/lib/bootupd/grub2-static/configs.d/08_greenboot.cfg
%dir %_prefix/lib/%pkgname
%dir %_prefix/lib/%pkgname/check
%dir %_prefix/lib/%pkgname/check/required.d
%dir %_prefix/lib/%pkgname/check/wanted.d
%dir %_prefix/lib/%pkgname/green.d
%dir %_prefix/lib/%pkgname/red.d
%dir %_sysconfdir/%pkgname
%dir %_sysconfdir/%pkgname/check
%dir %_sysconfdir/%pkgname/check/required.d
%dir %_sysconfdir/%pkgname/check/wanted.d
%dir %_sysconfdir/%pkgname/green.d
%dir %_sysconfdir/%pkgname/red.d

%files -n %pkgname-default-health-checks
%dir %_unitdir/greenboot-healthcheck.service.d
%_prefix/lib/%pkgname/check/wanted.d/01_update_platforms_check.sh
%_prefix/lib/%pkgname/check/required.d/02_watchdog.sh
%_prefix/lib/%pkgname/check/required.d/01_repository_dns_check.sh
%_unitdir/greenboot-healthcheck.service.d/10-network-online.conf

%changelog
* Sun Jun 21 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.16.3-alt1
- Initial build.
