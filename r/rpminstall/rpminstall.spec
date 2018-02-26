BuildRequires: desktop-file-utils

Name:		rpminstall
Version:	1.1.3
Release:	alt1
Summary:	Graphical application for install RPM packages using apt-get

License:	GPL
Group:		System/Configuration/Packaging
URL:		http://www.altlinux.org/Rpminstall

Packager:   	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar.gz

BuildRequires: gcc-c++ libqt4-devel
Requires: packageinstall

%description
Graphical application for install RPM packages using apt-get.

%prep
%setup -q
lrelease-qt4 %name.pro
DESTDIR=%buildroot PREFIX=/usr qmake-qt4 %name.pro

%build
%make_build

%install
%makeinstall
install -Dm644 apturl.js %buildroot%_libdir/firefox/defaults/preferences/apturl.js

%files
%doc AUTHORS README
%_bindir/%name
%dir %_datadir/apps/%name/
%_datadir/apps/%name/*
%_desktopdir/%name.desktop
%_datadir/services/apt.protocol
%_niconsdir/%name.png
%_libdir/firefox/defaults/preferences/apturl.js

%changelog
* Thu Dec 08 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- Move menu entry to System menu (like Synaptic)

* Mon Aug 29 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Remove apt:// prefix from arguments (thanks viy@) (closes: #26170)

* Mon Aug 01 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Complete support of apt:// protocol in Firefox (thanks viy@)

* Tue Jul 26 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Use for support apt:// protocol
- Hide interactive bar by default

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for rpminstall

* Mon Dec 27 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt3
- unhide desktop entry

* Wed Nov 10 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt2
- hide desktop entry in menu
- fix URL of project site (thanks Lenar Shakirov)

* Sun Sep 19 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial release to Sisyphus
