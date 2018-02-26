Name: tumbler
Version: 0.1.21
Release: alt1
Summary: A thumbnail D-Bus service
License: GPLv2+
Group: Graphical desktop/XFce
Url: http://git.xfce.org/apps/tumbler
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gtk-doc intltool libdbus-glib-devel libfreetype-devel libgio-devel libgtk+2-devel libjpeg-devel libpng-devel
BuildRequires: libffmpegthumbnailer-devel libpoppler-glib-devel

%description
Tumbler is a D-Bus service for applications to request
thumbnails for various URI schemes and MIME types.
It is an implementation of the thumbnail management D-Bus
specification

%package -n lib%name
Summary: A D-bus thumbnailing framweork
Group: System/Libraries

%description -n lib%name
Tumbler is a D-Bus service for applications to request
thumbnails for various URI schemes and MIME types

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C

%description -n lib%name-devel
Development files and headers for %name

%prep
%setup -q
%patch -p1

ls po/*.po | sed s/.po//g | sed sApo/AA | xargs > po/LINGUAS

%build
%autoreconf
%configure \
	--libexecdir=%_prefix/libexec \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir/%name-1 -name \*.la -delete

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS TODO
%_prefix/libexec/%name-1
%_libdir/%name-1
%_datadir/dbus-1/services/*.service

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name-1
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.21-alt1
- 0.1.21
- fixed path to tumblerd in dbus service files (closes: #25206)

* Mon Nov 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Tue Jan 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- initial release

