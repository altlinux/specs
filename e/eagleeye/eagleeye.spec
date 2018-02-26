Summary: GTK FreeNX client
Name: eagleeye
Version: 0.0.1
Release: alt2.gaec8671.1.qa1.1
License: GPL
Group: Networking/Remote access
Packager: Boris Savelev <boris@altlinux.org>
Url: https://code.launchpad.net/~freenx-team/freenx-server/eagleeye
Source: %name-%version.tar

# Automatically added by buildreq on Wed Apr 29 2009
BuildRequires: python-devel python-module-tacix
BuildRequires: desktop-file-utils

%description
This package contains the FreeNX Client.

%prep
%setup

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/eagleeye.desktop

%files
%_bindir/%name
%python_sitelibdir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/*
%_man1dir/%name.*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt2.gaec8671.1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.1-alt2.gaec8671.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for eagleeye

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2.gaec8671.1
- Rebuilt with python 2.6

* Wed May 13 2009 Boris Savelev <boris@altlinux.org> 0.0.1-alt2.gaec8671
- update from upstream

* Wed Apr 29 2009 Boris Savelev <boris@altlinux.org> 0.0.1-alt1
- initial build

