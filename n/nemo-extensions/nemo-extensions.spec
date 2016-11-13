%define api_ver 3.0

Name: nemo-extensions
Version: 3.2.1
Release: alt1
Summary: Extensions for Nemo

License: %gpl2plus and %lgpl2only
URL: https://github.com/linuxmint/nemo-extensions
Packager: Vladimir Didenko <cow at altlinux.org>
Group: Graphical desktop/GNOME

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-gnome rpm-build-licenses
BuildRequires: libnemo-devel
BuildRequires: python-devel python-module-distribute
BuildRequires: desktop-file-utils
BuildRequires: python-module-pygobject3-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: libnotify-devel
BuildRequires: libcjs-devel
BuildRequires: libevince-gir-devel
BuildRequires: libevince-devel
BuildRequires: libmusicbrainz5-devel
BuildRequires: gst-plugins1.0-gir-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libwebkit2gtk-devel
BuildRequires: libclutter-gtk3-devel
BuildRequires: libclutter-gtk3-gir-devel
BuildRequires: libclutter-gst3.0-devel
BuildRequires: libgtksourceview3-gir-devel
BuildRequires: libgtksourceview3-devel
BuildRequires: perl(XML/Parser.pm)
BuildRequires: libcogl-gir-devel

%description
Extensions for Nemo

%package     -n nemo-fileroller
Summary:     File Roller extension for Nemo
License:     %gpl2plus
Group: Graphical desktop/GNOME
Requires:    /usr/bin/file-roller

%description -n nemo-fileroller
This package contains the file-roller extension for the Nemo.

%package -n nemo-python
Summary: Python bindings for Nemo
License: %gpl2plus
Group: Graphical desktop/GNOME
Requires: nemo

%description -n nemo-python
Python bindings for Nemo

%package -n nemo-python-devel
Summary: Python bindings for Nemo
License: %gpl2plus
Group: Development/GNOME and GTK+
Requires: nemo-python = %version-%release

%description -n nemo-python-devel
Python bindings for Nemo

%package -n nemo-share
Summary: Share a folder from the Cinnamon Nemo file manager
License: %gpl2plus
Group: Graphical desktop/GNOME
Requires: nemo >= 2.8
Requires: samba >= 3.0.23
Requires: nemo-share-common

%description -n nemo-share
Application for the Cinnamon desktop integrated in Nemo, that allows
simple use of Nemo shares without signing in as root.

%package -n nemo-share-common
Summary: Common files for nemo-share
License: %gpl2plus
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n nemo-share-common
Common files for nemo-share.

%package -n nemo-terminal
Summary: Embedded terminal window for Nemo
License: %gpl3plus
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: nemo-python
Requires: libvte3_2.90-gir

%description -n nemo-terminal
Embedded terminal window for Nemo

%package -n nemo-preview
Summary: A quick previewer for Nemo
License: %gpl2plus
Group: Graphical desktop/GNOME
Requires: nemo

%description -n nemo-preview
Nemo Preview is a GtkClutter and Javascript-based quick previewer
for Nemo.
It is capable of previewing documents, PDFs, sound and video files,
some text files, and possibly others in the future.

To activate the preview, left-click the file and hit space.
The preview can be closed by hitting space again, or escape.

%package -n nemo-emblems
Summary: Emblem support for nemo
License: %gpl3plus
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: nemo-python

%description -n nemo-emblems
Restores the emblems functionality that used to be in GNOME 2.

%package -n nemo-image-converter
Summary: Nemo extension to mass resize images
Requires: ImageMagick
License: %gpl3plus
Group: Graphical desktop/GNOME

%description -n nemo-image-converter
Adds a "Resize Images..." menu item to the context menu. This opens a dialog where you set the desired image size and file name.

%package -n nemo-compare
Summary: Context menu comparison extension for nemo
License: %gpl3plus
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: nemo-python
Requires: meld
Requires: pyxdg

%description -n nemo-compare
Context menu comparison extension for Nemo file manager.

%prep
%setup -q
%patch -p1

%build
pushd nemo-fileroller
%autoreconf
%configure
%make
popd

pushd nemo-python
%autoreconf
%configure
%make
popd

pushd nemo-share
%autoreconf
%configure
%make
popd

%set_typelibdir %_libdir/nemo-preview
%set_girdir %_datadir/nemo-preview
pushd nemo-preview
[ ! -d m4 ] && mkdir m4
%autoreconf
%configure
%make
popd

