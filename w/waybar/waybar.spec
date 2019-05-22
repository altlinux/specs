Name: waybar
Version: 0.6.6
Release: alt1
License: MIT
Summary: Highly customizable Wayland bar for Sway and Wlroots based compositors
URL: https://github.com/Alexays/Waybar.git
Group: Graphical desktop/Other

Source: %name-%version.tar
BuildRequires(pre): rpm-build-xdg
# Automatically added by buildreq on Thu Jan 03 2019
BuildRequires: gcc-c++
BuildRequires: jsoncpp-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libfmt-devel
BuildRequires: libgtkmm3-devel
BuildRequires: libinput-devel
BuildRequires: libnl-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libudev-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libwayland-cursor-devel
BuildRequires: libspdlog-devel
BuildRequires: meson
BuildRequires: cmake
BuildRequires: wayland-protocols

%description
%summary.

%prep
%setup

%build
sed -i \
	-e "s/^if find_program('sway'/if find_program('true'/" \
	meson.build

%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/%name
%_xdgconfigdir/%name

%changelog
* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sat May 18 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Apr 02 2019 Alexey Gladkov <legion@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Thu Jan 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.3-alt1
- Initial build.
