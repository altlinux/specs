Name: greetd-regreet
Version: 0.2.0
Release: alt4
License: GPL-3.0

Summary: Clean and customizable greeter for greetd

Group: Graphical desktop/Other

Url: https://github.com/rharish101/ReGreet
Vcs: https://github.com/rharish101/ReGreet.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml
Source3: conf-sway
Source4: conf-hyprland
Source5: tmpfiles.conf

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)

Requires: greetd %name-config

Provides: greetd-greeter

%description
A clean and customizable GTK-based greetd greeter
written in Rust using Relm4. 
This is meant to be run under a Wayland compositor.

It is based on Max Moser's LightDM Elephant greeter,
which is based on Matt Shultz's Fischer's example LightDM greeter.

%package config-cage
Summary: Configuration for launching regreet with cage
Group: Graphical desktop/Other
BuildArch: noarch
Requires: %name
Provides: %name-config

%description config-cage
%summary.

%package config-sway
Summary: Configuration for launching regreet with Sway
Group: Graphical desktop/Other
BuildArch: noarch
Requires: %name
Provides: %name-config

%description config-sway
%summary.

%package config-hyprland
Summary: Configuration for launching regreet with Hyprland.
Group: Graphical desktop/Other
BuildArch: noarch
Requires: %name
Provides: %name-config

%description config-hyprland
%summary.

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

install -vD %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -vD %SOURCE2 %buildroot%_sysconfdir/greetd/greeters/regreet-cage.toml

# configs
install -vD %SOURCE3 %buildroot%_sysconfdir/greetd/regreet-conf-sway
install -vD %SOURCE4 %buildroot%_sysconfdir/greetd/regreet-conf-hyprland

for i in sway Hyprland; do
cat > %buildroot%_sysconfdir/greetd/greeters/regreet-${i,}.toml <<EOF
[terminal]
vt = 1

[default_session]
command = "$i -c %_sysconfdir/greetd/regreet-conf-${i,}"
user = "_greeter"
EOF
done

mkdir -p %buildroot%_altdir
# cage
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/regreet-cage.toml 40" \
	> %buildroot%_altdir/greetd-regreet-cage
# sway
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/regreet-sway.toml 41" \
	> %buildroot%_altdir/greetd-regreet-sway
# hyprland
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/regreet-hyprland.toml 42" \
	> %buildroot%_altdir/greetd-regreet-hyprland

%files
%doc regreet.sample.toml README.md
%_bindir/regreet
%_tmpfilesdir/%name.conf

%files config-cage
%_altdir/greetd-regreet-cage
%config(noreplace) %_sysconfdir/greetd/greeters/regreet-cage.toml

%files config-sway
%_altdir/greetd-regreet-sway
%config(noreplace) %_sysconfdir/greetd/greeters/regreet-sway.toml
%config(noreplace) %_sysconfdir/greetd/regreet-conf-sway

%files config-hyprland
%_altdir/greetd-regreet-hyprland
%config(noreplace) %_sysconfdir/greetd/greeters/regreet-hyprland.toml
%config(noreplace) %_sysconfdir/greetd/regreet-conf-hyprland

%changelog
* Sun Jun 29 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt4
- add tmpfiles config (ALT bug 54982)

* Sat Jun 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt3
- regreet-hyprland.toml: hyprland -> Hyprland (ALT bug 54975)

* Wed May 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt2
- add cage, hyprland and sway configs (ALT bug 54397)

* Mon Mar 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- Initial build
