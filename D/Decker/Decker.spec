Name:    Decker
Version: 1.73
Release: alt1

Summary: A multimedia sketchpad
License: MIT
Group:   Editors
Url:     https://github.com/JohnEarnest/Decker

Source: %name-%version.tar

BuildRequires: libSDL2-devel xxd libSDL2_image-devel
Requires: xdg-utils

%description
Decker is a multimedia platform for creating and sharing interactive documents,
with sound, images, hypertext, and scripted behavior.

%prep
%setup

%build
%make_build lilt decker EXTRA_FLAGS="%optflags"
%make_build docs

%install
install -Dm755 c/build/decker %buildroot%_bindir/decker
install -Dm755 c/build/lilt %buildroot%_bindir/lilt

install -Dm644 Decker.desktop %buildroot%_desktopdir/Decker.desktop
for DIM in 32 64 128 192 256 512; do
    install -Dm644 icon_${DIM}x${DIM}.png %buildroot%_iconsdir/hicolor/${DIM}x${DIM}/apps/decker.png
    install -Dm644 icon_${DIM}x${DIM}.png %buildroot%_iconsdir/hicolor/${DIM}x${DIM}/mimetypes/x-decker.png
done

install -Dm644 x-decker.xml %buildroot%_datadir/mime/packages/application-x-decker.xml

%files
%doc LICENSE.txt Readme.md VERSION docs/*.html docs/images
%_bindir/decker
%_bindir/lilt
%_datadir/mime/packages/application-x-decker.xml
%_desktopdir/Decker.desktop
%_iconsdir/hicolor/*/apps/decker.png
%_iconsdir/hicolor/*/mimetypes/x-decker.png

%changelog
* Mon Nov 23 2026 Sergey Palcheh <minergenon@altlinux.org> 1.73-alt1
- new version 1.73

* Sat Oct 31 2026 Sergey Palcheh <minergenon@altlinux.org> 1.72-alt1
- new version 1.72

* Fri Oct 09 2026 Sergey Palcheh <minergenon@altlinux.org> 1.71-alt1
- new version 1.71

* Sat Aug 22 2026 Sergey Palcheh <minergenon@altlinux.org> 1.70-alt1
- new version 1.70

* Sun Jul 19 2026 Sergey Palcheh <minergenon@altlinux.org> 1.69-alt1
- new version 1.69

* Mon Jul 06 2026 Sergey Palcheh <minergenon@altlinux.org> 1.68-alt1
- new version 1.68

* Wed Jun 17 2026 Sergey Palcheh <minergenon@altlinux.org> 1.67-alt1
- new version 1.67

* Tue May 26 2026 Sergey Palcheh <minergenon@altlinux.org> 1.66-alt1
- new version 1.66

* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 1.55-alt1
- new version 1.55 (with rpmrb script)

* Tue Feb 25 2025 Sergey Palcheh <minergenon@altlinux.org> 1.53-alt1
- Initial build for Sisyphus

