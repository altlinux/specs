Name:    wtype
Version: 0.5
Release: alt1

Summary: xdotool type for wayland
License: MIT
Group:   Graphical desktop/Other
URL:     https://github.com/atx/wtype

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake gcc-c++ meson
BuildRequires: git-core libwayland-client-devel libwayland-cursor-devel
BuildRequires: libxkbcommon-devel

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_bindir/%name
%_man1dir/%name.1.*


%changelog
* Thu Oct 22 2026 Sergey Palcheh <minergenon@altlinux.org> 0.5-alt1
- Initial build for Sisyphus
