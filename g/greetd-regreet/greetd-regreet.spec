Name: greetd-regreet
Version: 0.2.0
Release: alt1
License: GPL-3.0

Summary: Clean and customizable greeter for greetd

Group: Graphical desktop/Other

Url: https://github.com/rharish101/ReGreet
Vcs: https://github.com/rharish101/ReGreet.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)

Requires: greetd cage

Provides: greetd-greeter

%description
A clean and customizable GTK-based greetd greeter
written in Rust using Relm4. 
This is meant to be run under a Wayland compositor.

It is based on Max Moser's LightDM Elephant greeter,
which is based on Matt Shultz's Fischer's example LightDM greeter.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export REBOOT_CMD="systemctl reboot"
export POWEROFF_CMD="systemctl poweroff"
%rust_build --all-features

%install
install -Dm 755 target/release/regreet \
    %buildroot%_bindir/regreet

install -vD %SOURCE2 %buildroot%_sysconfdir/greetd/greeters/regreet.toml

mkdir -p %buildroot%_altdir
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/regreet.toml 40" \
	> %buildroot%_altdir/greetd-regreet

%files
%doc regreet.sample.toml README.md
%_bindir/regreet
%_altdir/greetd-regreet
%config(noreplace) %_sysconfdir/greetd/greeters/regreet.toml

%changelog
* Mon Mar 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- Initial build
