%def_without check

Name:    vaultwarden
Version: 1.36.0
Release: alt1

Summary: Unofficial Bitwarden compatible server
License: AGPL-3.0
Group:   Security/Networking
Url:     https://github.com/dani-garcia/vaultwarden

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name.cfg
Source3: %name.service
Source4: %name.sysusers

# 32bit incompatible, unable to build vendored mysqlclient-sys on ppc
ExcludeArch: %ix86 armh ppc64le

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(mariadb)
BuildRequires: pkgconfig(libpq)
# Uncomment req below to vendor dependencies inside chrooted env correctly.
# BuildRequires: cargo-vendor-filterer

Requires: %name-web

%description
Unofficial Bitwarden compatible server written in Rust,
formerly known as bitwarden_rs.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build --features sqlite,mysql,postgresql

%install
%rust_install
install -Dm 0644 %SOURCE2 %buildroot%_sysconfdir/%name/%name.cfg
install -Dp %SOURCE3 %buildroot%_unitdir/%name.service
install -Dp %SOURCE4 %buildroot%_sysusersdir/%name.conf
install -d %buildroot%_sharedstatedir/%name/data
install -d %buildroot%_runtimedir/%name

%check
%rust_test

%pre
if [ $1 -eq 1 ]; then
    %sysusers_create_package %name %SOURCE4
    echo "Database for %{name} configured by default to use SQLite"
    echo "placed in %{_sharedstatedir}/%{name}/data and owned by %{name}."
    echo "To use PostgreSQL or MySQL uncomment and edit DATABASE_URL variable"
    echo "in %{_sysconfdir}/%{name}/%{name}.cfg"
fi

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc *.md LICENSE.txt
%_bindir/%name
%_sysconfdir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.cfg
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %attr(0750, %name, %name) %_sharedstatedir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name/data
%dir %attr(0755, %name, %name) %ghost %_runtimedir/%name

%changelog
* Thu May 07 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.36.0-alt1
- New version.

* Mon Apr 13 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.35.6-alt1
- New version.

* Wed Feb 25 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.35.4-alt1
- New version.

* Wed Feb 11 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.35.3-alt1
- New version.

* Mon Jan 12 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.35.2-alt1
- New version.

* Mon Dec 29 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.35.0-alt1
- New version.

* Fri Sep 12 2025 Ilya Sorochan <k0tran@altlinux.org> 1.34.2-alt2
- Remove obsolete loongarch64 patch for mysqlclient-sys crate.

* Tue Jul 29 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.34.2-alt1
- New version.

* Tue May 27 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.34.1-alt1
- New version.

* Fri Feb 14 2025 Ilya Sorochan <k0tran@altlinux.org> 1.33.2-alt2
- Fix loongarch64 patch for mysqlclient-sys crate.

* Tue Feb 11 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.33.2-alt1
- New version.

* Fri Jan 31 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.33.0-alt1
- New version.

* Wed Jan 15 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.32.0-alt4
- Configure SQLite as default database (Closes #52663).

* Fri Dec 27 2024 Ilya Sorochan <k0tran@altlinux.org> 1.32.0-alt3
- Add bindings generation for loongarch64 for mysqlclient-sys crate.

* Thu Dec 12 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.32.0-alt2
- Added WebUI settings and requirement (Closes #51500).

* Tue Sep 17 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.32.0-alt1
- Initial build for Sisyphus
