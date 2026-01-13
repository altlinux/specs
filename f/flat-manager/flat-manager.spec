%define _unpackaged_files_terminate_build 1

Name: flat-manager
Version: 0.4.6
Release: alt3

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

Requires: python3(packaging)

%description client
%summary.

%prep
%setup -a10
%autopatch -p1
%rust_prep

%build
%rust_build

%install
%rust_install %name gentoken delta-generator-client
install -m755 -D %name-client %buildroot/%_bindir/%name-client
install -m644 -D %SOURCE11 %buildroot/%_unitdir/%name.service
install -m644 -D %SOURCE12 %buildroot/%_sysusersdir/%name.conf
install -m644 -D %SOURCE13 %buildroot/%_tmpfilesdir/%name.conf

%check
%rust_test

%pre
%sysusers_create_package %name %name.sysusers

%files
%_bindir/%name
%_bindir/gentoken
%_bindir/delta-generator-client
%_unitdir/%name.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%doc README.md example-config.json example.env

%files client
%_bindir/%name-client

%changelog
* Sat Jan 10 2026 Vladimir Romanov <rirusha@altlinux.org> 0.4.6-alt3
- Fixed sysusers and tmpfiles filenames.

* Sat Dec 13 2025 Vladimir Romanov <rirusha@altlinux.org> 0.4.6-alt2
- Added gentoken with delta-generator-client bins.
- Fixed flat-manager-client python3(packaging) missing require.

* Wed Dec 03 2025 Vladimir Romanov <rirusha@altlinux.org> 0.4.6-alt1
- Initial build.
