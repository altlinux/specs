%def_disable sessions
%def_enable cinnamonshell
%def_enable unity
%def_enable xfwm4

Name: yaru-theme
Version: 26.10.1
Release: alt1

Summary: Ubuntu Yaru theme suite

License: GPL-3.0 and CC-BY-SA-4.0
Group: Graphical desktop/GNOME
URL: https://github.com/ubuntu/yaru
VCS: https://github.com/ubuntu/yaru.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Styles for Cinnamon
Source1: Yaru.styles
# Styles for Folder Color Switcher
Source2: Yaru.json
# Build with all accent colors
Patch1: meson_options.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson

BuildRequires: libgtk+3-devel
BuildRequires: sassc
BuildRequires: meson >= 0.60
BuildRequires: xvfb-run
BuildRequires: inkscape

Requires: gtk-theme-Yaru = %EVR
Requires: sound-theme-Yaru = %EVR

%description
Yaru is the default theme for Ubuntu, backed by the community.

It contains:

* a GNOME Shell theme based on the upstream GNOME shell theme
* a light and dark GTK theme (gtk2 and gtk3) based on the upstream Adwaita Gtk theme
* an icon & cursor theme, derived from the Unity8 Suru icons and Suru icon theme
* a sound theme, combining sounds from the WoodenBeaver and Touch-Remix sound themes.

%package -n gtk-theme-Yaru
Summary: Yaru GTK theme from the Ubuntu Community
Group: Graphical desktop/GNOME
Requires: icon-theme-Yaru = %EVR
Requires: x-cursor-theme-Yaru = %EVR
%description -n gtk-theme-Yaru
This package contains the GTK theme parts.

%package -n icon-theme-Yaru
Summary: Yaru icon theme from the Ubuntu Community
Group: Graphical desktop/GNOME
%description -n icon-theme-Yaru
This package contains the icon theme.

%package -n sound-theme-Yaru
Summary: Yaru sound theme from the Ubuntu Community
Group: Graphical desktop/GNOME
%description -n sound-theme-Yaru
This package contains the sound theme.

%package -n x-cursor-theme-Yaru
Summary: Yaru cursor theme from the Ubuntu Community
Group: Graphical desktop/GNOME
%description -n x-cursor-theme-Yaru
This package contains the cursor theme.

%package -n cinnamon-style-yaru
Summary: Yaru style for Cinnamon
Group: Graphical desktop/Other
Requires: gtk-theme-Yaru = %EVR
%description -n cinnamon-style-yaru
This package contains the style for Cinnamon.

%package -n folder-color-switcher-yaru
Summary: Yaru style for Folder Color Switcher
Group: Graphical desktop/Other
Requires: icon-theme-Yaru = %EVR
%description -n folder-color-switcher-yaru
This package contains the style for Folder Color Switcher.

%prep
%setup
%autopatch -p1

%build
# Replace Ubuntu logo (https://github.com/ubuntu/yaru/pull/3931)
dir="icons/Yaru"
grid="actions/view-app-grid.png"
for i in 16 22 24 32 48 256; do
  for j in ${i}x${i} ${i}x${i}@2x; do
    logo="$dir/$j/places/start-here.png"
    [ -e "$logo" ] && rm -f "$logo"
    [ -e "$dir/$j/$grid" ] && ln -s "../$grid" "$logo"
  done
done
dir="$dir/scalable"
grid="actions/view-app-grid-symbolic.svg"
logo="$dir/places/start-here-symbolic.svg"
[ -e "$logo" ] && rm -f "$logo"
[ -e "$dir/$grid" ] && ln -s "../$grid" "$logo"

%meson %{?_disable_sessions:-Dsessions=false} \
       %{?_enable_cinnamonshell:-Dcinnamon-shell=true} \
       %{?_enable_unity:-Dubuntu-unity=true} \
       %{?_enable_xfwm4:-Dxfwm4=true}
%meson_build

%install
%meson_install
mkdir -p %buildroot%_datadir/cinnamon/styles.d
cp -a %SOURCE1 %buildroot%_datadir/cinnamon/styles.d
mkdir -p %buildroot%_datadir/folder-color-switcher/colors.d
cp -a %SOURCE2 %buildroot%_datadir/folder-color-switcher/colors.d

# Move gnome-shell themes
dir="%buildroot%_datadir/gnome-shell/theme"
themes="%buildroot%_datadir/themes"
pushd "$dir"
for t in *; do
  [ -L "$themes/$t/gnome-shell" ] &&
  rm -v "$themes/$t/gnome-shell" &&
  mv "$dir/$t" "$themes/$t/gnome-shell"
done
popd

%files
%doc AUTHORS CONTRIBUTING.md COPYING* LICENSE* README.md

%files -n gtk-theme-Yaru
%_datadir/*gtksourceview-*/styles/Yaru*.xml
%_datadir/themes/Yaru*

%files -n icon-theme-Yaru
%doc icons/AUTHORS icons/CONTRIBUTING.md icons/COPYING* icons/LICENSE* icons/README.md
%_datadir/icons/Yaru*
%exclude %_datadir/icons/Yaru/cursor*

%files -n sound-theme-Yaru
%_datadir/sounds/Yaru

%files -n x-cursor-theme-Yaru
%_datadir/icons/Yaru/cursor*

%files -n cinnamon-style-yaru
%_datadir/cinnamon/styles.d/Yaru.styles

%files -n folder-color-switcher-yaru
%_datadir/folder-color-switcher/colors.d/Yaru.json

%changelog
* Thu Jun 11 2026 Alexander Kovalev <alexvk@altlinux.org> 26.10.1-alt1
- New version 26.10.1.
- Fix mixed Cinnamon style appearance.

* Sun Apr 19 2026 Alexander Kovalev <alexvk@altlinux.org> 26.04.5-alt1
- New version 26.04.5.

* Sun Mar 22 2026 Alexander Kovalev <alexvk@altlinux.org> 26.04.3-alt1
- New version 26.04.3.

* Sat Oct 04 2025 Alexander Kovalev <alexvk@altlinux.org> 25.10.3-alt1
- New version 25.10.3.

* Fri Sep 05 2025 Alexander Kovalev <alexvk@altlinux.org> 25.10.2-alt1
- New version 25.10.2.

* Wed Jul 16 2025 Alexander Kovalev <alexvk@altlinux.org> 25.10.1-alt1
- New version 25.10.1.

* Thu Apr 17 2025 Alexander Kovalev <alexvk@altlinux.org> 25.04.2-alt1
- Initial build for ALT.
- Replace Ubuntu logo.
- Build with all accent colors.
- Disable build sessions component.
- Enable build Cinnamon Shell, Unity, xfwm4 themes.
- Add styles for Cinnamon and Folder Color Switcher.
