%define rname mint-themes

Name: gtk-themes-mint
Version: 2.3.8
Release: alt1
Summary: Mint themes
License: GPLv3+
Group: Graphical desktop/MATE
Url: https://github.com/linuxmint/mint-themes.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: gtk-themes-mint-x = %EVR
Requires: gtk-themes-mint-y = %EVR

Source: %rname-%version.tar

# Cinnamon styles are taken from file 22_mint-artwork.styles in archive
# http://packages.linuxmint.com/pool/main/m/mint-artwork/mint-artwork_1.9.3.tar.xz
Source1: 22_mint-x.styles
Source2: 22_mint-y.styles

BuildArch: noarch
BuildRequires: python3-module-libsass

%description
A collection of mint themes

%package -n gtk-themes-mint-x
Summary: Mint-X themes
Group: Graphical desktop/MATE
Requires: icon-themes-mint-x x-cursor-themes-Bibata
%description -n gtk-themes-mint-x
%summary.

%package -n gtk-themes-mint-y
Summary: Mint-Y themes
Group: Graphical desktop/MATE
Requires: icon-themes-mint-y x-cursor-themes-Bibata
%description -n gtk-themes-mint-y
%summary.

%package -n cinnamon-style-mint-x
Summary: Mint-X style for Cinnamon
Group: Graphical desktop/Other
Requires: gtk-themes-mint-x = %EVR
%description -n cinnamon-style-mint-x
%summary.

%package -n cinnamon-style-mint-y
Summary: Mint-Y style for Cinnamon
Group: Graphical desktop/Other
Requires: gtk-themes-mint-y = %EVR
%description -n cinnamon-style-mint-y
%summary.

%prep
%setup -q -n %rname-%version

# fix cursor theme for Mint-X
subst 's/CursorTheme=default/CursorTheme=Bibata-Modern-Classic/g' \
      files/usr/share/themes/Mint-X*/index.theme

%build
./generate-themes.py
for i in X Y; do cp metacity-theme-2.xml usr/share/themes/Mint-$i/metacity-1/; done

%install
mkdir -p %buildroot
cp -a usr %buildroot/
mkdir -p %buildroot%_datadir/cinnamon/styles.d
cp -a %SOURCE1 %SOURCE2 %buildroot%_datadir/cinnamon/styles.d

%files
%doc debian/copyright

%files -n gtk-themes-mint-x
%_datadir/themes/Mint-X*

%files -n gtk-themes-mint-y
%doc README.md
%_datadir/themes/Mint-Y*

%files -n cinnamon-style-mint-x
%_datadir/cinnamon/styles.d/22_mint-x.styles

%files -n cinnamon-style-mint-y
%_datadir/cinnamon/styles.d/22_mint-y.styles

%changelog
* Sun Jan 18 2026 Alexander Kovalev <alexvk@altlinux.org> 2.3.8-alt1
- 2.3.8
- do separate packages for Mint-X and Mint-Y themes
- add packages with styles for Cinnamon

* Fri Feb 21 2025 Valery Inozemtsev <shrek@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Thu Oct 10 2024 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Tue Aug 10 2021 Valery Inozemtsev <shrek@altlinux.ru> 1.8.8-alt1
- 1.8.8

* Wed Sep 09 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Tue May 05 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon Apr 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt3
- remove Mint-Y* themes

* Mon Apr 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt2
- do not generate Mint-Y* themes

* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- initial release
