Name: gnome-specimen
Version: 0.4
Release: alt1.2.1

Summary: Your favourite tool to preview and compare fonts on your GNOME desktop
Url: http://uwstopia.nl/blog/category/gnome

License: %gpl2plus
Group: Graphical desktop/GNOME
Packager: Alexey Rusakov <ktirf@altlinux.org>

Source: http://uwstopia.nl/geek/projects/%name/releases/%name-%version.tar.gz

BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-build-gnome >= 0.5
BuildPreReq: libGConf-devel GConf
# We need distutils
BuildPreReq: python-devel
BuildPreReq: intltool >= 0.35.0

BuildRequires: perl-XML-Parser

%description
A simple font preview application for GNOME.

%prep
%setup

%build
%configure --disable-schemas-install
%make

%install
%makeinstall

%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/%name
%dir %python_sitelibdir/specimen
%python_sitelibdir/specimen/*.py
%python_sitelibdir/specimen/*.pyc
%python_sitelibdir/specimen/*.pyo
%_desktopdir/%name.desktop
%dir %_datadir/%name
%dir %_datadir/%name/glade
%_datadir/%name/glade/%name.glade
%_datadir/%name/%name-about.png
%_iconsdir/hicolor/*/apps/%name.*
%gconf_schemasdir/%name.schemas

%exclude %_iconsdir/hicolor/icon-theme.cache

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.2.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.2
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.4-alt1.1.qa2
- NMU (by repocop): the following fixes applied:
  * update_menus for gnome-specimen
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gnome-specimen

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt1.1
- Rebuilt with python-2.5.

* Sun Jan 06 2008 Alexey Rusakov <ktirf@altlinux.org> 0.4-alt1
- New version (0.4).

* Sat Sep 08 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3.1-alt2
- fixed (hopefully) building on x86_64.

* Fri Sep 07 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3.1-alt1
- new version (0.3.1)

* Tue Aug 21 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt1
- Initial Sisyphus release

