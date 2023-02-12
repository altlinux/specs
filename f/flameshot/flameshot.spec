%def_with wayland

Name: flameshot
Version: 12.1.0
Release: alt2

Summary: Powerful yet simple to use screenshot software

License: GPLv3
Group: Graphics
Url: https://github.com/lupoDharkael/flameshot

Source: %name-%version.tar

Packager: Anton Shevtsov <x09@altlinux.org>

BuildRequires: qt5-base-devel qt5-tools-devel qt5-svg-devel cmake
%if_with wayland
BuildRequires: kf5-kguiaddons-devel
%endif

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake \
%if_with wayland
    -DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
%endif
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/applications/org.flameshot.Flameshot.desktop
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/flameshot.fish
%_datadir/zsh/site-functions/_%name
%_datadir/dbus-1/interfaces/org.flameshot.Flameshot.xml
%_datadir/dbus-1/services/org.flameshot.Flameshot.service
%_datadir/%name
%_iconsdir/hicolor/128x128/apps/org.flameshot.Flameshot.png
%_iconsdir/hicolor/48x48/apps/org.flameshot.Flameshot.png
%_iconsdir/hicolor/scalable/apps/org.flameshot.Flameshot.svg
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/org.flameshot.Flameshot.metainfo.xml
%_man1dir/flameshot.1.xz

%changelog
* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 12.1.0-alt2
- Added support of wayland clipboard.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 12.1.0-alt1
- Automatically updated to 12.1.0.

* Mon Jun 27 2022 Grigory Ustinov <grenka@altlinux.org> 12.0.0-alt1
- Automatically updated to 12.0.0.

* Tue Jan 18 2022 Grigory Ustinov <grenka@altlinux.org> 11.0.0-alt1
- Automatically updated to 11.0.0.

* Sun Oct 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt1
- Automatically updated to 0.10.1.

* Tue Apr 13 2021 Arseny Maslennikov <arseny@altlinux.org> 0.8.0-alt2
- NMU: Adapted to altlinux.org/CMakeMigration2021.

* Mon Sep 21 2020 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Automatically updated to 0.8.0.

* Mon Jun 03 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.0.0.53.git7ee9a3f-alt1
- Build from new commit.
- Fix problem with disabled tray icon (Closes: #36299).
  + (https://github.com/lupoDharkael/flameshot/pull/495)
- New try of fixing icon in autostarted program (Closes: #36134).
- E2K: strip UTF-8 BOM for lcc < 1.24 (thx to mike@).
- Minor spec cleanup (thx to mike@).

* Mon Mar 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.0.0.46.git4261915-alt1
- Fixed translation of system buttons in dialogs.
  + (https://github.com/lupoDharkael/flameshot/pull/474)
- Added russian translation of desktop file.
  + (https://github.com/lupoDharkael/flameshot/pull/475)
- Fixed errors in russian translation.
  + (https://github.com/lupoDharkael/flameshot/pull/476)
- Fixed export of startup option in configuration file (Closes: #36149).
  + (https://github.com/lupoDharkael/flameshot/pull/477)
- Fixed icon in autostarted program for i586 arch (Closes: #36134).

* Tue Feb 19 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.0.0.25.git94daa4f-alt1
- Fix icon in autostarted program (Closes: #36134).
- Update russian translation.

* Fri Nov 16 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt2
- Corrected the previous build according good sense.

* Mon Sep 03 2018 Anton Shevtsov <x09@altlinux.org> 0.6.0-alt1
- Initial build for ALT
