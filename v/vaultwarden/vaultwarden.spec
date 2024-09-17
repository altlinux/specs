%def_without check

Name:    vaultwarden
Version: 1.32.0
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

ExcludeArch: %ix86 armh ppc64le

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(mariadb)
BuildRequires: pkgconfig(libpq)

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
install -d %buildroot%_sharedstatedir/%name
install -d %buildroot%_runtimedir/%name

%check
%rust_test

%pre
%sysusers_create_package %name %SOURCE4

%post
if test ! -d %_sharedstatedir/%name/data; then
    echo "Database for %{name} did not configured."
    echo "To use SQLite create %{_sharedstatedir}/%{name}/data, owned by"
    echo "%{name} and fill DATABASE_URL variable in"
    echo "%{_sysconfdir}/%{name}/%{name}.cfg"
    echo "Or uncomment and edit DATABASE_URL for MySQL or PostgreSQL."
fi
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
%dir %attr(0755, %name, %name) %ghost %_runtimedir/%name

%changelog
* Tue Sep 17 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.32.0-alt1
- Initial build for Sisyphus
