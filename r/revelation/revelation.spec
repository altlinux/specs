%define ver_major 0.4
%define _unpackaged_files_terminate_build 1

Name: revelation
Version: %ver_major.13
Release: alt1

Summary: Keyring management program for the GNOME Desktop
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://oss.codepoet.no/%name

#Source: %name.tar
Source: ftp://oss.codepoet.no/%name/%name-%version.tar.xz
Patch: %name-0.4.12-alt1-configure.patch
Patch1: %name-0.4.13-alt-ru.po.patch

%define GConf_ver 2.10.0
PreReq: GConf >= %GConf_ver

BuildRequires: rpm-build-gnome rpm-build-licenses
BuildRequires: shared-mime-info intltool desktop-file-utils
BuildRequires: cracklib-devel cracklib-utils
BuildRequires: GConf libGConf-devel
BuildPreReq: python-module-pygtk-devel >= 2.8.0
BuildPreReq: python-module-pygnome-devel >= 2.10.0
BuildRequires: python-module-dbus-devel

BuildRequires: python-module-Crypto
BuildRequires: python-module-cracklib
BuildRequires: python-module-pygnome-gconf

%description
This a keyring management program for the GNOME Desktop.

%prep
%setup -n %name-%version
%patch -p1
%patch1

%build
%autoreconf
%configure \
		--disable-schemas-install \
		--disable-desktop-update \
		--disable-mime-update

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/%name
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/*.py
%python_sitelibdir/%name/*.pyc
%python_sitelibdir/%name/*.pyo
%dir %python_sitelibdir/%name/bundle
%dir %python_sitelibdir/%name/datahandler
%python_sitelibdir/%name/*/*.py
%python_sitelibdir/%name/*/*.pyc
%python_sitelibdir/%name/*/*.pyo
%_desktopdir/%name.desktop
%_datadir/mime/packages/revelation.xml
%_datadir/%name
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/*x*/apps/%name-locked.png
%_iconsdir/hicolor/*x*/mimetypes/gnome-mime-application-x-%name.png
%_iconsdir//hicolor/scalable/apps/revelation.svg
%config %gconf_schemasdir/%name.schemas

%changelog
* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.13-alt1
- 0.4.13 release

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.12-alt2
- build from current hg-repo

* Sat Apr 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.12-alt1
- 0.4.12

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.11-alt5.1
- Rebuild with Python-2.7

* Fri May 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.11-alt5
- disabled obsolete bonobo-applet

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.11-alt4.1
- Rebuilt with python 2.6

* Thu Mar 19 2009 Alexey Rusakov <ktirf@altlinux.org> 0.4.11-alt4
- Fixed crash due to an IndexError inside revelation.
- Removed deprecated macros from the specfile.
- Used RPM macros from rpm-build-gnome.
- Looks like upstream has disappeared :(

* Tue May 13 2008 Alexey Rusakov <ktirf@altlinux.org> 0.4.11-alt3
- Included missing subdirectories in the file list.
- Updated the License tag.

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.4.11-alt2.1
- Rebuilt with python-2.5.

* Mon Mar 19 2007 Alexey Rusakov <ktirf@altlinux.org> 0.4.11-alt2
- fixed building on x86_64

* Sun Mar 18 2007 Alexey Rusakov <ktirf@altlinux.org> 0.4.11-alt1
- new version, taken the package from orphaned.
- spec cleanup
- updated buildreqs
- removed Debian menu support
- _unpackaged_files_terminate_build from now on.

* Fri Apr 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Wed Mar 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt1
- First build for Sisyphus.
