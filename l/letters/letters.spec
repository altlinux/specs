%define _unpackaged_files_terminate_build 1

Name: letters
Version: 0.1.1
Release: alt4
Summary: Modern word processor for the GNOME desktop.
License: GPLv3+
Group: Editors
Url: https://codeberg.org/eyekay/letters
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: libgio-qt6-devel 
BuildRequires: libadwaita-devel
BuildRequires: python3-module-pypandoc
BuildRequires: python3-module-weasyprint

Conflicts: footage
Requires: python3-module-weasyprint

%description
%summary

%prep
%setup
%autopatch -p1
sed -i 's/^Categories=.*/Categories=Utility;TextEditor;/' data/net.codelogistics.letters.desktop.in

%build
%meson
%meson_build

%install
%meson_install 

%check
%__meson_test

%files
%doc *.md
%_bindir/%name
%_datadir/%name
%_datadir/applications/net.codelogistics.%name.desktop
%_datadir/dbus-1/services/net.codelogistics.%name.service
%_datadir/glib-2.0/schemas/net.codelogistics.%name.gschema.xml
%_datadir/icons/hicolor/scalable/actions/chain-link-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/image-round-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/insert-list-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/system-search-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/text-bold-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/text-italic-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/text-underline-symbolic.svg
%_datadir/icons/hicolor/scalable/apps/net.codelogistics.%name.svg
%_datadir/icons/hicolor/symbolic/apps/net.codelogistics.letters-symbolic.svg
%_datadir/metainfo/net.codelogistics.%name.metainfo.xml

%changelog
* Tue Oct 14 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.1-alt4
- Add reqires for package (ALT #56374).

* Fri Oct 10 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.1-alt3
- Update Freedesktop Additional Categories.

* Mon Oct 06 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.1-alt2
- Add missing Freedesktop Additional Categories to fix freedesktop-categories warn.

* Sat Oct 04 2025 Pavel Shilov <zerospirit@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
