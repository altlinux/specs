BuildRequires: desktop-file-utils
%def_enable nautilus

Name: gksu
Version: 2.0.2
Release: alt4

Summary: A Gtk+-based 'su' wrapper
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://www.nongnu.org/%name/

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: http://people.debian.org/~kov/%name/%name-%version.tar.gz
Source1: %name-l10n.tar
Patch2: nautilus-%name-2.0.2-fix-handler-invocation.patch
Patch3: 01_desktop_in.patch
Patch4: 02_format_security.patch
Patch5: 50_always_ask.patch
Patch6: 99_intltool.patch
Patch7: %name-only-glib.h-includes.patch

# From configure.ac
%define libgksu_ver 1.9.8
%define gtk_ver 2.4.0

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.ac
BuildPreReq: libgksu-devel >= %libgksu_ver
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: gettext-tools intltool
BuildPreReq: gtk-doc >= 1.0
%{?_enable_nautilus:BuildPreReq: libnautilus-devel gnome-vfs-devel}

BuildRequires: perl-XML-Parser

%description
GKSu is a stack of libraries and an application that provide a Gtk+
frontend to su and sudo. It supports login shells and preserving
environment when acting as a su frontend. It is useful to menu items or
other graphical programs that need to ask a user's password to run another
program as another user.

%if_enabled nautilus
%package -n nautilus-%name
Summary: A plugin for Nautilus to open files as a privileged user
Group: Graphical desktop/GNOME

%description -n nautilus-%name
This package contains a plugin for Nautilus that integrates su and sudo
into the file manager by means of GKSu software.
%endif

%prep
%setup -q
%patch7 -p2
%patch2 -p0 -b .fix-handler-invocation
%patch3 -p1 
%patch4 -p1 
%patch5 -p1 
%patch6 -p1 
tar xf %SOURCE1
# Remove deprecated line from .desktop file.
sed -i '/^Encoding/d' %name.desktop

%build
export CPPFLAGS="$CPPFLAGS `pkg-config --cflags-only-I gnome-vfs-2.0`"
export LDFLAGS="$LDFLAGS `pkg-config --libs gnome-vfs-2.0`"
%configure \
    %{?_enable_nautilus:--enable-nautilus-extension} \
    --disable-static \
    --enable-gtk-doc

%make_build nautilus_extensiondir=%nautilus_extdir

%install
%makeinstall_std nautilus_extensiondir=%nautilus_extdir

# Copy the icon to the standard location
mkdir -p %buildroot%_liconsdir
cp -a %buildroot%_pixmapsdir/%name-*.png %buildroot%_liconsdir/

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=System \
	%buildroot%_desktopdir/gksu.desktop

%files -f %name.lang
%_bindir/gksu
%_bindir/gksudo
%dir %_datadir/%name
%_datadir/%name/gksu-migrate-conf.sh
%_pixmapsdir/%name-*.png
%_liconsdir/%name-*.png
%_desktopdir/%name.desktop
%_man1dir/*.1.gz

%files -n nautilus-gksu
%nautilus_extdir/libnautilus-%name.so
%exclude %nautilus_extdir/*.la

%changelog
* Tue Apr 03 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt4
- Include only glib.h in sources

* Tue Apr 03 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt3
- Apply patches from Debian
- Complete translation on ar, ca, de, hu, ja, ko, pt_BR, ru and th

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.2-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gksu
  * postclean-03-private-rpm-macros for the spec file

* Tue Jul 28 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0.2-alt2
- Fixed incorrect invocation of a MIME type handler in nautilus-gksu.

* Tue Jul 28 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0.2-alt1
- New version (2.0.2).
- Updated buildreqs.

* Wed Dec 24 2008 Alexey Rusakov <ktirf@altlinux.org> 2.0.0-alt3
- Thanks to repocop:
  + Added Packager tag.
  + Remove 'Encoding' key from the .desktop file, it is deprecated.
  + Copy icons to the standard location.

* Sat Sep 13 2008 Alexey Rusakov <ktirf@altlinux.org> 2.0.0-alt2
- Use rpm-build-licenses and put the correct License.
- Fixed buildreqs and quickfixed building breakage (nautilus got rid
  of gnome-vfs, and gksu nautilus extension appeared to link with gnome-vfs
  implicitly).
- Updated the Nautilus extension to a new location for Nautilus extensions
  and separated it to a sub-package; use rpm-build-gnome.

* Tue Mar 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.0.0-alt1
- new version (2.0.0)
- Source address changed.

* Sat Sep 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.9.4-alt1
- The first build for Sisyphus.

