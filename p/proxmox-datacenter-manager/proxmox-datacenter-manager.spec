%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name:    proxmox-datacenter-manager
Version: 0.9.1
Release: alt1
License: AGPL-3.0
Summary: Manage multiple Proxmox VE cluster and other Proxmox projects
Group:   System/Servers
Url:     https://github.com/proxmox/proxmox-datacenter-manager
Vcs:     git://git.proxmox.com/git/proxmox-datacenter-manager.git

ExclusiveArch: x86_64 aarch64
Source:   %name-%version.tar

# Git submodule
Source12: pwt-assets.tar

Source13: basealt_logo.png
Source14: basealt_favicon.ico
Source15: basealt_logo-128.png

# PAM config for PDM authentication
Source16: proxmox-datacenter-auth

BuildRequires(pre): rpm-macros-rust rpm-macros-systemd
BuildRequires: rpm-build-rust clang-devel rust
BuildRequires: openssl-devel
BuildRequires: git rust-wasm32-unknown-unknown-target
BuildRequires: libapt-devel gcc-c++
BuildRequires: libudev-devel libssl-devel libacl-devel libsystemd-devel libpam-devel libfuse3-devel libuuid-devel
BuildRequires: lld20.1

Requires: proxmox-mini-journalreader
Requires: pve-xtermjs
Requires: proxmox-acme

%description
This package provides the API daemons of the Proxmox Datacenter Manager (PDM)
which allows one to add multiple Proxmox VE and Proxmox Backup Server
instances to manage them centrally.

%package client
Summary: CLI Client for the Proxmox Datacenter Manager
Group: System/Servers

%description client
This package provides the CLI client that can interface with a Proxmox
Datacenter Manager (PDM) instance.

%package ui
Summary: Web UI to for the Proxmox Datacenter Manager
Group: System/Servers
BuildRequires: esbuild
BuildRequires: grass-sass
BuildRequires: proxmox-wasm-builder
BuildRequires: fonts-font-awesome

Requires: pve-xtermjs
Requires: fonts-font-awesome 
Requires: pdm-i18n

%description ui
This package provides the web UI of the Proxmox Datacenter Manager (PDM)
which allows one to add multiple Proxmox VE and Proxmox Backup Server
remotes and to manage these remotes from a central UI.

%prep
%setup -q

tar -xf %SOURCE12 -C ui/pwt-assets

%build
%make_build BUILD_MODE=release
%make_build -C ui BUILD_MODE=release

%install
export BUILD_MODE=release
%makeinstall_std
%makeinstall_std -C ui

install -d %buildroot%_sysconfdir/pam.d
install -m0644 %SOURCE13 %buildroot%_datadir/javascript/%name/images/basealt_logo.png
install -m0644 %SOURCE14 %buildroot%_datadir/javascript/%name/images/favicon.ico
install -m0644 %SOURCE15 %buildroot%_datadir/javascript/%name/images/logo-128.png

install -m0644 %SOURCE16 %buildroot%_sysconfdir/pam.d/proxmox-datacenter-auth

# Cleanup
rm -f %buildroot%_unitdir/%name-banner.service
rm -f %buildroot%_unitdir/%name-daily-update.service
rm -f %buildroot%_unitdir/%name-daily-update.timer
      
%post
%post_systemd_postponed proxmox-datacenter-api.service proxmox-datacenter-privileged-api.service

%preun
%preun_systemd proxmox-datacenter-api.service proxmox-datacenter-privileged-api.service

%pre
%_sbindir/groupadd -r -f www-data 2>/dev/null ||:
%_sbindir/useradd -c 'www-data' -d /var/www -s '/sbin/nologin' -r -M www-data 2>/dev/null || :

%files
%doc debian/copyright
%_unitdir/proxmox-datacenter-api.service
%_unitdir/proxmox-datacenter-privileged-api.service
%_sbindir/%name-admin
%_sbindir/pdmAtoB
%_datadir/bash-completion/completions/%name-admin.bc
%_datadir/zsh/vendor-completions/_%name-admin
%_datadir/bash-completion/completions/proxmox-datacenter-api.bc
%_datadir/bash-completion/completions/proxmox-datacenter-privileged-api.bc
%_datadir/bash-completion/completions/pdmAtoB.bc
%_datadir/zsh/vendor-completions/_proxmox-datacenter-api
%_datadir/zsh/vendor-completions/_proxmox-datacenter-privileged-api
%_datadir/zsh/vendor-completions/_pdmAtoB
%_libexecdir/proxmox/*
%config(noreplace) %_sysconfdir/pam.d/proxmox-datacenter-auth

%files client
%_bindir/%name-client
%_datadir/bash-completion/completions/%name-client.bc
%_datadir/zsh/vendor-completions/_%name-client

%files ui
%doc debian/copyright
%_datadir/javascript/%name/

%changelog
* Thu Oct 16 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 0.9.1-alt1
- 0.9.1
- Provide PAM config for PDM authentication
- Disable symlink follow in fchownat
- Fix FIDO2 bindings to use libc::c_char
- Replace Proxmox branding with BaseALT assets
- Update links to BaseALT in ui
- Use grass instead of rust-grass in ui/Makefile
