Name: gtk-themes-mint-l
Version: 2.0.7
Release: alt1

Summary: Mint-L Theme

License: GPLv3+
Group: Graphical desktop/MATE
URL: https://github.com/linuxmint/mint-l-theme
VCS: https://github.com/linuxmint/mint-l-theme.git

Packager: Alexander Kovalev <alexvk@altlinux.org>

Source: %name-%version.tar

Requires: icon-themes-mint-l
Requires: x-cursor-themes-Bibata

BuildArch: noarch

BuildRequires: python3-module-libsass

%description
%summary.

%package -n cinnamon-style-mint-l
Summary: Mint-L style for Cinnamon
Group: Graphical desktop/Other
Requires: %name = %EVR
%description -n cinnamon-style-mint-l
This package contains the style for Cinnamon.

%prep
%setup

%build
# Patch cursor theme
subst 's/CursorTheme=DMZ-Black/CursorTheme=Bibata-Modern-Classic/g' src/Mint-L/index.theme*

./generate-themes.py

%install
mkdir -p %buildroot
cp -a usr %buildroot/

%files
%doc debian/copyright
%_datadir/themes/Mint-L*

%files -n cinnamon-style-mint-l
%_datadir/cinnamon/styles.d/00_mint-l.styles

%changelog
* Wed May 13 2026 Alexander Kovalev <alexvk@altlinux.org> 2.0.7-alt1
- New version 2.0.7.

* Sat Jan 17 2026 Alexander Kovalev <alexvk@altlinux.org> 2.0.6-alt1
- New version 2.0.6.

* Wed Sep 03 2025 Alexander Kovalev <alexvk@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Wed Jul 16 2025 Alexander Kovalev <alexvk@altlinux.org> 2.0.0-alt1
- New version 2.0.0.

* Sun May 18 2025 Alexander Kovalev <alexvk@altlinux.org> 1.9.9-alt1
- Initial build for ALT.
