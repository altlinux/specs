Name: notemeister
Version: 0.1.7
Release: alt7.qa4.1

Summary: NOTEMEISTER is a notes organizing tool for the GNOME2 desktop.

License: GPL
Group: Text tools
Url: http://notemeister.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: %name.png
Patch: %name-%version.patch

BuildArchitectures: noarch

Requires: PyXML
# fixme
Requires: python-module-pygnome-gconf, python-module-pygtk-libglade, python-module-pygnome-bonobo

# Automatically added by buildreq on Sun Jun 20 2004
BuildRequires: python-base python-dev python-modules-encodings

%description
NOTEMEISTER is a notes organizing tool for the GNOME2 desktop.

%description -l ru_RU.KOI8-R
NOTEMEISTER - программа для хранения заметок, предназначенная
для GNOME2.

%prep
%setup
%patch
%__subst "s|doc/%name|share/doc/%name|" setup.py
%__subst "s|ICON_SIZE_POPUP|#ICON_SIZE_POPUP|" src/lib/Stock.py

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_liconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=NoteMeister
Comment=Note organizating tool
Icon=%{name}
Exec=%name
Terminal=false
Categories=AudioVideo;Music;
EOF

%files -f INSTALLED_FILES
%_desktopdir/%{name}.desktop
%dir %_datadir/%name
%dir %_datadir/%name/pixmaps
%dir %_docdir/%name-%version
#%python_sitelibdir/%name
%_liconsdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.7-alt7.qa4.1
- Rebuild with Python-2.7

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt7.qa4
- NMU: converted debian menu to freedesktop

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.7-alt7.2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for notemeister
  * postclean-05-filetriggers for spec file

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt7.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.1.7-alt7.1
- Rebuilt with python-2.5.

* Fri Jul 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt7
- add correct requires: fix bug #6139

* Thu Mar 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt6
- drop strict find
- rebuild with python 2.4

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt5
- enable strict find requires
- remove requires from spec

* Tue Sep 07 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt4
- add python-module-gnome-bonobo requires

* Sun Aug 01 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt3
- add PyXML requires

* Fri Jul 23 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt2
- remove unneed icon_size_registry

* Thu Jul 15 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt1
- new version

* Sun Jun 20 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt0.1
- first build for Sisyphus

