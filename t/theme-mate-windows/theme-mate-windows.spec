Name:     theme-mate-windows
Version:  1.1
Release:  alt1

Summary:  Mate theme for Windows-like layout
License:  GPLv3+
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: gksu
Requires: dconf
# Required GTK+ themes
Requires: gtk3-theme-clearlooks-phenix
# Required fonts
Requires: fonts-ttf-google-noto-sans
Requires: fonts-ttf-google-crosextra-caladea
Requires: fonts-ttf-google-crosextra-carlito
# Other requirements
Requires: color-prompt-and-man
Requires: mintmenu

Conflicts: branding-alt-tonk-mate-settings

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
install -Dm0644 applications.list \
        %buildroot%_datadir/linuxmint/mintMenu/applications.list-themed

%files
%_datadir/glib-2.0/schemas/*.gschema.override
%_datadir/mate-panel/layouts/windows.layout
%_datadir/linuxmint/mintMenu/applications.list-themed

%changelog
* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Set window manager theme to Clearlooks-Phenix.

* Sun Jun 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
