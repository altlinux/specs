%global glib2_version 2.64
%global gtk3_version 3.24
%global vala_version 0.48

Name: budgie-desktop-view
Version: 1.3
Release: alt1

Summary: Official Budgie desktop icons application / implementation

License: Apache-2.0
Group: Graphical desktop/Other
Url: https://github.com/BuddiesOfBudgie/budgie-desktop-view

# Source0-url: %url/releases/download/v%version/%name-v%version.tar.xz
Source0: %name-%version.tar

Patch0: 0001-fix-compilation-under-newer-meson-and-gcc.patch

BuildRequires(pre):  rpm-macros-meson

BuildRequires: pkgconfig(glib-2.0) >= %glib2_version
BuildRequires: pkgconfig(gio-unix-2.0) >= %glib2_version
BuildRequires: pkgconfig(gdk-3.0) >= %gtk3_version
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk3_version
BuildRequires: pkgconfig(vapigen) >= %vala_version

BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: meson
BuildRequires: vala

%description
Official Budgie desktop icons application / implementation.

%prep
%setup

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/org.buddiesofbudgie.budgie-desktop-view.desktop

%files -f %name.lang
%doc README.md
%doc LICENSE.md
%_bindir/org.buddiesofbudgie.budgie-desktop-view
%_desktopdir/org.buddiesofbudgie.budgie-desktop-view.desktop
%_datadir/glib-2.0/schemas/org.buddiesofbudgie.budgie-desktop-view.gschema.xml
%_sysconfdir/xdg/autostart/org.buddiesofbudgie.budgie-desktop-view-autostart.desktop

%changelog
* Sat Mar 08 2025 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Sisyphus

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Joshua Strobl <me@joshuastrobl.com> - 1.3-6
- Added patch to resolve compilation against newer vala, meson, gcc (rhbz#2300582)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 16 2023 Joshua Strobl <me@joshuastrobl.com> - 1.3-1
- Update to 1.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Joshua Strobl <me@joshuastrobl.com> - 1.2.1-1
- Update to 1.2.1

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 15 2022 Joshua Strobl <me@joshuastrobl.com> - 1.2-1
- Initial version of the package
