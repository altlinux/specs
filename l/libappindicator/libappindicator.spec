%define ver_major 12.10
%define api_ver 0.1

Name: libappindicator
Version: %ver_major.0
Release: alt3
Summary: Application indicators library

Group: System/Libraries
License: LGPLv2 and LGPLv3
Url: https://launchpad.net/%name
Packager: Anton Midyukov <antohami@altlinux.org>

Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-%version.tar.gz
BuildRequires(pre): rpm-build-mono gcc
BuildRequires: gtk-doc vala-tools
BuildRequires: libdbus-glib-devel libdbusmenu-devel
BuildRequires: libdbusmenu-gtk2-devel libdbusmenu-gtk3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk+2-devel libgtk+2-gir-devel
BuildRequires: libgtk+3-devel libgtk+3-gir-devel
BuildRequires: libindicator-devel libindicator-gtk3-devel
BuildRequires: python-dev python-module-pygtk-devel
BuildRequires: libgtk-sharp2-devel libgtk-sharp2-gapi
BuildRequires: mono-devel mono-nunit-devel

%description
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

%package -n python-module-appindicator
Summary: Python 2 bindings for %name
Group: System/Libraries
Requires: %name-gir = %version-%release
Requires: %name-gtk3-gir = %version-%release

%description -n python-module-appindicator
This package contains the Python 2 bindings for the appindicator library.

%package devel
Summary: %summary
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for %name

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
This package provides GObject introspection data for the %name.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
This package provides GObject introspection devel data for the %name

%package gtk3
Summary: Application indicators library - GTK 3
Group: System/Libraries

%description gtk3
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

This package contains the GTK 3 version of this library.

%package gtk3-devel
Summary: Development files for %name-gtk3
Group: Development/Other
Requires: %name-gtk3 = %version-%release

%description gtk3-devel
This package contains the development files for the appindicator-gtk3 library.

%package gtk3-gir
Summary: GObject introspection data for the %name-gtk3
Group: System/Libraries
Requires: %name-gtk3 = %version-%release

%description gtk3-gir
This package provides GObject introspection data for the %name-gtk3.

%package gtk3-gir-devel
Summary: GObject introspection devel data for the %name-gtk3
Group: Development/Other
BuildArch: noarch
Requires: %name-gtk3-gir = %version-%release

%description gtk3-gir-devel
This package provides GObject introspection devel data for the %name-gtk3

%package devel-doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description devel-doc
This package contains the documentation for the appindicator libraries.

%package sharp
Summary: Application indicators library - C#
Group: System/Libraries
Requires: %name-gir = %version-%release
Requires: %name-gtk3-gir = %version-%release

%description sharp
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

This package contains the Mono C# bindings for this library.

%package sharp-devel
Summary: Development files for %name-sharp
Group: Development/Other
Requires: %name-sharp = %version-%release

%description sharp-devel
This package contains the development files for the appindicator-sharp library.

%prep
%setup -a0
mv %name-%version %name-gtk3

%build
%define opts --disable-static --enable-gtk-doc --disable-dumper

%autoreconf
export CFLAGS="%{optflags} $CFLAGS -Wno-deprecated-declarations"
%configure  %opts --with-gtk=2
make -j1 V=1
%make

pushd %name-gtk3
%autoreconf
export CFLAGS="%{optflags} $CFLAGS -Wno-deprecated-declarations"
%configure %opts --with-gtk=3
make -j1 V=1
popd

%install
%makeinstall_std

pushd %name-gtk3
%makeinstall_std
popd

%files
%_libdir/libappindicator.so.*

%files gir
%_typelibdir/AppIndicator-%api_ver.typelib

%files devel
%dir %_includedir/libappindicator-%api_ver/
%dir %_includedir/libappindicator-%api_ver/libappindicator/
%_includedir/libappindicator-%api_ver/libappindicator/*.h
%_libdir/libappindicator.so
%_pkgconfigdir/appindicator-%api_ver.pc
%_vapidir/appindicator-%api_ver.vapi
%_vapidir/appindicator-%api_ver.deps

%files gir-devel
%_girdir/AppIndicator-%api_ver.gir

%files -n python-module-appindicator
%dir %python_sitelibdir/appindicator/
%python_sitelibdir/appindicator/__init__.py*
%python_sitelibdir/appindicator/_appindicator.so
%python_sitelibdir/appindicator/_appindicator.la
%dir %_datadir/pygtk/
%dir %_datadir/pygtk/2.0/
%dir %_datadir/pygtk/2.0/defs/
%_datadir/pygtk/2.0/defs/appindicator.defs

%files gtk3
%_libdir/libappindicator3.so.*

%files gtk3-gir
%_typelibdir/AppIndicator3-%api_ver.typelib

%files gtk3-devel
%dir %_includedir/libappindicator3-%api_ver/
%dir %_includedir/libappindicator3-%api_ver/libappindicator/
%_includedir/libappindicator3-%api_ver/libappindicator/*.h
%_libdir/libappindicator3.so
%_pkgconfigdir/appindicator3-%api_ver.pc
%_vapidir/appindicator3-%api_ver.vapi
%_vapidir/appindicator3-%api_ver.deps

%files gtk3-gir-devel
%_girdir/AppIndicator3-%api_ver.gir

%files devel-doc
%doc %_datadir/gtk-doc/html/*
%doc AUTHORS README COPYING COPYING.LGPL.2.1

%files sharp
%dir %_libdir/cli/appindicator-sharp-%api_ver/
%_libdir/cli/appindicator-sharp-%api_ver/appindicator-sharp.dll
%_libdir/cli/appindicator-sharp-%api_ver/appindicator-sharp.dll.config
%_libdir/cli/appindicator-sharp-%api_ver/policy.0.0.appindicator-sharp.config
%_libdir/cli/appindicator-sharp-%api_ver/policy.0.0.appindicator-sharp.dll
%_libdir/cli/appindicator-sharp-%api_ver/policy.0.1.appindicator-sharp.config
%_libdir/cli/appindicator-sharp-%api_ver/policy.0.1.appindicator-sharp.dll
%dir %_monodir/appindicator-sharp/
%_monodir/appindicator-sharp/appindicator-sharp.dll
%_monodir/appindicator-sharp/policy.0.0.appindicator-sharp.dll
%dir %_monogacdir/appindicator-sharp/
%dir %_monogacdir/appindicator-sharp/*/
%_monogacdir/appindicator-sharp/*/appindicator-sharp.dll
%_monogacdir/appindicator-sharp/*/appindicator-sharp.dll.config
%dir %_monogacdir/policy.0.0.appindicator-sharp/
%dir %_monogacdir/policy.0.0.appindicator-sharp/*/
%_monogacdir/policy.0.0.appindicator-sharp/*/policy.0.0.appindicator-sharp.dll
%_monogacdir/policy.0.0.appindicator-sharp/*/policy.0.0.appindicator-sharp.config

%files sharp-devel
%_pkgconfigdir/appindicator-sharp-0.1.pc

%changelog
* Mon Jan 25 2016 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt3
- Fix build:
  - enable single make build;
  - enable CFLAGS -Wno-deprecated-declarations.

* Tue Sep 22 2015 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt2
- Updated requires.

* Sun Sep 20 2015 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt1
- Initial build for ALT Linux Sisyphus.
