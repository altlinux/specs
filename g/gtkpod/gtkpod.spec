Name: gtkpod
Version: 2.1.1
Release: alt3
Summary: A GUI for Apple's iPod using GTK2
License: GPL
Group: Sound
Url: http://www.gtkpod.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name = %version-%release

BuildRequires: flex mount intltool desktop-file-utils zlib-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libgtk+3-devel >= 3.0.8
BuildRequires: glib2-devel >= 2.28.5
BuildRequires: libglade-devel >= 2.4.0
BuildRequires: libgpod-devel >= 0.7.0
BuildRequires: anjuta-devel >= 2.91.0
BuildRequires: libgdl3-devel >= 3.0.0
BuildRequires: libgio-devel >= 2.28.5
BuildRequires: libxml2-devel >= 2.7.7
BuildRequires: libid3tag-devel >= 0.15
BuildRequires: libcurl-devel >= 7.10.0
BuildRequires: libwebkitgtk3-devel >= 1.3
BuildRequires: libclutter-gtk3-devel >= 1.0
BuildRequires: gstreamer-devel >= 0.10.25 gst-plugins-devel  >= 0.10.25
BuildRequires: libflac-devel  libmp4v2-devel libvorbis-devel faad
BuildRequires: glibc-kernheaders glibc-devel

%add_findreq_skiplist %_datadir/%name/scripts/*

%description
gtkpod is a platform independent Graphical User Interface for Apple's
iPod using GTK2. It supports the first to fifth Generation including
the iPod mini, iPod Photo, iPod Shuffle, iPod nano, and iPod Video.

%package -n lib%name
Group: System/Libraries
Summary: Shared library part of %name

%description -n lib%name
This is the shared library part of %{name}.

%package -n lib%name-devel
Group: Development/C
Summary: Development files for %name
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is the development part of %{name}.


%prep
%setup -q
%patch -p1
echo "%version" > version

%build
%autoreconf
%configure --disable-static
%make

%install
%makeinstall_std
%find_lang %name

%__subst "s|%_prefix/lib|%_libdir|g" %buildroot%_datadir/%name/scripts/sync-evolution.sh

desktop-file-install --vendor="" \
  --add-mime-type="x-content/audio-player" \
  --dir %buildroot%_datadir/applications %buildroot%_datadir/applications/*

%files -f %name.lang
%doc README AUTHORS ChangeLog
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/*.plugin
%_libdir/%name/*.so
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/%name.*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/gtkpod

%exclude %_libdir/%name/*.la

%changelog
* Thu May 17 2012 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt3
- rebuild with new libgdl

* Thu Mar 29 2012 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt2
- rebuild with new clutter

* Tue Jan 17 2012 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Thu Sep 15 2011 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0
- build with gtk+3

* Wed Apr 20 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0
- add library package

* Mon Jan 17 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt3
- skip findreq in %%_datadir/%name/scripts/*

* Mon Jan 17 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2
- rebuild with libgpod
- update buildreq

* Mon Dec 06 2010 Anton Protopopov <aspsk@altlinux.org> 1.0.0-alt1
- 1.0.0 (ALT 24638)

* Mon Aug 31 2009 Anton Protopopov <aspsk@altlinux.org> 0.99.14-alt2
- Don't pack icons-theme.cache into package (ALT 21279)

* Wed Jan 21 2009 Anton Protopopov <aspsk@altlinux.org> 0.99.14-alt1
- 0.99.14

* Sat Sep 13 2008 Anton Protopopov <aspsk@altlinux.org> 0.99.12-alt1
- Remove synchronizing with PalmOS

* Sat Sep 13 2008 Anton Protopopov <aspsk@altlinux.org> 0.99.12-alt0.1
- Initial buld
