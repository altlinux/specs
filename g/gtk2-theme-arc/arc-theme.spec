Name: gtk2-theme-arc
Version: 20221218
Release: alt1

Summary: Arc GTK theme

Group: Graphical desktop/GNOME
License: GPLv3
Url: https://github.com/jnsh/arc-theme

Source: %name-%version.tar

Packager: Konstantin Artyushkin <akv@altlinux.org>

BuildRequires: libgtk+3-devel
BuildRequires: pkg-config
BuildRequires: meson
BuildRequires: sassc
BuildRequires: cinnamon
BuildRequires: gnome-shell
BuildRequires: inkscape

Requires: libgtk-engine-murrine

BuildArch: noarch

%description
Arc is a flat theme with transparent elements.
It supports MATE, GNOME, Budgie, Xfce, and Cinnamon.

%package -n gtk2-theme-Arc-lighter
Group: Graphical desktop/GNOME
Summary: Arc-dark GTK theme
Group: Graphical desktop/GNOME
Requires: libgtk-engine-murrine
%description -n gtk2-theme-Arc-lighter
%summary

%package -n gtk2-theme-Arc-dark
Group: Graphical desktop/GNOME
Summary: Arc-dark GTK theme
Group: Graphical desktop/GNOME
Requires: libgtk-engine-murrine
%description -n gtk2-theme-Arc-dark
%summary

%package -n gtk2-theme-Arc-darker
Group: Graphical desktop/GNOME
Summary: Arc-darker GTK themeer
Group: Graphical desktop/GNOME
Requires: libgtk-engine-murrine
%description -n gtk2-theme-Arc-darker
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/themes/Arc/*

%files -n gtk2-theme-Arc-lighter
%_datadir/themes/Arc-Lighter/*

%files -n gtk2-theme-Arc-dark
%_datadir/themes/Arc-Dark/*

%files -n gtk2-theme-Arc-darker
%_datadir/themes/Arc-Darker/*

%changelog
* Mon Dec 19 2022 Grigory Ustinov <grenka@altlinux.org> 20221218-alt1
- Automatically updated to 20221218.

* Fri Jul 22 2022 Grigory Ustinov <grenka@altlinux.org> 20220405-alt1
- Built new version (Closes: #43040).
- Built from new upstream.
- Added Arc-lighter theme.

* Wed Jan 16 2019 Konstantin Artyushkin <akv@altlinux.org> 20170302-alt1.git20170302
- new version

* Tue Oct 11 2016 Konstantin Artyushkin <akv@altlinux.org> 20161005-alt1.git20161005
- new version

* Mon Apr 04 2016 Konstantin Artyushkin <akv@altlinux.org> 20160331-alt1.git20160331
- new version

* Sun Nov 29 2015 Konstantin Artyushkin <akv@altlinux.org> 20150922-alt1.git27809c6
- new version

