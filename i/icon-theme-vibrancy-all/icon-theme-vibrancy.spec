
Name: icon-theme-vibrancy-all
Version: 2.6
Release: alt3
Summary: full set of Vibrancy GNOME icon theme

Group: Graphical desktop/GNOME
License: GPL2
Url: http://www.ravefinity.com/p/vibrancy-colors-gtk-icon-icons.html

Source: vibrancy-%version.tar
Source1: distributor-logo-altlinux.svg

BuildArch: noarch
Packager: Konstantin Artyushkin <akv@altlinux.org>
Requires:icon-theme-vibrancy-colors
Requires:icon-theme-vibrancy-light
Requires:icon-theme-vibrancy-dark
Requires:icon-theme-vibrancy-full-dark
Requires:icon-theme-vibrancy-nonmono-light
Requires:icon-theme-vibrancy-nonmono-dark
Requires:icon-theme-vibrancy-docs

%description
This theme icons for Gnome provides icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and Gnome menu items.

%package -n icon-theme-vibrancy-docs
Group: Graphical desktop/GNOME
Summary: Vibrancy GNOME icons docs
Group: Graphical desktop/GNOME
%description -n icon-theme-vibrancy-docs
%summary

%package -n icon-theme-vibrancy-colors
Group: Graphical desktop/GNOME
Summary: Vibrancy-Colors GNOME icons
Group: Graphical desktop/GNOME
Requires:icon-theme-vibrancy-docs
%description -n icon-theme-vibrancy-colors
%summary

%package -n icon-theme-vibrancy-light
Group: Graphical desktop/GNOME
Summary: Vibrancy-Light GNOME icons
Group: Graphical desktop/GNOME
Requires:icon-theme-vibrancy-docs
%description -n icon-theme-vibrancy-light
%summary

%package -n icon-theme-vibrancy-dark
Group: Graphical desktop/GNOME
Summary: Vibrancy-Dark GNOME icons
Group: Graphical desktop/GNOME
Requires:icon-theme-vibrancy-docs
%description -n icon-theme-vibrancy-dark
%summary

%package -n icon-theme-vibrancy-full-dark
Group: Graphical desktop/GNOME
Summary: Vibrancy-Full-Dark GNOME icons
Group: Graphical desktop/GNOME
Requires:icon-theme-vibrancy-docs
%description -n icon-theme-vibrancy-full-dark
%summary

%package -n icon-theme-vibrancy-nonmono-light
Group: Graphical desktop/GNOME
Summary: Vibrancy-NonMono-Light GNOME icons
Group: Graphical desktop/GNOME
Requires:icon-theme-vibrancy-docs
%description -n icon-theme-vibrancy-nonmono-light
%summary

%package -n icon-theme-vibrancy-nonmono-dark
Group: Graphical desktop/GNOME
Summary: Vibrancy-NonMono-Dark GNOME icons
Group: Graphical desktop/GNOME
Requires:icon-theme-vibrancy-docs
%description -n icon-theme-vibrancy-nonmono-dark
%summary

%prep
%setup -q -n vibrancy-%version

#rename Copyrights&Licenses.txt
mv "Copyrights&Licenses.txt" CopyrightsLicenses.txt

# Fix distributor logo 
for i in $(ls | grep Vibrancy); do 
	cp %SOURCE1 ./$i/places/scalable/
done


%build

%install
mkdir -p %buildroot%_iconsdir
cp -R ./Vibrancy-* %buildroot%_iconsdir



%files 

%files -n icon-theme-vibrancy-docs
%doc README-Manual.txt CopyrightsLicenses.txt

%files -n icon-theme-vibrancy-colors
%_iconsdir/Vibrancy-Colors
%_iconsdir/Vibrancy-Colors-*

%files -n icon-theme-vibrancy-light
%_iconsdir/Vibrancy-Light-*

%files -n icon-theme-vibrancy-dark
%_iconsdir/Vibrancy-Dark-*/*

%files -n icon-theme-vibrancy-full-dark
%_iconsdir/Vibrancy-Full-Dark-*

%files -n icon-theme-vibrancy-nonmono-dark
%_iconsdir/Vibrancy-NonMono-Dark-*

%files -n icon-theme-vibrancy-nonmono-light
%_iconsdir/Vibrancy-NonMono-Light-*

%changelog
* Wed Nov 18 2015 Konstantin Artyushkin <akv@altlinux.org> 2.6-alt3
- inital pack for altlinux

