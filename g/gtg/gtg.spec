Name: gtg
Version: 0.2.5
Release: alt1

Source: %name-%version.tar
License:  GPL3
Group: Office
URL: http://gtg.fritalk.com/
Packager: Damir Shayhutdinov <damir@altlinux.ru>

Summary: Getting Things Gnome - personal organizer for the GNOME desktop environment

BuildPreReq: python-devel rpm-build-python python-module-pygtk python-module-pyxdg python-module-pygtk-libglade
BuildArch: noarch

Requires: python-module-pygtk-libglade
%description
GTG(Getting Things Gnome) is a personal organizer for the GNOME desktop environment,
it focuses on ease of use and flexibility, while keeping things simple.

%prep
%setup

%build
%python_build 

%install
%python_install

%files 
%doc %_man1dir/*
%_bindir/*
%python_sitelibdir/GTG/
%_datadir/%name/
%_datadir/locale/*/LC_MESSAGES/*.mo
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/dbus-1/services/*
%exclude %python_sitelibdir/GTG/plugins/geolocalized_tasks*

%changelog
* Tue Jan 31 2012 Alexey Morsov <swi@altlinux.ru> 0.2.5-alt1
- new version
- RTM sync plugin added

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.4-alt0.1.1
- Rebuild with Python-2.7

* Wed Apr 27 2011 Alexey Morsov <swi@altlinux.ru> 0.2.4-alt0.1
- new version
- spec fix

* Thu Mar 25 2010 Damir Shayhutdinov <damir@altlinux.ru> 0.2.3-alt1
- Updated to 0.2.3

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with python 2.6

* Sat Mar 21 2009 Damir Shayhutdinov <damir@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux

