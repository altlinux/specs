%set_verify_elf_method unresolved=relaxed
%define _kde4_alternate_placement 1

Name:      kmuddy
Version:   1.0.1
Release:   alt3

Summary:   MUD client powered by KDE
License:   GPLv2+
Group:     Games/Other
URL:       http://www.kmuddy.com/
Packager:  Andrey Cherepanov <cas@altlinux.ru>

Source:    %name-%version.tar.gz
Patch0:    %name-1.0-install-desktop.patch
Patch1:	   %name-fix-build.patch

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ 
BuildRequires: cmake
BuildRequires: libmxp-devel

Provides: lib%name = %version-%release
Obsoletes: lib%name

%description
KMuddy is a MUD client powered by KDE. It is a very powerful, fast,
feature-rich and easy to use MUD client.

%package devel
Summary: Development files for KMuddy
Group: Development/KDE and QT
Requires: kmuddy

%description devel
This package provides development files for KMuddy.

%prep
%setup
%patch0 -p0
%patch1 -p2

%build
%K4build

%install
%K4install
%K4find_lang --with-kde kmuddy

%files -f %name.lang
%doc AUTHORS CHANGELOG DESIGN LICENSE README Scripting-HOWTO TODO
%_kde4_bindir/%name
#%%_K4applnk/*
%_kde4_xdg_apps/*.desktop
#%%_K4iconsdir/*/*/*/*.*
%_K4srv/*.desktop
%_K4srvtyp/*.desktop
%dir %_K4apps/%name
%_K4apps/%name/
%_kde4_iconsdir/*/*/*/%name.png
%_K4libdir/*.so.*

%files devel
%_K4lib/*.so
%_K4link/*.so
%_K4includedir/%name

%changelog
* Fri Jun 08 2012 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt3
- Explicit link with zlib

* Fri Aug 26 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Fix build in Sisyphus
- Cleanup spec file

* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version 1.0.1

* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.8-alt5
- Fix build

* Wed Nov 19 2008 Andrey Cherepanov <cas@altlinux.org> 0.8-alt4
- Add missed header stdlib.h
- Remove update_desktop-database and update-menus macros
- Add xmllint requirement for documentation build

* Wed Jan 16 2008 Andrey Cherepanov <cas@altlinux.ru> 0.8-alt3
- Fix build with new GNU autotools

* Mon Oct 22 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8-alt2
- Fix icon pathes

* Mon Oct 15 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8-alt1
- Split to several packages

* Fri Oct 12 2007 Andrey Cherepanov <cas@altlinux.ru> 0.8-alt0
- Initial implementation
