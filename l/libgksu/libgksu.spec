Name: libgksu
Version: 2.0.12
Release: alt6.1

Summary: A 'su' and 'sudo' wrapper library for GTK+/GNOME applications
License: %lgpl2plus
Group: System/Libraries
Url: http://www.nongnu.org/gksu/
Source: http://people.debian.org/~kov/gksu/%name-%version.tar.gz
Source1: libgksu-l10n.tar
Patch1: %name-2.0.12-fix-desktop-file.patch
Patch2: %name-2.0.12-helperdir.patch
Patch3: %name-only-glib.h-includes.patch
Patch4: %name-2.0.12-alt-DSO.patch

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Requires(preun,post): GConf

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.ac
BuildPreReq: libgtk+2-devel >= 2.12.0
BuildPreReq: GConf2 libGConf2-devel libstartup-notification-devel libgnome-keyring-devel libgtop2-devel intltool
BuildPreReq: gettext-tools
BuildPreReq: gtk-doc >= 1.0

BuildRequires: perl-XML-Parser

%description
GKSu is a stack of libraries and an application that provide a Gtk+
frontend to su and sudo. It supports login shells and preserving
environment when acting as a su frontend. It is useful to menu items or
other graphical programs that need to ask a user's password to run
another program as another user.

This package contains the authentication library. To use the
application, install gksu package.

%package devel
Summary: Development files for libgksu
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
GKSu is a stack of libraries and an application that provide a Gtk+
frontend to su and sudo. It supports login shells and preserving
environment when acting as a su frontend. It is useful to menu items or
other graphical programs that need to ask a user's password to run
another program as another user.

This package contains the files necessary for development/compilation of
programs that use %name.

%define libname libgksu2

%prep
%setup -q
%patch1
%patch2
%patch3 -p2
%patch4 -p2
tar xf %SOURCE1

%build
touch README NEWS
%autoreconf
%configure \
    --disable-static \
    --enable-gtk-doc

%make

%install
%make_install install DESTDIR=%buildroot
# Fix icons location
mkdir -p %buildroot%_liconsdir
cp -a %buildroot%_pixmapsdir/gksu.png %buildroot%_liconsdir

%find_lang %name

%post
%gconf2_install gksu

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall gksu
fi

%files -f %name.lang
%_libdir/%libname.so.*
%dir %_libexecdir/%name
%_libexecdir/%name/gksu-run-helper
%_bindir/gksu-properties
%dir %_datadir/%name
%_datadir/%name/gksu-properties.ui
%_pixmapsdir/gksu.png
%_liconsdir/gksu.png
%_desktopdir/gksu-properties.desktop
%_man1dir/gksu-properties.1*
%config %gconf_schemasdir/gksu.schemas

%files devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/%libname.so
%_pkgconfigdir/%libname.pc
%dir %_datadir/gtk-doc/html/%name
%_datadir/gtk-doc/html/%name/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.12-alt6.1
- Fixed build

* Tue Apr 03 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.12-alt6
- Include only glib.h in sources

* Tue Apr 03 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.12-alt5
- Complete translation on Russian and Portugese (Brasil)

* Sun Dec 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.12-alt4
- gksu-run-helper installed in %%_libexecdir not %%_libdir (ALT #24742)

* Thu Nov 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.12-alt3
- rebuild for soname set-versions

* Tue Jul 28 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0.12-alt2
- package %_datadir/%name directory
- removed Encoding key in gksu-properties.desktop - last repocop notice
  fixed :)
- fixed a typo in the preun script that led to a GConf schema left behind
  after the package removal
- fixed a problem with a missing icon (part of ALT Bug 16775)

* Tue Jul 28 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0.12-alt1
- new version (2.0.12)
- updated the list of categories in gksu-properties.desktop
- updated buildreqs

* Sun Aug 10 2008 Alexey Rusakov <ktirf@altlinux.org> 2.0.7-alt1
- new version (2.0.7)
- use macros from rpm-build-licenses and rpm-build-gnome
- use %%make_install macro instead of %%makeinstall, fixing ALT Bug 16330
- require GConf for (de)installation explicitly
- added Packager tag (thanks to repocop for a reminder)
- fixed desktop file and icons location (thanks to repocop)

* Tue Mar 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.0.4-alt1
- new version (2.0.4)
- fixed building on x86_64
- Source address has changed
- spec cleanup

* Sat Sep 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.9.8-alt1
- the first build for Sisyphus.

