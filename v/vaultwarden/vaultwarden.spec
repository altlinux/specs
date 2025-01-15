%def_without check

Name:    vaultwarden
Version: 1.32.0
Release: alt4

Summary: Unofficial Bitwarden compatible server
License: AGPL-3.0
Group:   Security/Networking
Url:     https://github.com/dani-garcia/vaultwarden

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name.cfg
Source3: %name.service
Source4: %name.sysusers

Patch0: vaultwarden-1.32.0-alt-mysqlclient-crate-loongarch64.patch

# 32bit incompatible, unable to build vendored mysqlclient-sys on ppc
ExcludeArch: %ix86 armh ppc64le

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(mariadb)
BuildRequires: pkgconfig(libpq)
%ifarch loongarch64
BuildRequires: llvm17.0 libclang17 rustfmt rust-bindgen
%endif

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
%ifarch loongarch64
%patch0 -p2
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
     ./vendor/mysqlclient-sys/.cargo-checksum.json
bindgen --allowlist-function "mysql.*" --allowlist-function "mariadb.*" --allowlist-type "MYSQL.*" --allowlist-type "MARIADB.*" \
 		--allowlist-type "mysql.*" --allowlist-type "mariadb.*" --allowlist-var "MYSQL.*" --allowlist-var "MARIADB.*" \
 		--default-enum-style rust_non_exhaustive vendor/mysqlclient-sys/bindings/wrapper.h -- -I/usr/include/mysql \
 		-I/usr/lib/llvm-17.0/lib64/clang/17/include/ > ./vendor/mysqlclient-sys/bindings/bindings_mariadb_11_4_loongarch64_linux.rs
%endif

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
%sysusers_create_package %name %SOURCE4
echo "Database for %{name} configured by default to use SQLite"
echo "placed in %{_sharedstatedir}/%{name}/data and owned by %{name}."
echo "To use PostgreSQL or MySQL uncomment and edit DATABASE_URL variable"
echo "in %{_sysconfdir}/%{name}/%{name}.cfg"

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
* Wed Jan 15 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.32.0-alt4
- Configure SQLite as default database (Closes #52663).

* Fri Dec 27 2024 Ilya Sorochan <k0tran@altlinux.org> 1.32.0-alt3
- Add bindings generation for loongarch64 for mysqlclient-sys crate.

* Thu Dec 12 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.32.0-alt2
- Added WebUI settings and requirement (Closes #51500).

* Tue Sep 17 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.32.0-alt1
- Initial build for Sisyphus
