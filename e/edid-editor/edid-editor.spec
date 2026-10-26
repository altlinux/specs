%define _unpackaged_files_terminate_build 1
%define app_id io.github.sachesi.EdidEditor

%def_enable check

Name: edid-editor
Version: 0.5.0
Release: alt1
Summary: EDID editor for GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/sachesi/edid-editor
Vcs: https://github.com/sachesi/edid-editor

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

%description
EDID Editor inspects and edits EDID, the data a display sends to describe
itself: its name, size, timings, refresh ranges, color and HDR support, and
audio formats. It reads the base block, CTA-861 extensions and DisplayID 1.x
and 2.x blocks from files or from a connected display, and never writes to the
display itself. It is written with GTK 4 and libadwaita, and is based on wxEDID
by Tomasz Pawlak.

The command line interface is packaged separately as %name-cli.

%package -n %name-cli
Summary: EDID editor for the command line
Group: System/Configuration/Hardware

%description -n %name-cli
edid-editor-cli reads, edits, compares and converts EDID data from a terminal,
with the same parser as the EDID Editor application and without a dependency on
GTK. It ships a manual page and completions for bash, zsh and fish.

%prep
%setup

%build
%meson -Dgui=enabled
%meson_build

%install
%meson_install

%check
meson test -C %_target_platform --no-suite ui

%files
%doc LICENSE
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg
%_man1dir/%name.1*

%files -n %name-cli
%doc LICENSE
%_bindir/%name-cli
%_man1dir/%name-cli.1*
%_datadir/bash-completion/completions/%name-cli
%_datadir/zsh/site-functions/_%name-cli
%_datadir/fish/vendor_completions.d/%name-cli.fish

%changelog
* Mon Oct 12 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.5.0-alt1
- Initial build.

