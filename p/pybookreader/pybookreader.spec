Name: pybookreader
Version: 0.5.0
Release: alt6.1.qa2.1.1

Summary: PyBookReader is a PyGTK-based GUI book reader

License: GPL
Group: Text tools
Url: http://pybookreader.narod.ru/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source0: http://dl.sf.net/%name/PyBookReader-%version.tar.gz
Source1: pybookreader.desktop
Source2: ornamentbook.desktop
Source3: %name.png
Source4: fb2.xml
Source5: application-x-fb2.png
Source6: application-x-zip-compressed-fb2.png
Patch0: %name-0.4.11.patch

BuildPreReq: desktop-file-utils shared-mime-info

# Automatically added by buildreq on Mon Feb 26 2007
BuildRequires: libxml2-devel python-devel python-module-pygtk python-modules-encodings

Requires: python-module-pygtk-libglade

%description
PyBookReader is a PyGTK-based GUI book reader

%prep
%setup -q -n PyBookReader-%version
#%%patch0 -p0

%build
python setup.py build

%install
python setup.py install --root=%buildroot --record=INSTALLED_FILES

# application
install -D -m 644 %SOURCE1 %buildroot%_datadir/applications/pybookreader.desktop
install -D -m 644 %SOURCE2 %buildroot%_datadir/applications/ornamentbook.desktop
install -D -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

# mime
install -D -m 644 %SOURCE4 %buildroot%_datadir/mime/packages/fb2.xml
install -D -m 644 %SOURCE5 %buildroot%_datadir/icons/hicolor/48x48/mimetypes/application-x-fb2.png
install -D -m 644 %SOURCE6 %buildroot%_datadir/icons/hicolor/48x48/mimetypes/application-x-zip-compressed-fb2.png
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Office \
	--add-category=Viewer \
	--add-category=Literature \
	%buildroot%_desktopdir/ornamentbook.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Office \
	--add-category=Viewer \
	--add-category=Literature \
	%buildroot%_desktopdir/pybookreader.desktop

%files -f INSTALLED_FILES
%_datadir/mime/packages/*
%_datadir/applications/*
%_liconsdir/*.png
%_datadir/icons/hicolor/48x48/mimetypes/*.png
%dir %python_sitelibdir/ornamentbook
%dir %python_sitelibdir/ornamentbook/hyph_dicts
%dir %python_sitelibdir/ornamentbook/skins
%dir %python_sitelibdir/%name
%dir %python_sitelibdir/%name/dictclient

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt6.1.qa2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt6.1.qa2.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.0-alt6.1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for pybookreader
  * postclean-03-private-rpm-macros for the spec file

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.0-alt6.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for pybookreader
  * postclean-05-filetriggers for spec file

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt6.1
- Rebuilt with python 2.6

* Mon Jun 16 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.5.0-alt6
- fix subdirectory packaging

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt5.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for pybookreader

* Thu Mar 20 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.5.0-alt5
- Correct *.desktop files

* Tue Sep 11 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.5.0-alt4
- Add requires:python-module-pygtk-libglade (Bug#12733)

* Sun Mar 04 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.5.0-alt3
- Enable x-zip-compressed-fb2 mime type support (it works now:-)

* Mon Feb 26 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.5.0-alt2
- Correct buildreq

* Tue Jan 30 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.5.0-alt1
- Correct buildreq

* Mon Jan 29 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.5.0-alt0.1
- 0.5.0 + Ornament Book Reader

* Mon May 22 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.4.11-alt0.2.1
- Integrate into GNOME desktop environment

* Mon Oct 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.11-alt0.2
- fix arch (bug #8273)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.11-alt0.1
- first build for ALT Linux Sisyphus
