Name: libpostproc
Version: 8.0
Release: alt1
Epoch: 2

Summary: FFmpeg postprocessing library
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://github.com/michaelni/libpostproc

Source: %name-%version.tar

BuildRequires: nasm libavutil-devel

%define sover 59

%package -n libpostproc%sover
Summary: FFmpeg postprocessing library
Group: System/Libraries

%package devel
Summary: FFmpeg postprocessing library
Group: Development/C

%description
libpostproc is a library for filtering images and videos.
It currently supports the MPEG4 deblocking and deringing filters and
some old basic deinterlacing methods and old basic denoise.
These deblocking methods are effective on a wide range of old
formats, including jpeg, mpeg1, mpeg2, mpeg4, h261, h262, h263,
msmpeg4v1, msmpeg4v2, msmpeg4v3 and many other similar formats.

%description -n libpostproc%sover
libpostproc is a library for filtering images and videos.
It currently supports the MPEG4 deblocking and deringing filters and
some old basic deinterlacing methods and old basic denoise.
These deblocking methods are effective on a wide range of old
formats, including jpeg, mpeg1, mpeg2, mpeg4, h261, h262, h263,
msmpeg4v1, msmpeg4v2, msmpeg4v3 and many other similar formats.
This package contains shared libpostproc library.

%description devel
libpostproc is a library for filtering images and videos.
It currently supports the MPEG4 deblocking and deringing filters and
some old basic deinterlacing methods and old basic denoise.
These deblocking methods are effective on a wide range of old
formats, including jpeg, mpeg1, mpeg2, mpeg4, h261, h262, h263,
msmpeg4v1, msmpeg4v2, msmpeg4v3 and many other similar formats.
This package contains development part of libpostproc.

%prep
%setup

%build
%ifarch %ix86
%global optflags_lto %nil
%endif
./configure \
    --prefix=%_prefix \
    --libdir=%_libdir \
    --shlibdir=%_libdir \
    --mandir=%_mandir \
    --docdir=%_docdir/%name-%version \
    --disable-avutil \
    --disable-doc \
    --disable-debug \
    --disable-devices \
    --disable-bsfs \
    --disable-nvenc \
    --disable-linux-perf \
    --disable-network \
    --disable-encoders \
    --disable-muxers \
    --disable-stripping \
    --disable-static \
    --disable-rpath \
    --enable-shared \
    --enable-pic \
    --enable-postproc \
    --extra-libs=-lavutil \
    --extra-cflags='%optflags' \
    --extra-version=%release

%make_build V=1

%install
%makeinstall_std
rm -rf %buildroot%_datadir/postproc

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

%files -n libpostproc%sover
%doc LICENSE* README*
%_libdir/libpostproc.so.*

%files -n libpostproc-devel
%_includedir/libpostproc
%_libdir/libpostproc.so
%_pkgconfigdir/libpostproc.pc

%changelog
* Tue Dec 30 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2:8.0-alt1
- built as standalone library
