Name: libxcvt
Version: 0.1.2
Release: alt1
Summary: VESA CVT standard timing modelines generator
License: MIT
Group: System/Libraries
Url: https://gitlab.freedesktop.org/xorg/lib/libxcvt/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: meson

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

%package devel
Summary: VESA CVT Library and Header Files
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n cvt
Summary: Command line tool to calculate VESA CVT mode lines
Group: System/X11
Conflicts: xorg-server < 1.21

%description -n cvt
A standalone version of the command line tool cvt copied from the Xorg
implementation and is meant to be a direct replacement to the version
provided by the Xorg server.

%prep
%setup -q
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install

%files
%_libdir/*.so.*

%files devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n cvt
%_bindir/cvt
%_man1dir/cvt.1*

%changelog
* Wed Oct 19 2022 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Mon Nov 08 2021 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Wed Sep 22 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1.0-alt2.git69fb7bf48
- Added headers to -devel

* Tue Sep 21 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1.0-alt1.git69fb7bf48
- Initial build
