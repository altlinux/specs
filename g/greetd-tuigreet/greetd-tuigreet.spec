Name: greetd-tuigreet
Version: 0.9.1
Release: alt1

Summary: Graphical console greeter for greetd
License: GPLv3
Group:   Graphical desktop/Other

URL: https://github.com/apognu/tuigreet
VCS: https://github.com/apognu/tuigreet.git

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

Requires: greetd

Provides: greetd-greeter

%description
A graphical TUI-like greeter for greetd display manager. tuigreet offers
user-friendly terminal expirience with keyboard navigation, wayland support
combined with power and sessions management.

%prep
%setup -a1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build
cat > config.toml <<EOF
[terminal]
vt = 1

[default_session]
command = "tuigreet --power-shutdown 'systemctl poweroff' --power-reboot 'systemctl reboot'"
user = "_greeter"
EOF

%install
install -Dm755 target/release/tuigreet %buildroot%_bindir/tuigreet
install -Dm644 config.toml %buildroot%_sysconfdir/greetd/greeters/tuigreet.toml
mkdir -p %buildroot%_altdir
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/tuigreet.toml 80" \
	> %buildroot%_altdir/greetd-tuigreet
mkdir -p %buildroot%_cachedir/tuigreet

%check
%rust_test

%files
%doc README.md LICENSE
%_bindir/tuigreet
%_altdir/greetd-tuigreet
%dir %attr(750,_greeter,_greeter) %_cachedir/tuigreet
%config(noreplace) %_sysconfdir/greetd/greeters/tuigreet.toml

%changelog
* Fri Nov 07 2025 Ilya Sorochan <k0tran@altlinux.org> 0.9.1-alt1
- Initial build.
