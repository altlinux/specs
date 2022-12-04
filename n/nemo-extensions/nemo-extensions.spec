%define api_ver 3.0

Name: nemo-extensions
Version: 5.6.0
Release: alt1
Summary: Extensions for Nemo

License: %gpl2plus and %lgpl2only
URL: https://github.com/linuxmint/nemo-extensions
Packager: Vladimir Didenko <cow at altlinux.org>
Group: Graphical desktop/GNOME

Source: %name-%version.tar
Patch: %name-%version-%release.patch

AutoReqProv: nopython
%define __python %nil

BuildPreReq: rpm-build-gnome rpm-build-licenses rpm-build-python3
BuildRequires: libnemo-devel
BuildRequires: python3-dev
BuildRequires: desktop-file-utils
BuildRequires: python3-module-pygobject3-devel
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
BuildRequires: libgtksourceview4-gir-devel
BuildRequires: libgtksourceview4-devel
BuildRequires: perl(XML/Parser.pm)
BuildRequires: libcogl-gir-devel
BuildRequires: libxreader-gir-devel
BuildRequires: libcinnamon-desktop-devel
BuildRequires: libxreader-gir-devel
BuildRequires: meson

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
Requires: nemo-extensions-translations

%description -n nemo-python
Python bindings for Nemo

%package -n nemo-python-devel
Summary: Python bindings for Nemo
License: %gpl2plus
Group: Development/GNOME and GTK+
Requires: nemo-python = %version-%release

%description -n nemo-python-devel
Python bindings for Nemo

%package -n nemo-terminal
Summary: Embedded terminal window for Nemo
License: %gpl3plus
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: nemo-python
Requires: libvte3-gir
Requires: nemo-extensions-translations

%package -n nemo-share
Summary: Share a folder from the Cinnamon Nemo file manager
License: %gpl2plus
Group: Graphical desktop/GNOME
Requires: nemo >= 2.8
Requires: samba >= 3.0.23
Requires: nemo-share-common
Requires: nemo-extensions-translations

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

%description -n nemo-terminal
Embedded terminal window for Nemo

%package -n nemo-preview
Summary: A quick previewer for Nemo
License: %gpl2plus
Group: Graphical desktop/GNOME
Requires: nemo
Requires: nemo-extensions-translations

%description -n nemo-preview
Nemo Preview is a GtkClutter and Javascript-based quick previewer
for Nemo.
It is capable of previewing documents, PDFs, sound and video files,
some text files, and possibly others in the future.

To activate the preview, left-click the file and hit space.
The preview can be closed by hitting space again, or escape.

%package -n nemo-preview-gir-devel
Summary: GObject introspection devel data for the nemo-preview extension
Group: System/Libraries
BuildArch: noarch
Requires: nemo-preview = %version-%release

%description -n nemo-preview-gir-devel
GObject introspection devel data for the nemo-preview extension.

%package -n nemo-image-converter
Summary: Nemo extension to mass resize images
License: %gpl3plus
Group: Graphical desktop/GNOME
Requires: nemo-extensions-translations
Requires: ImageMagick

%description -n nemo-image-converter
Adds a "Resize Images..." menu item to the context menu. This opens a dialog where you set the desired image size and file name.

%prep
%setup -q
%patch -p1

%build
pushd nemo-fileroller
%meson
%meson_build
popd

pushd nemo-python
%meson
%meson_build
popd

pushd nemo-share
%meson
%meson_build
popd

%set_typelibdir %_libdir/nemo-preview
%set_girdir %_datadir/nemo-preview
pushd nemo-preview
%meson
%meson_build
popd

pushd nemo-image-converter
%meson
%meson_build
popd

pushd nemo-terminal
%python3_build
popd

%install
rm -rf %buildroot
mkdir -p %buildroot/%_datadir/nemo-python/extensions/

pushd nemo-fileroller
%meson_install
popd

pushd nemo-python
%meson_install
popd

pushd nemo-share
%meson_install
popd

pushd nemo-terminal
%python3_install
popd

pushd nemo-preview
%meson_install
popd

pushd nemo-image-converter
%meson_install
popd

