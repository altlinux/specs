%define _distconfdir /etc

Name:           tofi
Version:        0.9.1
Release:        alt1
Summary:        Tiny dynamic menu for Wayland
Group:          Graphical desktop/Other
License:        MIT
URL:            https://github.com/philj56/tofi
Source:         https://github.com/philj56/tofi/archive/refs/tags/v%{version}.tar.gz#$/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  libgio-devel

%description
A simple dmenu / rofi replacement for wlroots-based Wayland
compositors such as Sway.

When configured correctly, tofi can get on screen within a single frame.

ExcludeArch: %ix86

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Shells
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%prep
%setup

%build
%meson --sysconfdir=%{_distconfdir}
%meson_build

%install
%meson_install

%files
%doc README.md LICENSE

%{_bindir}/tofi
%{_bindir}/tofi-drun
%{_bindir}/tofi-run
%dir %{_distconfdir}/xdg/tofi
%{_distconfdir}/xdg/tofi/config
%{_mandir}/man1/tofi*
%{_mandir}/man5/tofi.5*

%files bash-completion
%{_datadir}/bash-completion/*

%changelog
* Fri Feb 20 2026 Artyom Bystrov <arbars@altlinux.org> 0.9.1-alt1
- initial build for ALT Sisyphus
