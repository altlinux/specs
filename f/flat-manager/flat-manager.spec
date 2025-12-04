%define _unpackaged_files_terminate_build 1

Name: flat-manager
Version: 0.4.6
Release: alt1

Summary: Manager for flatpak repositories
License: Apache-2.0 OR MIT
Group: Other
URL: https://github.com/flatpak/flat-manager
VCS: https://github.com/flatpak/flat-manager.git

Source: %name-%version.tar
Source10: vendor.tar
Source11: %name.service
Source12: %name.sysusers
Source13: %name.tmpfiles
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-python3
BuildRequires: rust-cargo
BuildRequires: pkgconfig(ostree-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libpq)

%description
flat-manager serves and maintains a Flatpak repository. You point it at an
ostree repository and it will allow Flatpak clients to install apps from the
repository over HTTP. Additionally, it has an HTTP API that lets you upload
new builds and manage the repository.

%package client
Summary: Client for %name
Group: Other

%description client
%summary.

%prep
%setup -a10
%autopatch -p1
%rust_prep

%build
%rust_build

%install
%rust_install
install -m755 -D %name-client %buildroot/%_bindir/%name-client
install -m644 -D %SOURCE11 %buildroot/%_unitdir/%name.service
install -m644 -D %SOURCE12 %buildroot/%_sysusersdir/%name.sysusers
install -m644 -D %SOURCE13 %buildroot/%_tmpfilesdir/%name.tmpfiles

%check
%rust_test

%pre
%sysusers_create_package %name %name.sysusers

%files
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.sysusers
%_tmpfilesdir/%name.tmpfiles
%doc README.md example-config.json example.env

%files client
%_bindir/%name-client

%changelog
* Wed Dec 03 2025 Vladimir Romanov <rirusha@altlinux.org> 0.4.6-alt1
- Initial build.
