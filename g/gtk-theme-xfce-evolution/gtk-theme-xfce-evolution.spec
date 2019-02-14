%define theme_name "Xfce Evolution"

Name: gtk-theme-xfce-evolution
Version: 5.6.7
Release: alt1
Summary: Xfce Evolution is a Gtk2 & Gtk3 themes
Group: Graphical desktop/XFce

License: %gpl2plus
URL: http://itgroup.ro/xfce-evolution
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: gtk2-theme-xfce-evolution = %version-%release
Requires: gtk3-theme-xfce-evolution = %version-%release
Requires: xfwm4-theme-xfce-evolution = %version-%release

%define _unpackaged_files_terminate_build 1

%description
Xfce Evolution is a Gtk2 & Gtk3 theme aimed at providing increased consistency
across the most commonly used GUI toolkits on the Xfce desktop (Gtk2/3, Qt4/5,
wxWidgets2/3, Open/LibreOffice); additionally, Xfce Evolution tries to be
"compatible" with the default Gtk3 theme 'Adwaita' in the sense that
an application GUI deskgned to look good on Adwaita should also look
good on Xfce Evolution.

Xfce Evolution is based on, and/or derived from:
  Greybird theme (xfwm4)
  Adwaita theme (gtk3, gtk3-csd)
  Ambiance theme (gtk2, wxWidgets2/3, qt4/5)
  Gtk2 Murrine Engine (gtk2, wxWidgets2/3, qt4/5)
  Qt5 Style Plugins (qt5+)


%package -n gtk2-theme-xfce-evolution
Summary: Xfce Evolution GTK+2 themes
Group: Graphical desktop/XFce
Requires: libgtk-engine-murrine

%description -n gtk2-theme-xfce-evolution
Themes for GTK+2 as part of the Xfce Evolution theme.

%package -n gtk3-theme-xfce-evolution
Summary: Xfce Evolution GTK+3 themes
Group: Graphical desktop/XFce

%description -n gtk3-theme-xfce-evolution
Themes for GTK+3 as part of the Xfce Evolution theme.

%package -n xfwm4-theme-xfce-evolution
Summary: Xfce Evolution Xfwm4 themes
Group: Graphical desktop/XFce

%description -n xfwm4-theme-xfce-evolution
Themes for Xfwm4 as part of the Xfce Evolution theme.

%prep
%setup
find -type f -executable -not -name "*.sh" -exec chmod -x '{}' \;

%install
mkdir -p %buildroot%_datadir/themes/%theme_name/
cp -r %theme_name/{gtk-2.0,gtk-3.0,xfwm4}/ %buildroot%_datadir/themes/%theme_name/

find -maxdepth 1 -type d -name %theme_name" *" | while read l; do
	mkdir %buildroot%_datadir/themes/"$l"/
	cp -r "$l"/{gtk-2.0,gtk-3.0}/ %buildroot%_datadir/themes/"$l"/
done

%files

%files -n gtk2-theme-xfce-evolution
%_datadir/themes/*/gtk-2.0/

%files -n gtk3-theme-xfce-evolution
%_datadir/themes/*/gtk-3.0/

%files -n xfwm4-theme-xfce-evolution
%_datadir/themes/*/xfwm4/

%changelog
* Thu Feb 14 2019 Mikhail Efremov <sem@altlinux.org> 5.6.7-alt1
- Initial build.
