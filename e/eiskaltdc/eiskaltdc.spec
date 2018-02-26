Name: eiskaltdc
Version: 1.0.41
Release: alt2.1
Summary: EiskaltDC++ - Direct Connect client with QT gui. Valknut fork
License: GPLv3
Group: Networking/File transfer
Url: http://sourceforge.net/projects/eiskaltdc/
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>
Epoch: 1

Source: %name-%version.tar
Patch: eiskaltdc-1.0.41-alt-DSO.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libqt4-devel bzlib-devel libxml2-devel

%description
EiskaltDC++ is a program that uses the Direct Connect protocol. 
It is compatible with other DC clients, such as the original DC from Neomodus, 
DC++ and derivatives. EiskaltDC++ also interoperates with all common DC hub software.

%prep
%setup
%patch -p2

%build
%cmake
%make_build -C BUILD

%install
%makeinstall -C BUILD DESTDIR="%buildroot/" install

%files
%_bindir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_pixmapsdir/*
%_man1dir/*
%doc COPYING COPYING.OpenSSL

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.41-alt2.1
- Fixed build

* Sun Nov 21 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1:1.0.41-alt2
- Rebuild with new openssl

* Sat Mar 13 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1:1.0.41-alt1
- Update to latest version (1.0.41)
- Project freezed (new poject - eiskaltdcpp)

* Mon Dec 14 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.1.0-alt0.2.svn653
- Switch from autotools to cmake

* Sat Dec 12 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.1.0-alt0.1.svn653
- Update to revision 653 (formelly 1.0.40 version)

* Sun Oct 18 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.1.0-alt0.1.svn491
- Update to revision 491 (formelly 1.0.3-RC3 version)

* Sun Sep 20 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.1.0-alt0.1.svn361
- Update to revision 361 (formelly 1.0.2 version)
- Remove movabletabs.patch (not needed anymore)

* Tue Sep 08 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.1.0-alt0.1.svn322
- Update to revision 322
  + Dynamic css-style loading
  + Private chat: outgoing messages do not generate notification event
  + New private message indication by tray icon
  + Multiple antispam keys now available by splitting phrase with | symbol
  + Updated man page
  + Autoconnect checkbox added to hublist items
- Update patch for movable tabs and close button on tabs

* Sat Aug 29 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt1
- Added patch for movable tabs and close button on tabs

* Wed Aug 26 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.1.rc2
- License now GPLv3

* Sun Aug 23 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.1.rc1
- Update to revision 228
  + IPFilter import-export support
  + Search results grouping (default: tth)
  + Search results coloring
  
* Wed Aug 19 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 0.5.1-alt0.1.svn194
- Update to revision 194
  + Lock file and magnet file moved to program configuration path (ALT #21101)
  + IPFilter full support

* Sun Aug 16 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 0.5.1-alt0.1.svn183
- Update to revision 183
  + IPFilter support
  + AntiSpam bot support

* Mon Aug 10 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 0.5.1-alt0.1.svn143
- Update to revision 143

* Fri Aug 07 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 0.5-alt0.1
- Initial build for ALTLinux
