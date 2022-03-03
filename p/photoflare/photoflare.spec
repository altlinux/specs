#define git_hash %nil
%define git_hash .git.e200ab7538

Name: photoflare
Version: 1.6.9
Release: alt2

Group: Graphics
Summary: Simple but powerful Cross Platform Image Editor
Url: https://photoflare.io/
License: GPLv3+

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-base-devel qt5-tools-devel libGraphicsMagick-c++-devel libgomp-devel

%description
This is an effort to bring quick, simple but powerful image editing to the
masses. Photoflare is inspired by the image editor currently only available
on Microsoft Windows - PhotoFiltre. However, it will not be a straight clone.
It is being built from the ground up to be much improved and cross platform too!


%prep
%setup
%patch -p1

# Fix version due build from master with Russian translation
sed -i 's/^\(\s*app\.setApplicationVersion(QObject::tr("\).*\("))\)/\1%version%git_hash\2/' src/main.cpp

%build
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%installqt5

%find_lang --with-qt --all-name %name

%files -f %name.lang
%doc LICENSE.md .github/README.md
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop
%_man1dir/%name.*
%_datadir/pixmaps/%name.png
%_datadir/metainfo/*.appdata.xml

%changelog
* Mon Feb 14 2022 Evgeny Sinelnikov <sin@altlinux.org> 1.6.9-alt2
- Drawing performance regression in 1.6.9 Photoflare#463
- Fix missing taskbar icon on kde plasma

* Mon Feb 14 2022 Evgeny Sinelnikov <sin@altlinux.org> 1.6.9-alt1
- Update to latest stable release

* Sun Apr 04 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.6.7.1-alt1
- Update to latest release

* Mon Oct 05 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.6.5-alt1
- Initial build for Sisyphus

