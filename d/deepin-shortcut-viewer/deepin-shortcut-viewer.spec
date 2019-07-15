Name: deepin-shortcut-viewer
Version: 5.0.2
Release: alt1
Summary: Deepin Shortcut Viewer
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-shortcut-viewer
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: qt5-base-devel dtk5-widget-devel

%description
The program displays a shortcut key window when a JSON data is passed.

%prep
%setup

%build
%qmake_qt5 PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%_bindir/%name

%changelog
* Fri Jul 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
