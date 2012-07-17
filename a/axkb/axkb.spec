Name: axkb
Version: 0.4.3
Release: alt1.85c44479.1

Summary: Antico XKB configuration utility
Group: Graphical desktop/Other
License: GPL
URL: http://github.com/disels/axkb

Packager: Boris Savelev <boris@altlinux.org>

Source0: %name-%version.tar
Patch0: axkb-0.4.3-alt-DSO.patch

# Automatically added by buildreq on Fri May 01 2009
BuildRequires: gcc-c++ libX11-devel libqt4-devel libxkbfile-devel

%description
AXKB this Qt application to adjust layouts by xkb. 
Part of the code and interface window settings taken from KXKB and Kkbswitch.
Completely absent on to the kde-libs. 
Originally developed as a complement to the Antico DE. 
But just as well work on other WM and DE. 
Depends only on Qt and X-server

%prep
%setup
%patch0 -p1

%build
qmake-qt4
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc README
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/qt4/translations/%{name}*

%changelog
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.85c44479.1
- Fixed build

* Sat Dec 19 2009 Terechkov Evgenii <evg@altlinux.ru> 0.4.3-alt1.85c44479
- update from upstream

* Sat Jun 27 2009 Boris Savelev <boris@altlinux.org> 0.4.2-alt3.gb219269
- update from upstream

* Sat Jun 06 2009 Boris Savelev <boris@altlinux.org> 0.4.2-alt2.ge69ae7c
- update from upstream

* Tue May 19 2009 Boris Savelev <boris@altlinux.org> 0.4.2-alt1.g118cc77
- update from upstream
- fix version

* Mon May 11 2009 Boris Savelev <boris@altlinux.org> 0.1-alt3.g807fa5f
- update from upstream

* Sun May 03 2009 Boris Savelev <boris@altlinux.org> 0.1-alt2.ge5dda08
- update from upstream (close: #19899)

* Fri May 01 2009 Boris Savelev <boris@altlinux.org> 0.1-alt1
- initial build for Sisyphus
