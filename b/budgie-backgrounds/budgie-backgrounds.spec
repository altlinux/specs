Name: budgie-backgrounds
Version: 3.0
Release: alt1

Summary: Default set of background images for the Budgie Desktop

License: CC0-1.0
Group: Graphical desktop/Other
Url: https://github.com/BuddiesOfBudgie/budgie-backgrounds

# Source0-url: %url/releases/download/v%version/%name-v%version.tar.xz
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: ImageMagick-tools
BuildRequires: gnupg2
BuildRequires: jhead
BuildRequires: meson

%description
Default set of background images for the Budgie Desktop.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%doc LICENSE
%dir %_datadir/backgrounds/
%dir %_datadir/backgrounds/budgie
%dir %_datadir/gnome-background-properties
%_datadir/backgrounds/budgie/*.jpg
%_datadir/gnome-background-properties/%name.xml

%changelog
* Sun Mar 09 2025 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- initial build for ALT Sisyphus

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 17 2024 Joshua Strobl <me@joshuastrobl.com> - 3.0-2
- Fix sources

* Sun Mar 17 2024 Joshua Strobl <me@joshuastrobl.com> - 3.0-1
- Update to 3.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 4 2023 Joshua Strobl <me@joshuastrobl.com> - 1.0-1
- Initial inclusion of Budgie Backgrounds
