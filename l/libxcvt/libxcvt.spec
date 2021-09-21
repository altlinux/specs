%define upstream_commit_id 69fb7bf48
Name: libxcvt
Version: 0.1.0
Release: alt1.git%{upstream_commit_id}
License: MIT
Summary: VESA CVT standard timing modelines generator
Group: System/Libraries

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson

%description
VESA CVT standard timing modeline generator library

%package devel
Group: Development/C
Summary: VESA CVT standard timing modeline generator - development files 

%description devel
VESA CVT standard timing modeline generator - development files

%package -n cvt
Group: System/X11
Summary: VESA CVT standard timing modeline generator - command line tool

%description -n cvt
VESA CVT standard timing modeline generator - command line tool

%prep
%setup -q
%patch -p1

%build

%meson
%meson_build -v

%install
%meson_install

%files
%_libdir/libxcvt.so.*

%files devel
%_libdir/libxcvt.so
%_libdir/pkgconfig/libxcvt.pc

%files -n cvt
%_bindir/cvt
%_man1dir/cvt.1.*

%changelog

* Tue Sep 21 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1.0-alt1.git69fb7bf48
- Initial build
