%define over rc1
Summary: One-click Windows package manager / wine frontend
Name: wine-doors
Version: 0.1.3
Release: alt3.1.1
Vendor: Wine-Doors
License: GPL
Packager: Boris Savelev <boris@altlinux.org>
Group: Emulators
Url: http://www.wine-doors.org
Source: http://www.wine-doors.org/releases/%name-%version.tar.gz
Patch: wine.py.patch
Requires: cabextract, unzip, liborange, /usr/bin/wine
ExclusiveArch: %ix86

# Automatically added by buildreq on Sat Jan 31 2009
BuildRequires: cabextract liborange
BuildRequires: python-module-PyXML python-module-pygnome-desktop
BuildRequires: python-module-pygtk-libglade python-modules-email
BuildRequires: python-modules-encodings unzip /usr/bin/wine

%description
Wine doors is an application designed to assist users in obtaining, installing,
uninstalling and working around the caveats associated with wine applications.
Using a web service to connect users to applications means wine-doors can be
community managed thus splitting application installation and configuration
from the user interface used to install the applications.

%prep
%setup -n %name-%version
%patch0 -p0

%install
mkdir -p %buildroot
python setup.py install --root %buildroot -S --temp=%buildroot --prefix=%prefix
mv %buildroot%_prefix/etc %buildroot%_sysconfdir
%files
%doc INSTALL LICENSE README
%_bindir/%name
%_datadir/%name
%_desktopdir/*
%_pixmapsdir/*
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/preferences.xml

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt3.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt3.1
- Rebuilt with python 2.6

* Wed Mar 04 2009 Boris Savelev <boris@altlinux.org> 0.1.3-alt3
- realy fix #19050

* Wed Mar 04 2009 Boris Savelev <boris@altlinux.org> 0.1.3-alt2
- fix #19050

* Wed Feb 11 2009 Boris Savelev <boris@altlinux.org> 0.1.3-alt1
- new version (0.1.3)

* Fri Jan 30 2009 Boris Savelev <boris@altlinux.org> 0.1.3-alt1.rc1
- initial build for Sisyphus

* Thu Jan 29 2009 Karl Lattimer <karl@wine-doors.org>
- Fixed problem with %_sysconfdir/wine-doors/preferences.xml

* Sun Jan 18 2009 Andrew Stormont <andyjstormont@googlemail.com>
- Updated for 0.1.3rc1

* Sun Jan 20 2008 Karl Lattimer <karl@wine-doors.org>
- Initial RPM build
- 0.1.2-1
