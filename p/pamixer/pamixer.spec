Name: pamixer
Version: 1.6
Release: alt1

Summary: pulseaudio command line mixer
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/cdemoulins/pamixer

Vcs: https://github.com/cdemoulins/pamixer.git
Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(cxxopts)

%description
pamixer is like amixer but for pulseaudio. It can control the volume
levels of the sinks.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_man1dir/%name.1*
%doc README*

%changelog
* Sun Nov 26 2023 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- first build for Sisyphus