rm -f %buildroot/%_libdir/nemo/extensions-3.0/*.la
rm -f %buildroot/%_libdir/nemo/extensions-3.0/*.a

%find_lang nemo-preview
%find_lang nemo-share

%files -n nemo-fileroller
%doc nemo-fileroller/README
%doc nemo-fileroller/COPYING
%_libdir/nemo/extensions-%api_ver/libnemo-fileroller.so

%files -n nemo-python
%doc nemo-python/COPYING
%_libdir/nemo/extensions-%api_ver/libnemo-python.so
%dir %_datadir/nemo-python/extensions

%files -n nemo-python-devel
%_pkgconfigdir/nemo-python.pc

%files -n nemo-share-common
%doc nemo-share/AUTHORS
%doc nemo-share/COPYING
%doc nemo-share/README
%_datadir/nemo-share/*
# Mint specific script with deps to Mint tools
%exclude %_datadir/nemo-share/install-samba

%files -n nemo-share -f nemo-share.lang
%_libdir/nemo/extensions-%api_ver/libnemo-share.so
%_datadir/polkit-1/actions/org.nemo.share.samba_install.policy

%files -n nemo-terminal
%doc nemo-terminal/README
%doc nemo-terminal/COPYING
%_bindir/nemo-terminal-prefs
%_datadir/nemo-python/extensions/nemo_terminal.py*
%_datadir/nemo-terminal/
%_datadir/glib-2.0/schemas/org.nemo.extensions.nemo-terminal.gschema.xml
%python3_sitelibdir_noarch/nemo_terminal-*.egg-*

%files -n nemo-preview -f nemo-preview.lang
%doc nemo-preview/README
%doc nemo-preview/COPYING
%_bindir/nemo-preview
%_libdir/nemo-preview
%_libexecdir/nemo-preview-start
%_datadir/nemo-preview/js
%_datadir/dbus-1/services/org.nemo.Preview.service

%files -n nemo-preview-gir-devel
%_datadir/nemo-preview/gir-1.0/*

%files -n nemo-image-converter
%doc nemo-image-converter/README
%doc nemo-image-converter/COPYING
%_libdir/nemo/extensions-%api_ver/libnemo-image-converter.so
%_datadir/nemo-image-converter/

%changelog
* Fri Dec 2 2022 Vladimir Didenko <cow@altlinux.org> 5.6.0-alt1
- 5.6.0

* Thu Jul 21 2022 Vladimir Didenko <cow@altlinux.org> 5.4.1-alt1
- 5.4.1

* Fri Jun 17 2022 Vladimir Didenko <cow@altlinux.org> 5.4.0-alt1
- 5.4.0
- don't pack nemo-emblems and nemo-compare because of build issues

* Mon Nov 20 2021 Vladimir Didenko <cow@altlinux.org> 5.2.1-alt1
- 5.2.1

* Mon Jun 28 2021 Vladimir Didenko <cow@altlinux.org> 5.0.1-alt1
- 5.0.1

* Tue Jun 1 2021 Vladimir Didenko <cow@altlinux.org> 5.0.0-alt2
- Don't pack gir development files as part of nemo-preview extension

* Mon May 31 2021 Vladimir Didenko <cow@altlinux.org> 5.0.0-alt1
- 5.0.0

* Fri Nov 27 2020 Vladimir Didenko <cow@altlinux.org> 4.8.0-alt1
- 4.8.0

* Sat May 16 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt2
- restore nemo-share

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt1
- 4.6.0
- don't pack nemo-share since it uses Linux Mint specific tools

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- 4.4.0

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1
- 4.0.2

* Tue Nov 20 2018 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1.1
- Fix build

* Tue Nov 20 2018 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1
- 4.0.1

* Thu May 3 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 19 2018 Vladimir Didenko <cow@altlinux.org> 3.6.2-alt2
- Switch to vte3 package for nemo-terminal

* Wed Dec 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.2-alt1
- 3.6.2-2-g5e72842

* Mon Oct 30 2017 Vladimir Didenko <cow@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.0-19-g0ad0a0c

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.0-9-g32afa18

* Fri May 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 3.2.3-alt1
- 3.2.3

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
