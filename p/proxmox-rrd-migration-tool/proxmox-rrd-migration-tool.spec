%define _unpackaged_files_terminate_build 1
%define libexecdir /usr/libexec
%define service_name proxmox-rrd-migration

Name: proxmox-rrd-migration-tool
Summary: Migrate Proxmox VE RRD metrics to new version format.
Version: 1.0.5
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://git.proxmox.com/

ExclusiveArch: x86_64 aarch64 loongarch64

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: rpm-build-rust clang-devel librrd-devel
# Required to run tests in %check
BuildRequires: faketime rrd-utils

%description
Migrate Proxmox VE RRD metrics to new version format.
Tool to migrate rrd-tools backed RRD files from previous format versions to
newer ones, e.g. for adding columns or making them more granular, like it was
done for Proxmox VE 9.0.


%prep
%setup
%patch -p1

%build
export BUILD_MODE=release
%make cargo-build

%install
export BUILD_MODE=release
%makeinstall_std
install -pD -m644 debian/%service_name.service %buildroot%systemd_unitdir/%service_name.service

%check
export BUILD_MODE=release
%make check

%post
%post_systemd_postponed %service_name

%preun
%preun_systemd %service_name

%files
%doc debian/copyright
%systemd_unitdir/%service_name.service
%libexecdir/proxmox/%name

%changelog
* Fri Aug 22 2025 Sergey Konev <darisishe@altlinux.org> 1.0.5-alt1
- Initial Build 
