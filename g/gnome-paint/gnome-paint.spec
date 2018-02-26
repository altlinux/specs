Name: gnome-paint
Version: 0.4.0
Release: alt1
Summary: Easy to use paint program for GNOME

Group: Graphics
License: GPLv3
Url: http://code.google.com/p/gnome-paint/
Packager: Radik Usupov <radik@altlinux.org>

Source: http://gnome-paint.googlecode.com/files/%name-%version.tar.gz

Patch: %name.packaging.patch

BuildRequires: intltool gtk2-devel desktop-file-utils
#Requires:

%description
gnome-paint is a simple, easy to use paint program for GNOME.
It is inspired by MS-Paint.

%prep
%setup
%patch0

# remove icon extensions
%__subst 's|Icon=gp.png|Icon=gp|g' %_builddir/%name-%version/data/desktop/%name.desktop.in.in

%build
autoreconf -fisv
%configure
%make_build

%install
%makeinstall_std
# remove docs, use rpmbuild instead
rm -rf %buildroot%prefix/doc
# install desktop files
desktop-file-install \
        --dir=%buildroot%_desktopdir \
%buildroot%_desktopdir/%name.desktop
%find_lang %name

%files -f %name.lang
%doc COPYING ChangeLog README INSTALL
%_bindir/gnome-paint
%_desktopdir/gnome-paint.desktop
%_datadir/gnome-paint/
%_miconsdir/gp.png
%_datadir/%name/

%changelog
* Thu Dec 30 2010 Radik Usupov <radik@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri Oct 29 2010 Radik Usupov <radik@altlinux.org> 0.3.0-alt2
- Added Russian language

* Wed Oct 27 2010 Radik Usupov <radik@altlinux.org> 0.3.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Feb 19 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.1-1
- Initial Build
