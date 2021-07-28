%define gname zimg
Name: libzimg
Version: 3.0.2
Release: alt1
Summary: Scaling, color space conversion, and dithering library
License: WTFPL
Group: System/Libraries
Url: https://github.com/sekrit-twc/zimg

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/release-%version/%gname-%version.tar.gz

BuildRequires: gcc-c++ autoconf automake libtool

%description
The "z" library implements the commonly required image processing basics of
scaling, color space conversion, and depth conversion. A simple API enables
conversion between any supported formats to operate with minimal knowledge from
the programmer. All library routines were designed from the ground-up with
correctness, flexibility, and thread-safety as first priorities. Allocation,
buffering, and I/O are cleanly separated from processing, allowing the
programmer to adapt "z" to many scenarios.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n zimg-release-%version

%build
autoreconf -vif
%configure \
    --disable-static \
    --disable-testapp
%make_build V=1

%install
%makeinstall_std
#install -m 755 -p -D testapp %%buildroot%%_bindir/testapp

find %buildroot -name '*.la' -delete

# Pick up docs in the files section
rm -fr %buildroot%_docdir/%gname

%files
%doc COPYING README.md ChangeLog
%_libdir/lib%gname.so.*

%files devel
#_bindir/testapp
%_includedir/*
%_libdir/lib%gname.so
%_pkgconfigdir/%gname.pc

%changelog
* Wed Jul 28 2021 Leontiy Volodin <lvol@altlinux.org> 3.0.2-alt1
- New version (3.0.2).
- Upstream:
  + arm: fix data alignment.
  + x86: fix detection of Zen2 and add detection of Zen3.

* Wed Jan 13 2021 Leontiy Volodin <lvol@altlinux.org> 3.0.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
