# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    gtkgreet
Version: 0.8
Release: alt1.20241017

Summary: GTK based greeter for greetd, to be run under cage or similar
License: GPL-3.0
Group:   Graphical desktop/Other
Url:     https://git.sr.ht/~kennylevinsen/gtkgreet

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: libgtk-layer-shell-devel
BuildRequires: libjson-c-devel
Requires: greetd
Requires: cage

Provides: greetd-greeter

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

# sample config
mkdir -p %buildroot%_sysconfdir/greetd/greeters
cat > %buildroot%_sysconfdir/greetd/greeters/gtkgreet.toml << EOF
[terminal]
vt = 1

[default_session]
command = "cage -sd -- gtkgreet"
user = "_greeter"
EOF

mkdir -p %buildroot%_altdir
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/gtkgreet.toml 35" \
	> %buildroot%_altdir/greetd-gtkgreet

%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_man1dir/%name.1.*
%_altdir/greetd-gtkgreet
%config(noreplace) %_sysconfdir/greetd/greeters/gtkgreet.toml

%changelog
* Mon Mar 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.8-alt1.20241017
- NMU:
  + new version
  + add greetd-greeter provides
  + pack base config

* Tue May 16 2023 Anton Midyukov <antohami@altlinux.org> 0.7-alt1.20230510
- Initial build for Sisyphus
