Name: myrulib
Version: 0.29.11
Release: alt1

Summary: Tool for maintaining fb2 files collection

Url: http://myrulib.lintest.ru/
Source: %name-%version.tar
License: GPL

# git://gitorious.org/myrulib/lintest.git
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Group: Office

# Automatically added by buildreq on Sat Feb 02 2013
# optimized out: fontconfig gnu-config libgdk-pixbuf libstdc++-devel libsystemd-daemon libwayland-client libwayland-server pkg-config
BuildRequires: bzlib-devel gcc-c++ libexpat-devel libsqlite3-devel libwxGTK-devel libxml2-devel

BuildRequires: bakefile

%description
Tool for maintaining home library, contaning fb2 files. Supports search,
export and so on.

%prep
%setup

%build
%configure --with-expat
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
%makeinstall_std
mkdir -p %buildroot%_iconsdir/hicolor/32x32/apps/
install sources/MyRuLib/desktop/home-32x32.png %buildroot%_iconsdir/hicolor/32x32/apps/myrulib.png
mkdir -p  %buildroot%_iconsdir/hicolor/64x64/apps/
install sources/MyRuLib/desktop/home-64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/myrulib.png
%find_lang %name

%files -f %name.lang
%_bindir/myrulib
%_desktopdir/myrulib.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/32x32/apps/myrulib.png
%_iconsdir/hicolor/48x48/apps/myrulib.png
%_iconsdir/hicolor/64x64/apps/myrulib.png

%changelog
* Sat Feb 02 2013 Vitaly Lipatov <lav@altlinux.ru> 0.29.11-alt1
- build new version
- update buidreqs

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.28.7-alt1.1
- Fixed build

* Tue Jul 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.28.7-alt1
- new version

* Tue May 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.27.4-alt1
- new version

* Tue Nov 09 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.24.18-alt1
- new version
- upstream git used

* Mon Apr 05 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.21-alt1
- new version
- translations

* Mon Feb 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.19-alt1
- new version

* Tue Dec 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.17-alt1
- new version
- compilation flags added

* Wed Dec 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.16-alt1
- initial build

