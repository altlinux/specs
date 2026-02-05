%def_without check

Name:    vaultwarden_ldap
Version: 2.2.0
Release: alt2

Summary: Automate LDAP invites to Vaultwarden
License: GPLv3+
Group:   Security/Networking
Url:     https://github.com/ViViDboarder/vaultwarden_ldap

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name.service

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(openssl)

%description
%summary.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

# It is assumed that the application will be installed on
# the same host as the server.
subst "s/vaultwarden:80/localhost:8000/g" ./example.config.toml

%build
%rust_build

%install
%rust_install
install -d %buildroot%_sysconfdir/vaultwarden
install -m644 ./example.config.toml \
%buildroot%_sysconfdir/vaultwarden/config.toml
install -Dp %SOURCE2 %buildroot%_unitdir/%name.service

%check
%rust_test --workspace

%pre
if [ $1 -eq 1 ]; then
    echo "Please configure service to communicate with vaultwarden."
    echo "By default it connected to localhost:8000"
    echo "and uses token from vaultwarden_admin_token value"
    echo "in %{_sysconfdir}/vaultwarden/config.toml."
fi

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc *.md
%_bindir/%name
%_sysconfdir/vaultwarden/config.toml
%_unitdir/%name.service

%changelog
* Thu Feb 05 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.2.0-alt2
- Added systemd unit and configuration file installation (Closes #57758).

* Wed Jan 21 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
