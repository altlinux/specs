Name:    Decker
Version: 1.67
Release: alt1

Summary: A multimedia sketchpad
License: MIT
Group:   Editors
Url:     https://github.com/JohnEarnest/Decker

Source: %name-%version.tar

BuildRequires: libSDL2-devel xxd libSDL2_image-devel

%description
Decker is a multimedia platform for creating and sharing interactive documents,
with sound, images, hypertext, and scripted behavior.

%prep
%setup

%build
%make_build lilt
%make_build decker
%make_build docs

%install
install -Dm755 c/build/decker %buildroot/usr/bin/decker
install -Dm755 c/build/lilt %buildroot/usr/bin/lilt

install -Dm644 Decker.desktop %buildroot/usr/share/applications/Decker.desktop
for DIM in 32 64 128 192 256 512; do
    install -Dm644 icon_${DIM}x${DIM}.png %buildroot/usr/share/icons/hicolor/${DIM}x${DIM}/apps/decker.png
done

install -Dm644 x-decker.xml %buildroot/usr/share/mime/packages/application-x-decker.xml

install -Dm644 -t %buildroot/usr/share/doc/decker docs/*.html
install -Dm644 -t %buildroot/usr/share/doc/decker/images docs/images/*

%files
%doc LICENSE.txt Readme.md VERSION
%_bindir/decker
%_bindir/lilt
%_datadir/doc/decker
%_datadir/mime/packages/application-x-decker.xml
%_desktopdir/Decker.desktop
%_iconsdir/hicolor/*/apps/decker.png

%changelog
* Wed Jun 17 2026 Sergey Palcheh <minergenon@altlinux.org> 1.67-alt1
- new version 1.67

* Tue May 26 2026 Sergey Palcheh <minergenon@altlinux.org> 1.66-alt1
- new version 1.66

* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 1.55-alt1
- new version 1.55 (with rpmrb script)

* Tue Feb 25 2025 Sergey Palcheh <minergenon@altlinux.org> 1.53-alt1
- Initial build for Sisyphus

