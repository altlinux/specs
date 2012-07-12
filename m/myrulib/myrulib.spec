Name: myrulib
Version: 0.28.7
Release: alt1.1

Summary: Tool for maintaining fb2 files collection
Url: http://myrulib.lintest.ru/
Source: %name-%version.tar
License: GPL

Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Group: Office

BuildRequires: wxGTK-devel gcc-c++ libsqlite3-devel libexpat-devel  bakefile

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
mkdir -p %buildroot/usr/share/icons/hicolor/32x32/apps/
install sources/MyRuLib/desktop/home-32x32.png %buildroot/usr/share/icons/hicolor/32x32/apps/myrulib.png
mkdir -p  %buildroot/usr/share/icons/hicolor/64x64/apps/
install sources/MyRuLib/desktop/home-64x64.png %buildroot/usr/share/icons/hicolor/64x64/apps/myrulib.png
%find_lang %name

%files -f %name.lang
%_bindir/myrulib
/usr/share/applications/myrulib.desktop
/usr/share/icons/hicolor/32x32/apps/myrulib.png
/usr/share/icons/hicolor/64x64/apps/myrulib.png

%changelog
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

