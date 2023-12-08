Name: xisxwayland
Version: 2
Release: alt2

Summary: Tool to check if the X server is XWayland
License: MIT
Group: System/X11

Url: https://gitlab.freedesktop.org/xorg/app/xisxwayland
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel

%description
xisxwayland is a tool to be used within shell scripts to determine whether
the X server in use is Xwayland. It exits with status 0 if the server is an
Xwayland server and 1 otherwise.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING
%_bindir/xisxwayland
%_man1dir/%name.1*

%changelog
* Thu Nov 30 2023 Artem Kurashov <saahriktu@altlinux.org> 2-alt2
- Tidying up the .spec file.

* Mon Feb 13 2023 Artem Kurashov <saahriktu@altlinux.org> 2-alt1
- Initial package.
