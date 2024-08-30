Name:     theme-mate-windows
Version:  2.7
Release:  alt1

Summary:  Mate theme for Windows-like layout
License:  GPLv3+
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: dconf
# Required GTK+ themes
Requires: mate-themes
# Main menu
Requires: mate-menu
# Required fonts
Requires: fonts-ttf-google-noto-sans
Requires: fonts-ttf-google-crosextra-caladea
Requires: fonts-ttf-google-crosextra-carlito
# Other requirements
Requires: color-prompt-and-man

%description
Mate theme for Windows-like layout: taskbar at bottom with menu button.

%prep
%setup

%install
#mate-settings
mkdir -p %buildroot%_datadir/glib-2.0/schemas
install -pm644 *.gschema.override \
        %buildroot%_datadir/glib-2.0/schemas/
install -pDm644 windows.layout \
        %buildroot%_datadir/mate-panel/layouts/windows.layout

%files
%_datadir/glib-2.0/schemas/*.gschema.override
%_datadir/mate-panel/layouts/windows.layout

%changelog
* Fri Aug 30 2024 Andrey Cherepanov <cas@altlinux.org> 2.7-alt1
- Do not force file manager background color (ALT #43513).

* Fri Sep 22 2023 Andrey Cherepanov <cas@altlinux.org> 2.6-alt1
- Remove deprecated toggle-shaded keybinding.

* Mon Feb 20 2023 Andrey Cherepanov <cas@altlinux.org> 2.5-alt1
- Deleted obsoleted keys.

* Tue Feb 14 2023 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- Decreased panel height from 30px to 28px.

* Fri Dec 09 2022 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- Removed show-flags=false for xkb indicator (ALT #43635).

* Thu Nov 17 2022 Andrey Cherepanov <cas@altlinux.org> 2.2-alt1
- Removed buttons-have-icons=false.

* Tue Aug 09 2022 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- Remove custom favorites for mint-menu.

* Sat Feb 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- Change window theme to Dopple (ALT #38488).

* Thu Apr 16 2020 Andrey Cherepanov <cas@altlinux.org> 1.9-alt1
- Remove gksu requirement.

* Sun Apr 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.8-alt1
- Remove zz-mate-menu.gschema.override obsoleted by mate-menu-20.04.

* Fri Oct 18 2019 Ivan A. Melnikov <iv@altlinux.org> 1.7-alt1
- Avoid overriding XKB configuration (altbug #37346).

* Tue Aug 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- Set BlueMenta as default GTK theme.

* Mon Aug 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Use mate-menu as successor of mintmenu.

* Thu Jul 11 2019 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Use standard Mate menu button instead of Brisk menu.
- Drop deprecated property custom-border-color.

* Fri Jul 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Replace Materia-light for TraditionalOk.

* Wed Jun 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Replace MintMenu for BriskMenu.
- Replace GTK theme Clearlooks-Phenix for Materia-light.
- Remove side-by-side-tiling parameter unsupported in new version of Marco.
- Increase bottom panel size to 30px.

* Tue Mar 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.1-alt2
- Remove conflict with branding-alt-tonk-mate-settings.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Set window manager theme to Clearlooks-Phenix.

* Sun Jun 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
