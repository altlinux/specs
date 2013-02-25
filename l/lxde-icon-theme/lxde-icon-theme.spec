Name:           lxde-icon-theme
Version:        0.5.0
Release:        alt1
Summary:        Default icon theme for LXDE

Group:          Graphical desktop/Other
License:        LGPLv3
URL:            http://nuovext.pwsp.net/
Source0:        %name-%version.tar.bz2

BuildArch:      noarch
Provides:       nuoveXT2-icon-theme = 2.2

%description
nuoveXT2 is a very complete set of icons for several operating systems. It is 
also the default icon-theme of LXDE, the Lightweight X11 Desktop Environment.


%prep
%setup

%build
%configure

%install
%makeinstall_std
touch %buildroot%_iconsdir/nuoveXT2/icon-theme.cache

%post
gtk-update-icon-cache -f -t %_iconsdir/nuoveXT2 &>/dev/null ||:

%files
%doc AUTHORS COPYING README
%ghost %_iconsdir/nuoveXT2/icon-theme.cache
%_iconsdir/nuoveXT2

%changelog
* Mon Feb 25 2013 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build in Sisyphus

