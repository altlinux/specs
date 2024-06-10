Name:           nwg-launchers
Version:        0.7.1.1
Release:        alt2
Summary:        GTK launchers and menu for sway and i3
License:        GPL-3.0-or-later
Group:          Graphical desktop/Other
URL:            https://github.com/nwg-piotr/nwg-launchers
Source:         %name-%version.tar
Patch0:         nwg-launchers-readme.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libgtk-layer-shell-devel
BuildRequires:  libgtkmm3-devel
BuildRequires:  librsvg-devel
BuildRequires:  meson
BuildRequires:  nlohmann-json-devel

%description
GTK-based launchers: application grid, button bar, dmenu for sway and other window managers.

%prep
%setup
%patch0 -p1
%ifarch %e2k
sed -E -i 's/(\[prefix, parser)(\].*)/\11\2auto\&parser=parser1;/' \
	grid/on_desktop_entry.h
%endif

%build
%meson
%meson_build

%install
%meson_install

%files

%doc README.md LICENSE
%_bindir/nwgbar
%_bindir/nwgdmenu
%_bindir/nwggrid
%_bindir/nwggrid-server
%dir %_datadir/nwg-launchers
%_datadir/nwg-launchers/nwgbar
%_datadir/nwg-launchers/nwgdmenu
%_datadir/nwg-launchers/nwggrid
%_datadir/nwg-launchers/icon-missing.png
%_datadir/nwg-launchers/icon-missing.svg

%changelog
* Mon Jun 10 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.7.1.1-alt2
- Fixed build for Elbrus

* Fri May 17 2024 Artyom Bystrov <arbars@altlinux.org> 0.7.1.1-alt1
- Initial commit rot Sisyphus
