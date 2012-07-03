Name: libgtk-engine-equinox
Version: 1.30.2
Release: alt1
Summary: Equinox GTK Engine

Group: Graphical desktop/GNOME
License: GPL
Url: http://gnome-look.org/content/show.php/Equinox+GTK+Engine?content=121881

Source: equinox-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libgtk+2-devel

%description
A heavily modified version of the beautiful Aurora engine

%package -n gtk2-themes-equinox
Summary: Equinox GTK2 themes
Group: Graphical desktop/GNOME
Requires: libgtk-engine-equinox = %version-%release
Requires: icon-theme-faenza
BuildArch: noarch

%description -n gtk2-themes-equinox
Equinox GTK2 themes:
 Equinox
 Equinox Classic
 Equinox Classic Glass
 Equinox Evolution
 Equinox Evolution Light
 Equinox Evolution Rounded
 Equinox Evolution Squared
 Equinox Glass
 Equinox Light
 Equinox Light Glass
 Equinox Wide

%prep
%setup -q -n equinox-%version
tar xzf equinox-gtk-engine.tar.gz
tar xzf equinox-themes.tar.gz

%build
pushd equinox-1.30 > /dev/null
    %configure --enable-animation
    %make_build
popd

%install
pushd equinox-1.30 > /dev/null
    %makeinstall_std
popd
mkdir -p %buildroot%_datadir/{doc/%name-%version,themes}
mv "Equinox Evolution.crx" %buildroot%_datadir/doc/%name-%version
cp userChrome.css %buildroot%_datadir/doc/%name-%version
install -m644 equinox-1.30/{COPYING,ChangeLog} %buildroot%_datadir/doc/%name-%version
cp -R Equinox* %buildroot%_datadir/themes

%files
%_libdir/gtk-2.0/2.10.0/engines/*
%_datadir/doc/%name-%version

%files -n gtk2-themes-equinox
%_datadir/themes/*

%changelog
* Mon Jan 24 2011 Vladimir Lettiev <crux@altlinux.ru> 1.30.2-alt1
- initial build

