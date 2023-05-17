# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    gtkgreet
Version: 0.7
Release: alt1.20230510

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
cat > config.toml << EOF
[terminal]
vt = 1

[default_session]
command = "cage -sd -- gtkgreet"
user = "_greeter"
EOF

%find_lang %name

%files -f %name.lang
%doc README.md config.toml
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Tue May 16 2023 Anton Midyukov <antohami@altlinux.org> 0.7-alt1.20230510
- Initial build for Sisyphus
