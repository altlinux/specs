Name: icon-theme-faenza
Version: 1.1
Release: alt1
Summary: Faenza GNOME icon theme

Group: Graphical desktop/GNOME
License: GPL
Url: http://gnome-look.org/content/show.php/Faenza?content=128143

Source: Faenza-%version.tar
Source1: distributor-logo-altlinux.svg

BuildArch: noarch
Packager: Vladimir Lettiev <crux@altlinux.ru>
BuildRequires: convert

%description
This icon theme for Gnome provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and Gnome menu items.

%package -n gtk2-themes-faenza
Group: Graphical desktop/GNOME
Summary: Faenza GNOME theme
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
%description -n gtk2-themes-faenza
%summary

%prep
%setup -q -n Faenza-%version
tar xf Faenza.tar.gz 2>/dev/null
tar xf Faenza-Ambiance.tar.gz 2>/dev/null
tar xf Faenza-Dark.tar.gz 2>/dev/null
tar xf Faenza-Darkest.tar.gz 2>/dev/null
tar xf Faenza-Darker.tar.gz 2>/dev/null
tar xf Faenza-Radiance.tar.gz 2>/dev/null
tar xf emesene-faenza-theme.tar.gz 2>/dev/null

# Fix distributor logo and start-here icon
cp %SOURCE1 ./Faenza/places/scalable/
pushd ./Faenza/places/scalable > /dev/null
    ln -sf ./distributor-logo-altlinux.svg distributor-logo.svg
    ln -sf ./start-here-gnome.svg start-here.svg
popd > /dev/null
pushd ./Faenza-Dark/places/scalable > /dev/null
    ln -sf ./start-here-gnome.svg start-here.svg
popd > /dev/null

for dir in 22 24 32 48; do
    pushd ./Faenza/places/$dir > /dev/null
        convert -background none -geometry ${dir}x${dir} \
            ../scalable/distributor-logo-altlinux.svg \
            ./distributor-logo-altlinux.png
        ln -sf ./distributor-logo-altlinux.png distributor-logo.png
        ln -sf ./start-here-gnome.png start-here.png
    popd > /dev/null

    pushd ./Faenza-Dark/places/$dir > /dev/null
        ln -sf ./start-here-gnome.png start-here.png
    popd > /dev/null
done

%build

%install
mkdir -p %buildroot%_iconsdir
cp -R ./Faenza %buildroot%_iconsdir
cp -R ./Faenza-Ambiance %buildroot%_iconsdir
cp -R ./Faenza-Dark %buildroot%_iconsdir
cp -R ./Faenza-Darkest %buildroot%_iconsdir
cp -R ./Faenza-Darker %buildroot%_iconsdir
cp -R ./Faenza-Radiance %buildroot%_iconsdir
cp -R ./emesene/themes %buildroot%_datadir


%files
%_iconsdir/Faenza
%_iconsdir/Faenza-Ambiance
%_iconsdir/Faenza-Dark
%_iconsdir/Faenza-Darkest
%_iconsdir/Faenza-Darker
%_iconsdir/Faenza-Radiance
%doc AUTHORS ChangeLog COPYING

%files -n gtk2-themes-faenza
%_datadir/themes/Faenza
%_datadir/themes/Faenza-Dark
%_datadir/themes/Faenza-Darkest

%changelog
* Thu Oct 20 2011 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- New version (1.1)

* Fri May 13 2011 Radik Usupov <radik@altlinux.org> 0.9.2-alt1
- New version (0.9.2)

* Mon Jan 24 2011 Vladimir Lettiev <crux@altlinux.ru> 0.8-alt1
- initial build

