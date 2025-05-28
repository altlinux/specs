%define _unpackaged_files_terminate_build 1

Name: wlrctl
Version: 0.2.2
Release: alt1

Summary: Command line utility for miscellaneous wlroots Wayland extensions
License: MIT
Group: Graphical desktop/Other
Url: https://git.sr.ht/~brocellous/wlrctl

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)

%description
wlrctl supports the foreign-toplevel-mangement (window/toplevel command),
virtual-keyboard (keyboard command), and virtual-pointer (pointer command)
protocols

%prep
%setup

# put zsh auto-completion to the correct folder
sed -i "s/site-functions/vendor-completions/" meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_bindir/*
%_datadir/zsh/vendor-completions/*

%changelog
* Sat May 24 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus
