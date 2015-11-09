Name:           mozo
Version:        1.12.0
Release:        alt1
Summary:        MATE Desktop menu editor

Group:		Graphical desktop/MATE
License:        LGPLv2+
URL:            http://mate-desktop.org
Source0:        %name-%version.tar
#VCS: 		https://github.com/mate-desktop/mozo

BuildRequires:  mate-common 
BuildRequires:  mate-menus-devel
BuildRequires:  python-devel
BuildRequires:  python-module-pygobject-devel
BuildRequires:  desktop-file-utils

Requires:       mate-menus

Provides:  mate-menu-editor = %version-%release
Obsoletes: mate-menu-editor < %version-%release

BuildArch:  noarch

%description
MATE Desktop menu editor.

%prep
%setup 

%build
%autoreconf
%configure
%make_build V=1

%install
%makeinstall_std

desktop-file-install                                  \
        --dir=%buildroot%_desktopdir    \
        %buildroot%_desktopdir/%name.desktop

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/%name
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/%name/
%_desktopdir/%name.desktop
%python_sitelibdir/Mozo/
%_man1dir/%name.1.*

%changelog
* Mon Nov 09 2015 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- Initial build in Sisyphus
