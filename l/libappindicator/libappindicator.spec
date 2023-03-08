%define ver_major 12.10
%define api_ver 0.1

Name: libappindicator
Version: %ver_major.0
Release: alt13
Summary: Application indicators library

Group: System/Libraries
License: LGPLv2 and LGPLv3
Url: https://launchpad.net/%name
Packager: Anton Midyukov <antohami@altlinux.org>

Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-%version.tar.gz
Patch: 0001_Fix_mono_dir.patch
Patch1: 0002_libappindicator-no-Werror.patch
Patch2: libappindicator-12.10.0-alt-application-service-marshal.patch
Patch3: nopython.patch
BuildRequires: libdbus-glib-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libgtk+3-devel
BuildRequires: gtk-doc
BuildRequires: libindicator-gtk3-devel

%description
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

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
Requires: %name-gtk3 = %EVR

%description gtk3-devel
This package contains the development files for the appindicator-gtk3 library.

%package devel-doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description devel-doc
This package contains the documentation for the appindicator libraries.

%prep
%setup
%patch0 -p1 -b .monodir
%patch1 -p2
#patch2 -p2
%patch3 -p1

sed -i "s#gmcs#mcs#g" configure.ac

%build
%define opts --disable-static --disable-gtk-doc --disable-dumper --enable-introspection=no --with-gtk=3 --disable-python
%autoreconf

export CFLAGS="%optflags $CFLAGS -Wno-deprecated-declarations"
%configure %opts
%make -j1

%install
%makeinstall_std

find %buildroot -type f -name '*.la' -delete

%files gtk3
%_libdir/libappindicator3.so.*

%files gtk3-devel
%dir %_includedir/libappindicator3-%api_ver/
%dir %_includedir/libappindicator3-%api_ver/libappindicator/
%_includedir/libappindicator3-%api_ver/libappindicator/*.h
%_libdir/libappindicator3.so
%_pkgconfigdir/appindicator3-%api_ver.pc

%files devel-doc
%dir %_datadir/gtk-doc/
%dir %_datadir/gtk-doc/html/
%doc %_datadir/gtk-doc/html/*

%changelog
* Mon Mar 06 2023 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt13
- disable gir packages
- disable vala api

* Mon Nov 23 2020 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt12
- build without gtk2

* Fri Feb 08 2019 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt11
- enable build mono for ix86 x86_64 aarch64 only

* Wed Feb 06 2019 Leontiy Volodin <lvol@altlinux.org> 12.10.0-alt10
- Disabled patch for application-service-marshal.
- Build Compile into one process for gtk3.

* Thu Dec 27 2018 Leontiy Volodin <lvol@altlinux.org> 12.10.0-alt9
- Fix syntax errors

* Fri Jul 13 2018 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt8.1
- Build Compile into one process (Fix FTBFS on a multiprocessor system)

* Thu Mar 22 2018 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt8
- Disable -Werror (Fix FTBFS)

* Thu Oct 26 2017 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt7
- Disable build with gtk-doc (Fix FTBFS)
- Enable build with mono.

* Wed Sep 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 12.10.0-alt6
- Updated build dependencies.

* Tue Jul 18 2017 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt5
- Disable build with mono.

* Mon Jul 18 2016 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt4
- Fix buildrequires.

* Mon Jan 25 2016 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt3
- Fix build:
  - enable single make build;
  - enable CFLAGS -Wno-deprecated-declarations.

* Tue Sep 22 2015 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt2
- Updated requires.

* Sun Sep 20 2015 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt1
- Initial build for ALT Linux Sisyphus.
