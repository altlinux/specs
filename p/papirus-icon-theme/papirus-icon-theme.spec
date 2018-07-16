Name:     papirus-icon-theme
Version:  20180601
Release:  alt1

Summary:  All Papirus icon themes
License:  GPLv3
Group:    Other
Url:      https://github.com/PapirusDevelopmentTeam/papirus-icon-theme

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: icon-theme-Papirus = %EVR
Requires: icon-theme-Papirus-Adapta = %EVR
Requires: icon-theme-Papirus-Adapta-Nokto = %EVR
Requires: icon-theme-Papirus-Dark = %EVR
Requires: icon-theme-Papirus-Light = %EVR
Requires: icon-theme-ePapirus = %EVR

%description
Papirus is a free and open source SVG icon theme for Linux, based on
Paper Icon Set with a lot of new icons and a few extras, like
Hardcode-Tray support, KDE colorscheme support, Folder Color support,
and others.

Papirus icon theme is available in six variants:

* Papirus (for Arc / Arc Darker)
* Papirus Dark (for Arc Dark)
* Papirus Light (light theme with Breeze colors)
* Papirus Adapta (for Adapta)
* Papirus Adapta Nokto (for Adapta Nokto)
* ePapirus (for elementary OS and Pantheon Desktop)

%package -n icon-theme-Papirus
Summary: Papirus icon theme
Group: Other

%description -n icon-theme-Papirus
%summary.

%package -n icon-theme-Papirus-Adapta
Summary: Papirus-Adapta icon theme
Group: Other

%description -n icon-theme-Papirus-Adapta
%summary.

%package -n icon-theme-Papirus-Adapta-Nokto
Summary: Papirus-Adapta-Nokto icon theme
Group: Other

%description -n icon-theme-Papirus-Adapta-Nokto
%summary.

%package -n icon-theme-Papirus-Dark
Summary: Papirus-Dark icon theme
Group: Other

%description -n icon-theme-Papirus-Dark
%summary.

%package -n icon-theme-Papirus-Light
Summary: Papirus-Light icon theme
Group: Other

%description -n icon-theme-Papirus-Light
%summary.

%package -n icon-theme-ePapirus
Summary: ePapirus icon theme
Group: Other

%description -n icon-theme-ePapirus
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_iconsdir
cp -a Papirus Papirus-Adapta Papirus-Adapta-Nokto Papirus-Dark Papirus-Light ePapirus %buildroot%_iconsdir

%files
%doc AUTHORS LICENSE README.md

%files -n icon-theme-Papirus
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus

%files -n icon-theme-Papirus-Adapta
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Adapta

%files -n icon-theme-Papirus-Adapta-Nokto
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Adapta-Nokto

%files -n icon-theme-Papirus-Dark
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Dark

%files -n icon-theme-Papirus-Light
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Light

%files -n icon-theme-ePapirus
%doc AUTHORS LICENSE README.md
%_iconsdir/ePapirus

%changelog
* Mon Jul 16 2018 Andrey Cherepanov <cas@altlinux.org> 20180601-alt1
- Initial build for Sisyphus
