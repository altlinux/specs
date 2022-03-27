%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define ver_major 0.5
%define rdn_name info.olasagasti.revelation

Name: revelation
Version: %ver_major.4
Release: alt1.1

Summary: Password manager for the GNOME 3 desktop
License: GPL-2.0
Group: Graphical desktop/GNOME
Url: http://revelation.olasagasti.info/

%if_disabled snapshot
Source: https://github.com/mikelolasagasti/%name/archive/%name-%version/%name-%version.tar.gz
%else
Vcs: https://github.com/mikelolasagasti/revelation.git
Source: %name-%version.tar
%endif

BuildArch: noarch

%define python_ver 3.7
%define gtk_ver 3.22

Requires: dconf
Requires: libgtk+3-gir >= %gtk_ver

BuildRequires(pre): meson rpm-build-python3 rpm-build-gir
BuildRequires: shared-mime-info desktop-file-utils %_bindir/appstream-util
BuildRequires: libgtk+3-gir-devel >= %gtk_ver
BuildRequires: python3-module-pygobject3-devel
BuildRequires: python3-module-pycryptodomex
BuildRequires: python3-module-pwquality

%description
Revelation is a password manager for the GNOME desktop. It stores all
your accounts and passwords in a single, secure place, and gives you
access to it through a user-friendly graphical interface.

%prep
%setup -n %name%{?_disable_snapshot:-%name}-%version
# fix for build with meson >= 0.61
sed -i '/^[[:space:]]*appdata\,/d' data/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=Settings \
	--add-category=X-PersonalSettings \
	--add-category=GTK \
	%buildroot%_desktopdir/%rdn_name.desktop

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%python3_sitelibdir/%name/
%_datadir/mime/packages/revelation.xml
%_datadir/%name
%_iconsdir/hicolor/*x*/*/*.png
%_iconsdir//hicolor/scalable/*/*.svg
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.appdata.xml

%changelog
* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1.1
- fixed build with meson >= 0.61

* Sun Oct 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4 (ported to Meson build sysytem)

* Thu Sep 17 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3 (ported to PyGobject3/GTK3 and PyCryptodome)

* Thu Feb 06 2020 Yuri N. Sedunov <aris@altlinux.org> 0.4.14-alt1.1
- add explicit python2 in all shebangs

* Mon Jan 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.14-alt1
- 0.14.4

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.13-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for revelation

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
