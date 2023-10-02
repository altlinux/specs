%define ver_major 12.10
%define api_ver 0.1

Name: libappindicator
Version: %ver_major.0
Release: alt14
Summary: Application indicators library

Group: System/Libraries
License: LGPLv2 and LGPLv3
Url: https://launchpad.net/%name

Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-%version.tar.gz
Patch: 0002_libappindicator-no-Werror.patch
Patch1: nopython.patch
Patch2: libappindicator-12.10.1-ayatana-port.patch
BuildRequires: libdbus-glib-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: gtk-doc
BuildRequires: libgtk+3-devel
BuildRequires: libayatana-indicator3-devel

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

%prep
%setup
%autopatch -p1

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

%changelog
* Mon Oct 02 2023 Anton Midyukov <antohami@altlinux.org> 12.10.0-alt14
- build with libayatana-indicator
- do'nt build devel and doc packages
- drop old patches

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
