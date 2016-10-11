Name: gtk2-theme-arc
Version: 20161005
Release: alt1.git20161005
Summary: Arc GTK theme

Group: Graphical desktop/GNOME
License: GPL3
Url: https://github.com/horst3180/Arc-theme

Source: %name-%version.tar

BuildArch: noarch
Packager: Konstantin Artyushkin <akv@altlinux.org>
BuildRequires: libgtk+3-devel pkg-config
Requires: libgtk-engine-murrine

%description
A flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell.
Latest commit from Github

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
./autogen.sh --prefix=/usr

%install
%makeinstall_std

%files
%_datadir/themes/Arc/*

%files -n gtk2-theme-Arc-dark
%_datadir/themes/Arc-Dark/*

%files -n gtk2-theme-Arc-darker
%_datadir/themes/Arc-Darker/*

%changelog
* Tue Oct 11 2016 Konstantin Artyushkin <akv@altlinux.org> 20161005-alt1.git20161005
- new version

* Mon Apr 04 2016 Konstantin Artyushkin <akv@altlinux.org> 20160331-alt1.git20160331
- new version

* Sun Nov 29 2015 Konstantin Artyushkin <akv@altlinux.org> 20150922-alt1.git27809c6
- new version