pushd nemo-image-converter
[ ! -d m4 ] && mkdir m4
%autoreconf
%configure
%make
popd

%install
rm -rf %buildroot
mkdir -p %buildroot/%_datadir/nemo-python/extensions/

pushd nemo-fileroller
%makeinstall_std
popd

pushd nemo-python
%makeinstall_std
popd

pushd nemo-share
%makeinstall_std
popd

pushd nemo-terminal
mkdir %buildroot/%_datadir/nemo-terminal
mkdir -p %buildroot/%_datadir/glib-2.0/schemas/
install -pm 0644 src/nemo_terminal.py %buildroot/%_datadir/nemo-python/extensions/
install -pm 0644 src/org.nemo.extensions.nemo-terminal.gschema.xml %buildroot/%_datadir/glib-2.0/schemas/
install -pm 0644 pixmap/logo_120x120.png %buildroot/%_datadir/nemo-terminal
popd

pushd nemo-preview
%makeinstall_std
popd

pushd nemo-emblems
install -pm 0644 nemo-extension/nemo-emblems.py %buildroot/%_datadir/nemo-python/extensions/
popd

pushd nemo-image-converter
%makeinstall_std
popd

pushd nemo-compare
mkdir -p %buildroot/%_datadir/applications/
install -pm 0644 src/{nemo-compare,nemo-compare-preferences,utils}.py %buildroot/%_datadir/nemo-python/extensions/
install -pm 0644 data/nemo-compare-preferences.desktop %buildroot/%_datadir/applications/
popd

rm -f %buildroot/%_libdir/nemo/extensions-3.0/*.la
rm -f %buildroot/%_libdir/nemo/extensions-3.0/*.a

%find_lang nemo-preview
%find_lang nemo-image-converter
%find_lang nemo-share

%files -n nemo-fileroller
%doc nemo-fileroller/README
%doc nemo-fileroller/COPYING
%_libdir/nemo/extensions-%api_ver/libnemo-fileroller.so

%files -n nemo-python
%doc nemo-python/COPYING
%_libdir/nemo/extensions-%api_ver/libnemo-python.so
%dir %_datadir/nemo-python/extensions
%doc %_docdir/nemo-python

%files -n nemo-python-devel
%_pkgconfigdir/nemo-python.pc

%files -n nemo-share-common -f nemo-share.lang
%doc nemo-share/AUTHORS
%doc nemo-share/COPYING
%doc nemo-share/README
%_datadir/nemo-share/*

%files -n nemo-share
%_libdir/nemo/extensions-%api_ver/libnemo-share.so

%files -n nemo-terminal
%doc nemo-terminal/README
%doc nemo-terminal/COPYING
%_datadir/nemo-python/extensions/nemo_terminal.py*
%_datadir/nemo-terminal/
%_datadir/glib-2.0/schemas/org.nemo.extensions.nemo-terminal.gschema.xml

%files -n nemo-preview -f nemo-preview.lang
%doc nemo-preview/README
%doc nemo-preview/COPYING
%_bindir/nemo-preview
%_libdir/nemo-preview
%_libexecdir/nemo-preview-start
%_datadir/nemo-preview
%_datadir/dbus-1/services/org.nemo.Preview.service

%files -n nemo-emblems
%doc nemo-emblems/COPYING.GPL3
%_datadir/nemo-python/extensions/nemo-emblems.py*

%files -n nemo-image-converter  -f nemo-image-converter.lang
%doc nemo-image-converter/README
%doc nemo-image-converter/COPYING
%_libdir/nemo/extensions-%api_ver/libnemo-image-converter.so
%_datadir/nemo-image-converter/

%files -n nemo-compare
%_datadir/nemo-python/extensions/nemo-compare.py*
%_datadir/nemo-python/extensions/nemo-compare-preferences.py*
%_datadir/nemo-python/extensions/utils.py*
%_datadir/applications/nemo-compare-preferences.desktop

%changelog
* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- 3.2.1

* Thu Sep 29 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt2
- Fix build with gnome 3.22
- Fix requires to file-roller

* Fri Jun 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.0-12-g4093c7b

* Tue Apr 26 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Feb 3 2016 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt2
- Add libvte3_2.90-gir to nemo-terminal deps
- Port nemo-preview to ClutterGst 3.0

* Tue Feb 2 2016 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt1
- Initial build for Sisyphus
