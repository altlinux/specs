%define soname 2
%define gname zimg

Name: zimg
Version: 3.0.4
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

%package -n lib%name%soname
Summary: %summary
Group: System/Libraries
Provides: lib%name = %version
Obsoletes: lib%name

%description -n lib%name%soname
The "z" library implements the commonly required image processing basics of
scaling, color space conversion, and depth conversion. A simple API enables
conversion between any supported formats to operate with minimal knowledge from
the programmer. All library routines were designed from the ground-up with
correctness, flexibility, and thread-safety as first priorities. Allocation,
buffering, and I/O are cleanly separated from processing, allowing the
programmer to adapt "z" to many scenarios.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
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

%files -n lib%name%soname
%doc COPYING README.md ChangeLog
%_libdir/lib%gname.so.%{soname}*

%files -n lib%name-devel
#_bindir/testapp
%_includedir/*
%_libdir/lib%gname.so
%_pkgconfigdir/%gname.pc

%changelog
* Mon Apr 25 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.4-alt1
- New version (3.0.4).

* Wed Nov 17 2021 Leontiy Volodin <lvol@altlinux.org> 3.0.3-alt1
- New version (3.0.3).
- Package:
  + rename libzimg to libzimg2.

* Wed Jul 28 2021 Leontiy Volodin <lvol@altlinux.org> 3.0.2-alt1
- New version (3.0.2).
- Upstream:
  + arm: fix data alignment.
  + x86: fix detection of Zen2 and add detection of Zen3.

* Wed Jan 13 2021 Leontiy Volodin <lvol@altlinux.org> 3.0.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
